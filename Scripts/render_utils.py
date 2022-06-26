import os
import bpy
import sys

true = True
false = False

EEVEE = 'BLENDER_EEVEE'
BENCH = 'BLENDER_WORKBENCH'

render_dir = "E:\\Blender\\Renders\\"

import importlib
import engine_utils
import shader_utils
import keyframe_utils

importlib.reload(engine_utils)
importlib.reload(shader_utils)
importlib.reload(keyframe_utils)

from engine_utils import *
from shader_utils import *
from keyframe_utils import *

def _switch_render_engine(engine):
    bpy.context.scene.render.engine = engine
    
    if (engine == EEVEE):
        set_eevee_default_settings()
    elif (engine == BENCH):
        set_bench_default_settings()

def _export(filepath):
    i = 0
    
    # Loop through keyframes.
    while last_frame() is False:
        bpy.context.scene.render.filepath = filepath + str(i)
        
        bpy.ops.render.render(write_still=True)
        
        i += 1

        jump_next(True)
    
def _export_render(obj, folder, prefix):
    # Jump to the first frame of the animation.
    jump_end(false)

    filepath = os.path.join(render_dir, folder, prefix)

    _export(filepath)
    
def export_render(ext = None):
    # Get the current object.
    obj = bpy.context.object

    if (obj is None or obj.animation_data is None):
        return

    selected = bpy.context.selected_objects
    filename = obj.animation_data.action.name

    if (ext == ".ss" or ext == None):
        _switch_render_engine(EEVEE)
    
        # Export the base, fully lit model animation.
        _export_render(obj, filename, filename + ".ss")

        print("export .ss\n")
        
    if (ext == ".nm" or ext == None):
        _switch_render_engine(BENCH)

        # Export the associated normal map animation.
        _export_render(obj, filename, filename + ".nm")

        print("export .nm\n")

    if (len(selected) > 0 and (ext == ".em" or ext == None)):
        _switch_render_engine(EEVEE)

        for sel in selected:
            attach_holdout_to_object_materials(sel)
    
        # Export the associated emission animation.
        _export_render(obj, filename, filename + ".em")

        for sel in selected:
            remove_holdout_from_object_materials(sel)
            
        print("export .em\n")
        
    # Restore working configs.
    _switch_render_engine(EEVEE)
        
    bpy.context.scene.render.filepath = render_dir

    bpy.ops.render.render('INVOKE_DEFAULT')

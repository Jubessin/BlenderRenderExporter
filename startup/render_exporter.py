import bpy
import sys
import os

script_dir = "E:\\Blender\\Scripts\\"

if not script_dir in sys.path:
    sys.path.append(script_dir);

import render_utils
import importlib

importlib.reload(render_utils)

from render_utils import export_render

class SpritesheetExporter(bpy.types.Operator):
    bl_idname = "export.spritesheet"
    bl_label = "Export Spritesheet"

    def execute(self, context):
        export_render()
        return {'FINISHED'}
    
class BaseSpritesheetExporter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export.spritesheet_base"
    bl_label = "Export Base Spritesheet"
    
    def execute(self, context):
        export_render(".ss")
        return {'FINISHED'}

class NormalSpritesheetExporter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export.spritesheet_normal"
    bl_label = "Export Normal Spritesheet"

    def execute(self, context):
        export_render(".nm")
        return {'FINISHED'}

class EmissionSpritesheetExporter(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "export.spritesheet_emission"
    bl_label = "Export Emission Spritesheet"

    def execute(self, context):
        export_render(".em")
        return {'FINISHED'}

def menu_func(self, context):
    layout = self.layout
    
    layout.separator()

    layout.operator("export.spritesheet")

classes = (
    SpritesheetExporter,
    BaseSpritesheetExporter,
    NormalSpritesheetExporter,
    EmissionSpritesheetExporter,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_render.append(menu_func)
        
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_render.remove(menu_func)

if __name__ == "__main__":
    register()

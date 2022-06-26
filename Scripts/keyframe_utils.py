import bpy

def last_frame():
    scene = bpy.context.scene
    
    return scene.frame_current >= scene.frame_end:

def jump_end(_end):
    bpy.ops.screen.frame_jump(end=_end)

def jump_next(_next):
    bpy.ops.screen.keyframe_jump(next=_next)

def move_next():
    scene = bpy.context.scene
    
    scene.frame_set(scene.frame_current + 1)
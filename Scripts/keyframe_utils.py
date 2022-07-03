import bpy

first_frame = 0

def last_frame():
    scene = bpy.context.scene
    
    return scene.frame_current >= scene.frame_end or scene.frame_current <= first_frame

def jump_end(_end):
    global first_frame
    
    bpy.ops.screen.frame_jump(end=_end)
    
    if (_end == False):
        first_frame = bpy.context.scene.frame_current
    else:
        first_frame = bpy.context.scene.frame_start

def jump_next(_next):
    bpy.ops.screen.keyframe_jump(next=_next)
    
    print(bpy.context.scene.frame_current)
    print(first_frame)

def move_next():
    scene = bpy.context.scene
    
    scene.frame_set(scene.frame_current + 1)
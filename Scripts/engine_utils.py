import bpy

true = True
false = False

def set_eevee_default_settings():
    scene = bpy.context.scene
    
    eevee = scene.eevee
    render = scene.render
    
    eevee.use_gtao = false
    eevee.use_bloom = false
    eevee.use_ssr = false
    eevee.use_motion_blur = false
    eevee.use_overscan = false
    
    render.filter_size = 0
    render.use_simplify = false
    render.use_simplify = false
    
    scene.grease_pencil_settings.antialias_threshold = 0
    
def set_bench_default_settings():
    scene = bpy.context.scene

    shading = bpy.data.scenes['Scene'].display.shading
    
    render = scene.render
    
    shading.light = 'MATCAP'
    shading.color_type = 'SINGLE'
    shading.single_color = (1, 1, 1)
    
    render.film_transparent = true
    render.use_simplify = false
    
    scene.grease_pencil_settings.antialias_threshold = 0

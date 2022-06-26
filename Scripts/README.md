The following scripts should be placed in the directory specified in 'render_exporter.py' (script_dir).

# engine_utils.py

Encapsulates render engine settings.

# keyframe_utils.py

Contains a few useful functions involving keyframe manipulation.

# render_utils.py

Handles the actual exporting of the render.
 
There are three supported render exports:
  
&emsp;_.ss_ - base spritesheet, fully lit<br>
&emsp;_.nm_ - normal map spritesheet<br>
&emsp;_.em_ - emission map spritesheet

# shader_utils.py

Handles attachment/detachment of a _holdout_ shader, for creating emission map spritesheets.

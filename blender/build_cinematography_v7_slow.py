import bpy, os

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v6_camera.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v7_slow_camera.blend"

sc=bpy.context.scene
cam=sc.camera
target=bpy.data.objects.get("Cine Target")
if target is None:
    target=bpy.data.objects.new("Cine Target",None)
    bpy.context.collection.objects.link(target)

# Preserve scene geometry; replace only camera/target/lens animation.
cam.animation_data_clear()
target.animation_data_clear()
cam.data.animation_data_clear()

track=next((c for c in cam.constraints if c.name=="Cine Track"),None)
if track is None:
    track=cam.constraints.new(type="DAMPED_TRACK")
    track.name="Cine Track"
track.target=target
track.track_axis="TRACK_NEGATIVE_Z"
cam.data.clip_start=.05
cam.data.clip_end=1000
# Revised 26-second choreography.  Below-grade cameras stay back at ~10 m.
shots=[
 (1,   (-.30,-22.0, 3.30), ( .10,.70,-.45),42.0,"01 Establish"),
 (48,  (-.30,-22.0, 3.30), ( .10,.70,-.45),42.0,"02 Establish Hold"),
 (120, (-4.30,-14.0, 2.50), (-5.35,.15,1.25),46.0,"03 Rectifier Approach"),
 (168, (-4.30,-14.0, 2.50), (-5.35,.15,1.25),46.0,"04 Rectifier Hold"),
 (228, (-3.40,-10.5, 1.00), (-2.40,.00,-.55),44.0,"05 Positive Circuit"),
 (300, ( 1.80,-10.0,-.30), ( 3.80,1.00,-1.80),42.0,"06 Below Grade Wide"),
 (360, ( 5.30,-10.0,-.50), ( 5.50,2.25,-2.45),46.0,"07 Groundbed Anodes"),
 (432, ( 4.70,-10.5,-.45), ( 2.60,.00,-1.30),46.0,"08 Pipeline Sweep R"),
 (492, (-2.60,-10.5,-.45), (-2.20,.00,-1.30),46.0,"09 Pipeline Sweep L"),
 (540, (-4.20,-10.0, .15), (-4.20,-.15,-.75),48.0,"10 Negative Return"),
 (588, (-1.30,-11.0,1.65), (-1.30,.10,.95),50.0,"11 Test Station"),
 (624, (-.30,-23.5,3.45), ( .10,.70,-.45),44.0,"12 Resolve"),
]

for m in list(sc.timeline_markers):
    sc.timeline_markers.remove(m)

for frame,loc,tgt,lens,label in shots:
    cam.location=loc
    target.location=tgt
    cam.data.lens=lens
    cam.keyframe_insert("location",frame=frame)
    target.keyframe_insert("location",frame=frame)
    cam.data.keyframe_insert("lens",frame=frame)
    sc.timeline_markers.new(label,frame=frame)
sc.frame_start=1
sc.frame_end=624
sc.render.fps=24
sc.frame_set(1)

# Keep production scene settings; preview scripts will override resolution/samples only.
bpy.ops.wm.save_as_mainfile(filepath=OUT)

print("CINEMATOGRAPHY_V7_SAVED")
print("DURATION_SECONDS",round((sc.frame_end-sc.frame_start+1)/sc.render.fps,2))
print("SHOT_COUNT",len(shots))
print("OUT",OUT)

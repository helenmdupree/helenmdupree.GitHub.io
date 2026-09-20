import bpy, math, os
from mathutils import Vector

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v6_camera.blend"
PREVIEW=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v6_animatic.mp4"

sc=bpy.context.scene
cam=sc.camera

# New animated focus target; no technical object is moved.
target=bpy.data.objects.get("Cine Target")
if target is None:
    target=bpy.data.objects.new("Cine Target",None)
    bpy.context.collection.objects.link(target)

for con in list(cam.constraints):
    if con.name=="Cine Track":
        cam.constraints.remove(con)
track=cam.constraints.new(type="DAMPED_TRACK")
track.name="Cine Track"
track.target=target
track.track_axis="TRACK_NEGATIVE_Z"

cam.data.dof.use_dof=False
cam.data.clip_start=.05
cam.data.clip_end=1000
# Camera choreography: frame, camera location, target, lens.
shots=[
 (1,   (-.30,-29.0, 3.55), ( 0.0, .7,-.45), 44.0, "01 Field Establish"),
 (42,  (-4.55,-12.0, 2.65),(-5.35,.15, 1.30), 48.0, "02 Approach Rectifier"),
 (78,  (-5.00, -6.8, 2.05),(-5.45,.15, 1.28), 58.0, "03 Rectifier"),
 (112, (-3.80, -6.2, .55), (-2.4, .0,-.55), 52.0, "04 Positive Circuit"),
 (150, ( 2.80, -6.2,-.15), ( 4.7,1.5,-2.15), 48.0, "05 Below Grade"),
 (188, ( 6.40, -5.5,-1.65), ( 5.5,2.25,-3.05),52.0, "06 Groundbed Anodes"),
 (226, ( 5.40, -6.4,-1.10), ( 2.4, .0,-1.30), 50.0, "07 Pipeline Sweep R"),
 (264, (-2.80, -6.4,-1.05), (-3.2, .0,-1.30),50.0, "08 Pipeline Sweep L"),
 (300, (-4.75, -6.1,-.15), (-4.25,-.15,-.75),55.0, "09 Negative Return"),
 (332, (-1.30, -6.6, 1.30), (-1.30,.10, .92),58.0, "10 Test Station"),
 (360, (-.30,-25.0, 3.40), ( 0.0, .7,-.45), 46.0, "11 Resolve"),
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
sc.frame_end=360
sc.render.fps=24
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=12
sc.render.resolution_x=640
sc.render.resolution_y=360
sc.render.resolution_percentage=100
sc.render.film_transparent=False

frames_dir=os.path.join(os.path.dirname(OUT),"v6_animatic_frames")
os.makedirs(frames_dir,exist_ok=True)
sc.render.image_settings.file_format="PNG"
sc.render.filepath=os.path.join(frames_dir,"frame_")
# Freeze the approved technician at the frame-36 interaction pose.
# The camera moves; the technician does not wander through the animation.
tech=bpy.data.objects.get("Rig Technician")
if tech and tech.type=="ARMATURE":
    sc.frame_set(36)
    bpy.context.view_layer.update()
    pose_basis={pb.name:pb.matrix_basis.copy() for pb in tech.pose.bones}
    if tech.animation_data:
        tech.animation_data.action=None
    for name,mx in pose_basis.items():
        tech.pose.bones[name].matrix_basis=mx
    bpy.context.view_layer.update()

# Preserve the approved still-frame state as v5; cinematography lives only in v6.
sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=OUT)

print("CINEMATOGRAPHY_V6_SAVED")
print("FRAME_RANGE",sc.frame_start,sc.frame_end,"FPS",sc.render.fps)
print("SHOTS",len(shots))
print("OUTPUT",PREVIEW)

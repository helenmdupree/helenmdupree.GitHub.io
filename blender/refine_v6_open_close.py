import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v6_camera.blend"
sc=bpy.context.scene
cam=sc.camera
target=bpy.data.objects["Cine Target"]

for frame,loc,tgt,lens in [
    (1,   (-.30,-22.0,3.30),(0.10,.70,-.45),42.0),
    (360, (-.30,-23.5,3.45),(0.10,.70,-.45),44.0),
]:
    cam.location=loc
    target.location=tgt
    cam.data.lens=lens
    cam.keyframe_insert("location",frame=frame)
    target.keyframe_insert("location",frame=frame)
    cam.data.keyframe_insert("lens",frame=frame)

sc.frame_start=1
sc.frame_end=360
sc.render.fps=24
sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
print("V6_OPEN_CLOSE_REFINED")

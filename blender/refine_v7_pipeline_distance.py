import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v7_slow_camera.blend"
sc=bpy.context.scene
cam=sc.camera
target=bpy.data.objects["Cine Target"]

updates=[
 (300,( 1.80,-16.0,-.10),( 3.80,1.00,-1.70),40.0),
 (360,( 5.00,-16.0,-.30),( 5.50,2.25,-2.35),42.0),
 (432,( 4.30,-16.0,-.25),( 2.60,.00,-1.25),42.0),
 (492,(-2.40,-16.0,-.25),(-2.20,.00,-1.25),42.0),
 (540,(-4.10,-14.5, .20),(-4.20,-.15,-.75),46.0),
 (588,(-1.30,-13.0,1.70),(-1.30,.10,.95),48.0),
]

for frame,loc,tgt,lens in updates:
    cam.location=loc
    target.location=tgt
    cam.data.lens=lens
    cam.keyframe_insert("location",frame=frame)
    target.keyframe_insert("location",frame=frame)
    cam.data.keyframe_insert("lens",frame=frame)

sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
print("V7_PIPELINE_DISTANCE_REFINED")

import bpy, os

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v6_camera.blend"
OUTDIR=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\v6_storyboard"
frames=[1,42,78,112,150,188,226,264,300,332,360]

os.makedirs(OUTDIR,exist_ok=True)
sc=bpy.context.scene
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=12
sc.render.resolution_x=640
sc.render.resolution_y=360
sc.render.resolution_percentage=100
sc.render.image_settings.media_type="IMAGE"
sc.render.image_settings.file_format="PNG"

for f in frames:
    sc.frame_set(f)
    sc.render.filepath=os.path.join(OUTDIR,f"shot_{f:03d}.png")
    bpy.ops.render.render(write_still=True)
    print("RENDERED",f,sc.render.filepath)

print("STORYBOARD_FRAMES_DONE",len(frames))

import bpy, os

OUTDIR=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\v8_1_fix_checks"
os.makedirs(OUTDIR,exist_ok=True)

sc=bpy.context.scene
cam=sc.camera
target=bpy.data.objects["Cine Target"]
sc.frame_set(48)
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=20
sc.render.resolution_x=1200
sc.render.resolution_y=675
sc.render.resolution_percentage=100
sc.render.image_settings.media_type="IMAGE"
sc.render.image_settings.file_format="PNG"

old_cam=cam.matrix_world.copy()
old_tgt=target.location.copy()
old_lens=cam.data.lens

shots=[
    ("01_generic_work_pickup",(5.37,-4.6,2.15),(5.37,6.94,.93),58.0),
    ("02_negative_cadweld_mastic",(-4.15,-3.2,-.20),(-4.15,-.24,-.99),72.0),
    ("03_test_lead_cadweld_mastic",(-.55,-3.1,-.18),(-.55,-.10,-.92),72.0),
]

for name,loc,tgt,lens in shots:
    cam.location=loc
    target.location=tgt
    cam.data.lens=lens
    bpy.context.view_layer.update()
    sc.render.filepath=os.path.join(OUTDIR,name+".png")
    bpy.ops.render.render(write_still=True)
    print("RENDERED",name)

cam.matrix_world=old_cam
target.location=old_tgt
cam.data.lens=old_lens
bpy.context.view_layer.update()
print("CHECKS_DONE")

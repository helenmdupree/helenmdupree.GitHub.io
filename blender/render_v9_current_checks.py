import bpy, os

OUTDIR=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\v9_current_checks"
shots=[(180,"01_rectifier_energized"),(265,"02_positive_circuit"),
       (365,"03_groundbed_anodes"),(450,"04_soil_pipeline"),
       (525,"05_negative_return"),(575,"06_test_measurement")]

os.makedirs(OUTDIR,exist_ok=True)
sc=bpy.context.scene
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=16
sc.render.resolution_x=800
sc.render.resolution_y=450
sc.render.resolution_percentage=100
sc.render.image_settings.media_type="IMAGE"
sc.render.image_settings.file_format="PNG"

for f,name in shots:
    sc.frame_set(f)
    sc.render.filepath=os.path.join(OUTDIR,name+".png")
    bpy.ops.render.render(write_still=True)
    print("RENDERED",f,name)

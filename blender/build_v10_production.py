import bpy, os

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v9_1_return_direction.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v10_production.blend"
FRAMES=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\v10_frames"

sc=bpy.context.scene

# Production timing/output.
sc.frame_start=1
sc.frame_end=624
sc.frame_step=1
sc.render.fps=24
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=8
sc.render.resolution_x=1280
sc.render.resolution_y=720
sc.render.resolution_percentage=100
sc.render.image_settings.media_type="IMAGE"
sc.render.image_settings.file_format="PNG"
sc.render.image_settings.color_mode="RGB"
sc.render.image_settings.color_depth="8"
sc.render.filepath=os.path.join(FRAMES,"frame_")
sc.render.use_file_extension=True

# Cinematic motion without smearing technical detail.
sc.render.use_motion_blur=True
sc.render.motion_blur_shutter=.22
sc.render.motion_blur_position="CENTER"
# Keep AgX color management from the realism master.
sc.view_settings.view_transform="AgX"
sc.view_settings.exposure=-.12

# Tone down explanatory current effects so they do not read as neon.
for mat_name,strength in [
    ("FX Positive Pulse",2.15),
    ("FX Negative Pulse",2.05),
    ("FX Soil Current",1.45),
    ("FX Measurement",1.25),
    ("FX Meter Energized",1.15),
]:
    m=bpy.data.materials.get(mat_name)
    if not m or not m.use_nodes:
        continue
    em=next((n for n in m.node_tree.nodes if n.bl_idname=="ShaderNodeEmission"),None)
    if em:
        # Preserve animated meter keys; only reduce non-animated steady materials here.
        if mat_name!="FX Meter Energized":
            em.inputs["Strength"].default_value=strength

# Guardrails: corrected truck and pipe connections must be present.
assert bpy.data.objects.get("Truck Generic Work Pickup") is not None
assert bpy.data.objects.get("Negative Cadweld Mastic") is not None
assert bpy.data.objects.get("Test Lead Cadweld Mastic") is not None
assert bpy.data.objects.get("Permanent Reference Electrode") is not None
# Guardrail: animated negative return must run pipe -> rectifier.
ret=bpy.data.objects["FX Negative Return"]
sp=ret.data.splines[0]
pts=[tuple(p.co[:3]) for p in sp.points]
assert pts[0][0] > pts[-1][0], "Negative return overlay is not reversed pipe-to-rectifier"

os.makedirs(FRAMES,exist_ok=True)

# Save a new production master; v9.1 remains untouched.
sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=OUT)

print("V10_PRODUCTION_SAVED",OUT)
print("OUTPUT_FRAMES",FRAMES)
print("RESOLUTION",sc.render.resolution_x,sc.render.resolution_y)
print("FPS",sc.render.fps,"FRAMES",sc.frame_start,sc.frame_end)
print("SAMPLES",sc.eevee.taa_render_samples)
print("MOTION_BLUR",sc.render.use_motion_blur,sc.render.motion_blur_shutter)
print("RETURN_START",tuple(round(v,3) for v in pts[0]))
print("RETURN_END",tuple(round(v,3) for v in pts[-1]))

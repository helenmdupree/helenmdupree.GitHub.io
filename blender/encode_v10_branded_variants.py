import bpy, os, sys

ROOT=r"C:\GitHub\soubel-iccp-v5-cleanstart"
FRAMES=os.path.join(ROOT,"blender","v10_frames")
EXPECTED=624

VARIANTS=[
    ("url_only",
     os.path.join(ROOT,"blender","branding_overlays","overlay_soubel_url.png"),
     os.path.join(ROOT,"blender","iccp_cinematic_v10_SOUBEL_url_720p24.mp4")),
    ("logo_url",
     os.path.join(ROOT,"blender","branding_overlays","overlay_soubel_logo_url.png"),
     os.path.join(ROOT,"blender","iccp_cinematic_v10_SOUBEL_logo_url_720p24.mp4")),
]

missing=[i for i in range(1,EXPECTED+1)
         if not os.path.exists(os.path.join(FRAMES,f"frame_{i:04d}.png"))]
if missing:
    print("MISSING_FRAMES",len(missing),missing[:20])
    raise SystemExit(2)
def add_base_sequence(sc):
    sc.sequence_editor_clear()
    se=sc.sequence_editor_create()
    first=os.path.join(FRAMES,"frame_0001.png")
    base=se.strips.new_image("ICCP v10 Production",first,1,1,fit_method="FIT")
    for i in range(2,EXPECTED+1):
        base.elements.append(f"frame_{i:04d}.png")
    return se

for label,overlay_path,out in VARIANTS:
    sc=bpy.context.scene
    se=add_base_sequence(sc)
    ov=se.strips.new_image("SOUBEL Branding",overlay_path,2,1,fit_method="ORIGINAL")
    ov.frame_final_duration=EXPECTED
    ov.blend_type="ALPHA_OVER"

    sc.frame_start=1
    sc.frame_end=EXPECTED
    sc.render.fps=24
    sc.render.resolution_x=1280
    sc.render.resolution_y=720
    sc.render.resolution_percentage=100
    sc.render.image_settings.media_type="VIDEO"
    sc.render.image_settings.file_format="FFMPEG"
    sc.render.ffmpeg.format="MPEG4"
    sc.render.ffmpeg.codec="H264"
    sc.render.ffmpeg.constant_rate_factor="MEDIUM"
    sc.render.ffmpeg.ffmpeg_preset="GOOD"
    sc.render.filepath=out

    bpy.ops.render.render(animation=True)
    print("BRANDED_ENCODE_DONE",label,out,os.path.getsize(out) if os.path.exists(out) else -1)

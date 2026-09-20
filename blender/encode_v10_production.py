import bpy, os, sys

FRAMES=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\v10_frames"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v10_production_720p24.mp4"
EXPECTED=624

missing=[i for i in range(1,EXPECTED+1)
         if not os.path.exists(os.path.join(FRAMES,f"frame_{i:04d}.png"))]
if missing:
    print("MISSING_FRAMES",len(missing),missing[:20])
    raise SystemExit(2)

sc=bpy.context.scene
sc.sequence_editor_clear()
se=sc.sequence_editor_create()

first=os.path.join(FRAMES,"frame_0001.png")
strip=se.strips.new_image("ICCP v10 Production",first,1,1,fit_method="FIT")
for i in range(2,EXPECTED+1):
    strip.elements.append(f"frame_{i:04d}.png")

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
sc.render.filepath=OUT

bpy.ops.render.render(animation=True)

print("V10_ENCODE_DONE",OUT)
print("SIZE",os.path.getsize(OUT) if os.path.exists(OUT) else -1)

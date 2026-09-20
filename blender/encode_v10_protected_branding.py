import bpy, os

ROOT=r"C:\GitHub\soubel-iccp-v5-cleanstart"
FRAMES=os.path.join(ROOT,"blender","v10_frames")
BOTTOM=os.path.join(ROOT,"blender","branding_overlays","overlay_soubel_logo_url.png")
OUT=os.path.join(ROOT,"blender","iccp_cinematic_v10_SOUBEL_protected_720p24.mp4")
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
base=se.strips.new_image("ICCP v10 Production",first,1,1,fit_method="FIT")
for i in range(2,EXPECTED+1):
    base.elements.append(f"frame_{i:04d}.png")
# Formal fixed branding along the lower edge.
brand=se.strips.new_image("SOUBEL Formal Branding",BOTTOM,2,1,fit_method="ORIGINAL")
brand.frame_final_duration=EXPECTED
brand.blend_type="ALPHA_OVER"

# Subtle interior watermark positions, changed at major camera/story beats.
segments=[
    (1,119,(0.82,0.82)),
    (120,227,(0.18,0.66)),
    (228,359,(0.22,0.82)),
    (360,491,(0.78,0.62)),
    (492,587,(0.62,0.80)),
    (588,624,(0.20,0.56)),
]

for idx,(start,end,loc) in enumerate(segments,1):
    length=end-start+1
    t=se.strips.new_effect(f"SOUBEL Watermark {idx}","TEXT",2+idx,start,length=length)
    t.text="SOUBEL.com"
    t.location=loc
    t.font_size=34
    t.alignment_x="CENTER"
    t.color=(1.0,1.0,1.0,1.0)
    t.blend_alpha=0.16
    t.use_shadow=True
    t.shadow_color=(0.0,0.0,0.0,0.30)
    t.shadow_blur=2.0
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

print("PROTECTED_ENCODE_DONE",OUT)
print("SIZE",os.path.getsize(OUT) if os.path.exists(OUT) else -1)

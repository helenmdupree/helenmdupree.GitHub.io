import bpy, os

OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_v9_1_negative_return_segment.mp4"
sc=bpy.context.scene
sc.frame_start=470
sc.frame_end=575
sc.frame_step=2
sc.render.fps=12
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=2
sc.render.resolution_x=640
sc.render.resolution_y=360
sc.render.resolution_percentage=100
sc.render.image_settings.media_type="VIDEO"
sc.render.image_settings.file_format="FFMPEG"
sc.render.ffmpeg.format="MPEG4"
sc.render.ffmpeg.codec="H264"
sc.render.ffmpeg.constant_rate_factor="MEDIUM"
sc.render.ffmpeg.ffmpeg_preset="GOOD"
sc.render.filepath=OUT
bpy.ops.render.render(animation=True)
print("RETURN_SEGMENT_DONE",os.path.getsize(OUT) if os.path.exists(OUT) else -1)

import bpy

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v9_current_animation.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v9_1_return_direction.blend"

o=bpy.data.objects["FX Negative Return"]
for s in o.data.splines:
    if s.type=="POLY":
        vals=[tuple(p.co) for p in s.points]
        for p,co in zip(s.points,reversed(vals)):
            p.co=co
    elif s.type=="BEZIER":
        vals=[(p.co.copy(),p.handle_left.copy(),p.handle_right.copy(),
               p.handle_left_type,p.handle_right_type) for p in s.bezier_points]
        vals=list(reversed(vals))
        for p,(co,hl,hr,hlt,hrt) in zip(s.bezier_points,vals):
            p.co=co
            p.handle_left=hr
            p.handle_right=hl
            p.handle_left_type=hrt
            p.handle_right_type=hlt
    else:
        vals=[tuple(p.co) for p in s.points]
        for p,co in zip(s.points,reversed(vals)):
            p.co=co

# Keep the existing reveal timing: frame 492 -> 558.
o.data.bevel_factor_start=0.0

# Save as a new corrected master.
bpy.ops.wm.save_as_mainfile(filepath=OUT)

s=o.data.splines[0]
pts=[tuple(round(v,3) for v in p.co[:3]) for p in s.points]
print("V9_1_SAVED",OUT)
print("RETURN_POINT_ORDER",pts)
print("EXPECTED_START_PIPE",pts[0])
print("EXPECTED_END_RECTIFIER",pts[-1])

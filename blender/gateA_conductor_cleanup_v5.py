import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateA_clean.png"

def tube(name,pts,r,mat):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(mat); return o

black=bpy.data.materials.get("Black")

# Remove the awkward diagonal service path from Gate A.
for n in ["Utility Conductor","Utility Conductor.001","AC Service"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

# Keep only clean distant background utility conductors at the pole.
ux,uy=-13.0,32.0
tube("Utility Conductor",[(ux-4.0,uy,7.42),(ux+4.0,uy,7.42)],.008,black)
tube("Utility Conductor.001",[(ux-4.0,uy+.16,7.28),(ux+4.0,uy+.16,7.28)],.008,black)

sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_A_CLEAN_SAVED")
print("AC_SERVICE_PRESENT",bool(bpy.data.objects.get("AC Service")))

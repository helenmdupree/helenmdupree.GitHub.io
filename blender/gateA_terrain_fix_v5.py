import bpy
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateA_terrain_fixed.png"

def tube(name,pts,r,mat):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(mat); return o

# Extend the approved surface plane far into the background so the utility pole is grounded.
ground=bpy.data.objects.get("Ground Surface")
if ground:
    ground.location.y=15.0
    ground.dimensions.y=42.0
    bpy.context.view_layer.objects.active=ground
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)

black=bpy.data.materials.get("Black")
ux,uy=-13.0,32.0
rx,ry=-5.5,.15

# Replace only the utility/service conductors with a cleaner distant-source route.
for n in ["Utility Conductor","Utility Conductor.001","AC Service"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

tube("Utility Conductor",[(ux-2.4,uy,7.42),(ux,uy,7.42),(-10.2,25.0,7.05),(-8.2,14.0,6.35)],.008,black)
tube("Utility Conductor.001",[(ux-2.4,uy+.12,7.42),(ux,uy+.12,7.42),(-10.1,25.1,7.02),(-8.1,14.1,6.32)],.008,black)
tube("AC Service",[(-8.15,14.05,6.34),(-7.3,8.0,5.15),(-6.25,3.6,3.55),(rx,ry,1.86)],.010,black)

sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("TERRAIN_FIX_SAVED")
print("GROUND_Y_RANGE",round(ground.location.y-ground.dimensions.y/2,2),round(ground.location.y+ground.dimensions.y/2,2))
print("UTILITY_POLE_Y",bpy.data.objects["Utility Pole"].location.y)

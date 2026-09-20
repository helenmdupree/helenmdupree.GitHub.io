import bpy
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateA_final.png"

def tube(name,pts,r,mat):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(mat); return o

def look(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat("-Z","Y").to_euler()

black=bpy.data.materials.get("Black")

# Move only the utility-source assembly into the distant background.
dx,dy=(-3.2,24.8)
for o in list(bpy.data.objects):
    if o.name=="Utility Pole" or o.name=="Utility Crossarm" or o.name.startswith("Utility Insulator"):
        o.location.x += dx
        o.location.y += dy

ux,uy=-13.0,32.0
# Rebuild the simple utility conductors and service route from the new pole location.
for n in ["Utility Conductor","Utility Conductor.001","AC Service"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

tube("Utility Conductor",[(ux-2.3,uy,7.42),(ux,uy,7.42),(-8.0,8.0,6.3)],.010,black)
tube("Utility Conductor.001",[(ux-2.3,uy+.12,7.42),(ux,uy+.12,7.42),(-7.7,8.1,6.15)],.010,black)
tube("AC Service",[(-7.8,8.0,6.2),(-6.8,4.0,4.4),(-5.5,.15,1.85)],.014,black)

# Camera refinement only: slightly wider, farther back, and more cinematic.
cam=bpy.context.scene.camera
cam.location=(-.3,-29.0,3.55)
cam.data.lens=44
look(cam,(-.2,1.8,-.50))

sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_A_FINAL_SAVED")
print("UTILITY_LOC",tuple(round(v,2) for v in bpy.data.objects["Utility Pole"].location))
print("CAM_LOC",tuple(round(v,2) for v in cam.location))
print("CAM_LENS",cam.data.lens)

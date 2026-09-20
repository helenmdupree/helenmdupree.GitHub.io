import bpy
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_technician12.png"

sc=bpy.context.scene
sc.frame_set(36)
arm=bpy.data.objects["Rig Technician"]

LOCKED=["30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head",
"Utility Pole","Permanent Reference Electrode","Camera","Anode 1","Anode 2","Anode 3",
"Anode 4","Anode 5","Truck Real Pickup 09"]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),tuple(bpy.data.objects[n].scale)) for n in LOCKED}

# Measured from evaluated boot tread geometry: sole bottom 1.04 m, ground top 0.04 m.
arm.location.z -= 1.0
bpy.context.view_layer.update()
# Re-seat hardhat pieces to the lowered head position.
head=arm.matrix_world @ arm.pose.bones["scout:head"].head
dome=bpy.data.objects.get("Rig Tech Hardhat Dome")
brim=bpy.data.objects.get("Rig Tech Hardhat Brim")
if dome:
    dome.location=(head.x,head.y,head.z+.145)
if brim:
    brim.location=(head.x,head.y-.005,head.z+.095)

# Confirm boot soles land on grade using evaluated mesh geometry.
dg=bpy.context.evaluated_depsgraph_get()
sole_z=[]
for o in bpy.data.objects:
    if o.name.startswith("Rig Tech |") and "boot-tread" in o.name.lower() and o.type=="MESH" and not o.hide_render:
        ev=o.evaluated_get(dg); me=ev.to_mesh()
        sole_z.extend([(ev.matrix_world@v.co).z for v in me.vertices])
        ev.to_mesh_clear()

ground_top=bpy.data.objects["Ground Surface"].location.z+bpy.data.objects["Ground Surface"].dimensions.z/2
# Verify all non-technician scene geometry stayed frozen.
changed=[]
for n,(loc0,rot0,scale0) in baseline.items():
    o=bpy.data.objects[n]
    now=(tuple(o.location),tuple(o.rotation_euler),tuple(o.scale))
    for label,a,b in (("location",loc0,now[0]),("rotation",rot0,now[1]),("scale",scale0,now[2])):
        if any(abs(x-y)>1e-7 for x,y in zip(a,b)):
            changed.append((n,label))
if changed:
    raise RuntimeError("Locked transforms changed: "+repr(changed))

bones=[b.name for b in arm.data.bones]
assert bones.count("scout:upperarm01.L")==1
assert bones.count("scout:upperarm01.R")==1

sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)
wrist=arm.matrix_world @ arm.pose.bones["scout:wrist.L"].head
print("TECHNICIAN12_RENDERED")
print("LOCK_CHANGES",len(changed))
print("GROUND_TOP",round(ground_top,4))
print("SOLE_MIN",round(min(sole_z),4))
print("LEFT_WRIST",tuple(round(v,3) for v in wrist))
print("HEAD",tuple(round(v,3) for v in head))
print("ARM_COUNTS",bones.count("scout:upperarm01.L"),bones.count("scout:upperarm01.R"))

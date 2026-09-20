import bpy, math
from mathutils import Vector, Matrix

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
GLB=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\assets\3dassets\rigged_technician_base\rigged_scout.glb"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_technician10.png"

LOCKED=["30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head","Utility Pole",
"Permanent Reference Electrode","Camera","Anode 1","Anode 2","Anode 3","Anode 4","Anode 5","Truck Real Pickup 09"]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),tuple(bpy.data.objects[n].scale)) for n in LOCKED}

# Preserve old technician, but remove it from this render.
for o in bpy.data.objects:
    if o.name.startswith("Tech"):
        o.hide_render=True
        o.hide_set(True)

old_hat=bpy.data.objects.get("Tech Hardhat")
hat=old_hat.copy()
hat.data=old_hat.data.copy()
bpy.context.collection.objects.link(hat)
hat.name="Rig Tech Hardhat"
hat.hide_render=False
hat.hide_set(False)
before=set(bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=GLB)
added=[o for o in bpy.data.objects if o not in before]
arm=next(o for o in added if o.type=="ARMATURE")
arm.name="Rig Technician"
arm.rotation_mode="XYZ"
arm.rotation_euler=(0,0,math.radians(-129))
arm.scale=(1.02,1.02,1.02)

# Hide the scout field cap; PPE hardhat will replace it.
for n in ["field-cap-crown","field-cap-band","stitched-cap-visor"]:
    o=bpy.data.objects.get(n)
    if o:
        o.hide_render=True
        o.hide_set(True)

# High-vis work shirt / dark trousers / boots.
def base_color(matname,color,rough=None):
    m=bpy.data.materials.get(matname)
    if m and m.use_nodes:
        bs=m.node_tree.nodes.get("Principled BSDF")
        if bs:
            bs.inputs["Base Color"].default_value=(*color,1)
            if rough is not None: bs.inputs["Roughness"].default_value=rough

base_color("scout-cloth",(.48,.62,.045),.62)
base_color("scout-pants",(.025,.045,.065),.72)
base_color("scout-leather",(.035,.035,.03),.62)
# Use the rig's grasp animation at a stable one-hand interaction pose.
arm.animation_data_create()
arm.animation_data.action=bpy.data.actions.get("grasp")
sc=bpy.context.scene
sc.frame_set(36)
bpy.context.view_layer.update()

# Aim the reaching wrist at the existing rectifier control area.
target_xy=Vector((-5.22,-0.10,0))
wrist=arm.matrix_world @ arm.pose.bones["scout:wrist.L"].head
arm.location.x += target_xy.x-wrist.x
arm.location.y += target_xy.y-wrist.y
bpy.context.view_layer.update()

# Put the full skinned figure on grade without moving the scene.
rig_meshes=[o for o in added if o.type=="MESH" and o.find_armature()==arm]
pts=[]
for o in rig_meshes:
    if not o.hide_render:
        pts.extend([o.matrix_world@Vector(c) for c in o.bound_box])
minz=min(p.z for p in pts)
arm.location.z += .02-minz
bpy.context.view_layer.update()

# Attach the preserved hardhat to the actual head bone.
head=arm.matrix_world @ arm.pose.bones["scout:head"].head
hat.scale=(.78,.78,.78)
hat.rotation_mode="XYZ"
hat.rotation_euler=(0,0,arm.rotation_euler.z)
hat.location=(head.x,head.y,head.z+.14)
# Give the hardhat a more realistic safety-white material and parent it to the head bone.
hm=bpy.data.materials.get("Rig Hardhat White") or bpy.data.materials.new("Rig Hardhat White")
hm.use_nodes=True
hbs=hm.node_tree.nodes.get("Principled BSDF")
hbs.inputs["Base Color"].default_value=(.72,.76,.77,1)
hbs.inputs["Roughness"].default_value=.36
hbs.inputs["Metallic"].default_value=.06
hat.data.materials.clear()
hat.data.materials.append(hm)
for poly in hat.data.polygons: poly.use_smooth=True

world=hat.matrix_world.copy()
hat.parent=arm
hat.parent_type="BONE"
hat.parent_bone="scout:head"
hat.matrix_world=world

# Rename imported rig objects for easy recovery/audit.
for o in added:
    if o is not arm:
        o.name="Rig Tech | "+o.name

# Verify only the technician changed.
changed=[]
for n,(loc0,rot0,scale0) in baseline.items():
    o=bpy.data.objects[n]
    now=(tuple(o.location),tuple(o.rotation_euler),tuple(o.scale))
    for label,a,b in (("location",loc0,now[0]),("rotation",rot0,now[1]),("scale",scale0,now[2])):
        if any(abs(x-y)>1e-7 for x,y in zip(a,b)):
            changed.append((n,label))
if changed:
    raise RuntimeError("Locked transforms changed: "+repr(changed))
# Anatomy sanity check: one left arm chain, one right arm chain.
bones=[b.name for b in arm.data.bones]
left_upper=[n for n in bones if n=="scout:upperarm01.L"]
right_upper=[n for n in bones if n=="scout:upperarm01.R"]
if len(left_upper)!=1 or len(right_upper)!=1:
    raise RuntimeError("Unexpected arm anatomy")

sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

wrist=arm.matrix_world @ arm.pose.bones["scout:wrist.L"].head
head=arm.matrix_world @ arm.pose.bones["scout:head"].head
print("TECHNICIAN10_SAVED")
print("LOCK_CHANGES",len(changed))
print("ARM_BONES",len(bones),"LEFT_UPPER",len(left_upper),"RIGHT_UPPER",len(right_upper))
print("LEFT_WRIST",tuple(round(v,3) for v in wrist))
print("HEAD",tuple(round(v,3) for v in head))
print("ARM_LOC",tuple(round(v,3) for v in arm.location))

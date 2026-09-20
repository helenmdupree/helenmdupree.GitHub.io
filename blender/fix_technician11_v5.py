import bpy, math
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_technician11.png"
arm=bpy.data.objects["Rig Technician"]
sc=bpy.context.scene
sc.frame_set(36)

def simple(name,color,rough=.6,metal=.0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value=(*color,1)
    bs.inputs["Roughness"].default_value=rough
    bs.inputs["Metallic"].default_value=metal
    return m

hivis=simple("Tech HiVis",(.62,.78,.045),.58)
navy=simple("Tech Navy",(.018,.032,.052),.70)
boot=simple("Tech Boot",(.025,.022,.018),.62)
white=simple("Tech Hardhat White",(.82,.84,.83),.38,.05)
# Reassign visible workwear directly so imported texture nodes cannot override the colors.
for o in bpy.data.objects:
    if not o.name.startswith("Rig Tech |") or o.type!="MESH":
        continue
    lname=o.name.lower()
    if any(k in lname for k in ["overshirt","collar","placket","map-pocket","instrument-pocket"]):
        o.data.materials.clear(); o.data.materials.append(hivis)
    elif "trousers" in lname:
        o.data.materials.clear(); o.data.materials.append(navy)
    elif any(k in lname for k in ["field-boot","layered-sole","boot-lacing","boot-tongue","boot-tread","boot-eyelet"]):
        o.data.materials.clear(); o.data.materials.append(boot)

# Reorient the technician more squarely toward the cabinet.
arm.rotation_mode="XYZ"
arm.rotation_euler=(0,0,math.radians(-95))
bpy.context.view_layer.update()

# Keep the reaching left wrist on the cabinet front edge.
target=Vector((-5.22,-0.14,0))
w=arm.matrix_world @ arm.pose.bones["scout:wrist.L"].head
arm.location.x += target.x-w.x
arm.location.y += target.y-w.y
bpy.context.view_layer.update()
# Re-ground after reorientation.
rig_meshes=[o for o in bpy.data.objects if o.name.startswith("Rig Tech |") and o.type=="MESH" and not o.hide_render]
pts=[]
for o in rig_meshes:
    pts.extend([o.matrix_world@Vector(c) for c in o.bound_box])
minz=min(p.z for p in pts)
arm.location.z += .02-minz
bpy.context.view_layer.update()

# Remove the misplaced copied hardhat and build a compact safety hardhat at the actual head bone.
old=bpy.data.objects.get("Rig Tech Hardhat")
if old:
    bpy.data.objects.remove(old,do_unlink=True)

head=arm.matrix_world @ arm.pose.bones["scout:head"].head
bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, location=(head.x,head.y,head.z+.145))
dome=bpy.context.object; dome.name="Rig Tech Hardhat Dome"
dome.scale=(.165,.145,.085)
bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
dome.data.materials.append(white)
for poly in dome.data.polygons: poly.use_smooth=True

bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=.18, depth=.025, location=(head.x,head.y-.005,head.z+.095))
brim=bpy.context.object; brim.name="Rig Tech Hardhat Brim"
brim.scale=(1.0,.83,1.0)
bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
brim.data.materials.append(white)
# Keep the hat pieces grouped with the technician for later animation work.
for o in (dome,brim):
    o.rotation_euler=(0,0,arm.rotation_euler.z)

# Anatomy sanity check remains explicit.
bones=[b.name for b in arm.data.bones]
assert bones.count("scout:upperarm01.L")==1
assert bones.count("scout:upperarm01.R")==1

# Save and render this correction pass.
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

w=arm.matrix_world @ arm.pose.bones["scout:wrist.L"].head
h=arm.matrix_world @ arm.pose.bones["scout:head"].head
print("TECHNICIAN11_RENDERED")
print("WRIST",tuple(round(v,3) for v in w))
print("HEAD",tuple(round(v,3) for v in h))
print("ARM_LOC",tuple(round(v,3) for v in arm.location))
print("ARM_COUNTS",bones.count("scout:upperarm01.L"),bones.count("scout:upperarm01.R"))

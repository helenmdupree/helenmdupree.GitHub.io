import bpy, math
from mathutils import Vector

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v8_realism.blend"
GLB=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\assets\3dassets\generic_work_pickup_canopy\generic_work_pickup_canopy.glb"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v8_1_realism_truckfix.blend"

# Hide prior truck, preserve for rollback.
for o in bpy.data.objects:
    if o.name=="Truck Real Pickup 09" or o.name.startswith("Truck 09 |"):
        o.hide_render=True
        o.hide_set(True)

before=set(bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=GLB)
added=[o for o in bpy.data.objects if o not in before]

root=next(o for o in added if o.type=="EMPTY" and o.parent is None and o.name.startswith("double-cab-pickup-canopy"))
keep=set()
def collect(o):
    keep.add(o)
    for ch in o.children:
        collect(ch)
collect(root)

for o in list(added):
    if o not in keep:
        bpy.data.objects.remove(o,do_unlink=True)

root.name="Truck Generic Work Pickup"
root.rotation_mode="XYZ"
root.rotation_euler=(0,0,math.radians(-90))
root.scale=(1,1,1)
root.location=(5.37,6.94,0.02)
bpy.context.view_layer.update()
# Normalize imported truck materials to a neutral field-service palette.
used_mats=set()
for o in keep:
    if o.type=="MESH":
        for m in o.data.materials:
            if m: used_mats.add(m)

for m in used_mats:
    m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    if not bs: continue
    n=m.name.lower()
    # Disconnect imported color textures where necessary so the result is clean and neutral.
    if n.startswith("paint"):
        for link in list(bs.inputs["Base Color"].links): m.node_tree.links.remove(link)
        bs.inputs["Base Color"].default_value=(.72,.75,.77,1)
        bs.inputs["Roughness"].default_value=.27
        bs.inputs["Metallic"].default_value=.06
        bs.inputs["Coat Weight"].default_value=.38
        bs.inputs["Coat Roughness"].default_value=.18
    elif n.startswith("glass"):
        for link in list(bs.inputs["Base Color"].links): m.node_tree.links.remove(link)
        bs.inputs["Base Color"].default_value=(.025,.055,.07,1)
        bs.inputs["Roughness"].default_value=.12
        bs.inputs["Transmission Weight"].default_value=.58
        bs.inputs["IOR"].default_value=1.45
    elif n.startswith("trim"):
        for link in list(bs.inputs["Base Color"].links): m.node_tree.links.remove(link)
        bs.inputs["Base Color"].default_value=(.018,.02,.022,1)
        bs.inputs["Roughness"].default_value=.62
        bs.inputs["Metallic"].default_value=.02
    elif n.startswith("alloy"):
        for link in list(bs.inputs["Base Color"].links): m.node_tree.links.remove(link)
        bs.inputs["Base Color"].default_value=(.32,.34,.35,1)
        bs.inputs["Roughness"].default_value=.24
        bs.inputs["Metallic"].default_value=.78
    elif n.startswith("interior"):
        for link in list(bs.inputs["Base Color"].links): m.node_tree.links.remove(link)
        bs.inputs["Base Color"].default_value=(.055,.06,.065,1)
        bs.inputs["Roughness"].default_value=.72

# Rename imported hierarchy for auditability.
for o in list(keep):
    if o is not root:
        o.name="Truck Generic | "+o.name

# Re-center precisely on the old truck footprint and ground the tyres.
pts=[]
for o in keep:
    if o.type=="MESH":
        pts.extend([o.matrix_world@Vector(c) for c in o.bound_box])
mins=[min(p[i] for p in pts) for i in range(3)]
maxs=[max(p[i] for p in pts) for i in range(3)]
center=[(mins[i]+maxs[i])/2 for i in range(3)]
root.location.x += 5.37-center[0]
root.location.y += 6.94-center[1]
root.location.z += .02-mins[2]
bpy.context.view_layer.update()

# Final measured bounds.
pts=[]
for o in keep:
    if o.type=="MESH":
        pts.extend([o.matrix_world@Vector(c) for c in o.bound_box])
mins=[min(p[i] for p in pts) for i in range(3)]
maxs=[max(p[i] for p in pts) for i in range(3)]
dims=[maxs[i]-mins[i] for i in range(3)]
center=[(mins[i]+maxs[i])/2 for i in range(3)]

# Technical corrections must survive the truck replacement.
assert bpy.data.objects.get("Negative Cadweld Mastic") is not None
assert bpy.data.objects.get("Test Lead Cadweld Mastic") is not None
assert bpy.data.objects.get("Permanent Reference Electrode") is not None

bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("V8_1_TRUCKFIX_SAVED",OUT)
print("TRUCK_DIMS",tuple(round(v,3) for v in dims))
print("TRUCK_CENTER",tuple(round(v,3) for v in center))
print("TRUCK_MINZ",round(mins[2],3))
print("NEG_MASTIC",tuple(round(v,4) for v in bpy.data.objects["Negative Cadweld Mastic"].location))
print("TEST_MASTIC",tuple(round(v,4) for v in bpy.data.objects["Test Lead Cadweld Mastic"].location))

import bpy, math
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
GLB=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\assets\3dassets\modern_double_cab_pickup\modern_double_cab_pickup.glb"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_truck09.png"

LOCKED=["30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head","Utility Pole",
"Permanent Reference Electrode","Camera","Anode 1","Anode 2","Anode 3","Anode 4","Anode 5"]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),tuple(bpy.data.objects[n].scale)) for n in LOCKED}

for o in bpy.data.objects:
    if o.name.startswith("Truck"):
        o.hide_render=True
        o.hide_set(True)

before=set(bpy.data.objects)
bpy.ops.import_scene.gltf(filepath=GLB)
added=[o for o in bpy.data.objects if o not in before]
root=next(o for o in added if o.type=="EMPTY" and o.parent is None and o.name.startswith("double-cab-pickup"))
keep=set()
def collect(o):
    keep.add(o)
    for ch in o.children: collect(ch)
collect(root)
for o in list(added):
    if o not in keep:
        bpy.data.objects.remove(o,do_unlink=True)

root.name="Truck Real Pickup 09"
root.rotation_mode="XYZ"
root.rotation_euler=(0,0,math.radians(-90))
s=4.75/5.652
root.scale=(s,s,s)
bpy.context.view_layer.update()

def bbox():
    pts=[]
    for o in keep:
        if o.type=="MESH":
            pts.extend([o.matrix_world@Vector(c) for c in o.bound_box])
    mins=[min(p[i] for p in pts) for i in range(3)]
    maxs=[max(p[i] for p in pts) for i in range(3)]
    return mins,maxs
mins,maxs=bbox()
cx,cy=(mins[0]+maxs[0])/2,(mins[1]+maxs[1])/2
root.location+=(Vector((5.37-cx,6.94-cy,.02-mins[2])))
bpy.context.view_layer.update()
paint=next((m for m in bpy.data.materials if m.name=="paint" or m.name.startswith("paint.")),None)
if paint and paint.use_nodes:
    bs=paint.node_tree.nodes.get("Principled BSDF")
    if bs:
        bs.inputs["Base Color"].default_value=(.72,.75,.76,1)
        bs.inputs["Metallic"].default_value=.08
        bs.inputs["Roughness"].default_value=.32

for o in list(keep):
    if o is not root:
        o.name="Truck 09 | "+o.name

changed=[]
for n,(loc0,rot0,scale0) in baseline.items():
    o=bpy.data.objects[n]
    now=(tuple(o.location),tuple(o.rotation_euler),tuple(o.scale))
    for label,a,b in (("location",loc0,now[0]),("rotation",rot0,now[1]),("scale",scale0,now[2])):
        if any(abs(x-y)>1e-7 for x,y in zip(a,b)):
            changed.append((n,label))
if changed:
    raise RuntimeError("Locked transforms changed: "+repr(changed))
mins,maxs=bbox()
dims=[maxs[i]-mins[i] for i in range(3)]
center=[(mins[i]+maxs[i])/2 for i in range(3)]

sc=bpy.context.scene
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("TRUCK09_SAVED")
print("LOCK_CHANGES",len(changed))
print("TRUCK_DIMS",tuple(round(v,3) for v in dims))
print("TRUCK_CENTER",tuple(round(v,3) for v in center))
print("TRUCK_MIN_Z",round(mins[2],3))

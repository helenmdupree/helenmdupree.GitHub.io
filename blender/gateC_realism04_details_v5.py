import bpy, math, random
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_realism04.png"

LOCKED=[
 "30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head",
 "Utility Pole","Truck Body","Truck Cab","Truck Bed","Permanent Reference Electrode",
 "Camera","Anode 1","Anode 2","Anode 3","Anode 4","Anode 5"
]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),
             tuple(bpy.data.objects[n].scale)) for n in LOCKED}

def mat(name,color,rough=.6,metal=.0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value=(*color,1)
    bs.inputs["Roughness"].default_value=rough
    bs.inputs["Metallic"].default_value=metal
    return m
def box(name,loc,dims,m,bev=.02):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bev:
        md=o.modifiers.new("Bevel","BEVEL"); md.width=bev; md.segments=3
    o.data.materials.append(m)
    return o

def cyl(name,loc,r,depth,m,rot=(0,0,0),verts=32):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc,rotation=rot)
    o=bpy.context.object; o.name=name; o.data.materials.append(m)
    return o

steel=mat("Detail Steel",(.26,.29,.30),.35,.72)
dark=mat("Detail Dark",(.015,.02,.022),.50,.05)
rubber=mat("Detail Rubber",(.012,.014,.015),.72,.0)
amber=mat("Detail Amber",(.65,.28,.02),.34,.0)
redlamp=mat("Detail Red Lamp",(.45,.015,.012),.36,.0)
gravel=mat("Service Gravel",(.22,.20,.17),.94,.0)
# Service track beneath/behind the truck; additive surface detail only.
track=box("Service Track",(5.4,7.15,.045),(8.4,3.0,.05),gravel,.06)

# Rectifier cabinet: rain hood, latch/handle, door trim and conduit collars.
box("Rectifier Rain Hood",(-5.5,.15,1.87),(.64,.54,.065),steel,.025)
box("Rectifier Handle",(-5.29,-.128,1.43),(.035,.025,.18),dark,.009)
box("Rectifier Label Plate",(-5.5,-.132,1.72),(.26,.018,.055),steel,.006)
cyl("Rectifier Conduit Collar A",(-5.62,.15,1.02),.055,.07,steel)
cyl("Rectifier Conduit Collar B",(-5.38,.15,1.02),.055,.07,steel)

# Test station: cap, face bezel and terminal studs.
box("Test Station Cap",(-1.3,.10,1.43),(.28,.21,.055),steel,.018)
box("Test Station Bezel",(-1.3,-.012,1.23),(.18,.018,.24),steel,.006)
for j,x in enumerate((-1.345,-1.255),1):
    cyl(f"Test Terminal {j}",(x,-.027,1.23),.018,.025,dark,(math.radians(90),0,0),24)
# Utility pole: transformer and simple service hardware on the distant pole.
cyl("Utility Transformer",(-12.72,31.98,6.25),.24,.62,steel,(0,0,0),32)
box("Transformer Bracket",(-12.86,31.98,6.25),(.18,.18,.72),steel,.018)
for j,z in enumerate((6.47,6.63),1):
    cyl(f"Transformer Bushing {j}",(-12.72,31.98,z),.035,.12,dark)

# Truck: visible-side details only. Base truck geometry remains locked.
box("Truck Front Bumper",(3.26,7.0,.55),(.18,1.80,.16),steel,.035)
box("Truck Rear Bumper",(7.48,7.0,.54),(.18,1.76,.14),steel,.035)
box("Truck Door Trim",(4.45,6.135,1.02),(1.18,.018,.86),dark,.018)
box("Truck Door Handle",(4.76,6.115,1.07),(.18,.025,.035),dark,.008)
box("Truck Side Mirror",(3.74,6.03,1.25),(.20,.10,.16),dark,.025)
box("Truck Headlamp",(3.32,6.14,.73),(.08,.025,.16),amber,.012)
box("Truck Tail Lamp",(7.42,6.14,.73),(.08,.025,.16),redlamp,.012)
for j,x in enumerate((4.05,6.62),1):
    cyl(f"Truck Hub {j}",(x,6.105,.34),.13,.055,steel,(math.radians(90),0,0),32)

# Distant vegetation breaks the empty horizon while staying behind all technical assets.
tree_mats=[
    mat("Tree Green A",(.045,.10,.028),.90,0),
    mat("Tree Green B",(.065,.14,.035),.90,0),
    mat("Tree Green C",(.08,.17,.045),.90,0)
]
random.seed(19)
for i in range(28):
    x=-11.7+i*(23.4/27.0)+random.uniform(-.25,.25)
    y=random.uniform(24.0,34.0)
    r=random.uniform(.55,1.15)
    z=r*.82
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2,radius=r,location=(x,y,z))
    o=bpy.context.object; o.name=f"Distant Tree {i+1:02d}"
    o.scale=(random.uniform(.75,1.18),random.uniform(.70,1.05),random.uniform(1.05,1.45))
    o.data.materials.append(tree_mats[i%len(tree_mats)])
# Verify every locked transform before saving.
violations=[]
for n,(loc0,rot0,scale0) in baseline.items():
    o=bpy.data.objects[n]
    now=(tuple(o.location),tuple(o.rotation_euler),tuple(o.scale))
    for label,a,b in (("location",loc0,now[0]),("rotation",rot0,now[1]),("scale",scale0,now[2])):
        if any(abs(x-y)>1e-7 for x,y in zip(a,b)):
            violations.append((n,label,a,b))
if violations:
    raise RuntimeError("LOCKED_GEOMETRY_CHANGED: "+repr(violations))

sc=bpy.context.scene
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_C_REALISM04_SAVED")
print("LOCK_VIOLATIONS",len(violations))
print("DETAIL_TREES",len([o for o in bpy.data.objects if o.name.startswith("Distant Tree")]))
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))

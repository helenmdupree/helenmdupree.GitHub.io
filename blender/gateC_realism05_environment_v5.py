import bpy, math, random
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_realism05.png"

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
glass=mat("Truck Side Glass",(.025,.085,.11),.18,.08)
rubber=mat("Detail Rubber",(.012,.014,.015),.72,0)
gravel=mat("Service Gravel",(.19,.17,.14),.96,0)
# Refine existing grass material with stronger natural color breakup and micro-bump.
grass=bpy.data.materials.get("Grass")
if grass and grass.use_nodes:
    nt=grass.node_tree
    bs=nt.nodes.get("Principled BSDF")
    noise=next((n for n in nt.nodes if n.bl_idname=="ShaderNodeTexNoise"),None)
    ramp=next((n for n in nt.nodes if n.bl_idname=="ShaderNodeValToRGB"),None)
    bump=next((n for n in nt.nodes if n.bl_idname=="ShaderNodeBump"),None)
    if noise:
        noise.inputs["Scale"].default_value=11.0
        noise.inputs["Detail"].default_value=5.0
        noise.inputs["Roughness"].default_value=.72
    if ramp:
        ramp.color_ramp.elements[0].color=(.025,.065,.012,1)
        ramp.color_ramp.elements[1].color=(.115,.21,.045,1)
    if bump:
        bump.inputs["Strength"].default_value=.16
        bump.inputs["Distance"].default_value=.035
    if bs:
        bs.inputs["Roughness"].default_value=.95

# Replace the rectangular road slab with an irregular, thin gravel access track.
old=bpy.data.objects.get("Service Track")
if old: bpy.data.objects.remove(old,do_unlink=True)

verts=[
    (2.0,5.55,.048),(3.2,5.42,.050),(5.0,5.52,.049),(6.7,5.46,.050),(8.3,5.66,.048),
    (8.15,8.18,.050),(6.6,8.34,.049),(5.0,8.24,.050),(3.3,8.36,.049),(2.1,8.08,.048)
]
faces=[tuple(range(len(verts)))]
mesh=bpy.data.meshes.new("Service Track Mesh")
mesh.from_pydata(verts,[],faces); mesh.update()
track=bpy.data.objects.new("Service Track",mesh); bpy.context.collection.objects.link(track)
track.data.materials.append(gravel)
bev=track.modifiers.new("Track Bevel","BEVEL"); bev.width=.12; bev.segments=4
# Remove Pass 04 low-poly vegetation and rebuild it smaller, farther back, and smooth.
for o in list(bpy.data.objects):
    if o.name.startswith("Distant Tree"):
        bpy.data.objects.remove(o,do_unlink=True)

tree_mats=[
    mat("Tree Green A",(.035,.085,.022),.92,0),
    mat("Tree Green B",(.05,.115,.028),.92,0),
    mat("Tree Green C",(.065,.14,.035),.92,0),
]
trunkmat=mat("Tree Trunk",(.10,.055,.025),.88,0)
random.seed(51)
for i in range(34):
    x=-11.4+i*(22.8/33.0)+random.uniform(-.22,.22)
    y=random.uniform(31.4,35.2)
    crown_r=random.uniform(.34,.68)
    crown_z=random.uniform(.72,1.18)
    cyl(f"Tree Trunk {i+1:02d}",(x,y,.30),.045,.60,trunkmat,verts=12)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3,radius=crown_r,location=(x,y,crown_z))
    o=bpy.context.object; o.name=f"Distant Tree {i+1:02d}"
    o.scale=(random.uniform(.78,1.12),random.uniform(.72,1.00),random.uniform(.95,1.30))
    bpy.ops.object.shade_smooth()
    o.data.materials.append(tree_mats[i%len(tree_mats)])
# Refine the truck side profile by removing the oversized dark door panel.
for n in ["Truck Door Trim","Truck Side Window","Truck Rear Side Window","Truck Door Seam A","Truck Door Seam B"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

box("Truck Side Window",(4.18,6.135,1.12),(.72,.018,.40),glass,.028)
box("Truck Rear Side Window",(4.76,6.135,1.12),(.34,.018,.38),glass,.025)
box("Truck Door Seam A",(4.52,6.125,.91),(.018,.018,.88),dark,.004)
box("Truck Door Seam B",(4.92,6.125,.91),(.018,.018,.78),dark,.004)
box("Truck Rocker Trim",(5.28,6.12,.52),(2.55,.024,.055),dark,.008)

# Make the utility transformer read at the distant scale instead of vanishing.
for n in ["Utility Transformer","Transformer Bracket","Transformer Bushing 1","Transformer Bushing 2"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

cyl("Utility Transformer",(-12.66,31.94,6.20),.34,.86,steel,verts=40)
box("Transformer Bracket",(-12.86,31.94,6.20),(.22,.20,.92),steel,.02)
for j,z in enumerate((6.48,6.68),1):
    cyl(f"Transformer Bushing {j}",(-12.66,31.94,z),.045,.15,dark,verts=24)
# Subtle near-field breakup: sparse grass tufts and gravel specks, not a carpet of props.
grassblade=mat("Grass Blade",(.045,.11,.018),.90,0)
random.seed(72)
for i in range(42):
    x=random.uniform(-11.0,11.0)
    y=random.uniform(1.8,22.0)
    if (-6.4<x<-4.2 and y<3.0) or (-2.0<x<-.5 and y<2.0):
        continue
    h=random.uniform(.08,.22)
    bpy.ops.mesh.primitive_cone_add(vertices=7,radius1=random.uniform(.018,.035),radius2=.002,
                                    depth=h,location=(x,y,.02+h/2))
    o=bpy.context.object; o.name=f"Grass Tuft {i+1:02d}"
    o.data.materials.append(grassblade)

pebblemat=mat("Gravel Speck",(.11,.10,.085),.98,0)
random.seed(89)
for i in range(34):
    x=random.uniform(2.2,8.0); y=random.uniform(5.75,8.05)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=random.uniform(.025,.06),location=(x,y,.075))
    o=bpy.context.object; o.name=f"Gravel Speck {i+1:02d}"
    o.scale.z=random.uniform(.35,.65)
    o.data.materials.append(pebblemat)
# Verify locked transforms before save/render.
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

print("GATE_C_REALISM05_SAVED")
print("LOCK_VIOLATIONS",len(violations))
print("TREES",len([o for o in bpy.data.objects if o.name.startswith("Distant Tree")]))
print("GRASS_TUFTS",len([o for o in bpy.data.objects if o.name.startswith("Grass Tuft")]))
print("TRACK",bool(bpy.data.objects.get("Service Track")))

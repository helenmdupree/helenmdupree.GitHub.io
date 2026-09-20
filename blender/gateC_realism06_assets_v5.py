import bpy, math, random, os

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_realism06.png"
ASSETS=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\assets\polyhaven"

LOCKED=[
 "30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head",
 "Utility Pole","Truck Body","Truck Cab","Truck Bed","Permanent Reference Electrode",
 "Camera","Anode 1","Anode 2","Anode 3","Anode 4","Anode 5"
]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),
             tuple(bpy.data.objects[n].scale)) for n in LOCKED}

def loadimg(path,noncolor=False):
    img=bpy.data.images.load(path,check_existing=True)
    if noncolor:
        img.colorspace_settings.name="Non-Color"
    return img
def pbrmat(name,folder,prefix,scale):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    nt=m.node_tree; nt.nodes.clear()
    out=nt.nodes.new("ShaderNodeOutputMaterial")
    bs=nt.nodes.new("ShaderNodeBsdfPrincipled")
    tc=nt.nodes.new("ShaderNodeTexCoord")
    mp=nt.nodes.new("ShaderNodeMapping")
    nt.links.new(tc.outputs["Generated"],mp.inputs["Vector"])
    mp.inputs["Scale"].default_value=(scale,scale,scale)

    diff=nt.nodes.new("ShaderNodeTexImage")
    diff.image=loadimg(os.path.join(folder,prefix+"_diffuse.jpg"))
    nt.links.new(mp.outputs["Vector"],diff.inputs["Vector"])
    nt.links.new(diff.outputs["Color"],bs.inputs["Base Color"])

    rough=nt.nodes.new("ShaderNodeTexImage")
    rough.image=loadimg(os.path.join(folder,prefix+"_rough.jpg"),True)
    nt.links.new(mp.outputs["Vector"],rough.inputs["Vector"])
    nt.links.new(rough.outputs["Color"],bs.inputs["Roughness"])
    norm=nt.nodes.new("ShaderNodeTexImage")
    norm.image=loadimg(os.path.join(folder,prefix+"_normal.png"),True)
    nt.links.new(mp.outputs["Vector"],norm.inputs["Vector"])
    nmap=nt.nodes.new("ShaderNodeNormalMap")
    nmap.inputs["Strength"].default_value=.65
    nt.links.new(norm.outputs["Color"],nmap.inputs["Color"])

    disp=nt.nodes.new("ShaderNodeTexImage")
    disp.image=loadimg(os.path.join(folder,prefix+"_disp.png"),True)
    nt.links.new(mp.outputs["Vector"],disp.inputs["Vector"])
    bump=nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value=.18
    bump.inputs["Distance"].default_value=.05
    nt.links.new(disp.outputs["Color"],bump.inputs["Height"])
    nt.links.new(nmap.outputs["Normal"],bump.inputs["Normal"])
    nt.links.new(bump.outputs["Normal"],bs.inputs["Normal"])

    bs.inputs["Specular IOR Level"].default_value=.28
    nt.links.new(bs.outputs["BSDF"],out.inputs["Surface"])
    return m
grass_folder=os.path.join(ASSETS,"grass_ground")
gravel_folder=os.path.join(ASSETS,"gravel_road")
grassmat=pbrmat("Grass PBR",grass_folder,"grass_ground",9.0)
gravelmat=pbrmat("Gravel Road PBR",gravel_folder,"gravel_road",4.0)

ground=bpy.data.objects.get("Ground Surface")
if ground:
    ground.data.materials.clear()
    ground.data.materials.append(grassmat)

track=bpy.data.objects.get("Service Track")
if track:
    track.data.materials.clear()
    track.data.materials.append(gravelmat)

# Remove primitive vegetation/pebbles from the previous pass.
for o in list(bpy.data.objects):
    if o.name.startswith("Distant Tree") or o.name.startswith("Tree Trunk") or o.name.startswith("Grass Tuft") or o.name.startswith("Gravel Speck"):
        bpy.data.objects.remove(o,do_unlink=True)
# Append one real tree mesh, then use linked duplicates for an irregular distant tree line.
tree_blend=os.path.join(ASSETS,"tree_small_02","tree_small_02_1k.blend")
with bpy.data.libraries.load(tree_blend,link=False) as (data_from,data_to):
    data_to.objects=["tree_small_02_LOD1"]
master=data_to.objects[0]
master.name="Real Tree Master"
bpy.context.collection.objects.link(master)

random.seed(106)
tree_positions=[]
for row,(count,y0,x0,x1) in enumerate(((11,33.6,-10.8,10.8),(7,30.9,-9.4,9.4))):
    for i in range(count):
        t=i/(count-1) if count>1 else .5
        x=x0+(x1-x0)*t+random.uniform(-.55,.55)
        y=y0+random.uniform(-.55,.55)
        s=random.uniform(.52,.78) if row==0 else random.uniform(.42,.64)
        tree_positions.append((x,y,s,random.uniform(-math.pi,math.pi)))
for idx,(x,y,s,rz) in enumerate(tree_positions):
    if idx==0:
        o=master
    else:
        o=master.copy()
        o.data=master.data
        bpy.context.collection.objects.link(o)
    o.name=f"Real Tree {idx+1:02d}"
    o.location=(x,y,0)
    o.rotation_euler=(0,0,rz)
    o.scale=(s,s,s*random.uniform(.94,1.08))

# Smooth source mesh where appropriate; linked copies share the mesh.
for p in master.data.polygons:
    p.use_smooth=True

# Keep imported image paths project-relative for reproducibility.
for img in bpy.data.images:
    if "tree_small_02" in img.name:
        img.filepath=bpy.path.relpath(bpy.path.abspath(img.filepath))
# Verify locked transforms before save/render.
changed=[]
for n,(loc0,rot0,scale0) in baseline.items():
    o=bpy.data.objects[n]
    now=(tuple(o.location),tuple(o.rotation_euler),tuple(o.scale))
    for label,a,b in (("location",loc0,now[0]),("rotation",rot0,now[1]),("scale",scale0,now[2])):
        if any(abs(x-y)>1e-7 for x,y in zip(a,b)):
            changed.append((n,label))
if changed:
    raise RuntimeError("Locked transforms changed: "+repr(changed))
sc=bpy.context.scene
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_C_REALISM06_SAVED")
print("LOCK_CHANGES",len(changed))
print("REAL_TREES",len([o for o in bpy.data.objects if o.name.startswith("Real Tree")]))
print("GRASS_PBR",ground.data.materials[0].name if ground else "NA")
print("GRAVEL_PBR",track.data.materials[0].name if track else "NA")

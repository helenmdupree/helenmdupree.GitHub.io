import bpy, math, random

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_realism07.png"

LOCKED=[
 "30in Pipeline","Rectifier Cabinet","Rectifier Support","Test Post","Test Head",
 "Utility Pole","Truck Body","Truck Cab","Truck Bed","Permanent Reference Electrode",
 "Camera","Anode 1","Anode 2","Anode 3","Anode 4","Anode 5"
]
baseline={n:(tuple(bpy.data.objects[n].location),tuple(bpy.data.objects[n].rotation_euler),
             tuple(bpy.data.objects[n].scale)) for n in LOCKED}

# Preserve the real PBR grass texture, but mix in restrained living-green variation.
m=bpy.data.materials["Grass PBR"]
nt=m.node_tree
bs=nt.nodes.get("Principled BSDF")
diff=next(n for n in nt.nodes if n.bl_idname=="ShaderNodeTexImage" and n.image and "diffuse" in n.image.name)
mapping=next(n for n in nt.nodes if n.bl_idname=="ShaderNodeMapping")
noise=nt.nodes.new("ShaderNodeTexNoise")
noise.name="ROW Green Variation"
noise.inputs["Scale"].default_value=1.35
noise.inputs["Detail"].default_value=2.2
noise.inputs["Roughness"].default_value=.62
nt.links.new(mapping.outputs["Vector"],noise.inputs["Vector"])

ramp=nt.nodes.new("ShaderNodeValToRGB")
ramp.name="ROW Green Mix Amount"
ramp.color_ramp.elements[0].position=.28
ramp.color_ramp.elements[0].color=(.14,.14,.14,1)
ramp.color_ramp.elements[1].position=.72
ramp.color_ramp.elements[1].color=(.40,.40,.40,1)
nt.links.new(noise.outputs["Fac"],ramp.inputs["Fac"])

mix=nt.nodes.new("ShaderNodeMixRGB")
mix.name="ROW Mixed Green Brown"
mix.blend_type="MIX"
mix.inputs["Color2"].default_value=(.075,.19,.032,1)
nt.links.new(ramp.outputs["Color"],mix.inputs["Fac"])
nt.links.new(diff.outputs["Color"],mix.inputs["Color1"])
nt.links.new(mix.outputs["Color"],bs.inputs["Base Color"])
# Re-stage the real tree asset into a less regular, more natural background.
trees=sorted([o for o in bpy.data.objects if o.name.startswith("Real Tree")],key=lambda o:o.name)
master=trees[0]
for o in trees[1:]:
    bpy.data.objects.remove(o,do_unlink=True)

placements=[
 (-10.6,35.8,.48,-2.6),(-9.0,30.7,.61,1.4),(-7.3,37.4,.41,-.8),
 (-6.0,33.1,.58,2.5),(-3.5,35.5,.50,-1.9),(-1.7,30.4,.64,.7),
 (.3,37.7,.40,2.9),(2.0,33.0,.57,-2.4),(4.3,36.2,.47,.9),
 (5.8,30.8,.62,-.4),(7.6,34.5,.52,2.2),(9.5,31.6,.59,-1.1),
 (10.9,37.2,.39,1.8),(-.1,34.8,.46,-.2)
]

for i,(x,y,s,rz) in enumerate(placements):
    o=master if i==0 else master.copy()
    if i>0:
        o.data=master.data
        bpy.context.collection.objects.link(o)
    o.name=f"Real Tree {i+1:02d}"
    o.location=(x,y,0)
    o.rotation_euler=(0,0,rz)
    depth_scale=1.0-(max(y-30.0,0)*.008)
    o.scale=(s*depth_scale,s*depth_scale,s*depth_scale)
# Slight atmospheric softening of the real-tree materials without adding fog to the ICCP foreground.
for matname in ["tree_small_02_branches","tree_small_02_leaves","tree_small_02_trunk"]:
    tm=bpy.data.materials.get(matname)
    if tm and tm.use_nodes:
        tbs=tm.node_tree.nodes.get("Principled BSDF")
        if tbs:
            tbs.inputs["Roughness"].default_value=max(tbs.inputs["Roughness"].default_value,.58)

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

print("GATE_C_REALISM07_SAVED")
print("LOCK_CHANGES",len(changed))
print("REAL_TREES",len([o for o in bpy.data.objects if o.name.startswith("Real Tree")]))
print("GRASS_MAT",bpy.data.objects["Ground Surface"].data.materials[0].name)
sc=bpy.context.scene
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_C_REALISM07_SAVED")
print("LOCK_CHANGES",len(changed))
print("REAL_TREES",len([o for o in bpy.data.objects if o.name.startswith("Real Tree")]))
print("GRASS_MAT",bpy.data.objects["Ground Surface"].data.materials[0].name)

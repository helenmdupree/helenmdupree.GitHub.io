import bpy, math

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_realism02.png"

def reset(mat):
    mat.use_nodes=True
    nt=mat.node_tree
    nt.nodes.clear()
    out=nt.nodes.new("ShaderNodeOutputMaterial")
    bs=nt.nodes.new("ShaderNodeBsdfPrincipled")
    nt.links.new(bs.outputs["BSDF"],out.inputs["Surface"])
    return nt,bs

def simple(name,color,rough=.55,metal=.0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt,bs=reset(m)
    bs.inputs["Base Color"].default_value=(*color,1)
    bs.inputs["Roughness"].default_value=rough
    bs.inputs["Metallic"].default_value=metal
    return m
def organic(name,c1,c2,scale=4.0,detail=4.0,rough=.82,bump=.10):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt,bs=reset(m)
    coord=nt.nodes.new("ShaderNodeTexCoord")
    tex=nt.nodes.new("ShaderNodeTexNoise")
    nt.links.new(coord.outputs["Generated"],tex.inputs["Vector"])
    tex.inputs["Scale"].default_value=scale
    tex.inputs["Detail"].default_value=detail
    tex.inputs["Roughness"].default_value=.68
    ramp=nt.nodes.new("ShaderNodeValToRGB")
    ramp.color_ramp.elements[0].color=(*c1,1)
    ramp.color_ramp.elements[1].color=(*c2,1)
    nt.links.new(tex.outputs["Fac"],ramp.inputs["Fac"])
    nt.links.new(ramp.outputs["Color"],bs.inputs["Base Color"])
    bs.inputs["Roughness"].default_value=rough
    bumpn=nt.nodes.new("ShaderNodeBump")
    bumpn.inputs["Strength"].default_value=bump
    bumpn.inputs["Distance"].default_value=.05
    nt.links.new(tex.outputs["Fac"],bumpn.inputs["Height"])
    nt.links.new(bumpn.outputs["Normal"],bs.inputs["Normal"])
    return m
organic("Grass",(.035,.095,.02),(.13,.24,.055),8,4,.94,.10)
organic("Section Topsoil",(.105,.052,.024),(.22,.115,.048),5,4,.97,.13)
organic("Section Upper Soil",(.19,.105,.052),(.33,.205,.105),4,4,.96,.12)
organic("Section Lower Soil",(.16,.095,.052),(.29,.19,.11),3.5,4,.97,.10)
organic("Groundbed Carbon Backfill",(.025,.025,.022),(.095,.09,.078),7,4,.95,.14)
organic("Pipeline Green",(.014,.07,.032),(.045,.19,.08),3.0,3.0,.44,.025)

simple("Steel",(.34,.37,.38),.38,.72)
simple("White",(.58,.61,.61),.46,.08)
simple("Black",(.012,.015,.018),.48,.04)
organic("Wood",(.12,.055,.02),(.27,.13,.045),3.5,3,.78,.08)
simple("Glass",(.025,.10,.14),.20,.12)

simple("Circuit Positive Bright",(.50,.022,.016),.34,0)
simple("Circuit Negative Blue",(.015,.065,.28),.36,0)
simple("Test Lead Gray",(.16,.18,.19),.42,0)
simple("Reference Lead Bright",(.58,.38,.025),.40,0)
simple("Coating Repair Patch",(.018,.022,.018),.65,0)
simple("Reference Electrode Ceramic",(.42,.46,.34),.58,.04)
simple("Technician Navy",(.014,.025,.04),.66,0)
simple("HiVis Vest",(.42,.56,.04),.55,0)
simple("Skin",(.37,.21,.13),.64,0)
anode_mat=organic("Anode Alloy",(.12,.13,.13),(.28,.29,.28),5,3,.64,.06)
for i in range(1,6):
    o=bpy.data.objects.get(f"Anode {i}")
    if o:
        o.data.materials.clear()
        o.data.materials.append(anode_mat)

for n in ["Rectifier Cabinet","Rectifier Support","Test Post","Test Head"]:
    o=bpy.data.objects.get(n)
    if o:
        o.data.materials.clear()
        o.data.materials.append(bpy.data.materials["Steel"])

for n in ["Rectifier Door","Truck Body","Truck Cab","Truck Bed","Tech Hardhat"]:
    o=bpy.data.objects.get(n)
    if o:
        o.data.materials.clear()
        o.data.materials.append(bpy.data.materials["White"])

for n in ["Truck Glass"]:
    o=bpy.data.objects.get(n)
    if o:
        o.data.materials.clear()
        o.data.materials.append(bpy.data.materials["Glass"])
# Safe daylight world: uniform sky color, no physical-sky below-horizon artifact.
world=bpy.context.scene.world
world.use_nodes=True
wn=world.node_tree
wn.nodes.clear()
wout=wn.nodes.new("ShaderNodeOutputWorld")
bg=wn.nodes.new("ShaderNodeBackground")
bg.inputs["Color"].default_value=(.19,.33,.48,1)
bg.inputs["Strength"].default_value=.62
wn.links.new(bg.outputs["Background"],wout.inputs["Surface"])

sun=bpy.data.objects.get("Sun")
if sun:
    sun.data.energy=1.8
    sun.data.angle=math.radians(6)
    sun.data.color=(1.0,.84,.68)
    sun.rotation_euler=(math.radians(32),math.radians(-18),math.radians(-42))

area=bpy.data.objects.get("Area")
if area:
    area.data.energy=300
    area.data.size=12
    area.data.color=(.63,.74,1.0)
sc=bpy.context.scene
sc.render.engine="BLENDER_EEVEE"
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.film_transparent=False
sc.view_settings.exposure=-0.25
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_C_REALISM02_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("CAM_LOC",tuple(round(v,3) for v in sc.camera.location))
print("ANODE_CENTERS",[round(bpy.data.objects[f"Anode {i}"].location.z,3) for i in range(1,6)])
print("REF_LOC",tuple(round(v,3) for v in bpy.data.objects["Permanent Reference Electrode"].location))

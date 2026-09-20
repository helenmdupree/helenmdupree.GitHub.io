import bpy, math, os

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v7_slow_camera.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v8_realism.blend"

def reset_principled(matname, base, rough=.5, metal=0.0):
    m=bpy.data.materials.get(matname)
    if not m: return None,None
    m.use_nodes=True
    nt=m.node_tree
    bs=nt.nodes.get("Principled BSDF")
    if not bs:
        bs=nt.nodes.new("ShaderNodeBsdfPrincipled")
    bs.inputs["Base Color"].default_value=(*base,1)
    bs.inputs["Roughness"].default_value=rough
    bs.inputs["Metallic"].default_value=metal
    return m,bs

def add_noise_bump(m,bs,scale=8,detail=4,strength=.18,distance=.04):
    nt=m.node_tree
    tc=nt.nodes.new("ShaderNodeTexCoord")
    noise=nt.nodes.new("ShaderNodeTexNoise")
    noise.inputs["Scale"].default_value=scale
    noise.inputs["Detail"].default_value=detail
    noise.inputs["Roughness"].default_value=.7
    bump=nt.nodes.new("ShaderNodeBump")
    bump.inputs["Strength"].default_value=strength
    bump.inputs["Distance"].default_value=distance
    nt.links.new(tc.outputs["Generated"],noise.inputs["Vector"])
    nt.links.new(noise.outputs["Fac"],bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"],bs.inputs["Normal"])
    return noise,bump
# Pipeline coating: dark green fusion-bonded coating with subtle surface texture.
m,bs=reset_principled("Pipeline Green",(0.035,0.18,0.11),.42,.02)
if m:
    bs.inputs["Coat Weight"].default_value=.18
    bs.inputs["Coat Roughness"].default_value=.22
    add_noise_bump(m,bs,scale=42,detail=3,strength=.08,distance=.012)

# Soil layers: related but distinct tones and granular bump.
soil_specs=[
    ("Section Topsoil",(0.16,0.09,0.045),.93,8,.28,.06),
    ("Section Upper Soil",(0.23,0.14,0.075),.92,6,.24,.07),
    ("Section Lower Soil",(0.19,0.115,0.065),.94,5,.20,.08),
]
for mn,color,rough,scale,strength,dist in soil_specs:
    m,bs=reset_principled(mn,color,rough,0.0)
    if m:
        add_noise_bump(m,bs,scale=scale,detail=5,strength=strength,distance=dist)

# Carbonaceous backfill should read very dark, matte, and granular.
m,bs=reset_principled("Groundbed Carbon Backfill",(0.025,0.028,0.028),.97,.0)
if m:
    add_noise_bump(m,bs,scale=18,detail=5,strength=.35,distance=.05)

# Galvanized equipment metal: slightly warm gray, high roughness, subtle mottling.
m,bs=reset_principled("Steel",(0.46,0.49,0.50),.46,.62)
if m:
    add_noise_bump(m,bs,scale=28,detail=3,strength=.07,distance=.01)

m,bs=reset_principled("Anode Alloy",(0.34,0.36,0.37),.38,.78)
if m:
    add_noise_bump(m,bs,scale=36,detail=2,strength=.08,distance=.008)

# Truck: neutral fleet white, real glass, dark rubber, restrained alloy.
m,bs=reset_principled("paint",(0.72,0.74,0.75),.24,.08)
if m:
    bs.inputs["Coat Weight"].default_value=.42
    bs.inputs["Coat Roughness"].default_value=.16

m,bs=reset_principled("glass",(0.035,0.07,0.085),.12,.02)
if m:
    bs.inputs["Transmission Weight"].default_value=.62
    bs.inputs["IOR"].default_value=1.45

reset_principled("rubber",(0.012,0.013,0.013),.78,.0)
reset_principled("alloy",(0.34,0.36,0.37),.22,.82)

# Mastic stays black, low-profile, matte.
reset_principled("Cadweld Mastic Black",(0.004,0.004,0.005),.78,.0)
# Subtle edge bevels so field equipment stops reading as perfect CG boxes.
for name,width in [
    ("Rectifier Cabinet",.018),("Rectifier Support",.012),
    ("Test Head",.010),("Test Post",.006)
]:
    o=bpy.data.objects.get(name)
    if not o or o.type!="MESH": continue
    if not any(md.type=="BEVEL" and md.name=="Realism Bevel" for md in o.modifiers):
        md=o.modifiers.new("Realism Bevel","BEVEL")
        md.width=width
        md.segments=3

# Production daylight world: physical sky plus existing controlled lights.
world=bpy.context.scene.world
world.use_nodes=True
nt=world.node_tree
nt.nodes.clear()
out=nt.nodes.new("ShaderNodeOutputWorld")
bg=nt.nodes.new("ShaderNodeBackground")
sky=nt.nodes.new("ShaderNodeTexSky")
sky.sky_type="MULTIPLE_SCATTERING"
sky.sun_elevation=math.radians(24)
sky.sun_rotation=math.radians(225)
sky.altitude=0.2
sky.air_density=1.05
sky.aerosol_density=1.8
bg.inputs["Strength"].default_value=.34
nt.links.new(sky.outputs["Color"],bg.inputs["Color"])
nt.links.new(bg.outputs["Background"],out.inputs["Surface"])
# Balance existing lights for warmer natural surface light and readable cutaway fill.
light_settings={
    "Sun":(1.55,(1.0,.91,.80)),
    "Area":(280.0,(.95,.97,1.0)),
    "Anchor Fill":(360.0,(1.0,.93,.84)),
    "Cutaway Fill":(430.0,(.82,.90,1.0)),
    "Groundbed Fill":(460.0,(.86,.92,1.0)),
}
for name,(energy,color) in light_settings.items():
    o=bpy.data.objects.get(name)
    if not o or o.type!="LIGHT": continue
    o.data.energy=energy
    o.data.color=color
    if o.data.type=="SUN":
        o.data.angle=math.radians(4.5)

sc=bpy.context.scene
sc.render.engine="BLENDER_EEVEE"
sc.eevee.taa_render_samples=32
sc.view_settings.view_transform="AgX"
sc.view_settings.exposure=-.15

# Save to a new realism master; v7 remains the camera baseline.
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("REALISM_V8_SAVED",OUT)



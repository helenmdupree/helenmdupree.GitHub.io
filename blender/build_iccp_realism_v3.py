import bpy, math, os
from mathutils import Vector
OUT_BLEND=r"C:\GitHub\soubel-iccp-interactive\blender\iccp_realism_v3.blend"
OUT_RENDER=r"C:\GitHub\soubel-iccp-interactive\blender\iccp_realism_v3.png"

def mat(name,c,metal=0,rough=.55):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF"); b.inputs["Base Color"].default_value=(*c,1); b.inputs["Metallic"].default_value=metal; b.inputs["Roughness"].default_value=rough
    return m

def textured_mat(name,c1,c2,metal=0,rough=.55,scale=5.0,bump=.12):
    m=bpy.data.materials.new(name=name); m.use_nodes=True
    nt=m.node_tree; b=nt.nodes.get("Principled BSDF")
    b.inputs["Metallic"].default_value=metal; b.inputs["Roughness"].default_value=rough
    tex=nt.nodes.new("ShaderNodeTexCoord")
    noise=nt.nodes.new("ShaderNodeTexNoise"); noise.inputs["Scale"].default_value=scale; noise.inputs["Detail"].default_value=4.0; noise.inputs["Roughness"].default_value=.7
    ramp=nt.nodes.new("ShaderNodeValToRGB"); ramp.color_ramp.elements[0].color=(*c1,1); ramp.color_ramp.elements[1].color=(*c2,1)
    bp=nt.nodes.new("ShaderNodeBump"); bp.inputs["Strength"].default_value=bump; bp.inputs["Distance"].default_value=.16
    nt.links.new(tex.outputs["Generated"],noise.inputs["Vector"]); nt.links.new(noise.outputs["Fac"],ramp.inputs["Fac"]); nt.links.new(ramp.outputs["Color"],b.inputs["Base Color"]); nt.links.new(noise.outputs["Fac"],bp.inputs["Height"]); nt.links.new(bp.outputs["Normal"],b.inputs["Normal"])
    return m
def box(name,loc,dims,m,bev=0):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bev: md=o.modifiers.new("Bevel","BEVEL"); md.width=bev; md.segments=3
    o.data.materials.append(m); return o
def cyl(name,loc,r,depth,m,rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=48,radius=r,depth=depth,location=loc,rotation=rot); o=bpy.context.object; o.name=name; o.data.materials.append(m); return o
def tube(name,pts,r,m):
    c=bpy.data.curves.new(name,'CURVE'); c.dimensions='3D'; c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new('POLY'); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o); o.data.materials.append(m); return o
def txt(body,loc,size,m):
    bpy.ops.object.text_add(location=loc,rotation=(math.radians(90),0,0)); o=bpy.context.object; o.data.body=body; o.data.align_x='CENTER'; o.data.size=size; o.data.extrude=.006; o.data.materials.append(m); return o
def look(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()

bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
sc=bpy.context.scene; sc.unit_settings.system='METRIC'; sc.unit_settings.length_unit='METERS'
sc.render.engine='BLENDER_EEVEE'; sc.render.resolution_x=1600; sc.render.resolution_y=900; sc.render.resolution_percentage=100; sc.render.image_settings.file_format='PNG'; sc.render.filepath=OUT_RENDER
sc.world.use_nodes=True; bg=sc.world.node_tree.nodes.get('Background'); bg.inputs['Color'].default_value=(.32,.52,.64,1); bg.inputs['Strength'].default_value=.70
soil=textured_mat('Soil',(.16,.095,.055),(.38,.25,.16),0,.92,3.2,.38); grade=textured_mat('Grade',(.075,.16,.07),(.22,.36,.16),0,.88,9.0,.20); steel=textured_mat('Pipeline Coating',(.055,.075,.082),(.16,.22,.24),.18,.32,13.0,.07); galv=textured_mat('Galvanized Cabinet',(.44,.49,.49),(.76,.80,.79),.72,.34,8.0,.08); wood=textured_mat('Pole Wood',(.16,.075,.03),(.42,.24,.09),0,.68,3.0,.20); black=mat('Cable Black',(.018,.022,.025),0,.40); red=mat('Positive Cable',(.60,.025,.02),0,.34); blue=mat('Negative Cable',(.025,.10,.48),0,.32); anode=textured_mat('Anode Metal',(.22,.25,.25),(.48,.52,.51),.74,.35,9.0,.08); white=mat('Label',(.92,.96,.97),0,.50); cyan=mat('Accent',(.03,.66,.76),0,.33); human=mat('Human',(.10,.10,.11),0,.72); warn=mat('Warning',(.92,.13,.04),0,.48); brass=mat('Hardware',(.34,.28,.12),.55,.30)
PIPE_OD=.762; R=PIPE_OD/2; COVER=.9144; CZ=-(COVER+R)
box('Soil Volume',(0,0,-2.05),(26,4,4.1),soil); box('Grade Strip',(0,0,.04),(26,4,.08),grade)
cyl('30in Pipeline',(0,0,CZ),R,24,steel,(0,math.radians(90),0))
for x in (-5.5,5.5): cyl('Pipe Joint',(x,0,CZ),R*1.035,.12,galv,(0,math.radians(90),0))
# utility and rectifier poles
px=-8.6; cyl('Utility Pole',(px,0,4.3),.16,8.6,wood); box('Crossarm',(px,0,7.3),(2,.16,.14),wood,.03)
for dx in (-.72,0,.72): cyl('Insulator',(px+dx,0,7.45),.055,.20,galv)
for y in (-.08,.08): tube('AC Conductor',[(px-1.5,y,7.5),(px,y,7.5),(-6.3,y,6.5)],.018,black)
rx=-6.0; cyl('Rectifier Pole',(rx,0,3.6),.14,7.2,wood)
cw=.559; cd=.457; ch=.762; rz=1.45
box('Pole-mounted Rectifier',(rx,0,rz),(cw,cd,ch),galv,.035); box('Rectifier Door',(rx,-cd/2-.012,rz),(cw*.86,.024,ch*.82),galv,.015); box('Meter',(rx,-cd/2-.027,rz+.11),(.17,.018,.10),black,.01); box('Vent',(rx,-cd/2-.027,rz-.13),(.22,.018,.08),black,.005); box('Danger Label',(rx,-cd/2-.029,rz-.005),(.18,.012,.07),warn,.004); box('Door Handle',(rx+cw*.33,-cd/2-.04,rz),(.025,.035,.18),brass,.006); box('Top Rain Hood',(rx,0,rz+ch/2+.035),(cw+.07,cd+.07,.055),galv,.018)
tube('AC Drop',[(-6.3,0,6.5),(-6.05,0,2.10),(rx,0,1.83)],.025,black)
# test station
tx=-1.8; cyl('Test Post',(tx,0,.62),.045,1.24,galv); box('Test Head',(tx,0,1.24),(.24,.18,.34),galv,.025); box('Test Face',(tx,-.102,1.24),(.17,.026,.24),black,.01); box('Test Cap',(tx,0,1.43),(.27,.20,.05),galv,.015)
# leads
tube('Positive Lead',[(rx,0,1.07),(rx,0,.18),(5.8,0,.18)],.035,red); tube('Negative Lead',[(rx+.12,0,1.07),(rx+.12,0,-.25),(rx+.5,0,CZ),(-4.6,0,CZ)],.035,blue)
# anodes
for i,x in enumerate([4.0,5.4,6.8,8.2,9.6],1):
    top=-.80; L=1.50; center=top-L/2; cyl(f'Anode {i}',(x,0,center),.0375,L,anode); tube(f'Anode Lead {i}',[(x,0,.18),(x,0,top)],.022,red)
# human 1.70m
hx=-3.6; cyl('Human Torso',(hx,0,1.08),.18,.75,human); bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,radius=.14,location=(hx,0,1.60)); bpy.context.object.data.materials.append(human)
for dx in (-.10,.10): cyl('Human Leg',(hx+dx,0,.38),.065,.72,human)
for dx in (-.23,.23): cyl('Human Arm',(hx+dx,0,1.10),.05,.68,human)
# labels
txt('1.70 m person',(hx,.26,1.95),.25,white); txt('30 in / 0.762 m OD',(0,.26,CZ-.75),.27,white); txt('36 in / 0.914 m cover',(1.6,.26,-.45),.25,cyan); txt('Rectifier cabinet ~22 x 18 x 30 in | operator-access height',(rx,.28,2.35),.23,white); txt('REALISM STUDY V3 | SCALE LOCKED | CONCEPTUAL - NOT FOR DESIGN',(0,.28,3.25),.30,cyan)
for z in range(8): box(f'Scale tick {z}',(-11.2,.15,z),(.28,.04,.025),cyan)
txt('meters',(-11.2,.2,7.55),.20,white)
# camera
bpy.ops.object.camera_add(location=(0,-27,2.6)); cam=bpy.context.object; sc.camera=cam; look(cam,(0,0,1.15)); cam.data.type='PERSP'; cam.data.lens=58
bpy.ops.object.light_add(type='SUN',location=(-6,-8,12)); sun=bpy.context.object; sun.data.energy=2.4; sun.data.angle=math.radians(6); sun.rotation_euler=(math.radians(34),math.radians(-14),math.radians(-32))
bpy.ops.object.light_add(type='AREA',location=(0,-10,7)); area=bpy.context.object; area.data.energy=1450; area.data.shape='RECTANGLE'; area.data.size=14; area.data.size_y=9; look(area,(0,0,.8)); bpy.ops.object.light_add(type='AREA',location=(7,-5,3)); fill=bpy.context.object; fill.data.energy=650; fill.data.size=7; look(fill,(1,0,.5))
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND); bpy.ops.render.render(write_still=True)
print('SAVED',OUT_BLEND); print('RENDER',OUT_RENDER)
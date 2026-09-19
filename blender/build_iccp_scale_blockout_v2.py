import bpy, math, os
from mathutils import Vector
OUT_BLEND=r"C:\GitHub\soubel-iccp-interactive\blender\iccp_scale_blockout_v2.blend"
OUT_RENDER=r"C:\GitHub\soubel-iccp-interactive\blender\iccp_scale_blockout_v2.png"

def mat(name,c,metal=0,rough=.55):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name); m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF"); b.inputs["Base Color"].default_value=(*c,1); b.inputs["Metallic"].default_value=metal; b.inputs["Roughness"].default_value=rough
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
sc.world.use_nodes=True; bg=sc.world.node_tree.nodes.get('Background'); bg.inputs['Color'].default_value=(.055,.075,.085,1); bg.inputs['Strength'].default_value=.45
soil=mat('Soil',(.24,.17,.12),0,.95); grade=mat('Grade',(.18,.31,.20),0,.9); steel=mat('Pipeline Steel',(.12,.20,.23),.72,.27); galv=mat('Cabinet Metal',(.62,.68,.68),.58,.30); wood=mat('Pole Wood',(.28,.16,.075),0,.72); black=mat('Cable Black',(.025,.03,.035),0,.45); red=mat('Positive Cable',(.55,.03,.025),0,.4); blue=mat('Negative Cable',(.03,.12,.42),0,.38); anode=mat('Anode Metal',(.30,.34,.35),.72,.32); white=mat('Label',(.9,.94,.95),0,.55); cyan=mat('Accent',(.05,.62,.70),0,.38); human=mat('Human',(.12,.12,.13),0,.72)
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
box('Pole-mounted Rectifier',(rx,0,rz),(cw,cd,ch),galv,.035); box('Rectifier Door',(rx,-cd/2-.012,rz),(cw*.86,.024,ch*.82),galv,.015); box('Meter',(rx,-cd/2-.027,rz+.09),(.16,.018,.09),black,.01); box('Vent',(rx,-cd/2-.027,rz-.11),(.20,.018,.08),black,.005)
tube('AC Drop',[(-6.3,0,6.5),(-6.05,0,2.10),(rx,0,1.83)],.025,black)
# test station
tx=-1.8; cyl('Test Post',(tx,0,.62),.045,1.24,galv); box('Test Head',(tx,0,1.24),(.22,.16,.32),galv,.025); box('Test Face',(tx,-.09,1.24),(.16,.025,.23),black,.01)
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
txt('1.70 m person',(hx,.26,1.95),.25,white); txt('30 in / 0.762 m OD',(0,.26,CZ-.75),.27,white); txt('36 in / 0.914 m cover',(1.6,.26,-.45),.25,cyan); txt('Rectifier cabinet ~22 x 18 x 30 in | operator-access height',(rx,.28,2.35),.23,white); txt('TRUE-SCALE BLOCKOUT | CONCEPTUAL - NOT FOR DESIGN',(0,.28,3.25),.30,cyan)
for z in range(8): box(f'Scale tick {z}',(-11.2,.15,z),(.28,.04,.025),cyan)
txt('meters',(-11.2,.2,7.55),.20,white)
# camera
bpy.ops.object.camera_add(location=(0,-30,2.25)); cam=bpy.context.object; sc.camera=cam; look(cam,(0,0,1.35)); cam.data.type='ORTHO'; cam.data.ortho_scale=24.5
bpy.ops.object.light_add(type='SUN',location=(0,-5,10)); sun=bpy.context.object; sun.data.energy=2.0; sun.rotation_euler=(math.radians(28),math.radians(-18),math.radians(-25))
bpy.ops.object.light_add(type='AREA',location=(0,-8,8)); area=bpy.context.object; area.data.energy=1200; area.data.shape='RECTANGLE'; area.data.size=12; area.data.size_y=8; look(area,(0,0,0))
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND); bpy.ops.render.render(write_still=True)
print('SAVED',OUT_BLEND); print('RENDER',OUT_RENDER)
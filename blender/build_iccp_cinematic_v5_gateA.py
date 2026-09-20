import bpy, math
from mathutils import Vector

OUT_BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
OUT_RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateA.png"

PIPE_OD=.762
PIPE_R=PIPE_OD/2
COVER=.9144
PIPE_Z=-(COVER+PIPE_R)

def mat(name,color,metal=0.0,rough=.6):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value=(*color,1)
    b.inputs["Metallic"].default_value=metal
    b.inputs["Roughness"].default_value=rough
    return m

def box(name,loc,dims,m,bev=.03):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bev:
        md=o.modifiers.new("Bevel","BEVEL"); md.width=bev; md.segments=3
    o.data.materials.append(m); return o
def cyl(name,loc,r,depth,m,rot=(0,0,0),verts=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=depth,location=loc,rotation=rot)
    o=bpy.context.object; o.name=name; o.data.materials.append(m); return o

def tube(name,pts,r,m):
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(m); return o

def limb(name,a,b,r,m):
    a,b=Vector(a),Vector(b); mid=(a+b)/2; vec=b-a
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=vec.length,location=mid)
    o=bpy.context.object; o.name=name
    o.rotation_euler=vec.to_track_quat("Z","Y").to_euler()
    o.data.materials.append(m); return o

def look(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat("-Z","Y").to_euler()

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

sc=bpy.context.scene
sc.unit_settings.system="METRIC"
sc.render.engine="BLENDER_EEVEE"
sc.render.resolution_x=1600; sc.render.resolution_y=900; sc.render.resolution_percentage=100
sky=(.44,.62,.76)
sc.world.use_nodes=True
sc.world.node_tree.nodes["Background"].inputs["Color"].default_value=(*sky,1)
sc.world.node_tree.nodes["Background"].inputs["Strength"].default_value=.75

grass=mat("Grass",(.16,.30,.10),0,.9)
soil=mat("Soil",(.31,.20,.12),0,.95)
pipe_mat=mat("Pipeline Green",(.06,.28,.13),.08,.38)
steel=mat("Steel",(.48,.53,.54),.55,.34)
wood=mat("Wood",(.32,.17,.07),0,.72)
black=mat("Black",(.02,.025,.03),0,.55)
red=mat("Positive",(.65,.03,.025),0,.38)
blue=mat("Negative",(.03,.12,.55),0,.36)
yellow=mat("Reference Lead",(.55,.42,.08),0,.48)
refmat=mat("Reference Electrode",(.28,.38,.30),.06,.5)
navy=mat("Technician Navy",(.035,.07,.11),0,.65)
vest=mat("HiVis Vest",(.62,.78,.12),0,.48)
skin=mat("Skin",(.52,.32,.22),0,.62)
white=mat("White",(.88,.90,.90),.05,.42)
glass=mat("Glass",(.08,.18,.22),.12,.24)
pad=mat("Attachment Repair",(.055,.065,.06),0,.72)

# Stage: surface and a vertical cutaway face behind buried objects.
box("Ground Surface",(0,2.5,.02),(28,14,.04),grass,.01)
box("Cutaway Soil Face",(0,4.45,-2.25),(28,.18,4.5),soil,.02)

# Pipeline: 30-inch OD, approximately 36-inch cover.
cyl("30in Pipeline",(0,0,PIPE_Z),PIPE_R,16.5,pipe_mat,(0,math.radians(90),0))
# Utility pole is deliberately remote/background, not adjacent to rectifier.
ux,uy=-9.8,7.2
cyl("Utility Pole",(ux,uy,4.2),.16,8.4,wood)
box("Utility Crossarm",(ux,uy,7.15),(1.8,.16,.14),wood,.025)
for dx in (-.65,0,.65):
    cyl("Utility Insulator",(ux+dx,uy,7.34),.05,.18,steel)
for dy in (-.07,.07):
    tube("Utility Conductor",[(ux-2.2,uy+dy,7.42),(ux,uy+dy,7.42),(-6.5,4.2+dy,6.1)],.012,black)

# Operator-owned rectifier support and cabinet.
rx,ry=-5.5,.15
cyl("Rectifier Support",(rx,ry,1.8),.11,3.6,steel)
box("Rectifier Cabinet",(rx,ry,1.45),(.559,.457,.762),steel,.035)
box("Rectifier Door",(rx,ry-.245,1.45),(.48,.025,.64),white,.018)
box("Rectifier Meter",(rx,ry-.262,1.57),(.15,.018,.09),black,.008)
box("Rectifier Vent",(rx,ry-.262,1.30),(.19,.018,.07),black,.006)
tube("AC Service",[(-6.5,4.2,6.1),(-6.5,2.6,3.0),(rx,ry,1.85)],.018,black)

# Test station.
tx,ty=-1.3,.10
cyl("Test Post",(tx,ty,.62),.045,1.24,steel)
box("Test Head",(tx,ty,1.23),(.22,.16,.32),steel,.025)
box("Test Face",(tx,ty-.09,1.23),(.15,.02,.21),black,.008)
# Separate right-side groundbed zone.  It is behind/right of the pipeline, not intersecting it.
anode_xs=[3.7,4.6,5.5,6.4,7.3]
groundbed_y=2.25
anode_top=-2.20
anode_len=1.35
anode_center=anode_top-anode_len/2
header_z=-1.95

# Positive route from rectifier to a separate buried header.
tube("Positive Main",[(rx+.16,ry,1.08),(rx+.16,.65,-.42),(2.9,1.55,-1.30),(3.35,groundbed_y,header_z)],.011,red)
tube("Positive Header",[(3.35,groundbed_y,header_z),(7.65,groundbed_y,header_z)],.010,red)

for i,x in enumerate(anode_xs,1):
    cyl(f"Anode {i}",(x,groundbed_y,anode_center),.055,anode_len,steel)
    tube(f"Anode Lead {i}",[(x,groundbed_y,header_z),(x,groundbed_y,anode_top)],.006,red)

# Rectifier negative connection: its own compact pipe attachment.
neg_x=-4.15
tube("Rectifier Negative",[(rx-.15,ry,1.08),(rx-.15,.10,-.38),(neg_x,.02,PIPE_Z+PIPE_R)],.010,blue)
box("Rectifier Negative Attachment",(neg_x,.02,PIPE_Z+PIPE_R+.018),(.14,.08,.035),pad,.012)

# Test-station structure lead: separate pipe attachment.
test_attach_x=-.55
tube("Test Structure Lead",[(tx,ty,1.08),(tx,.22,-.42),(test_attach_x,.20,PIPE_Z+PIPE_R)],.005,black)
box("Test Structure Attachment",(test_attach_x,.20,PIPE_Z+PIPE_R+.018),(.12,.07,.032),pad,.011)
# Permanent reference electrode beside the pipe, never bonded to it.
refx,refy=1.10,1.20
cyl("Permanent Reference Electrode",(refx,refy,-1.95),.065,.30,refmat)
tube("Reference Electrode Lead",[(tx,ty,1.08),(tx,.55,-.50),(refx,refy,-1.80)],.005,yellow)

# Two-armed technician blockout at rectifier.
hx,hy=-4.65,-.48
box("Tech Torso",(hx,hy,1.08),(.40,.27,.58),navy,.08)
box("Tech Vest",(hx,hy-.145,1.08),(.42,.03,.48),vest,.02)
box("Tech Pelvis",(hx,hy,.72),(.32,.23,.18),navy,.045)
bpy.ops.mesh.primitive_uv_sphere_add(segments=28,ring_count=14,radius=.13,location=(hx,hy,1.52))
head=bpy.context.object; head.name="Tech Head"; head.data.materials.append(skin)
bpy.ops.mesh.primitive_uv_sphere_add(segments=28,ring_count=14,radius=.15,location=(hx,hy,1.64))
hat=bpy.context.object; hat.name="Tech Hardhat"; hat.scale=(1.06,.94,.48); hat.data.materials.append(white)

limb("Tech Left Leg",(hx-.10,hy,.68),(hx-.11,hy,.16),.066,navy)
limb("Tech Right Leg",(hx+.10,hy,.68),(hx+.11,hy,.16),.066,navy)
box("Tech Left Boot",(hx-.11,hy-.05,.07),(.17,.31,.12),black,.03)
box("Tech Right Boot",(hx+.11,hy-.05,.07),(.17,.31,.12),black,.03)

# Exactly two arms, each made of upper arm + forearm segments.
ls=(hx-.20,hy,1.28); le=(-4.95,-.34,1.29); lh=(-5.25,-.12,1.45)
rs=(hx+.20,hy,1.27); re=(-4.90,-.30,1.12); rh=(-5.24,-.12,1.18)
limb("Tech Left Upper Arm",ls,le,.052,navy); limb("Tech Left Forearm",le,lh,.050,navy)
limb("Tech Right Upper Arm",rs,re,.052,navy); limb("Tech Right Forearm",re,rh,.050,navy)
for name,p in [("Tech Left Glove",lh),("Tech Right Glove",rh)]:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=10,radius=.062,location=p)
    bpy.context.object.name=name; bpy.context.object.data.materials.append(black)

# Simple service-truck proxy in background for composition only.
px,py=5.4,7.0
box("Truck Body",(px,py,.58),(4.1,1.72,.50),white,.11)
box("Truck Cab",(px-1.00,py,.98),(1.65,1.66,1.08),white,.11)
box("Truck Glass",(px-1.38,py-.845,1.08),(.66,.025,.43),glass,.02)
box("Truck Bed",(px+1.05,py,.88),(1.65,1.56,.17),white,.04)
for x in (px-1.35,px+1.22):
    for y in (py-.78,py+.78):
        cyl("Truck Wheel",(x,y,.34),.32,.20,black,(math.radians(90),0,0),32)

# Camera: cinematic field-level oblique view that preserves depth separation.
bpy.ops.object.camera_add(location=(-.6,-25.5,3.15))
cam=bpy.context.object; cam.name="Camera"; cam.data.lens=48
look(cam,(-.2,1.1,-.45)); sc.camera=cam

# Lighting for legibility only; not the realism pass.
bpy.ops.object.light_add(type="SUN",location=(-6,-8,12))
sun=bpy.context.object; sun.data.energy=2.2; sun.rotation_euler=(math.radians(30),math.radians(-15),math.radians(-32))
bpy.ops.object.light_add(type="AREA",location=(0,-10,8))
area=bpy.context.object; area.data.energy=1000; area.data.size=16; look(area,(0,1,-.2))

sc.render.filepath=OUT_RENDER
bpy.ops.wm.save_as_mainfile(filepath=OUT_BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_A_SAVED",OUT_BLEND)
print("GATE_A_RENDER",OUT_RENDER)
print("TECH_ARM_SEGMENTS",len([o for o in bpy.data.objects if "Tech" in o.name and ("Upper Arm" in o.name or "Forearm" in o.name)]))
print("ANODES",len([o for o in bpy.data.objects if o.name.startswith("Anode ")]))
print("REFERENCE",bool(bpy.data.objects.get("Permanent Reference Electrode")))
print("UTILITY_RECTIFIER_DISTANCE_M",round(((Vector((ux,uy,0))-Vector((rx,ry,0))).length),2))

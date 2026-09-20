import bpy
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateB_dollhouse.png"
PIPE_Z=-1.2954
PIPE_R=.381

def mat(name,color,metal=0.0,rough=.72):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value=(*color,1)
    b.inputs["Metallic"].default_value=metal
    b.inputs["Roughness"].default_value=rough
    return m

def box(name,loc,dims,m,bev=.015):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bev:
        md=o.modifiers.new("Bevel","BEVEL"); md.width=bev; md.segments=2
    o.data.materials.append(m); return o
def tube(name,pts,r,m):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=4
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(m); return o

topsoil=mat("Section Topsoil",(.23,.14,.075),0,.95)
upper=mat("Section Upper Soil",(.34,.235,.145),0,.96)
lower=mat("Section Lower Soil",(.285,.195,.12),0,.97)
backfill=mat("Groundbed Carbon Backfill",(.13,.13,.12),0,.93)
red=bpy.data.materials.get("Positive")
blue=bpy.data.materials.get("Negative")
black=bpy.data.materials.get("Black")
yellow=bpy.data.materials.get("Reference Lead")

# Remove the old single face and any rejected Gate B panels.
for n in ["Cutaway Soil Face","Cutaway Topsoil","Cutaway Upper Soil",
          "Cutaway Lower Soil","Groundbed Backfill Panel"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)
# Move the front edge of the grass plane behind the main buried section.
ground=bpy.data.objects.get("Ground Surface")
if ground:
    back_edge=36.0
    front_edge=.80
    ground.location.y=(front_edge+back_edge)/2
    ground.dimensions.y=back_edge-front_edge
    bpy.context.view_layer.objects.active=ground
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)

# Main pipeline section face at y=.85, split around the recessed groundbed window.
main_y=.85
left_x=-5.45
left_w=17.10
right_x=10.95
right_w=6.10

# Three visible soil bands make the locked cover legible without moving the pipe.
for x,w,suffix in [(left_x,left_w,"L"),(right_x,right_w,"R")]:
    box(f"Topsoil {suffix}",(x,main_y,-.13),(w,.10,.26),topsoil,.008)
    box(f"Upper Soil {suffix}",(x,main_y,-.57),(w,.10,.62),upper,.008)
    box(f"Lower Soil {suffix}",(x,main_y,-2.68),(w,.10,3.60),lower,.008)

# Recessed groundbed section behind the five anodes.
gb_y=2.65
box("Groundbed Topsoil",(5.50,gb_y,-.13),(5.70,.10,.26),topsoil,.008)
box("Groundbed Upper Soil",(5.50,gb_y,-.57),(5.70,.10,.62),upper,.008)
box("Groundbed Backfill",(5.50,gb_y,-2.68),(5.70,.10,3.60),backfill,.008)
rx,ry=-5.5,.15
tx,ty=-1.3,.10

# Main buried circuits sit in front of the section face so the viewer can actually read them.
tube("Positive Main",[
    (rx+.16,ry,1.08),
    (rx+.16,.28,-.28),
    (-4.4,.28,-.48),
    (2.65,.28,-.48),
    (3.15,1.10,-1.05),
    (3.35,2.25,-1.92)
],.011,red)

tube("Rectifier Negative",[
    (rx-.15,ry,1.08),
    (rx-.15,-.28,-.34),
    (-4.65,-.28,-.70),
    (-4.15,-.28,PIPE_Z+PIPE_R)
],.010,blue)

tube("Test Structure Lead",[
    (tx,ty,1.08),
    (tx,.02,-.34),
    (-.95,.02,-.68),
    (-.55,.02,PIPE_Z+PIPE_R)
],.0065,black)

tube("Reference Electrode Lead",[
    (tx,ty,1.08),
    (tx,.40,-.38),
    (-.30,.40,-1.00),
    (1.10,.45,-1.80)
],.0065,yellow)
# Side returns make the right-hand groundbed read as a recessed cutaway rather than a flat diagram.
box("Groundbed Left Return",(3.12,1.75,-2.30),(.10,1.80,4.60),lower,.008)
box("Groundbed Right Return",(7.88,1.75,-2.30),(.10,1.80,4.60),lower,.008)

# Keep pipe attachments compact and on distinct viewing planes.
a=bpy.data.objects.get("Rectifier Negative Attachment")
if a: a.location.y=-.28
a=bpy.data.objects.get("Test Structure Attachment")
if a: a.location.y=.02

# Reference electrode remains beside the pipe, not bonded to it, and in front of the soil face.
ref=bpy.data.objects.get("Permanent Reference Electrode")
if ref:
    ref.location.x=1.10
    ref.location.y=.45
    ref.location.z=-1.95

# Rebuild the groundbed header and five drops in front of the recessed backfill face.
tube("Positive Header",[(3.35,2.25,-1.92),(7.65,2.25,-1.92)],.010,red)
for i,x in enumerate([3.7,4.6,5.5,6.4,7.3],1):
    tube(f"Anode Lead {i}",[(x,2.25,-1.92),(x,2.25,-2.20)],.007,red)
# Preserve the locked Gate A camera and above-grade composition.
sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_B_DOLLHOUSE_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("GROUND_FRONT_EDGE",round(ground.location.y-ground.dimensions.y/2,2))
print("MAIN_SECTION_Y",main_y)
print("GROUNDBED_SECTION_Y",gb_y)
print("REF_Y",round(ref.location.y,2) if ref else "NA")
print("ANODE_BODIES",len([o for o in bpy.data.objects if o.type=="MESH" and o.name.startswith("Anode ")]))
print("ANODE_LEADS",len([o for o in bpy.data.objects if o.name.startswith("Anode Lead")]))

import bpy, math

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateB_circuits.png"
PIPE_Z=-1.2954
PIPE_R=.381

def material(name,color,rough=.42):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    b=m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value=(*color,1)
    b.inputs["Roughness"].default_value=rough
    return m

def tube(name,pts,r,m):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=5
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(m); return o
def pad(name,x,y,z,m):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=1, location=(x,y,z))
    o=bpy.context.object; o.name=name
    o.scale=(.075,.028,.020)
    o.data.materials.append(m)
    return o

red=material("Circuit Positive Bright",(.78,.035,.025),.34)
blue=material("Circuit Negative Blue",(.025,.17,.72),.34)
testmat=material("Test Lead Gray",(.36,.39,.41),.38)
yellow=material("Reference Lead Bright",(.78,.58,.06),.36)
padmat=material("Coating Repair Patch",(.055,.06,.055),.58)
refmat=material("Reference Electrode Ceramic",(.64,.69,.57),.52)

rx,ry=-5.5,.15
tx,ty=-1.3,.10
# Compact pipe-surface attachments on two distinct front quadrants.
neg_x,neg_y=-4.15,-.24
neg_z=PIPE_Z+math.sqrt(PIPE_R**2-neg_y**2)
test_x,test_y=-.55,-.10
test_z=PIPE_Z+math.sqrt(PIPE_R**2-test_y**2)

tube("Rectifier Negative",[
    (rx-.15,ry,1.08),
    (rx-.15,-.24,-.32),
    (-4.72,-.24,-.72),
    (neg_x,neg_y,neg_z)
],.012,blue)

tube("Test Structure Lead",[
    (tx,ty,1.08),
    (tx,-.10,-.34),
    (-.96,-.10,-.68),
    (test_x,test_y,test_z)
],.0085,testmat)

pad("Rectifier Negative Attachment",neg_x,neg_y,neg_z+.012,padmat)
pad("Test Structure Attachment",test_x,test_y,test_z+.012,padmat)
# Reference electrode remains at the approved location, but gets a readable ceramic body.
ref=bpy.data.objects.get("Permanent Reference Electrode")
if ref: bpy.data.objects.remove(ref,do_unlink=True)

bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=.075,depth=.34,location=(1.10,.45,-1.95))
ref=bpy.context.object; ref.name="Permanent Reference Electrode"
ref.data.materials.append(refmat)

bpy.ops.mesh.primitive_uv_sphere_add(segments=24,ring_count=12,radius=.078,location=(1.10,.45,-1.78))
cap=bpy.context.object; cap.name="Reference Electrode Cap"
cap.scale.z=.35; cap.data.materials.append(refmat)

tube("Reference Electrode Lead",[
    (tx,ty,1.08),
    (tx,.34,-.36),
    (-.28,.34,-1.00),
    (1.10,.45,-1.78)
],.0085,yellow)
# Positive circuit stays in its approved route, but the groundbed header is lowered into view.
tube("Positive Main",[
    (rx+.16,ry,1.08),
    (rx+.16,.28,-.28),
    (-4.40,.28,-.48),
    (2.65,.28,-.48),
    (3.12,1.05,-1.05),
    (3.35,2.15,-2.02)
],.0125,red)

tube("Positive Header",[
    (3.35,2.15,-2.02),
    (7.65,2.15,-2.02)
],.012,red)

for i,x in enumerate([3.7,4.6,5.5,6.4,7.3],1):
    tube(f"Anode Lead {i}",[
        (x,2.15,-2.02),
        (x,2.25,-2.20)
    ],.0085,red)
sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_B_CIRCUITS_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("NEG_ATTACH",round(neg_y,3),round(neg_z,3))
print("TEST_ATTACH",round(test_y,3),round(test_z,3))
print("REF_LOC",tuple(round(v,3) for v in bpy.data.objects["Permanent Reference Electrode"].location))
print("HEADER_Z",-2.02)
print("ANODE_BODIES",len([o for o in bpy.data.objects if o.type=="MESH" and o.name.startswith("Anode ")]))
print("ANODE_LEADS",len([o for o in bpy.data.objects if o.name.startswith("Anode Lead")]))

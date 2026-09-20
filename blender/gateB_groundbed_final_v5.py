import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateB_groundbed_final.png"

def tube(name,pts,r,m):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    c=bpy.data.curves.new(name,"CURVE"); c.dimensions="3D"
    c.bevel_depth=r; c.bevel_resolution=5
    s=c.splines.new("POLY"); s.points.add(len(pts)-1)
    for p,co in zip(s.points,pts): p.co=(*co,1)
    o=bpy.data.objects.new(name,c); bpy.context.collection.objects.link(o)
    o.data.materials.append(m); return o

red=bpy.data.materials.get("Circuit Positive Bright")
yellow=bpy.data.materials.get("Reference Lead Bright")
refmat=bpy.data.materials.get("Reference Electrode Ceramic")

# Groundbed header remains above anode tops physically, but is pulled forward in the cutaway.
HEADER_Y=.80
HEADER_Z=-2.05
ANODE_Y=2.25
ANODE_TOP=-2.20
# Rebuild the visible positive approach and header without moving any equipment.
tube("Positive Main",[
    (-5.34,.15,1.08),
    (-5.34,.28,-.28),
    (-4.40,.28,-.48),
    (2.65,.28,-.48),
    (3.12,.55,-1.10),
    (3.35,HEADER_Y,HEADER_Z)
],.0125,red)

tube("Positive Header",[
    (3.35,HEADER_Y,HEADER_Z),
    (7.65,HEADER_Y,HEADER_Z)
],.013,red)

for i,x in enumerate([3.7,4.6,5.5,6.4,7.3],1):
    tube(f"Anode Lead {i}",[
        (x,HEADER_Y,HEADER_Z),
        (x,1.65,HEADER_Z),
        (x,ANODE_Y,ANODE_TOP)
    ],.009,red)
# Slightly strengthen the reference electrode silhouette without exaggerating its scale.
for n in ["Permanent Reference Electrode","Reference Electrode Cap"]:
    o=bpy.data.objects.get(n)
    if o: bpy.data.objects.remove(o,do_unlink=True)

bpy.ops.mesh.primitive_cylinder_add(
    vertices=32,radius=.085,depth=.40,location=(1.10,.25,-1.98)
)
ref=bpy.context.object; ref.name="Permanent Reference Electrode"
ref.data.materials.append(refmat)

bpy.ops.mesh.primitive_uv_sphere_add(
    segments=24,ring_count=12,radius=.087,location=(1.10,.25,-1.78)
)
cap=bpy.context.object; cap.name="Reference Electrode Cap"
cap.scale.z=.32; cap.data.materials.append(refmat)

tube("Reference Electrode Lead",[
    (-1.30,.10,1.08),
    (-1.30,.32,-.36),
    (-.28,.32,-1.00),
    (1.10,.25,-1.78)
],.009,yellow)
sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_B_GROUNDBED_FINAL_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("HEADER_Y_Z",HEADER_Y,HEADER_Z)
print("REF_LOC",tuple(round(v,3) for v in ref.location))
print("ANODE_BODIES",len([o for o in bpy.data.objects if o.type=="MESH" and o.name.startswith("Anode ")]))
print("ANODE_LEADS",len([o for o in bpy.data.objects if o.name.startswith("Anode Lead")]))

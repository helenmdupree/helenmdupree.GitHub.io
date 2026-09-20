import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateB_wiring_clean.png"

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
HEADER_Y=2.25
HEADER_Z=-2.12
ANODE_TOP=-2.20
# Positive main ends at the real groundbed plane.
tube("Positive Main",[
    (-5.34,.15,1.08),
    (-5.34,.28,-.28),
    (-4.40,.28,-.48),
    (2.65,.28,-.48),
    (3.12,.85,-1.10),
    (3.35,HEADER_Y,HEADER_Z)
],.0125,red)

tube("Positive Header",[
    (3.35,HEADER_Y,HEADER_Z),
    (7.65,HEADER_Y,HEADER_Z)
],.013,red)

# Five clean, straight drops: no depth jogs and no triangular artifacts.
for i,x in enumerate([3.7,4.6,5.5,6.4,7.3],1):
    tube(f"Anode Lead {i}",[
        (x,HEADER_Y,HEADER_Z),
        (x,HEADER_Y,ANODE_TOP)
    ],.009,red)
# Reference-electrode lead: continuous and visibly separate from pipe-bond leads.
tube("Reference Electrode Lead",[
    (-1.30,.10,1.08),
    (-1.30,.30,-.34),
    (1.10,.25,-.58),
    (1.10,.25,-1.78)
],.009,yellow)

sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_B_WIRING_CLEAN_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("HEADER",HEADER_Y,HEADER_Z)
print("ANODE_LEADS",len([o for o in bpy.data.objects if o.name.startswith("Anode Lead")]))
print("REF_LOC",tuple(round(v,3) for v in bpy.data.objects["Permanent Reference Electrode"].location))

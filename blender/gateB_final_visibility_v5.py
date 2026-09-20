import bpy

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateB_final_visibility.png"

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
ANODE_DROP=.45
NEW_ANODE_TOP=-2.65
# Lower all five anodes together without changing their spacing or groundbed plane.
for i,x in enumerate([3.7,4.6,5.5,6.4,7.3],1):
    o=bpy.data.objects.get(f"Anode {i}")
    if o:
        o.location.z -= ANODE_DROP
    tube(f"Anode Lead {i}",[
        (x,HEADER_Y,HEADER_Z),
        (x,HEADER_Y,NEW_ANODE_TOP)
    ],.009,red)

# Bring the reference electrode slightly forward and lower for an unmistakable visual termination.
ref=bpy.data.objects.get("Permanent Reference Electrode")
cap=bpy.data.objects.get("Reference Electrode Cap")
if ref:
    ref.location=(1.10,-.15,-2.08)
if cap:
    cap.location=(1.10,-.15,-1.88)

tube("Reference Electrode Lead",[
    (-1.30,.10,1.08),
    (-1.30,.26,-.34),
    (-.20,.08,-1.02),
    (1.10,-.15,-1.88)
],.009,yellow)
sc=bpy.context.scene
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_B_FINAL_VISIBILITY_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("ANODE_TOP",NEW_ANODE_TOP)
print("ANODE_CENTERS",[round(bpy.data.objects[f"Anode {i}"].location.z,3) for i in range(1,6)])
print("REF_LOC",tuple(round(v,3) for v in bpy.data.objects["Permanent Reference Electrode"].location))
print("ANODE_LEADS",len([o for o in bpy.data.objects if o.name.startswith("Anode Lead")]))

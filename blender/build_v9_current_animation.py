import bpy, math, os
from mathutils import Vector

SRC=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v8_1_realism_truckfix.blend"
OUT=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v9_current_animation.blend"

sc=bpy.context.scene
fx=bpy.data.collections.get("ICCP Current FX")
if fx is None:
    fx=bpy.data.collections.new("ICCP Current FX")
    sc.collection.children.link(fx)

def fxmat(name,color,strength=2.5):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    nt=m.node_tree
    nt.nodes.clear()
    out=nt.nodes.new("ShaderNodeOutputMaterial")
    em=nt.nodes.new("ShaderNodeEmission")
    em.inputs["Color"].default_value=(*color,1)
    em.inputs["Strength"].default_value=strength
    nt.links.new(em.outputs["Emission"],out.inputs["Surface"])
    return m
pos_mat=fxmat("FX Positive Pulse",(1.0,.055,.025),3.0)
neg_mat=fxmat("FX Negative Pulse",(.02,.28,1.0),2.8)
soil_mat=fxmat("FX Soil Current",(.02,.72,.76),2.1)
measure_mat=fxmat("FX Measurement",(.88,.72,.18),1.8)

def overlay_curve(src_name,fx_name,mat,start,end,mult=1.45):
    src=bpy.data.objects[src_name]
    data=src.data.copy()
    o=src.copy()
    o.data=data
    o.name=fx_name
    fx.objects.link(o)
    for col in list(o.users_collection):
        if col is not fx:
            col.objects.unlink(o)
    o.data.materials.clear()
    o.data.materials.append(mat)
    o.data.bevel_depth=src.data.bevel_depth*mult
    o.data.bevel_resolution=max(src.data.bevel_resolution,5)
    o.data.bevel_factor_start=0.0
    o.data.bevel_factor_end=0.0
    o.data.keyframe_insert("bevel_factor_end",frame=start)
    o.data.bevel_factor_end=1.0
    o.data.keyframe_insert("bevel_factor_end",frame=end)
    return o
# Current path on the real conductors.
overlay_curve("Positive Main","FX Positive Main",pos_mat,190,300,1.55)
overlay_curve("Positive Header","FX Positive Header",pos_mat,292,338,1.55)

for i in range(1,6):
    overlay_curve(
        f"Anode Lead {i}",f"FX Anode Lead {i}",
        pos_mat,330+(i-1)*4,374+(i-1)*4,1.7
    )

# Negative return is shown only after pipeline current reaches the return point.
overlay_curve("Rectifier Negative","FX Negative Return",neg_mat,492,558,1.6)

# Test/reference leads are measurement cues, not ICCP return-current arrows.
overlay_curve("Test Structure Lead","FX Test Measurement",measure_mat,548,582,1.5)
overlay_curve("Reference Electrode Lead","FX Reference Measurement",measure_mat,558,592,1.45)
def make_path(name,pts,mat,start,end,depth=.012):
    cu=bpy.data.curves.new(name+" Data","CURVE")
    cu.dimensions="3D"
    cu.resolution_u=2
    cu.bevel_depth=depth
    cu.bevel_resolution=4
    sp=cu.splines.new("POLY")
    sp.points.add(len(pts)-1)
    for p,co in zip(sp.points,pts):
        p.co=(*co,1.0)
    o=bpy.data.objects.new(name,cu)
    fx.objects.link(o)
    cu.materials.append(mat)
    cu.bevel_factor_start=0.0
    cu.bevel_factor_end=0.0
    cu.keyframe_insert("bevel_factor_end",frame=start)
    cu.bevel_factor_end=1.0
    cu.keyframe_insert("bevel_factor_end",frame=end)
    return o

# Subtle current streamlines through electrolyte/soil from groundbed toward pipe.
for j,x in enumerate([3.8,4.45,5.1,5.75,6.4,7.05]):
    pts=[(x,2.23,-3.05),(x-.08,1.72,-2.72),(x+.05,1.17,-2.24),
         (x-.04,.67,-1.82),(x,.30,-1.52)]
    make_path(f"FX Soil Stream {j+1}",pts,soil_mat,365+j*5,438+j*4,.010)
# Protective-current cue along the near side of the coated pipeline.
pipe_pts=[(7.1,-.37,-1.23),(5.0,-.37,-1.23),(2.2,-.37,-1.23),
          (-1.0,-.37,-1.23),(-4.05,-.37,-1.23)]
make_path("FX Pipeline Current",pipe_pts,soil_mat,420,500,.011)

# Restrained rectifier meter energization cue.
meter=bpy.data.objects["Rectifier Meter"]
bpy.ops.mesh.primitive_cube_add(location=(-5.5,-.124,1.57))
panel=bpy.context.object
panel.name="FX Rectifier Meter Glow"
panel.dimensions=(.132,.006,.072)
bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
for col in list(panel.users_collection):
    col.objects.unlink(panel)
fx.objects.link(panel)

panel_mat=fxmat("FX Meter Energized",(.12,.72,.50),0.0)
panel.data.materials.append(panel_mat)
em=panel_mat.node_tree.nodes.get("Emission")
em.inputs["Strength"].default_value=0.0
em.inputs["Strength"].keyframe_insert("default_value",frame=150)
em.inputs["Strength"].default_value=1.6
em.inputs["Strength"].keyframe_insert("default_value",frame=180)
em.inputs["Strength"].keyframe_insert("default_value",frame=300)
# Technical guardrails.
assert bpy.data.objects.get("Truck Generic Work Pickup") is not None
assert bpy.data.objects["Truck Generic Work Pickup"].hide_render is False
assert bpy.data.objects.get("Negative Cadweld Mastic") is not None
assert bpy.data.objects.get("Test Lead Cadweld Mastic") is not None
assert bpy.data.objects.get("Permanent Reference Electrode") is not None

sc.frame_start=1
sc.frame_end=624
sc.render.fps=24
sc.frame_set(1)
bpy.ops.wm.save_as_mainfile(filepath=OUT)

print("V9_CURRENT_ANIMATION_SAVED",OUT)
print("FX_OBJECTS",len(fx.objects))
print("TRUCK",bpy.data.objects["Truck Generic Work Pickup"].name)
print("CADWELDS",
      bpy.data.objects["Negative Cadweld Mastic"].name,
      bpy.data.objects["Test Lead Cadweld Mastic"].name)

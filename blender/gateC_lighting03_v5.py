import bpy, math
from mathutils import Vector

BLEND=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5.blend"
RENDER=r"C:\GitHub\soubel-iccp-v5-cleanstart\blender\iccp_cinematic_v5_gateC_lighting03.png"

def look(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat("-Z","Y").to_euler()

def area(name,loc,target,energy,size,color):
    old=bpy.data.objects.get(name)
    if old: bpy.data.objects.remove(old,do_unlink=True)
    bpy.ops.object.light_add(type="AREA",location=loc)
    o=bpy.context.object; o.name=name
    o.data.energy=energy
    o.data.shape="DISK"
    o.data.size=size
    o.data.color=color
    look(o,target)
    return o

sc=bpy.context.scene
world=sc.world
bg=world.node_tree.nodes.get("Background") if world and world.use_nodes else None
if bg:
    bg.inputs["Color"].default_value=(.22,.38,.56,1)
    bg.inputs["Strength"].default_value=.78
sun=bpy.data.objects.get("Sun")
if sun:
    sun.data.energy=2.25
    sun.data.angle=math.radians(5.5)
    sun.data.color=(1.0,.88,.74)
    sun.rotation_euler=(math.radians(34),math.radians(-16),math.radians(-40))

area0=bpy.data.objects.get("Area")
if area0:
    area0.data.energy=420
    area0.data.size=14
    area0.data.color=(.68,.78,1.0)

# Dedicated fills illuminate the exposed section without changing geometry.
area("Cutaway Fill",(0,-8.5,.2),(0,.8,-1.8),520,10.0,(.82,.88,1.0))
area("Groundbed Fill",(5.5,-5.5,-.2),(5.5,2.2,-2.8),580,5.5,(.86,.90,1.0))
area("Anchor Fill",(-5.0,-7.5,4.2),(-5.0,.1,1.0),620,6.0,(1.0,.91,.80))

# Restore a little coated-steel highlight to the pipeline.
pm=bpy.data.materials.get("Pipeline Green")
if pm and pm.use_nodes:
    bs=pm.node_tree.nodes.get("Principled BSDF")
    if bs:
        bs.inputs["Roughness"].default_value=.32
        bs.inputs["Metallic"].default_value=.05
# Keep the established AgX transform; lift exposure only enough for late-morning readability.
sc.view_settings.exposure=.08
sc.render.engine="BLENDER_EEVEE"
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.image_settings.file_format="PNG"
sc.render.filepath=RENDER

bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)

print("GATE_C_LIGHTING03_SAVED")
print("PIPE_Z",round(bpy.data.objects["30in Pipeline"].location.z,4))
print("CAM_LOC",tuple(round(v,3) for v in sc.camera.location))
print("ANODE_CENTERS",[round(bpy.data.objects[f"Anode {i}"].location.z,3) for i in range(1,6)])
print("REF_LOC",tuple(round(v,3) for v in bpy.data.objects["Permanent Reference Electrode"].location))
print("EXPOSURE",sc.view_settings.exposure)
print("FILLS",[n for n in ["Cutaway Fill","Groundbed Fill","Anchor Fill"] if bpy.data.objects.get(n)])

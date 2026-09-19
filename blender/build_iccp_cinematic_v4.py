import bpy, math
from mathutils import Vector

BLEND=r"C:\\GitHub\\soubel-iccp-interactive\\blender\\iccp_cinematic_v4.blend"
RENDER=r"C:\\GitHub\\soubel-iccp-interactive\\blender\\iccp_cinematic_v4_blocking.png"

def look(obj,target):
    obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()

def getmat(name,color,metal=0.0,rough=.55):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    b=m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value=(*color,1)
    b.inputs['Metallic'].default_value=metal
    b.inputs['Roughness'].default_value=rough
    return m
def box(name,loc,dims,mat,bev=.04):
    bpy.ops.mesh.primitive_cube_add(location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bev:
        md=o.modifiers.new('Bevel','BEVEL'); md.width=bev; md.segments=3
    o.data.materials.append(mat)
    return o

def cyl_between(name,a,b,r,mat):
    a,b=Vector(a),Vector(b); mid=(a+b)/2; vec=b-a
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=r,depth=vec.length,location=mid)
    o=bpy.context.object; o.name=name
    o.rotation_euler=vec.to_track_quat('Z','Y').to_euler()
    o.data.materials.append(mat)
    return o
# Remove old mannequin; preserve ICCP equipment.
for o in list(bpy.data.objects):
    if o.name.startswith('Human') or o.name=='Sphere':
        bpy.data.objects.remove(o,do_unlink=True)

navy=getmat('Technician Navy',(.035,.075,.11),0,.62)
skin=getmat('Technician Skin',(.52,.31,.20),0,.62)
helmet=getmat('Hardhat White',(.92,.94,.93),0,.34)
vest=getmat('HiVis Vest',(.64,.76,.12),0,.48)
rubber=getmat('Tire Rubber',(.025,.028,.03),0,.78)
truck=getmat('Service Truck White',(.72,.76,.76),.08,.38)
glass=getmat('Truck Glass',(.08,.16,.19),.15,.23)
field=getmat('Rear Field',(.12,.25,.08),0,.92)
rowmat=getmat('ROW Track',(.30,.25,.15),0,.95)

box('Rear Field',(0,9.0,.015),(34,14,.03),field,.02)
box('ROW Track',(0,7.0,.035),(30,3.2,.035),rowmat,.02)
hx,hy=-5.03,-.92
box('Tech Torso',(hx,hy,1.08),(.42,.28,.58),navy,.09)
box('Tech Vest',(hx,hy-.15,1.08),(.44,.035,.50),vest,.025)
box('Tech Pelvis',(hx,hy,.72),(.34,.25,.18),navy,.05)
bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=.13,location=(hx,hy,1.52))
head=bpy.context.object; head.name='Tech Head'; head.data.materials.append(skin)
bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=.15,location=(hx,hy,1.64))
hat=bpy.context.object; hat.name='Tech Hardhat'; hat.scale=(1.08,.95,.48); hat.data.materials.append(helmet)

cyl_between('Tech Left Leg',(hx-.10,hy,.68),(hx-.12,hy,.16),.07,navy)
cyl_between('Tech Right Leg',(hx+.10,hy,.68),(hx+.12,hy,.16),.07,navy)
box('Tech Left Boot',(hx-.12,hy-.05,.07),(.18,.34,.12),rubber,.035)
box('Tech Right Boot',(hx+.12,hy-.05,.07),(.18,.34,.12),rubber,.035)

ls=(hx-.22,hy,1.28); le=(-5.36,-.73,1.27); lh=(-5.73,-.43,1.35)
rs=(hx+.22,hy,1.28); re=(-5.22,-.69,1.12); rh=(-5.62,-.42,1.17)
for name,a,b in [('Tech Left Upper Arm',ls,le),('Tech Left Forearm',le,lh),('Tech Right Upper Arm',rs,re),('Tech Right Forearm',re,rh)]:
    cyl_between(name,a,b,.055,navy)
for name,p in [('Tech Left Glove',lh),('Tech Right Glove',rh)]:
    bpy.ops.mesh.primitive_uv_sphere_add(segments=20,ring_count=10,radius=.065,location=p)
    bpy.context.object.name=name; bpy.context.object.data.materials.append(rubber)

tx,ty=2.2,7.1
box('Truck Body',(tx,ty,.58),(4.4,1.82,.52),truck,.12)
box('Truck Cab',(tx-1.00,ty,.98),(1.75,1.76,1.12),truck,.12)
box('Truck Windshield',(tx-1.42,ty-.90,1.08),(.70,.035,.46),glass,.03)
box('Truck Bed',(tx+1.12,ty,.88),(1.80,1.68,.18),truck,.05)
for x in (tx-1.45,tx+1.35):
    for y in (ty-.83,ty+.83):
        bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=.34,depth=.22,location=(x,y,.34),rotation=(math.radians(90),0,0))
        bpy.context.object.name='Truck Wheel'; bpy.context.object.data.materials.append(rubber)
cam=bpy.context.scene.camera
cam.location=(-.4,-21.5,2.45)
cam.data.lens=48
look(cam,(-1.4,0,.45))

sc=bpy.context.scene
sc.render.resolution_x=1600
sc.render.resolution_y=900
sc.render.resolution_percentage=100
sc.render.filepath=RENDER
bpy.ops.wm.save_as_mainfile(filepath=BLEND)
bpy.ops.render.render(write_still=True)
print('V4_BLOCKING_SAVED',BLEND)
print('V4_BLOCKING_RENDER',RENDER)
print('TECH_ARM_SEGMENTS',len([o for o in bpy.data.objects if 'Arm' in o.name or 'Forearm' in o.name]))
print('TECH_LEGS',len([o for o in bpy.data.objects if 'Leg' in o.name]))

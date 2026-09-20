import bpy, math, sys
from mathutils import Vector

pipe=bpy.data.objects["30in Pipeline"]
r=0.381
cz=pipe.location.z

def mat(name):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes=True
    bs=m.node_tree.nodes.get("Principled BSDF")
    bs.inputs["Base Color"].default_value=(0.006,0.006,0.007,1)
    bs.inputs["Roughness"].default_value=0.72
    bs.inputs["Metallic"].default_value=0.0
    return m

mastic=mat("Cadweld Mastic Black")

for oldname,newname in [
    ("Rectifier Negative Attachment","Negative Cadweld Mastic"),
    ("Test Structure Attachment","Test Lead Cadweld Mastic"),
]:
    old=bpy.data.objects.get(oldname)
    if old is None:
        print("MISSING",oldname)
        continue

    x,y,_=old.location
    zsurf=cz + math.sqrt(max(r*r-y*y,0.0))
    normal=Vector((0.0,y,zsurf-cz)).normalized()

    bpy.data.objects.remove(old,do_unlink=True)

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=48, ring_count=24,
        location=(x,y,zsurf+0.008)
    )
    o=bpy.context.object
    o.name=newname
    o.scale=(0.12,0.075,0.018)
    o.rotation_mode="QUATERNION"
    o.rotation_quaternion=Vector((0,0,1)).rotation_difference(normal)
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(mastic)
    for poly in o.data.polygons:
        poly.use_smooth=True

    print(newname,"LOC",tuple(round(v,4) for v in o.location),
          "NORMAL",tuple(round(v,4) for v in normal))

bpy.ops.wm.save_as_mainfile(filepath=bpy.data.filepath)
print("CADWELD_MASTIC_CORRECTION_SAVED",bpy.data.filepath)

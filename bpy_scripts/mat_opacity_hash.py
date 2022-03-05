import bpy
def blend_method():
    for m in bpy.data.materials:
        m.blend_method = 'HASHED'
blend_method()
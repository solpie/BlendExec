import bpy
bpy.ops.object.duplicate()
bpy.ops.object.modifier_add(type='SOLIDIFY')
obj = bpy.context.active_object
obj.modifiers["Solidify"].use_flip_normals = True
obj.active_material.use_backface_culling = True

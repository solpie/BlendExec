# [as_exec]
import bpy
def main():
    mesh_obj_arr = []
    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            mesh_obj_arr.append(obj)
    bpy.ops.object.empty_add(type='PLAIN_AXES', align='CURSOR')
    ept_obj = bpy.context.view_layer.objects.active
    for obj in mesh_obj_arr:
        obj.select_set(1)
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
    bpy.ops.object.rotation_clear(clear_delta=False)
    for obj in mesh_obj_arr:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.transform_apply(rotation=True)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        obj.select_set(0)
    bpy.context.view_layer.objects.active = ept_obj
    bpy.ops.object.delete(use_global=False)

main()

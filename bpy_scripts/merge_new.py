#[as_exec]
import bpy

def merge_new():
    merge_obj = None
    hide_arr = []
    dupli_arr = []
    
    for obj in bpy.context.selected_objects:
        if obj.type =="MESH":
            hide_arr.append(obj.name)
    # duplicate mesh
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False})
    act_obj = bpy.context.selected_objects[0]
    for obj in bpy.context.selected_objects:
        if obj.type =="MESH":
            dupli_arr.append(obj)
    # apply mirror part
    for obj in dupli_arr:
        if obj.type =="MESH":
            bpy.context.view_layer.objects.active = obj
            for m in obj.modifiers:
                if m.type in ["MIRROR","SOLIDIFY","BEVEL"]:
                    bpy.ops.object.modifier_apply(modifier=m.name)

    bpy.context.view_layer.objects.active = act_obj
    bpy.ops.object.join()
    # remove double
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.001)
    bpy.ops.object.mode_set(mode='OBJECT')
    #hide part
    for obj in hide_arr:
        bpy.data.objects[obj].hide_set(1)

    merge_obj = bpy.context.active_object
    merge_obj.name = "*"+merge_obj.name
    
merge_new()
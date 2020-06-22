#[as_exec]
import bpy
def main():
    mesh_obj_arr = []
    rig_obj = None
    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            if not obj.active_shape_key:
                mesh_obj_arr.append(obj)
        elif obj.type == "ARMATURE":
            rig_obj = obj
        pass
    if rig_obj and len(mesh_obj_arr) > 0:
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)
        for obj in mesh_obj_arr:
            tmp_mdf = obj.modifiers.new(name="new_rig", type="ARMATURE")
            for mdf in obj.modifiers:
                if mdf.type == "ARMATURE":
                    tmp_mdf.object = mdf.object
                    pass
                pass
            bpy.context.view_layer.objects.active = obj
            while obj.modifiers[0].name!="new_rig":
                bpy.ops.object.modifier_move_up(modifier="new_rig")
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="new_rig")
        # bpy.context.view_layer.objects.active = rig_obj
        # bpy.ops.object.mode_set(mode='POSE', toggle=False)
        # bpy.ops.pose.armature_apply(selected=False)
    pass
main()

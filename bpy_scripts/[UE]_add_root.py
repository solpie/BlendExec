#[as_exec]
import bpy

def add_Root(old_root_name=''):
    bpy.ops.view3d.snap_cursor_to_center()
    bpy.ops.object.mode_set(mode='EDIT')
    old_root = None
    if old_root_name:
        old_root = bpy.context.active_object.data.edit_bones[old_root_name]

    # amrt  = bpy.context.active_object
    # old_root = bpy.context.selected_bones[0]
    # print('old_root bone '+old_root.name)
    
    bpy.ops.armature.bone_primitive_add(name='Root')
    bpy.ops.armature.select_linked()
    new_root = bpy.context.selected_bones[0]
    old_root.parent = new_root

    bpy.ops.object.mode_set(mode='POSE')

    # new_root.select = False
    # old_root.select = True
    # new_root.select = True
    # bpy.ops.armature.parent_set(type='OFFSET')

# pelvis for auto rig pro
add_Root('pelvis')
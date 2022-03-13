import bpy


def main():
    def get_spine_list():
        spine_bone_list = [
             'c_head.x'
             ,'c_neck.x'
                ,'c_spine_03.x'#
            , 'c_spine_02.x'#
            , 'c_spine_01.x'#
            , 'c_root_master.x'#
            # 'neck_ref.x'
            # , 'spine_03_ref.x'#
            # , 'spine_02_ref.x'#
            # , 'spine_01_ref.x'#
            # , 'root_ref.x'#
        ]
        a = []
        for bn in spine_bone_list:
            if bpy.context.active_object.pose.bones.get(bn):
                a.append(bn)
        return a
        pass
    def add_constraint(const_type, const_entity, target_obj, sub_target_name,head_tail=0.0):
        constraint = const_entity.constraints.new(const_type)
        constraint.target = target_obj
        constraint.subtarget = sub_target_name
        constraint.head_tail = head_tail
        return constraint

    bpy.ops.object.mode_set(mode='EDIT')
    bones = bpy.context.active_object.data.bones
    rig_obj = bpy.context.active_object

    spine_bone_list = get_spine_list()
    #
    edit_bones = rig_obj.data.edit_bones
    pose_bones = rig_obj.pose.bones
    # 创建neck root
    head_root = bpy.context.active_object.data.edit_bones.new('head_root[S]')
    head_root.head = bones['c_head.x'].head_local
    # head_root.head = (head_root.head[0],
    #                 head_root.head[1]+0.2, head_root.head[2])
    head_root.tail = (head_root.head[0],
                    head_root.head[1]+0.2, head_root.head[2])
    # edit_bones['c_head.x'].parent = neck_root
    #
    # create rev bone
    last_rev_bone_name  = None
    sun_bone_list = []
    for bone_name in spine_bone_list:
        bpy.ops.object.mode_set(mode='EDIT')
        spine_bone = bones[bone_name]
        rev_bone = bpy.context.active_object.data.edit_bones.new(
                bone_name+'[R]')
        rev_bone.tail = spine_bone.head_local
        rev_bone.head = spine_bone.tail_local
        
        rev_bone_name = rev_bone.name
        
        sun_bone = bpy.context.active_object.data.edit_bones.new(
                bone_name+'[S]')
        sun_bone.head = spine_bone.head_local
        sun_bone.tail = (sun_bone.head[0],
                            sun_bone.head[1]+0.5, sun_bone.head[2])
        sun_bone_name = sun_bone.name
        sun_bone_list.append(sun_bone_name)
        # edit_bones[sun_bone_name].parent = head_root
        # set parent
        if last_rev_bone_name:
            edit_bones[rev_bone.name].parent = edit_bones[last_rev_bone_name]
            pass
        last_rev_bone_name = rev_bone.name
        # set constraint
        bpy.ops.object.mode_set(mode='POSE')
        add_constraint('COPY_LOCATION', pose_bones[bone_name], rig_obj, rev_bone_name,1)
        add_constraint('DAMPED_TRACK', pose_bones[rev_bone_name], rig_obj, sun_bone_name)
        pose_bones[sun_bone_name].custom_shape=pose_bones['c_arms_pole.r'].custom_shape
        pose_bones[sun_bone_name].custom_shape_translation[1] = 0.5
        pose_bones[sun_bone_name].custom_shape_scale_xyz[0] = 0.2
        pose_bones[sun_bone_name].custom_shape_scale_xyz[1] = 0.2
        pose_bones[sun_bone_name].custom_shape_scale_xyz[2] = 0.2
        # lock x y rotation
        pose_bones[bone_name].lock_rotation[0] = True
        pose_bones[bone_name].lock_rotation[2] = True
    # set pole parent
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.armature.select_all(action='DESELECT')
    head_root.select = True
    sun_bone_list.append('c_head.x[R]')
    for bone_name in sun_bone_list:
        edit_bones[bone_name].parent = edit_bones['head_root[S]']
        pass
    bpy.ops.object.mode_set(mode='POSE')
main()

import bpy


def main():
    def add_constraint(const_type, const_entity, target_obj, sub_target_name):
        constraint = const_entity.constraints.new(const_type)
        constraint.target = target_obj
        constraint.subtarget = sub_target_name
        # constraint.head_tail = 1.0
        return constraint

    bpy.ops.object.mode_set(mode='EDIT')
    bones = bpy.context.active_object.data.bones
    rig_obj = bpy.context.active_object
    spine_bone_list = [
        # 'c_neck.x'
        # , 'c_spine_03.x'#
        # , 'c_spine_02.x'#
        # , 'c_spine_01.x'#
        # , 'c_root_master.x'#
        'neck_ref.x'
        , 'spine_03_ref.x'#
        , 'spine_02_ref.x'#
        , 'spine_01_ref.x'#
        , 'root_ref.x'#
    ]
    conf = []
    sun_mao_conf = []
    last_mao =  None
    last_spine_bone = None
    for bone_name in spine_bone_list:
        spine_bone = bones[bone_name]
        # 断开parent
        rig_obj.data.edit_bones[bone_name].parent = None

        sun_bone = bpy.context.active_object.data.edit_bones.new(
            bone_name+'[S]')
        sun_bone.head = spine_bone.tail_local
        sun_bone.tail = (sun_bone.head[0],
                         sun_bone.head[1]+0.2, sun_bone.head[2])

        mao_bone = bpy.context.active_object.data.edit_bones.new(
            bone_name+'[M]')
        mao_bone.head = spine_bone.head_local
        mao_bone.tail = (mao_bone.head[0],
                         mao_bone.head[1]+0.2, mao_bone.head[2])
        conf.append([bone_name, sun_bone.name, mao_bone.name])
        if last_mao:
            sun_mao_conf.append([sun_bone.name,last_mao])
        # last tmp
        last_mao = mao_bone.name
        last_spine_bone = spine_bone.name
        pass

    bpy.ops.object.mode_set(mode='POSE')
    for c in conf:
        bone_name = c[0]
        sun_bone = c[1]
        mao_bone = c[2]
        print('spine_bone '+spine_bone.name)
        pose_spine_bone = rig_obj.pose.bones[bone_name]
        add_constraint('COPY_LOCATION', pose_spine_bone, rig_obj, mao_bone)
        add_constraint('DAMPED_TRACK', pose_spine_bone, rig_obj, sun_bone)
        add_constraint('LIMIT_DISTANCE', pose_spine_bone, rig_obj, sun_bone)
        pass
    # 下骨榫接上骨卯
    for sm in sun_mao_conf:
        sun_bone = sm[0]
        mao_bone = sm[1]
        pose_spine_bone = rig_obj.pose.bones[sun_bone]
        rig_obj.data.bones[sun_bone].hide = True
        add_constraint('COPY_LOCATION', pose_spine_bone, rig_obj, mao_bone)
    pass


main()

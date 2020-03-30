import bpy


def dump_track_rig():
    map_to = {
        #
        'Neck': 'c_neck.x',
        'head.x': 'c_head.x',   
        #
        'Clavicle_R': 'c_shoulder.r',
        'Clavicle_L': 'c_shoulder.l',
        'UpperArm_R': 'arm.r',#上臂
        'UpperArm_L': 'arm.l',
        'Forearm_R': 'forearm.r',#前臂
        'Forearm_L': 'forearm.l',
        'Hand_R': 'hand.r',
        'Hand_L': 'hand.l',
        #手指
        'Finger1_R': 'c_index1.r',
        'Finger11_R': 'c_index2.r',
        'Finger12_R': 'c_index3.r',
        'Finger1_L': 'c_index1.l',
        'Finger11_L': 'c_index2.l',
        'Finger12_L': 'c_index3.l',
        'Finger0_R': 'c_thumb1.r',
        'Finger01_R': 'c_thumb2.r',
        'Finger02_R': 'c_thumb3.r',
        'Finger0_L': 'c_thumb1.l',
        'Finger01_L': 'c_thumb2.l',
        'Finger02_L': 'c_thumb3.l',

        'Finger2_R': 'c_middle1.r',
        'Finger21_R': 'c_middle2.r',
        'Finger22_R': 'c_middle3.r',
        'Finger2_L': 'c_middle1.l',
        'Finger21_L': 'c_middle2.l',
        'Finger22_L': 'c_middle3.l',
        # leg
        'thigh.r': 'thigh.r',
        'thigh.l': 'thigh.l',
        'Calf_R': 'leg.r',
        'Calf_L': 'leg.l',
        'Foot_R': 'foot.r',
        'Foot_L': 'foot.l',
        
        'Toe0_R': 'c_toes_ik.r',
        'Toe0_L': 'c_toes_ik.l',
    }
    copy_all = {
        'Pelvis':'c_root_master.x',
        'Spine':'c_spine_01.x'}
    def rename(from_rig, target_rig):
        for b in from_rig.data.bones:
            if b.name in map_to.keys():
                b.name = map_to[b.name]
                print('keys', b.name)
                pass
        pass

    def add_constraint(const_type, const_entity, target_obj, sub_target_name):
        '''Works only in pose mode'''
        if len(const_entity.constraints) == 1 and const_entity.constraints[0].type == const_type:
            constraint = const_entity.constraints[0]
        else:
            constraint = const_entity.constraints.new(const_type)
        constraint.target = target_obj
        constraint.subtarget = sub_target_name
        constraint.head_tail = 1.0
        return constraint

    from_rig = bpy.data.objects['Armature_0']
    target_rig = bpy.data.objects['rig']

    rename(from_rig, target_rig)

    print(from_rig, target_rig)
    for pb in from_rig.pose.bones:
        if pb.name in map_to.values():
            add_constraint('DAMPED_TRACK', pb, target_rig, pb.name)
            #
            print(pb.name)
    pass


dump_track_rig()

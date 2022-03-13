import bpy
def main():
    bpy.ops.object.mode_set(mode='EDIT')
    bones = bpy.context.active_object.data.bones
    rig_obj = bpy.context.active_object
    spine_bone_list = [

         'c_spine_03.x'#
        , 'c_spine_02.x'#
        , 'c_spine_01.x'#

    ]
    for bone in spine_bone_list:
        if rig_obj.pose.bones.get(bone):
            pb = rig_obj.pose.bones[bone]
            for c in pb.constraints:
                pb.constraints.remove(c)

    pass
main()
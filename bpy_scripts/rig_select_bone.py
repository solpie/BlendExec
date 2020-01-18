import bpy


def select_bone(rig, bone):
    #rig = 'rig'
    #bone = 'c_hand_fk.r'
    mode = bpy.context.mode
    if mode == 'OBJECT':
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[rig].select_set(1)
        bpy.ops.object.posemode_toggle(1)
    bpy.ops.pose.select_all(action='DESELECT')
    armt = bpy.data.armatures[bpy.data.objects[rig].data.name]
    armt.bones[bone].select = True
    pass


select_bone('rig', 'c_hand_fk.r')

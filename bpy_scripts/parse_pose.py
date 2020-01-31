import bpy
import os

def paser_pose():
    file_globals = {}
    tmp_path = 'c:/tmp'
    data_filepath = os.path.join(tmp_path,'pose.py')
    exec(open(data_filepath).read(),file_globals)
    bones = file_globals["bones"]
    print(bones)
    rig = 'rig'
    mode = bpy.context.mode
    if mode == 'OBJECT':
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[rig].select_set(1)
        bpy.ops.object.posemode_toggle(1)
    
    bpy.ops.pose.select_all(action='SELECT')
    for b_ in bpy.context.selected_pose_bones:
        bone_data = bones[b_.name]
        loc = bone_data[1]
        rot = bone_data[0]
        scale = bone_data[2]
        # print(bone_data)
        if scale != (1.0, 1.0, 1.0):
            b_.scale = scale
        if loc != (0.0, 0.0, 0.0):
            b_.location = loc
        if rot != (0.0, 0.0, 0.0,'XYZ'):
            b_.rotation_mode = rot[3]
            b_.rotation_euler.x = rot[0]
            b_.rotation_euler.y = rot[1]
            b_.rotation_euler.z = rot[2]
    bpy.ops.pose.select_all(action='DESELECT')

paser_pose()

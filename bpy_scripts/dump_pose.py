import bpy


def dump_pose():
    rig = 'rig'
    mode = bpy.context.mode
    if mode == 'OBJECT':
        bpy.ops.object.select_all(action="DESELECT")
        bpy.data.objects[rig].select_set(1)
        bpy.ops.object.posemode_toggle(1)
    bpy.ops.pose.select_all(action='SELECT')
    # armt = bpy.data.armatures[bpy.data.objects[rig].data.name]
    line_str = 'bones={}\n'
    for b in bpy.context.selected_pose_bones:
        print(b.name)
        rot_euler = b.rotation_euler
        rot_euler = (rot_euler.x, rot_euler.y, rot_euler.z, rot_euler.order)
        loc = b.location
        location = (loc.x, loc.y, loc.z)
        s = b.scale
        scale = (s.x, s.y, s.z)
        line_str += 'bones["'+b.name+'"]=[' + str(rot_euler)+","+str(location)+","+str(scale)+"]\n"
        # line_str +="$".join([b.name , str(rot_euler),str(location),str(scale)])+'\n'
        print(line_str)
    line_str+='camera={}\n'
    cam = bpy.context.scene.camera
    loc = cam.location
    location = (loc.x, loc.y, loc.z)
    rot_euler = cam.rotation_euler
    rot_euler = (rot_euler.x, rot_euler.y, rot_euler.z, rot_euler.order)
    shift_x = cam.data.shift_x
    shift_y = cam.data.shift_y
    lens = cam.data.lens
    lens_unit = cam.data.lens_unit
    cam_type = cam.data.type


    line_str+='camera["location"]='+str(location)+"\n"
    line_str+='camera["rotation"]='+str(rot_euler)+"\n"

    line_str+='camera["shift_x"]='+str(shift_x)+"\n"
    line_str+='camera["shift_y"]='+str(shift_y)+"\n"
    line_str+='camera["type"]="'+cam_type+'"'+"\n"
    line_str+='camera["lens_unit"]="'+lens_unit+'"'+"\n"
    line_str+='camera["lens"]='+str(lens)+"\n"
    with open('c:\\tmp\\pose_1.txt', 'w') as f:
        f.write(line_str)
        f.close()
    bpy.ops.pose.select_all(action='DESELECT')


    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render("c:/tmp/2.jpg")

dump_pose()

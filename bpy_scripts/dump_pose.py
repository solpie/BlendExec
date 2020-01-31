import bpy
import base64
import os

def dump_pose():
    rig = 'rig'
    tmp_path = 'c:/tmp'
    data_filepath = os.path.join(tmp_path,'pose.py')
    thumbnail_filepath = os.path.join(tmp_path,'thumbnail.jpg')

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
    #save camera data
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

    bpy.ops.pose.select_all(action='DESELECT')
    #gen thumbnail
    render = bpy.context.scene.render
    render_w = render.resolution_x
    render_h = render.resolution_y
    render_perc = render.resolution_percentage
    format = render.image_settings.file_format
    thumbnail_w = 1024
    
    if render_w>render_h:
        render.resolution_percentage = thumbnail_w*100/render_w
    else:
        render.resolution_percentage = thumbnail_w*100/render_h
        
    render.image_settings.file_format = "JPEG"
    bpy.ops.render.render()
    bpy.data.images['Render Result'].save_render(thumbnail_filepath)
    render.resolution_percentage = render_perc
    render.image_settings.file_format = format
    

    with open(thumbnail_filepath, 'rb') as f:
        image_data = f.read()
        base64_data = base64.b64encode(image_data).decode('utf-8')  # base64编码
        #print(base64_data)
        f.close()
    line_str+='thumbnail="'+'data:image/jpg;base64,'+str(base64_data)+'"\n'
        # with open(img_path+'.txt','w') as f2:
        #     f2.write('data:image/jpg;base64,'+str(base64_data))
        #     f2.close()
    #write data
    with open(data_filepath, 'w') as f:
        f.write(line_str)
        f.close()
dump_pose()

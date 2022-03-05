#[as_exec]
import bpy


def merge_new():
    global info
    info = ''

    def oops(self, context):
        global info
        self.layout.label(text=info)

    def check_uvmap():
        # 检查uvmap是否唯一且名字为默认UVMap
        global info
        for obj in bpy.context.selected_objects:
            if obj.type == "MESH":
                if len(obj.data.uv_layers) > 1:
                    info = obj.name + ' UVMap 不唯一'
                    return
                if len(obj.data.uv_layers) < 1:
                    info = obj.name + ' 没有UVMap'
                    return
                uvmap_name = obj.data.uv_layers[0].name
                if uvmap_name != 'UVMap':
                    info = obj.name + " UVMap名字为" + uvmap_name
                    obj.data.uv_layers[0].name = 'UVMap'
                    return
    check_uvmap()
    if info != '':
        bpy.context.window_manager.popup_menu(
            oops, title="Error", icon='ERROR')
        return
    # merge new
    merge_obj = None
    hide_arr = []
    dupli_arr = []

    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            hide_arr.append(obj)
        else:
            obj.select_set(False)

    
    bpy.ops.object.select_all(action="DESELECT")
    for obj in hide_arr:
        if obj.type == "MESH":
            obj.select_set(1)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False})
            dupli_arr.append(bpy.context.active_object)
            # act_obj1.select_set(False)
            for m in obj.modifiers:
                if m.type in ["SUBDIVISION", "ARRAY", "MIRROR", "SOLIDIFY", "BEVEL", "CURVE"]:
                    bpy.ops.object.modifier_apply(modifier=m.name)
            bpy.ops.object.select_all(action="DESELECT")
            
    for obj in dupli_arr:
        obj.select_set(1)
        bpy.context.view_layer.objects.active = obj

    bpy.ops.object.join()
    # remove double
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.0005)
    bpy.ops.object.mode_set(mode='OBJECT')
    # hide part
    for obj in hide_arr:
        obj.hide_set(1)

    merge_obj = bpy.context.active_object
    merge_obj.name = "*"+merge_obj.name
    # todo move to new collection
    return
    # duplicate mesh
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked": False})
    act_obj = bpy.context.selected_objects[0]
    for obj in bpy.context.selected_objects:
        if obj.type == "MESH":
            dupli_arr.append(obj)
        # else:
    # return
    bpy.ops.object.select_all(action="DESELECT")
    # apply mirror part
    for obj in dupli_arr:
        if obj.type == "MESH":
            obj.select_set(1)
            bpy.context.view_layer.objects.active = obj
            for m in obj.modifiers:
                if m.type in ["SUBDIVISION", "ARRAY", "MIRROR", "SOLIDIFY", "BEVEL", "CURVE"]:
                    bpy.ops.object.modifier_apply(modifier=m.name)
            obj.select_set(0)

    bpy.context.view_layer.objects.active = act_obj
    bpy.ops.object.join()
    # remove double
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=0.001)
    bpy.ops.object.mode_set(mode='OBJECT')
    # hide part
    for obj in hide_arr:
        bpy.data.objects[obj].hide_set(1)

    merge_obj = bpy.context.active_object
    merge_obj.name = "*"+merge_obj.name


merge_new()

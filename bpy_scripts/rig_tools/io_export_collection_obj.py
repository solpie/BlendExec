#[as_exec]
import bpy


def merge_new():
    global info
    info = ''

    def oops(self, context):
        global info
        self.layout.label(text=info)

    def export_obj():
        base_path = 'F:/tmp/'
        collection_obj = bpy.context.collection
        # for obj in collection_obj.all_objects:
        #     obj.select_set(True)
        bpy.ops.export_scene.obj(
            filepath=base_path+collection_obj.name+'.obj', use_selection=True)
        pass
    def check_uvmap():
        # 检查uvmap是否唯一且名字为默认UVMap
        global info
        collection_obj = bpy.context.collection
        for obj in collection_obj.all_objects:
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
    hide_arr = []
    dupli_arr = []

    for obj in bpy.context.collection.all_objects:
        if obj.hide_viewport:
            continue
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
            if bpy.context.active_object:
                dupli_arr.append(bpy.context.active_object)
            # act_obj1.select_set(False)
            for m in obj.modifiers:
                if m.type in ["SUBDIVISION", "ARRAY", "MIRROR", "SOLIDIFY", "BEVEL", "CURVE"]:
                    bpy.ops.object.modifier_apply(modifier=m.name)
            bpy.ops.object.select_all(action="DESELECT")
            
    for obj in dupli_arr:
        if obj.hide_viewport:
            continue
        obj.select_set(1)
        bpy.context.view_layer.objects.active = obj

    act_obj = bpy.context.active_object
    act_obj.name = "*"+act_obj.name
    export_obj()
    bpy.ops.object.delete(use_global=False)

merge_new()

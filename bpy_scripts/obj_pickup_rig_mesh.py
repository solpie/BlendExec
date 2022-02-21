#[as_exec]
# 选中rig pick binded的obj
import bpy
 
def main():
    rig_name = ''
    # new_rig = bpy.data.objects['rig_face']  
    
    obj = bpy.context.selected_objects[0]
    if obj.type == "ARMATURE":
        rig_name = obj.name
    # set active object
    bpy.context.view_layer.objects.active = None
    bpy.ops.object.select_all(action='DESELECT')
    if rig_name == "":
        return
    for obj in bpy.data.objects:
        if obj.type == "MESH":
            for m in obj.modifiers:
                if m.type == "ARMATURE" and m.object.name == rig_name:
                    try:
                        # m.object = new_rig
                        obj.select_set(True)
                        bpy.context.view_layer.objects.active = obj
                    except Exception as e:
                        pass
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')              
main()

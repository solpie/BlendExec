#[as_exec]
# 上面这一行不要留空格在 #[ 中间
import bpy
from bpy.types import Operator


def main():
    # register
    _register_classes = []

    def register_class(cls):
        '''Decorator'''
        _register_classes.append(cls)
        return cls

    def register_all():
        for item in _register_classes:
            bpy.utils.register_class(item)

    # FLOATING PANEL
    @register_class
    class VIEW3D_PT_FloatingPanel(Operator):
        bl_idname = "floating.rig"
        bl_label = "Rig FloatingPanel"

        def draw(self, context):
            layout = self.layout
            box = layout.column(align=True)
            box.label(text="CAMERAS LISTER", icon="OUTLINER_OB_CAMERA")
            box.separator()
            # ui button
            box.operator("floating.pick_rig_mesh",
                         text="pick_rig_mesh", icon="TRIA_RIGHT")
            box.operator("floating.obj_delete_cs_shape",
                         text="[OBJ] delete cs shape")
            box.operator("floating.obj_uncheck_auto_normal", text="unckeck_auto_normal")
        def invoke(self, context, event):
            wm = context.window_manager
            return wm.invoke_popup(self)

        def execute(self, context):
            # self.report({'INFO'}, self.my_enum)
            return {'FINISHED'}

    def start():
        register_all()
        # 弹框
        bpy.ops.floating.rig('INVOKE_DEFAULT')
        pass

    # module start
    # 选中rig pick binded的obj
    def pick_rig_mesh():
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
        pass

    @register_class
    class PickRigMesh(Operator):
        bl_idname = 'floating.pick_rig_mesh'
        bl_label = 'pick_rig_mesh'
        bl_description = "pick_rig_mesh"
        bl_options = {'UNDO'}

        def execute(self, context):
            pick_rig_mesh()
            return{'FINISHED'}
    # module end

    # module start 删除cs shape obj
    @register_class
    class ObjDeleteCsShape(Operator):
        bl_idname = 'floating.obj_delete_cs_shape'
        bl_label = 'obj_delete_cs_shape'
        bl_description = "删除 cs shape obj"

        bl_options = {'UNDO'}

        def execute(self, context):
            bpy.ops.object.select_pattern(pattern="cs_*")
            bpy.ops.object.delete(use_global=False)
            return{'FINISHED'}
    # module end
    @register_class
    class ObjUncheckAutoNormal(Operator):
        bl_idname = 'floating.obj_uncheck_auto_normal'
        bl_label = 'obj_uncheck_auto_normal'
        bl_description = "obj_uncheck_auto_normal"

        bl_options = {'UNDO'}

        def execute(self, context):
            for obj in bpy.context.selected_objects:
                obj.data.use_auto_smooth = False
            return{'FINISHED'}

    # start 弹框
    start()
    pass


main()

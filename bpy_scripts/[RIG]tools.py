#[as_exec]
# 上面这一行不要留空格在 #[ 中间
import bpy
from bpy.types import Operator


def main():
    # bpy path
    bpy_path = 'F:\\projects\\BlendExec\\bpy_scripts\\'
    def run_bpy(filename):
        bpypath = bpy_path+filename
        with open(bpypath, 'r+') as f:
            bpy_text = f.read()
            print('BlenCall')
            if '#[as_module]' in bpy_text:
                print('as_module')
                if len(bpy_text):
                    if 'exec' not in bpy.data.texts:
                        bpy.data.texts.new('exec')
                    bpy.data.texts['exec'].from_string(bpy_text)
                    bpy.data.texts['exec'].as_module()
                    bpy.data.texts['exec'].from_string('')
                else:
                    print('no bpy')
            else:
                print('exec compile')
                exec(compile(bpy_text, '<string>', 'exec'))
                pass
            f.close()
        pass
    # register
    _register_classes = []

    def register_class(cls):
        '''Decorator'''
        _register_classes.append(cls)
        return cls

    def register_all():
        for item in _register_classes:
            bpy.utils.register_class(item)
        add_keymap()

    def add_keymap():
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Object Mode')
        kmi = km.keymap_items.new('floating.rig', 'V', 'PRESS', alt=False)
        kmi.active = True
        pass

    # FLOATING PANEL
    @register_class
    class VIEW3D_PT_FloatingPanel(Operator):
        bl_idname = "floating.rig"
        bl_label = "Rig FloatingPanel"

        def draw(self, context):
            layout = self.layout
            split = layout.split(factor=0.5)
            box = split.column()
            box2 = split.column()
            box.label(text="[RIG] tools", icon="OUTLINER_OB_CAMERA")
            box.separator()
            # ui button
            box.operator("floating.make_override_library",
                         text="make_override_library")

            box.operator("floating.action_stash",
                         text="action_stash")

            box.operator("floating.pick_rig_mesh",
                         text="pick_rig_mesh", icon="TRIA_RIGHT")

            box.operator("floating.obj_delete_cs_shape",
                         text="[OBJ] delete cs shape")

            box.operator("floating.obj_set_rig",
                         text="[OBJ] obj_set_rig")

            box.operator("floating.obj_uncheck_auto_normal",
                         text="unckeck_auto_normal")

            box.operator('bpylist.run',
            text="Re224_doll_rig", 
            icon='RADIOBUT_ON'
            ).filename = bpy_path+'rig_tools\\Re224_doll_rig.py'

            box.operator('bpylist.run',
            text="Re224_doll_delete", 
            icon='RADIOBUT_ON'
            ).filename = bpy_path+'rig_tools\\Re224_doll_delete.py'
# Re224_doll_rig.py
            box2.label(text="[MD]")
            # box2.operator("floating.export_abc")
            op = box2.operator('bpylist.run', text="export_pose_abc.py",
                               icon='RADIOBUT_ON')
            op.filename = bpy_path+'rig_tools\\export_pose_abc.py'

            op = box2.operator('bpylist.run', text="merge_new.py",
                               icon='RADIOBUT_ON')

            op.filename = bpy_path+'merge_new.py'

            box2.operator('bpylist.run',
            text="export_collection_obj", 
            icon='RADIOBUT_ON'
            ).filename = bpy_path+'rig_tools\\io_export_collection_obj.py'

            box2.operator('bpylist.run',
            text="import_cloth_out", 
            icon='RADIOBUT_ON'
            ).filename = bpy_path+'rig_tools\\io_import_cloth_out.py'

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

    # 设置已rig的选中mesh的rig
    @register_class
    class ObjSetRig(Operator):
        bl_idname = 'floating.obj_set_rig'
        bl_label = 'obj_set_rig'
        bl_description = "obj_set_rig"

        bl_options = {'UNDO'}

        def execute(self, context):
            rig_obj = bpy.context.active_object
            for obj in bpy.context.selected_objects:
                if obj.type == "MESH":
                    for modify in obj.modifiers:
                        if modify.type == "ARMATURE":
                            modify.object = rig_obj
                            pass
            return{'FINISHED'}
            # bpy.ops.object.make_override_library()

    # 设置已rig的选中mesh的rig
    @register_class
    class ObjMakeOverrideLibrary(Operator):
        bl_idname = 'floating.make_override_library'
        bl_label = 'make_override_library'
        bl_description = "make_override_library"

        bl_options = {'UNDO'}

        def execute(self, context):
            bpy.ops.object.make_override_library()
            return{'FINISHED'}

    # bpy.ops.action.stash
    @register_class
    class RigActionStash(Operator):
        bl_idname = 'floating.action_stash'
        bl_label = 'action_stash'
        bl_description = "action_stash"

        bl_options = {'UNDO'}

        def execute(self, context):
            bpy.ops.action.stash()
            return{'FINISHED'}

    # start 弹框
    start()
    pass


main()

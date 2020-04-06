
bl_info = {
    "name":        "BpyList",
    "description": "bpylist",
    "author":      "solpie",
    "version":     (0, 0, 2),
    "blender":     (2, 80, 0),
    "location":    "View 3D > Header",
    # "wiki_url":    "http://docs.retopoflow.com",
    "category":    "3D View"
}
import bpy
from bpy.types import Menu, Operator, Panel,UIList
from bpy.props import StringProperty, IntProperty, BoolProperty
import os

class BpyList_Prefs(bpy.types.AddonPreferences):
    bl_idname = __package__
    bpypath = StringProperty(
        name="tmp path",
        default='F:\\projects\\BlendExec\\bpy_scripts',
        description="tmp bpy.py write path",
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="set bpy dir")
        layout.prop(self, "bpypath")
        # layout.label(text="set port")
        # layout.prop(self, "port")

class BpyList_Refresh(Operator):
    bl_idname = 'bpylist.refresh'
    bl_label = 'open bpylist dir'
    bl_description = 'refresh bpylist dir add to list'

    def execute(self, context):
        addon_prefs = context.preferences.addons[__package__].preferences
        tmp_path = addon_prefs.bpypath
        os.system('explorer ' + tmp_path)
        unregister()
        register()
        return {'PASS_THROUGH'}

class BpyList_Run(Operator):
    bl_idname = 'bpylist.run'
    bl_label = 'run'
    bl_description = 'run bpyscript'
    filename = bpy.props.StringProperty(default='')
    def execute(self, context):
        print(self.filename)
        bpypath = self.filename
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
        return {'FINISHED'}

class BL_UL_list(UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        layout.label(text=item.name,icon='WORLD_DATA')
        # if item.name == context.scene.world.name:
        #     layout.label(text='',icon='CHECKBOX_HLT')
        # layout.operator('bp_world.delete_world',icon='X',text="",emboss=False).world_name = item.name

class VIEW3D_PT_BpyList(Panel):
    """BpyList Blender Menu"""
    bl_label = "BpyList"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'HEADER'

    @staticmethod
    def is_editing_target(context):
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object
        gp_edit = obj and obj.mode in {'EDIT_GPENCIL', 'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL'}
        return not gp_edit and edit_object and mode_string == 'EDIT_MESH'

    def draw(self, context):
        layout = self.layout
        layout.label(text='BpyList')
        addon_prefs = context.preferences.addons[__package__].preferences
        location = addon_prefs.bpypath
        # r=>root, d=>directories, f=>files
        i = 0
        box = layout.box()
        for r, d, f in os.walk(location):
            for item in f:
                if '.py' in item:
                    filename_1 = os.path.join(r, item)
                    with open(filename_1, 'r+') as f:
                        line_1 = f.readline()
                        f.close()
                        if '#[as_exec]' not in line_1 and '#[as_module]' not in line_1:
                            continue
                    i += 1
                    # files_in_dir.append({"name":item,"path":os.path.join(r, item),"idx":i})
                    row = box.row()
                    op = row.operator('bpylist.run',text="",icon='RADIOBUT_ON')
                    op.filename = os.path.join(r, item)
                    row.label(text=item)
                    # layout.label(text="",icon=sel_icon)
        # layout.template_list("BP_UL_worlds", "", bpy.data, "worlds", scene.bp_props, "selected_world_index", rows=4)
        # layout.template_list("BL_UL_list", "", files_in_dir,'name',rows=4)

        layout.separator()
        layout.label(text='BpyList Updater')
        col = layout.column()
        col.operator('bpylist.refresh')

    #############################################################################
    # the following two methods add/remove RF to/from the main 3D View menu
    # NOTE: this is a total hack: hijacked the draw function!
    @staticmethod
    def menu_add():
        # for more icon options, see:
        #     https://docs.blender.org/api/current/bpy.types.UILayout.html#bpy.types.UILayout.operator
        VIEW3D_PT_BpyList.menu_remove()
        VIEW3D_PT_BpyList._menu_original = bpy.types.VIEW3D_MT_editor_menus.draw_collapsible
        def hijacked(context, layout):
            obj = context.active_object
            mode_string = context.mode
            edit_object = context.edit_object
            gp_edit = obj and obj.mode in {'EDIT_GPENCIL', 'PAINT_GPENCIL', 'SCULPT_GPENCIL', 'WEIGHT_GPENCIL'}

            VIEW3D_PT_BpyList._menu_original(context, layout)

            row = layout.row(align=True)
            row.popover(panel="VIEW3D_PT_BpyList", text="BpyList")
            row.operator('bpylist.refresh', text="", icon='QUESTION')
        bpy.types.VIEW3D_MT_editor_menus.draw_collapsible = hijacked
    @staticmethod
    def menu_remove():
        if not hasattr(VIEW3D_PT_BpyList, '_menu_original'): return
        bpy.types.VIEW3D_MT_editor_menus.draw_collapsible = VIEW3D_PT_BpyList._menu_original
        del VIEW3D_PT_BpyList._menu_original

# registration
classes = [
    VIEW3D_PT_BpyList,
    BpyList_Prefs,
    BpyList_Refresh,
    BL_UL_list,
    BpyList_Run,
] 

def register():
    for cls in classes: bpy.utils.register_class(cls)
    VIEW3D_PT_BpyList.menu_add()

def unregister():
    VIEW3D_PT_BpyList.menu_remove()
    for cls in reversed(classes): bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()

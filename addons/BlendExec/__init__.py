# -*- coding: utf-8 -*-
__author__ = 'SolPie'
import urllib.request
import urllib3
from bpy.props import StringProperty, IntProperty, BoolProperty
import bpy
import os
bl_info = {
    "name": "BlendExec",
    "author": "SolPie",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "c:/tmp",
    "description": "Blender Float call from external app",
    "warning": "",
    "category": "Misc"}


# Addon prefs

class BlenFloatPrefs(bpy.types.AddonPreferences):
    bl_idname = __package__
    bpypath = StringProperty(
        name="tmp path",
        default='c:/tmp/',
        description="tmp bpy.py write path",
    )
    port = StringProperty(
        name="server port",
        default='8066',
        description="localhost server port",
    )

    def draw(self, context):
        layout = self.layout
        layout.label(text="set tmp dir")
        layout.prop(self, "bpypath")
        layout.label(text="set port")
        layout.prop(self, "port")
    # self.checkEnable(context)
####################################


http = urllib3.PoolManager()


class BlendCallout(bpy.types.Operator):
    bl_idname = "blendexec.callout"
    bl_label = "blendexec callout"

    def execute(self, context):
        addon_prefs = context.preferences.addons[__package__].preferences
        # port = addon_prefs.port
        # r = http.request('GET', "http://localhost:"+port+"/callout")
        # print(r.data)
        tmp_path = addon_prefs.bpypath
        with open(os.path.join(tmp_path, 'callout.x'), 'w') as f:
            line = []
            mode = bpy.context.mode
            line.append('mode:'+mode+'\n')
            line.append('eof')
            f.writelines(line)
            f.close()
        return {'PASS_THROUGH'}


class BlenCall(bpy.types.Operator):
    bl_idname = "blenfloat.call"
    bl_label = "run.BlenCall"

    def execute(self, context):
        # context.preferences.addons[__package__].preferences.sidebarPanelSize
        user_preferences = context.preferences
        addon_prefs = user_preferences.addons[__package__].preferences
        bpypath = addon_prefs.bpypath
        try:
            with open(bpypath + 'bpy.py', 'r+') as f:
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
                f.seek(0)
                f.write('')
                f.truncate()
                f.close()
                pass
        except Exception as e:
            print('stop BlenCall', e)
        return {'PASS_THROUGH'}


# store keymaps here to access after registration
addon_keymaps = []

###########


def register():
    bpy.utils.register_class(BlenFloatPrefs)
    bpy.utils.register_class(BlenCall)
    bpy.utils.register_class(BlendCallout)
    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name="Window", space_type="EMPTY")
    # key
    kmi = km.keymap_items.new(BlenCall.bl_idname, 'F5', 'PRESS')
    addon_keymaps.append((km, kmi))

    kmi = km.keymap_items.new(BlendCallout.bl_idname, 'ACCENT_GRAVE', 'PRESS')
    # kmi = km.keymap_items.new(BlendCallout.bl_idname, 'ACCENT_GRAVE', 'PRESS', shift=True)
    addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_class(BlenFloatPrefs)
    bpy.utils.unregister_class(BlenCall)
    bpy.utils.unregister_class(BlendCallout)
    # handle the keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

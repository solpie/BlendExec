# [as_module]
import bpy


_register_classes = []
_register_functions = []

_unregister_functions = []


def register_class(cls):
    '''Decorator'''
    _register_classes.append(cls)
    return cls


def register_function(func, ):
    _register_functions.append(func)
    return func


def unregister_function(func):
    _unregister_functions.append(func)
    return func

# main


@register_class
class MSETBakerExport(bpy.types.Operator):
    bl_idname = "msetbaker.export"
    bl_label = "MSETBaker export"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        settings = context.scene.MDToolSetting
        base_path = settings.out_dir
        bpy.ops.object.select_all(action='DESELECT')
        # lo_me = context.scene.MDToolSetting.low_mesh
        # lo_me.select_set(True)
        # name1 = lo_me.name
        # lo_me.name = 'bake_low'
        # bpy.ops.export_scene.fbx(
        #     filepath=base_path+"bake_low.fbx", use_selection=True)
        # lo_me.select_set(False)
        # lo_me.name = name1

        collection_abc = settings.collection_abc
        for obj in collection_abc.all_objects:
            obj.select_set(True)
        bpy.ops.export_scene.fbx(
            filepath=base_path+"pose.abc", use_selection=True)
        return {"FINISHED"}

@register_class
class CharToolMuteRig(bpy.types.Operator):
    bl_idname = "chartool.muterig"
    bl_label = "mute mute_rig"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        settings = context.scene.MDToolSetting
        bpy.ops.object.select_all(action='DESELECT')

        collection = settings.collection_mute_rig
        for obj in collection.all_objects:
            obj.select_set(True)
            for m in obj.modifiers:
                if m.type=="ARMATURE":
                    m.show_viewport = False
                    
        return {"FINISHED"}

class BasePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MDTool"


@register_class
class MDToolSettings(bpy.types.PropertyGroup):
    collection_abc: bpy.props.PointerProperty(type=bpy.types.Collection, name="Abc",
                                         description="The mesh that's exporting to pose.abc")

    collection_mute_rig: bpy.props.PointerProperty(type=bpy.types.Collection, name="Mute Rig",
                                         description="unable rig")
 
    low_mesh: bpy.props.PointerProperty(type=bpy.types.Object, name="Low Mesh",
                                        description="The mesh that's exporting to bake_low.fbx")

    out_dir: bpy.props.StringProperty(name="working dir:", default="f:/tmp/",
                                      description="working dir")


@register_class
class MDToolPanel(BasePanel):
    bl_idname = "MDTool_PT_msetbaker_panel"
    bl_label = "MDTool"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        settings = context.scene.MDToolSetting
        col.prop(settings, "collection_abc")
        col.separator()
        col.prop(settings, "collection_mute_rig")
        col.operator("chartool.muterig", text="mute rig")
        col.separator()
        col.prop(settings, "out_dir")
        col.separator()
        row = col.row(align=True)
        row.operator("msetbaker.export", text="export")


@register_function
def register():
    bpy.types.Scene.MDToolSetting = bpy.props.PointerProperty(
        type=MDToolSettings)


@unregister_function
def unregister():
    del bpy.types.Scene.MDToolSetting


##################
def register_all():
    for item in _register_classes:
        bpy.utils.register_class(item)

    for item in _register_functions:
        item()


unregister()

register_all()

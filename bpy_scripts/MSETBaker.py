#[as_module]
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

################## main


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
        settings = context.scene.MSETBaker_settings
        base_path = settings.out_dir
        bpy.ops.object.select_all(action='DESELECT')
        lo_me = context.scene.MSETBaker_settings.low_mesh
        lo_me.select_set(True)
        name1 = lo_me.name
        lo_me.name = 'bake_low'
        bpy.ops.export_scene.fbx(filepath=base_path+"bake_low.fbx",use_selection=True)
        lo_me.select_set(False)
        lo_me.name = name1
        
        hi_me = context.scene.MSETBaker_settings.high_mesh
        hi_me.select_set(True)
        name2 = hi_me.name
        hi_me.name = "bake_high"
        bpy.ops.export_scene.fbx(filepath=base_path+"bake_high.fbx",use_selection=True)
        hi_me.name = name2
        return {"FINISHED"}
        
    
class BasePanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MSETBaker"
    
@register_class
class MSETBakerSettings(bpy.types.PropertyGroup):
    high_mesh: bpy.props.PointerProperty(type=bpy.types.Object, name="High Mesh",
        description="The mesh that's exporting to bake_high.fbx")

    low_mesh: bpy.props.PointerProperty(type=bpy.types.Object, name="Low Mesh",
        description="The mesh that's exporting to bake_low.fbx")
        
    out_dir:bpy.props.StringProperty(name="fbx dir:", default="f:/tmp/",
        description="fbx export dir")
        
@register_class
class SoftWrapPanel(BasePanel):
    bl_idname = "MSETBaker_PT_msetbaker_panel"
    bl_label = "MSETBaker"

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        settings = context.scene.MSETBaker_settings
        col.prop(settings, "high_mesh")
        col.separator()
        col.prop(settings, "low_mesh")
        col.separator()
        col.prop(settings, "out_dir")
        col.separator()
        row = col.row(align=True)
        row.operator("msetbaker.export", text="export")
        
@register_function
def register():
    bpy.types.Scene.MSETBaker_settings = bpy.props.PointerProperty(
        type=MSETBakerSettings)


@unregister_function
def unregister():
    del bpy.types.Scene.MSETBaker_settings


##################
def register_all():
    for item in _register_classes:
        bpy.utils.register_class(item)

    for item in _register_functions:
        item()


register_all()
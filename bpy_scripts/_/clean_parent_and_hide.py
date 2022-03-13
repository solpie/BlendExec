#[as_exec]
import bpy


class CleanParent(bpy.types.Operator):
    bl_idname = "object.clean_parent_hide"
    bl_label = 'clean parent and hide'
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.ops.object.hide_view_set(unselected=False)
        return {'FINISHED'}
    
bpy.utils.register_class(CleanParent)
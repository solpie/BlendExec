#[as_exec]
import bpy

def main():
    bpy.ops.object.duplicate_move()
    # remove vertex group
    obj = bpy.context.view_layer.objects.active
    for vg in obj.vertex_groups:
        obj.vertex_groups.remove(vg)
    bpy.ops.transform.resize(value=(-1, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False),
                             mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    # flip normal
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.editmode_toggle()
main()

import bpy
# bpy.ops.import_scene.obj(filepath="", filter_glob="*.obj;*.mtl", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=True, split_mode='ON', global_clamp_size=0, axis_forward='-Z', axis_up='Y')
# Load a Wavefront OBJ File
def main():
    base_path = 'F:/tmp/'
    bpy.ops.import_scene.obj(
            filepath=base_path+'c.obj')
    for obj in bpy.context.selected_objects:
        obj.data.use_auto_smooth = False
    pass


main()
import bpy
# bpy.ops.wm.alembic_export(filepath="", check_existing=True,
#  filter_blender=False, filter_backup=False,
# filter_image=False, filter_movie=False,
#  filter_python=False, filter_font=False,
# filter_sound=False, filter_text=False,
# filter_archive=False, filter_btx=False,
#  filter_collada=False, filter_alembic=True,
# filter_usd=False, filter_obj=False, filter_volume=False,
# filter_folder=True, filter_blenlib=False,
#  filemode=8, display_type='DEFAULT',
#  sort_method='DEFAULT',
# start=-2147483648, end=-2147483648,
# xsamples=1, gsamples=1, sh_open=0,
# sh_close=1, selected=False, visible_objects_only=False,
#  flatten=False, uvs=True, packuv=True, normals=True,
# vcolors=False, orcos=True, face_sets=False, subdiv_schema=False,
# apply_subdiv=False, curves_as_mesh=False,
# use_instancing=True, global_scale=1,
# triangulate=False, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY', export_hair=True, export_particles=True, export_custom_properties=True, as_background_job=False, evaluation_mode='RENDER', init_scene_frame_range=False)
# Export current scene in an Alembic archive


def main():
    base_path = 'F:/tmp/'
    bpy.ops.object.select_all(action='DESELECT')
    collection_abc = bpy.context.collection
    for obj in collection_abc.all_objects:
        obj.select_set(True)
    bpy.ops.wm.alembic_export(
        start = 0, end =90,
        filepath=base_path+"pose.abc", selected=True, apply_subdiv=True)
    pass


main()

import bpy
def fix_path():
    for img in bpy.data.images:
        print(img.filepath)
        new_path = img.filepath.replace('WRP_FBXExporter\\Exports\\CORRIDOR_','JP_School corridor\\Texture\\')
        new_path = new_path.replace('_MainTex','')
        new_path = new_path.replace('_BumpMap','')
        
        img.filepath = new_path
        print(new_path)
fix_path()
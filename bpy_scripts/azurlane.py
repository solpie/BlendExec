#[as_exec]
import bpy


def gen_tex():
    import os.path
    import re
    regex = re.compile('Texture2D\'(.+)\'')
    re_tex_type = re.compile('Name=(.+)\s')
    base_path = 'H:\\models\\char4\\3yue\\Azur Lane\\'

    def search(arr, str):
        for s in arr:
            if s in str and not 'OL' in str:
                return True

    def find_tex_path(chname, mat):
        # mat = bpy.data.objects[3].material_slots[0].material
        fname = base_path + chname + '\\Material\\'+mat.name+'.props.txt '
        print(fname)
        if os.path.isfile(fname):
            with open(fname) as f:
                txt = f.read()
                f.close()
                r1 = regex.findall(txt)
                r2 = re_tex_type.findall(txt)
                # print(txt)
                if 'TextureBase' in r2[0]:
                    # print(r1)
                    tex_path = base_path + chname + '\\Texture\\' + \
                        r1[0].split('/')[-1].split('.')[-1]+'.tga'
                    if os.path.isfile(tex_path):
                        print(mat.name, tex_path)
                        return tex_path

    def loadTex(chname, mat):
        tex_path = find_tex_path(chname, mat)
        if tex_path:
            links = mat.node_tree.links
            nodes = mat.node_tree.nodes
            principled_bsdf = mat.node_tree.nodes.get('Principled BSDF')
            base_color = nodes.new('ShaderNodeTexImage')
            base_color.location = -300, -300
            base_color.image = bpy.data.images.load(tex_path)
            links.new(principled_bsdf.inputs["Base Color"],
                      base_color.outputs["Color"])
        pass
    for obj in bpy.data.objects:
        if '_Model' in obj.name:
            print(obj.name)
            obj.rotation_mode = 'XYZ'
            obj.rotation_euler.z = -1.5707966089248657
        if 'Armature_0' in obj.name:
            obj.hide_set(1)
    bpy.ops.mesh.separate(type='MATERIAL')
    # hide machine
    for obj in bpy.data.objects:
        if '_Model' in obj.name:
            mat = obj.material_slots[0].material
            mat.name = mat.name.replace('_COLOR_0','')
            chname = obj.name[0:5]
            print(chname)
            loadTex(chname, mat)
            if search(['Face', 'Body', 'Hair','Cloth',"Head"], mat.name):
                # print(obj.name)
                obj.hide_set(0)
            else:
                obj.hide_set(1)
        if 'Armature_0' in obj.name:
            obj.hide_set(1)
    bpy.ops.file.pack_all()


gen_tex()

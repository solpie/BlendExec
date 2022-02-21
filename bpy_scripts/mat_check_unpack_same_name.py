#[as_exec]
import bpy
import os
def main():
    same_imgs = {}
    for img in bpy.data.images:
        a = img.filepath.split('\\')
        a = a[-1].split('/')
        a = a[-1].split('//')
        filename = a[-1]
        print(img.name,filename)
        if filename in same_imgs:
            print("-->exist",img.name,filename)
            bpy.ops.image.unpack(method='WRITE_ORIGINAL', id=img.name)
            dirname = os.path.dirname(bpy.data.filepath)
            fn = os.path.join(dirname,img.filepath[2:])
            # //textures abspath
            dirname = os.path.dirname(fn)
            print("-->rename",filename,new_file_name)
            fn2, file_extension = os.path.splitext(fn)
            new_file_name = os.path.join(dirname,img.name+file_extension)
            os.rename(os.path.join(dirname,filename),new_file_name)
            # reload new file
            img.filepath = new_file_name
            break
        same_imgs[filename] = filename
        #img.reload()
    print("[sus] not exist same image")
    pass

main()

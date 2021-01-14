#[as_exec]
import bpy
def main():
    for obj in bpy.data.objects:
        if obj.type =="CAMERA" and obj.name.find("ref")>-1:
            print(obj.name)
            is_show = obj.data.background_images[0].show_background_image
            obj.data.background_images[0].show_background_image = not is_show
            

main()

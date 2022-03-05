import os
import sys
 
def walk_dir(dir, topdown = True):
    for root, dirs, files in os.walk(dir, topdown):
        for name in files:
            cmd = '"c:\\Program Files\\Blender Foundation\\Blender 3.0\\blender.exe" -b $b -f 1'
            fn = os.path.join(root, name)
            if '.blend' in fn:
                cmd = cmd.replace('$b',fn)
                print(cmd)
                rename_cmd = 'rename c:\\tmp\\0001.png '+name.replace('.blend','.png')
                print(rename_cmd)
                if not os.path.exists('c:\\tmp\\'+name.replace('.blend','.png')):
                    os.system(cmd)
                    os.system(rename_cmd)


 
walk_dir(".")


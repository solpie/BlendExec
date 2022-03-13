from MVPython import  MarvelousDesignerAPI
from MVPython.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
# sys.path.append("F:/projects/BlendExec/bmd/")
#If you want to load your python file, please type "sys.path.append(input path where file is located here)" in console.
#ex) sys.path.append("C:/Users/Young/Downloads/") or sys.path.append("C:\\\\Users\\\\Young\\\\Downloads\\\\")
class BIO():
    mdsa = None

    def test1(self,object):
        object.clear_console() 
        #initialize mdsa module
        object.initialize() 
        # def avatar_file_open(object, open_file_path, obj_type = 0, scale = "mm", fps = 30):
        object.avatar_file_open(open_file_path='F:/tmp/pose.abc',scale ="m",fps=30)
        object.garment_file_open(open_file_path='F:/tmp/sweat.obj')
        object.set_garment_file_path(open_file_path='F:/tmp/sweat.obj')
        mdsa.set_garment_file_path(open_garment_file_path='F:/tmp/sweat.obj')
        pass
 
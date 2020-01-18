from _gui import MainWin
import os
import wx
from exec import ExecInfo
exec_call = ExecInfo()
tmp_path = 'c:\\tmp'
def get_filelist(dir):
    arr = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            arr.append(os.path.join(home, filename))
    return arr


class BlendExec(MainWin):
    def init_ui(self):
        arr = get_filelist('./bpy_scripts')
        for b in arr:
            self.m_listBox_bpy.InsertItems(arr, 0)
        pass

    def on_list_DClick(self, event):
        bpy_filename = event.GetString()
        with open(bpy_filename, 'r') as f:
            bpy = f.read()
            f.close()
            with open(os.path.join(tmp_path, 'bpy.py'),'w') as f2:
                f2.write(bpy)
                f2.close()
        print('on_exec_bpy',event.GetString())

    def run(self, bpy_name):
        shell.SendKeys("{F5}")
        pass

    def on_refresh_hwnd(self, event):
        hwnd_arr = []
        exec_call.refresh_win(hwnd_arr)
        # print(hwnd_arr)
        title_arr = []
        for hwnd, title in hwnd_arr:
            print(hwnd, title)
            title_arr.append(title)
        self.m_choice_hwnd.SetItems(title_arr)


if __name__ == "__main__":
    app = wx.App(False)
    m = BlendExec(None)
    m.Show()
    m.init_ui()
    app.MainLoop()
    pass

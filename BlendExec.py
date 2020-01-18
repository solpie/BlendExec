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
            arr.append((filename, os.path.join(home, filename)))
    return arr


class BlendExec(MainWin):
    bpy_script_map = {}
    hwnd_map = {}
    target_hwnd = None

    def init_ui(self):
        arr = get_filelist('./bpy_scripts')
        name_arr = []
        for name, path in arr:
            self.bpy_script_map[name] = path
            name_arr.append(name)
        self.m_listBox_bpy.InsertItems(name_arr, 0)
        self.on_refresh_hwnd()

    def on_list_DClick(self, event):
        if self.target_hwnd != None:
            bpy_filename = self.bpy_script_map[event.GetString()]
            with open(bpy_filename, 'r') as f:
                bpy = f.read()
                f.close()
                with open(os.path.join(tmp_path, 'bpy.py'), 'w') as f2:
                    f2.write(bpy)
                    f2.close()
                    exec_call.call_blender(self.target_hwnd)
            print('on_exec_bpy', event.GetString())
        else:
            print('no hwnd')

    # def run(self, bpy_name):
    #     shell.SendKeys("{F5}")
    #     pass

    def on_choice_hwnd(self, event):
        title = event.GetString()
        hwnd = self.hwnd_map[title]
        self.target_hwnd = hwnd
        print(title, hwnd)
        pass

    def on_refresh_hwnd(self, event=None):
        hwnd_arr = []
        exec_call.refresh_win(hwnd_arr)
        # print(hwnd_arr)
        title_arr = []
        last_hwnd = None
        for hwnd, title in hwnd_arr:
            print(hwnd, title)
            title_arr.append(title)
            self.hwnd_map[title] = hwnd
            last_hwnd = hwnd
        self.m_choice_hwnd.SetItems(title_arr)
        if len(title_arr) == 1:
            self.m_choice_hwnd.SetSelection(0)
            self.target_hwnd = last_hwnd


if __name__ == "__main__":
    app = wx.App(False)
    m = BlendExec(None)
    m.Show()
    m.init_ui()
    app.MainLoop()
    pass

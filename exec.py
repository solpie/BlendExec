import win32con
import win32gui
import win32api
import win32com.client

# shell = win32com.client.Dispatch("WScript.Shell")
# shell.Run("blender")
# shell.SendKeys("{F5}")
hwnd_map = {}
# set Blender Foreground

def window_enum_handler(hwnd, resultList):
    title = win32gui.GetWindowText(hwnd)
    if "Blender" in title and "[" in title:
        print("find Blender hwnd", hwnd, title)
        # shell.SendKeys("")
        hwnd_map[title] = hwnd
        resultList.append((hwnd, title))
        # win32gui.SetForegroundWindow(hwnd)


def set_win_fg_by_title(title):
    hwnd = hwnd_map[title]
    win32gui.SetForegroundWindow(hwnd)


def setBlenderForeground():
    win32gui.EnumWindows(window_enum_handler, [])


# exec Info
shell = win32com.client.Dispatch("WScript.Shell")


class ExecInfo(object):
    def __init__(self, *args):
        super(ExecInfo, self).__init__(*args)
        self.code = "import bpy;bpy.ops.object.select_all()"
        # self.refresh_win()

    def callBlender(self):
        setBlenderForeground()
        # shell.AppActivate("Blender")
        # win32api.Sleep(50)

        # shell.SendKeys("{F5}")

        # i = 5
        # while i>0:
        #     i -=1
        #     win32api.Sleep(1000)
        #     hwnd = win32gui.GetForegroundWindow()
        #     print(hwnd)
        #     pass
        # shell.SendKeys("+^%b")
    def refresh_win(self, arr):
        win32gui.EnumWindows(window_enum_handler, arr)
        pass

    def push(self, code):
        self.code = code

    def pop(self):
        c = self.code
        self.code = ""
        return c


if __name__ == "__main__":
    pass
    execInfo = ExecInfo()
    execInfo.callBlender()

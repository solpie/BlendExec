import win32con
import win32gui
import win32api
import win32com.client

hwnd_map = {}
find_title = ""

def window_enum_handler(hwnd, resultList):
    title = win32gui.GetWindowText(hwnd)
    if "Blender" in title and "[" in title:
        print("find Blender hwnd", hwnd, title)
        # shell.SendKeys("")
        hwnd_map[title] = hwnd
        resultList.append((hwnd, title))


def window_enum_handler2(hwnd, res_arr):
    title = win32gui.GetWindowText(hwnd)
    if find_title in title:
        res_arr.append((hwnd, title))


def set_win_fg_by_title(title):
    hwnd = hwnd_map[title]
    win32gui.SetForegroundWindow(hwnd)


def setBlenderForeground():
    win32gui.EnumWindows(window_enum_handler, [])


# exec Info
shell = win32com.client.Dispatch("WScript.Shell")


def get_cursor_pos():
    pos = win32api.GetCursorPos()
    return int(pos[0]), int(pos[1])


class ExecInfo(object):
    blender_hwnd =None
    def __init__(self, *args):
        super(ExecInfo, self).__init__(*args)
        self.code = "import bpy;bpy.ops.object.select_all()"
        # self.refresh_win()

    def get_active_hwnd(self):
        return win32gui.GetForegroundWindow()

    def get_win_title(self, hwnd):
        return win32gui.GetWindowText(hwnd)

    def get_cursor_pos(self):
        return get_cursor_pos()

    def call_blender(self, hwnd):
        win32gui.SetForegroundWindow(hwnd)
        shell.SendKeys("{F5}")

    def send_key(self, k):
        shell.SendKeys(k)

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
    def set_win_top_by_hwnd(self, hwnd):
        win32gui.SetForegroundWindow(hwnd)
        
    def set_win_top(self, title):
        arr = []
        find_title = title
        win32gui.EnumWindows(window_enum_handler2, arr)
        for hwnd, title2 in arr:
            if find_title in title2:
                print('set_win_top',title2)
                win32gui.SetForegroundWindow(hwnd)
                return hwnd

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
    execInfo = ExecInfo()
    execInfo.callBlender()

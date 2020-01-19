import time
from exec import ExecInfo
from threading import Thread
from flask import Flask, jsonify, request, url_for
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QEventLoop, QTimer
import os
import sys

win_title = 'BlendExec___#'
app_1 = {"win":None}

class BrowserRender(QWebEngineView):
    def __init__(self, display=True):
        self.app = QApplication([])
        QWebEngineView.__init__(self)
        # self.move(300, 300)
        self.setWindowTitle(win_title)
        self.resize(1080, 640)
        self.page().profile().clearHttpCache()
        self.html = ''

    def open(self, url):
        self.load(QUrl(url))
        self.show()
        self.app.exec_()


def get_filelist(dir):
    arr = []
    for home, dirs, files in os.walk(dir):
        for filename in files:
            arr.append((filename, os.path.join(home, filename)))
    return arr


app = Flask(__name__, static_folder='assets', static_url_path='/')
port = 8066
tmp_path = 'c:/tmp'
exec_info = ExecInfo()

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/test')
def test():
    return 'test'


@app.route('/hwnd')
def get_hwnd():
    hwnd_arr = []
    exec_info.refresh_win(hwnd_arr)
    return jsonify({"hwnd_arr": hwnd_arr})


@app.route('/bpy')
def get_bpy_script():
    arr = get_filelist('./bpy_scripts')
    return jsonify({"bpy_arr": arr})

# @app.route('/config')
# def get_config():
#     return url_for('static', filename='config.json')


@app.route('/sendkey', methods=['POST'])
def send_key():
    data = request.json
    key = data['key']
    exec_info.send_key(key)
    return "OK"


@app.route('/save', methods=['POST'])
def save_file():
    data = request.json
    filename = data['filename']
    filename = os.path.join('./assets/', filename)
    with open(filename, 'w') as f:
        f.write(data['data'])
        f.close()
    return 'OK'


@app.route('/exec', methods=['POST'])
def call_blender():
    data = request.json
    hwnd = exec_info.blender_hwnd
    if hwnd != None:
        bpy_str = data['str']
        if bpy_str:
            bpy = bpy_str
        else:
            bpy_name = data['bpy']
            bpy_filename = bpy_name
            with open(bpy_filename, 'r') as f:
                bpy = f.read()
                f.close()
        with open(os.path.join(tmp_path, 'bpy.py'), 'w') as f2:
            f2.write(bpy)
            f2.close()
            exec_info.call_blender(hwnd)
        return 'ok'
        print('on_exec_bpy', bpy_name)
    else:
        print('no hwnd')
        return 'no hwnd'


def blender_callout(mode):
    print('blender_callout mode', mode)
    x, y = exec_info.get_cursor_pos()
    hwnd = exec_info.get_active_hwnd()
    title = exec_info.get_win_title(hwnd)
    exec_info.blender_hwnd = hwnd
    print(title,x,y)
    try:
        if app_1['win']:
            app_1['win'].activateWindow()
            pass
        else:
            exec_info.set_win_top(win_title)
    except Exception as e:
        blender_callout(mode)
        print(e)
        pass

    print(title, hwnd, x, y)
    return 'ok'


def check_callout():
    path_callout = os.path.join(tmp_path, 'callout.x')
    while True:
        time.sleep(0.05)
        if os.path.isfile(path_callout):
            with open(path_callout, 'r+') as f:
                lines = f.readlines()
                mode = ''
                for line in lines:
                    print(line)
                    if 'eof' in line:
                        print('exist  callout')
                        blender_callout(mode)
                        f.seek(0)
                        f.write('')
                        f.truncate()
                        f.close()
                    elif 'mode' in line:
                        mode = line[5:]
            pass


def start_check_callout():
    t = Thread(target=check_callout)
    t.daemon = True
    t.start()


is_debug = True


def main():
    app_thread = Thread(target=app.run, args=["localhost", port])
    app_thread.daemon = True
    app_thread.start()
    start_check_callout()
    br = BrowserRender()
    url = 'http://localhost:' + str(port) + '/index.html'
    print('index url', url)
    app_1['win'] =br
    br.open(url)
    pass


def dev_gui():
    br = BrowserRender()
    br.open('http://localhost:8067')


def debug_server():
    start_check_callout()
    # app.run("localhost", port, debug=False)
    app.run("localhost", port, debug=True)


if __name__ == '__main__':
    is_dev = False
    for arg in sys.argv:
        if '-gui' in arg:
            is_dev = True
            dev_gui()
        elif '-server' in arg:
            is_dev = True
            debug_server()
    if not is_dev:    
        main()

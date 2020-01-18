from exec import ExecInfo
from threading import Thread
from flask import Flask, jsonify,request
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QEventLoop, QTimer
import os


class BrowserRender(QWebEngineView):
    def __init__(self, display=True):
        self.app = QApplication([])
        QWebEngineView.__init__(self)
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


app = Flask(__name__)
port = 8066
tmp_path = 'c:/tmp'
exec_info = ExecInfo()
@app.route("/")
def hello():
    return "<a href='http://127.0.0.1:5000/test'>AA</a><br />Hello World!"


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


@app.route('/exec',methods=['POST'])
def call_blender():
    data = request.json
    hwnd = data['hwnd']
    bpy_name = data['bpy']
    if hwnd != None:
        bpy_filename =bpy_name
        with open(bpy_filename, 'r') as f:
            bpy = f.read()
            f.close()
            with open(os.path.join(tmp_path, 'bpy.py'), 'w') as f2:
                f2.write(bpy)
                f2.close()
                exec_info.call_blender(hwnd)
        return 'ok'
        print('on_exec_bpy',bpy_name)
    else:
        print('no hwnd')
        return 'no hwnd'


is_debug = True

def main():
    app_thread = Thread(target=app.run, args=["localhost", port])
    app_thread.daemon = True
    app_thread.start()
    br = BrowserRender()
    if is_debug:
        br.open('http://localhost:8080/')
    else:
        br.open('http://localhost:'+str(port)+'/')
        pass


def debug_server():
    app.run("localhost", port, debug=True)


if __name__ == '__main__':
    debug_server()
    # main()
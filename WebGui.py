from threading import Thread
from flask import Flask
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QEventLoop, QTimer


class BrowserRender(QWebEngineView):
    def __init__(self, display=True):
        self.app = QApplication([])
        QWebEngineView.__init__(self)
        self.html = ''

    def open(self, url):
        self.load(QUrl(url))
        self.show()
        self.app.exec_()


app = Flask(__name__)
port = 8066


@app.route("/")
def hello():
    return "<a href='http://127.0.0.1:5000/test'>AA</a><br />Hello World!"


@app.route('/test')
def test():
    return 'test'


def main():
    app_thread = Thread(target=app.run, args=["localhost", port])
    app_thread.daemon = True
    app_thread.start()
    br = BrowserRender()
    br.open('http://localhost:'+str(port)+'/')


if __name__ == '__main__':
    main()

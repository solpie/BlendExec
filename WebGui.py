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
 
 
def main():
    br = BrowserRender()
    br.open('http://baidu.com')
 
 
if __name__ == '__main__':
    main()
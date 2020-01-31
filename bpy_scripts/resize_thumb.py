import io
import base64
import sys
from PIL import Image


def changeimgtobase64(img_url, max_width=120, max_height=80):
    """
    :param img_url: 图片地址
    :param max_width: 长边
    :param max_height: 短边
    :return:
    """
    rotate = False  # 是否短边为宽
    result = ''
    try:
        img = Image.open(img_url)
        width, height = img.size
        if width < height:
            # 使图片长边为宽
            rotate = True
            width, height = height, width
        if width > max_width or height > max_height:
            width = min([width, max_width])
            height = min([height, max_height])
            if rotate:
                # Image.ANTIALIAS参数平滑图片，使图片更清晰
                img = img.resize((height, width), Image.ANTIALIAS)
            else:
                img = img.resize((width, height), Image.ANTIALIAS)

        img_buffer = io.BytesIO()  # 生成buffer
        img.save(img_buffer, format='PNG')
        byte_data = img_buffer.getvalue()
        base64_data = base64.b64encode(byte_data)
        s = base64_data.decode()
        result = 'data:image/jpg;base64,%s' % s
        print(result)
    except Exception.e:
        pass
        # exc_type, exc_obj, exc_tb = sys.exc_info()
        # alertmsg = u'%s %s Exception. %s --- %s' % (
        #     exc_tb.tb_lineno, sys._getframe().f_code.co_name, code, e)
        # log.error(alertmsg)
    return result

if __name__ == "__main__":
    
    changeimgtobase64("c:/tmp/2.jpg")
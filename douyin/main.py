# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import uiautomator2 as u2
import cv2
import matplotlib
import numpy
# 语音播报模块
import pyttsx3
import pydub
from pydub import AudioSegment
import win32
def show_Image():
    i = 1
    while i:
        time.sleep(3)
        im = d(resourceId="com.ss.android.ugc.aweme:id/brh").screenshot()
        # im.save('heart3.jpg')
        heart_name = "{}.jpg".format(time.time())
        im.save(heart_name)
        img_test = cv2.imread(heart_name)
        # img_gray = cv2.imread("heart.jpg")
        print(img_test[75, 75])  # 读取图像里坐标为横轴为100，纵轴为100那个点的像素值
        # print(img_gray[75, 75])
        test = img_test[75, 75]
        # gray = img_gray[75, 75]
        # if (test == gray).all():
        if(test >= 230).all():
            print("赞")
            d(resourceId="com.ss.android.ugc.aweme:id/brh").click()
            # 模块初始化
            engine = pyttsx3.init()

            # 语音播报内容
            content = "肖战抖音更新了"

            # 输出文件格式
            outFile= 'out.aiff'

            print('准备开始语音播报...')

            # 设置要播报的Unicode字符串
            engine.say(content)

            # 等待语音播报完毕
            engine.runAndWait()

            # # 将文字输出为 aiff 格式的文件
            # engine.save_to_file(content, outFile) 11341   ][';
            
            #
            # # 将文件转换为mp3格式
            # AudioSegment.from_file(outFile).export("Python.mp3", format="mp3")

            d.swipe_ext("up")
        else:
            break

def add_Fivorite():

    d.screen_on()

    # d.unlock('151404)
    d.swipe_ext("up")

    d.click(0.194, 0.615)
    d.settings['wait_timeout'] = 1.0
    d.click(0.472, 0.717)
    d.settings['wait_timeout'] = 1.0
    d.click(0.242, 0.614)
    d.settings['wait_timeout'] = 1.0
    d.click(0.194, 0.72)
    d.settings['wait_timeout'] = 1.0
    d.click(0.485, 0.917)
    d.settings['wait_timeout'] = 1.0
    d.click(0.194, 0.72)
    d.app_start("com.ss.android.ugc.aweme", ".splash.SplashActivity")
    print(d.app_current())

    time.sleep(5)

    # d(text="我").wait(timeout=3.0)
    #d(text="关注").exists(timeout=3)
    d.click(0.888, 0.963)
    # d(text="我").click()
    d(text="关注").click()
    d(resourceId="com.ss.android.ugc.aweme:id/fl_intput_hint_container").click()
    d.send_keys("肖战")
    d(text="有趣的灵魂.").click()
    time.sleep(3)
    d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/cgk"]/android.widget.FrameLayout[1]').click()

if __name__ == '__main__':
    d = u2.connect('STSDU19C18019852')
    print(d.info)
    add_Fivorite()
    show_Image()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/




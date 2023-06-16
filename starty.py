import pyautogui
import time
from PIL import ImageGrab, Image
import cv2
import numpy as np
import os
import glob

color =(255, 158, 24)

def get_position():
# 获取鼠标当前位置
    current_x, current_y = pyautogui.position()

    # 获取当前鼠标所在位置的屏幕颜色
    current_color = pyautogui.screenshot().getpixel((current_x, current_y))
    coordinate = (current_x, current_y)
    print("当前鼠标位置：({0}, {1})".format(current_x, current_y))
    print("当前鼠标位置的颜色值：{0}".format(current_color))
    return coordinate
def screenshoot(a,b,c,d,e):

    bbox = (a,b,c,d)
    img = ImageGrab.grab(bbox)

    # 保存截图到文件
    img.save("abs/"+e+'.png')


def get_position_and_shoot(filename):
    coordinate1=get_position()
    for i in range (5):
        time.sleep(1)
        print("还剩%d秒"%(5-i))
    coordinate2=get_position()
    screenshoot(coordinate1[0],coordinate1[1],coordinate2[0],coordinate2[1],filename)
    print("保存成功！")     

def multiple_play():
    while(1):
        status = 0
        while(status==0):
            status = check("defeat_pic")
            time.sleep(5)
            status = check("recruit") 
            time.sleep(5)
            if(status==0):
                print("还在战斗中")
                time.sleep(20)

        check("recruit_start")
        time.sleep(60)

def ring_bell():
    file_names = read_file_name()
    
    print(file_names)
    while(1):
        for i in range(0,len(file_names)):
            status = check("ringbell/"+file_names[i])   
        time.sleep(1)          
                


def read_file_name():
    # 指定要读取的文件夹路径
    folder_path = "C:/Users/99685/Desktop/script/ringbell"

    # 使用 glob 模块匹配指定路径下所有文件的路径
    files = glob.glob(os.path.join(folder_path, "*"))

    # 创建一个空数组用于保存文件名
    file_names = []

    # 遍历所有文件路径，获取每个文件的文件名，并添加到数组中
    for file_path in files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_names.append(file_name)

    # 返回数组
    return file_names

def story_read():
    while(1):
            #new_story
        move_and_click(973, 405)

        move_and_click(925, 615)
        current_x, current_y = pyautogui.position()    
        current_color = pyautogui.screenshot().getpixel((current_x, current_y))
        if(current_color==color):
            #story 1
            move_and_click(1187, 72)
            check()
            move_and_click(988, 673)
            #story 2   
        move_and_click(935, 502)
        move_and_click(1187, 72)
        check()
        move_and_click(988, 673)
            #story 3   
        move_and_click(946, 398)
        move_and_click(1187, 72)
        check() 
        move_and_click(988, 673)
            #back
        move_and_click(726, 983)

def move_and_click(click_x, click_y):
  pyautogui.moveTo(click_x, click_y)
  pyautogui.click()




def check(filename):
        # 读取大图片和小图片
    bbox = (0, 0,1920, 1080)
    img = ImageGrab.grab(bbox)

    # 保存截图到文件
    img.save('screenshot.png')
    img_large = cv2.imread('screenshot.png')
    img_small = cv2.imread(filename+'.png')

    # 获取小图片的尺寸
    h, w = img_small.shape[:2]

    # 匹配模板
    result = cv2.matchTemplate(img_large, img_small, cv2.TM_CCOEFF_NORMED)

    # 设置匹配阈值，这里设为0.8
    threshold = 0.8

    # 找到匹配的位置

    y, x = np.where(result >= threshold)

    if(x.size>0 and y.size>0):
        move_and_click(x[0]+w/2,y[0]+h/2)
        status = 1
        return status
    else:
        
        status = 0
        return status
    # # 标记匹配位置
    # for (x, y) in zip(x, y):
    #     cv2.rectangle(img_large, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # # 显示匹配结果
    # cv2.imshow('Result', img_large)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def abs():
    while(1):
        while(1):
            time.sleep(10)
            if(check("abs/"+"give up")):
                print("点放弃")
                break
        while(1):
            time.sleep(1)
            if(check("abs/"+"ok")):
                print("点ok")
                break
        while(1):
            time.sleep(1)
            if(check("abs/"+"choose")):
                print("点选关")
                break
        while(1):
            time.sleep(1)
            if(check("abs/"+"ok")):
                print("点ok")
                break
        while(1):
            time.sleep(3)
            if(check("abs/"+"zidong")):
                print("点自动")
                break
        while(1):
            time.sleep(1)
            if(check("abs/"+"start")):
                print("点开始")
                break
def main():
    #get_position_and_shoot("choose") #截图
    #story_read()  #故事模式
    #multiple_play()
    #ring_bell()
    abs()
if __name__== "__main__" :
    main()

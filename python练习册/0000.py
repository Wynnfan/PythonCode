from PIL import Image,ImageDraw,ImageFont
import random

im = Image.open('bg.jpg') #打开照片
wDraw, hDraw = im.size  #获取照片尺寸
w, h = int(wDraw*0.9),int(hDraw*0.1) #确定数字的位置
num = str(random.randint(0,99))
font = ImageFont.truetype('arial.ttf',30) #加载字体文件
draw = ImageDraw.Draw(im)
draw.text((w, h), num, font=font, fill='red') #在图片上书写文本
im.save('python.jpg')
im.show()
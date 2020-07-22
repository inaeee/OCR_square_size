from PIL import Image
import os


num=0
for i in range(1,230):
    try:
        img=Image.open("C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_size500\\square_"+str(i)+".jpg")
        #print(str(i))
        img2=img.resize((500,500))
        print(str(i)+"사이즈변경")
        img2.save("C:\\Users\\inaee\\Desktop\\2020-1MAKERS\\OCR\\square_size500\\square_"+str(i)+".jpg")
        num=num+1
        print(str(i)+"사이즈변경완료")
    except:
        print(str(i)+"존재안함")

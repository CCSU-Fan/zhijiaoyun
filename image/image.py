from PIL import Image
import time
import pytesseract


# 灰化处理
img = Image.open('5.jpg').convert('L')
# 像素数据
pixdata = img.load()

w,h = img.size

# 去燥
for y in range(h):
	for x in range(w):
		if pixdata[x, y] < 160:
			pixdata[x, y] = 0
		else:
			pixdata[x ,y] = 255

for i in range(h): # 最左列和最右列
		#print(pixdata[0, i]) # 最左边一列的像素点信息
		#print(pixdata[w-1, i]) # 最右边一列的像素点信息
		if pixdata[0, i] == 0 and pixdata[1, i] == 255:
			pixdata[0, i] = 255
		if pixdata[w-1, i] == 0 and pixdata[w-2, i] == 255:
			pixdata[w-1, i] = 255

for i in range(w): # 最上行和最下行
	# print(pixdata[i, 0]) # 最上边一行的像素点信息
	# print(pixdata[i, h-1]) # 最下边一行的像素点信息
	if pixdata[i, 0] == 0 and pixdata[i, 1] == 255:
		pixdata[i, 0] = 255
	if pixdata[i, h-1] == 0 and pixdata[i, h-2] == 255:
		pixdata[i, h-1] = 255

for y in range(1, h-1):
	for x in range(1, w-1):
		if pixdata[x, y] == 0: # 遍历除了四个边界之外的像素黑点
			count = 0 # 统计某个黑色像素点周围九宫格中白块的数量（最多8个）
			if pixdata[x+1, y+1] == 255:
					count = count + 1
			if pixdata[x+1, y] == 255:
					count = count + 1
			if pixdata[x+1, y-1] == 255:
					count = count + 1
			if pixdata[x, y+1] == 255:
					count = count + 1
			if pixdata[x, y-1] == 255:
					count = count + 1
			if pixdata[x-1, y+1] == 255:
					count = count + 1
			if pixdata[x-1, y] == 255:
					count = count + 1
			if pixdata[x-1, y-1] == 255:
				count = count + 1

			if count > 6:
				pixdata[x, y] = 255

for i in range(h): # 最左列和最右列
	if pixdata[0, i] == 0 and pixdata[1, i] == 255:
		pixdata[0, i] = 255
	if pixdata[w-1, i] == 0 and pixdata[w-2, i] == 255:
		pixdata[w-1, i] = 255

for i in range(w): # 最上行和最下行
	if pixdata[i, 0] == 0 and pixdata[i, 1] == 255:
		pixdata[i, 0] = 255
	if pixdata[i, h-1] == 0 and pixdata[i, h-2] == 255:
		pixdata[i, h-1] = 255


img.save('10.png')
image = Image.open("10.png")
#图片转文字
text = pytesseract.image_to_string(image) 
print(text)





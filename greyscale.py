from PIL import Image
from numpy import sqrt
import sys

blocksize = int(sys.argv[1])
palette = [' ', '.', ':', '/', 's', 'O', '9', '8', '@', '▒', '▄']

im = Image.open(sys.argv[2])
pix = im.load()
print(im.size)
open("outimage.txt", 'w').close()
f = open("outimage.txt", 'a+')
print("Loading image...")
w, h = im.size[0], im.size[1];
greyscale = [[0 for x in range(w)] for y in range(h)]

test = Image.new('RGBA', (int(w/sqrt(blocksize))+1, int(h/sqrt(blocksize))+1))
testimage = test.load()

map = [[0 for x in range(int(w/sqrt(blocksize))+1)] for y in range(int(h/sqrt(blocksize))+1)]

print("Processing...")
for i in range(h):
	for j in range(w):
		greyvalue = (pix[j,i][0] + pix[j,i][1] + pix[j,i][2])/3
		map[int(i/sqrt(blocksize))][int(j/sqrt(blocksize))] += greyvalue

for i in range(int(h/sqrt(blocksize))+1):
	for j in range(int(w/sqrt(blocksize))+1):
		map[i][j] = int(map[i][j]/blocksize)
		value = int(((255-map[i][j])/255)*10)
		if(i == int(h/sqrt(blocksize)) or  j == int(w/sqrt(blocksize))):
			f.write(' ')
		else:
			if(value > 10):
				f.write(palette[10])
			else:
				f.write(palette[int(((255-map[i][j])/255)*10)])
		f.write(' ')
	f.write("\n")



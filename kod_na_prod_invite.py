from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

empty_image_filename = 'Kod-na-prod_invite_empty.png'
result_filename = 'kod_na_prod_invite_{}.png'

script_filename = 'Rubik_medium.ttf'
font_size = 120
default_name = 'nickname'
name = default_name
default_text = "Привет, {}!"
resolution = 1000

def main(name=default_name):
	res = resolution
	if len(sys.argv) > 1:
		name = sys.argv[1]
	if len(sys.argv) > 2:
		try:
			res = int(sys.argv[2])
		except:
			pass
	# print(default_text)
	text = default_text.format(name)
	res_filename = result_filename.format(name)
	# print(text)

	img = Image.open(empty_image_filename)
	draw = ImageDraw.Draw(img)
	# font = ImageFont.truetype(<font-file>, <font-size>)
	font = ImageFont.truetype(script_filename, font_size)
	# draw.text((x, y),"Sample Text",(r,g,b))
	draw.text((img.width / 2, 450), text, (255, 255, 255),  anchor='mb',font=font, align='center')
	img = img.resize((res, res))
	img.save(res_filename)


if __name__ == '__main__':
	main()
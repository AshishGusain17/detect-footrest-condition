import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import pandas as pd
import cv2
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import os













def check():
	image = imageio.imread("img1.jpg")
	bbs = BoundingBoxesOnImage([
	BoundingBox(x1=0, x2=0, y1=0, y2=0)
	], shape=image.shape)
	for i in range(1):
		rotate=iaa.Affine(rotate=(-12, 12))
		image_aug, bbs_aug = rotate(image=image, bounding_boxes=bbs)
		
		for j in range(1):
			r="AddToHue"
			aug = iaa.AddToBrightness((-30, 30))
			image_aug, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)


			aug = iaa.AddToHue((-15, 15))
			image_aug, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)





			# cv2.imwrite("a.jpg",image_aug)
			print(bbs_aug[0].x1)
			ia.imshow(bbs_aug.draw_on_image(image_aug, size=2))

# check()
















def alpha(image , xmin1 , ymin1 , xmax1 , ymax1 , classy , img_name):
	global xml_list
	ctt = 0 
	if classy == 'open':
		for i in range(10):
			rotate=iaa.Affine(rotate=(-12, 12))
			image_aug = rotate(image=image)
			
			for j in range(10):
				aug = iaa.AddToBrightness((-30, 30))
				image_color= aug(image=image_aug)

				aug = iaa.AddToHue((-15, 15))
				image_color= aug(image=image_color)


				ctt = ctt+1
				name_changed = str(ctt)+img_name


				cv2.imwrite(os.path.join(fin_folder, "training" , name_changed),image_color)
				# ia.imshow(draw_on_image(image_aug, size=2))

				value = (name_changed , 624 , 832 , 'open' , 0 , 0 , 0 , 0)
				xml_list.append(value)
	else:
		bbs = BoundingBoxesOnImage([
		BoundingBox(x1=xmin1, x2=xmax1, y1=ymin1, y2=ymax1)
		], shape=image.shape)
		for i in range(10):
			rotate=iaa.Affine(rotate=(-12, 12))
			image_aug, bbs_aug = rotate(image=image, bounding_boxes=bbs)
			
			for j in range(10):
				r="AddToHue"
				aug = iaa.AddToBrightness((-30, 30))
				image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)


				aug = iaa.AddToHue((-15, 15))
				image_color, bbs_aug = aug(image=image_color, bounding_boxes=bbs_aug)



				ctt = ctt+1
				name_changed = str(ctt)+img_name


				cv2.imwrite(os.path.join(fin_folder, "training" , name_changed),image_color)
				# ia.imshow(bbs_aug.draw_on_image(image_color, size=2))

				value = (name_changed , 624 , 832 , 'closed' , bbs_aug[0].x1 , bbs_aug[0].y1 , bbs_aug[0].x2 , bbs_aug[0].y2)

				xml_list.append(value)





fin_folder = os.path.join(os.getcwd() , "final_size")
examples = pd.read_csv(os.path.join(fin_folder , "training1_labels.csv"))
filename = np.array(examples["filename"])
classy = np.array(examples["class"])
xmin = np.array(examples["xmin"])
ymin = np.array(examples["ymin"])
xmax = np.array(examples["xmax"])
ymax = np.array(examples["ymax"])
lent = len(filename)
# print(filename)
# print(classy)
# print(xmin)
# print(ymin)
# print(xmax)
# print(ymax)


# print(os.listdir(fin_folder))

cl = "training1"
fin_name =  os.path.join(fin_folder, cl)
xml_list = []
for img in os.listdir(fin_name):
	fin_image_path = os.path.join(fin_name , img)
	if fin_image_path[-3:] == 'xml':
		pass
	else:
		xmin1 , ymin1 , xmax1 , ymax1 , classy = 0 , 0 , 0 , 0 , 'open'
		for i in range(lent):
			if img == filename[i]:
				xmin1 , ymin1 , xmax1 , ymax1 , classy = xmin[i] , ymin[i] , xmax[i] , ymax[i] , 'closed'
				break
		print(fin_image_path)
		image = imageio.imread(fin_image_path)
		alpha(image , xmin1 , ymin1 , xmax1 , ymax1 , classy , img)
		print(xmin1 , ymin1 , xmax1 , ymax1 , classy , img)
		# break

		

		


column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
xml_df = pd.DataFrame(xml_list, columns=column_name)
xml_df.to_csv((fin_folder + '/training_labels.csv'), index=None)
print('Created csv file')

























# elif r == "AddToHueAndSaturation":
# 	aug = iaa.AddToHueAndSaturation((-50, 50), per_channel=True)
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)

# elif r == "AddToSaturation":
# 	aug = iaa.AddToSaturation((-50, 50))
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)

# elif r == "ChangeColorTemperature":
# 	aug = iaa.ChangeColorTemperature((1100, 10000))
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)






# elif r == "GRAY":
# 	aug = iaa.ChangeColorspace( to_colorspace='GRAY')
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)

# elif r == "BGR":
# 	aug = iaa.ChangeColorspace( to_colorspace='BGR')
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)

# elif r == "HSV":
# 	aug = iaa.ChangeColorspace( to_colorspace='HSV')
# 	image_color, bbs_aug = aug(image=image_aug, bounding_boxes=bbs_aug)



import cv2
import os




org_folder = os.path.join(os.getcwd() , "org_size")
fin_folder = os.path.join(os.getcwd() , "final_size")

print(os.listdir(org_folder))

for cl in os.listdir(org_folder):
	org_name =  os.path.join(org_folder, cl)
	fin_name =  os.path.join(fin_folder, cl)
	for img in os.listdir(org_name):
		org_image_path = os.path.join(org_name , img)
		fin_image_path = os.path.join(fin_name , img)
		print(org_image_path)
	


		image_path = cv2.imread(org_image_path)



		image_path = cv2.resize(image_path,(624,832))

		cv2.imwrite(fin_image_path,image_path)

		# cv2.imshow("Dfv",image_path)
		# cv2.waitKey(0)



# 3120  width        4160 height
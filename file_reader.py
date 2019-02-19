import csv
import os
filepath = 'hitlist.csv'  
destination='cropped_images/'

with open(filepath) as fp:  
   lines = csv.reader(fp, delimiter=',', quotechar='|')
   cnt = 1
   for line in lines:
       if (cnt==1):
           print("hello world")
           
       else:
	       parameters=line
	       print(len(line))
	       image_path=parameters[0]+'.jpg'
	       path_test_image="C:/Users/GAME/Desktop/researc_project/object_detection/"
	       test_image_paths=[ os.path.join(path_test_image, image_path)]
	       clut_image=image_path.split('\\')
	       image=clut_image[1]
	       destination_file='cropped{}{}'.format(cnt,image)
	       destination_folder=os.path.join(destination,destination_file)
	       label=parameters[1]
	       socre=parameters[2]
	       cord1=parameters[3]
	       cord2=parameters[4]
	       ord3=parameters[5]
	       cord4=parameters[6]
	       print(image_path)
	       print(destination_folder)
       #print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
from PIL import Image
import os
from skimage import io
import csv

filepath = 'C:/Users/GAME/Desktop/researc_project/object_detection/hitlist.csv'  
destination='C:/Users/GAME/Desktop/researc_project/object_detection/cropped_images/'
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    width=0
    height=0
    width,height=image_obj.size
    (left, right, top, bottom) = (coords[1] * width, coords[3] * width,coords[0] * height, coords[2] * height)
    print(left)
    cropped_image = image_obj.crop((left, top, right, bottom))
    cropped_image.save(saved_location)
    #cropped_image.show()
def crop_images(path_images, path_output, dimensions, centre=True):
    """
    Batch crop images from top left hand corner to dimensions specified. Skips
    images where dimensions are incompatible.
    """
    print ('cropping images...')
    for i, filename in enumerate(os.listdir(path_images)):
        try:
            image = io.imread('{}{}'.format(path_images, filename))
            cropped = crop_image(image, dimensions, centre=centre)
            io.imsave(
                fname='{}{}'.format(path_output, filename),
                arr=cropped
            )
            print ('{}: {}'.format(i, filename))
        except IndexError:
            print ('{}: {} failed - dimensions incompatible'.format(i, filename))

    print ('all images cropped and saved.')
#img = Image.open("image1.jpg")
#area = (40, 40, 80, 80)
#images="C:/Users/GAME/Desktop/researc_project/patching/images/"
#output_path="C:/Users/GAME/Desktop/researc_project/patching/"
#crop_images(images,output_path,area,centre=True)
#cropped_img = img.crop(area)
#cropped_img.show()
image = 'image1.jpg'

#crop(image, (40, 40, 80, 80), 'image.jpg')

with open(filepath) as fp:  
   lines = csv.reader(fp, delimiter=',', quotechar='|')
   cnt = 1
   for line in lines:
	   parameters=line
	   print(len(line))
	   image_path=parameters[0]+'.jpg'
	   path_test_image="C:/Users/GAME/Desktop/researc_project/object_detection/"
	   test_image_paths=os.path.join(path_test_image, image_path)
	   clut_image=image_path.split('\\')
	   #image=clut_image[0]
	   destination_file='cropped{}{}'.format(cnt,image)
	   destination_folder=os.path.join(destination,destination_file)
	   label=parameters[1]
	   socre=float(parameters[2])
	   cord1=float(parameters[3])
	   cord2=float(parameters[4])
	   cord3=float(parameters[5])
	   cord4=float(parameters[6])
	   #print(test_image_paths)
	   #print(destination_folder)
	   line = fp.readline()
	   area = (cord1,cord2, cord3, cord4)
	   crop(test_image_paths, (cord1,cord2, cord3, cord4), destination_folder)
	   cnt += 1



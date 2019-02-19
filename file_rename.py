# importing os module 
import os 
  
# Function to rename multiple files 
def main(): 
    i = 1
      
    for filename in os.listdir("C:/Users/GAME/Desktop/researc_project/object_detection/test_images/"): 
        dst ="image" + str(i) + ".jpg"
        src ='C:/Users/GAME/Desktop/researc_project/object_detection/test_images/'+ filename 
        dst ='C:/Users/GAME/Desktop/researc_project/object_detection/test_images/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
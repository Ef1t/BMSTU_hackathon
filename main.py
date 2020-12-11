import cv2
import imutils 


cam = cv2.VideoCapture('subway.mp4') # вместо subway.mp4 название файлика kattyg 

# Initializing the HOG person 
hog = cv2.HOGDescriptor() 
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) 

def is_intersected(sq1, sq2):
    x1 = sq1[0]
    x11 = sq1[0] + sq1[2]
    y1 = sq1[1]
    y11 = sq1[1] - sq1[3]
    x2 = sq2[0]
    x21 = sq2[0] + sq2[2]
    y2 = sq2[1]
    y21 = sq2[1] - sq2[3]

    if (x1 > x21) or (x11 < x2) or (y1 < y21) or (y11 > y2):
        return False
    else:
        return True

while True:
    success, image = cam.read()

    # Reading the Image 
    #image = cv2.imread('kek.jpg') 
    
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #image = cv2.flip(image, 1) # отрзаить камеру по горизонтали

    # Resizing the Image 
    image = imutils.resize(image, 
                          width=min(500, image.shape[1])) 
       
    # Detecting all humans 
    (humans, _) = hog.detectMultiScale(image,  
                                        winStride=(4, 4), 
                                        padding=(3, 3), 
                                        scale=1.1)
    # getting no. of human detected
    #print('Human Detected : ', len(humans))


    # Drawing the rectangle regions
    for (x, y, w, h) in humans: 
        cv2.rectangle(image, (x, y),  
                      (x + w, y + h),  
                      (0, 0, 255), 2) 
    
    count = 0
    for i in range(len(humans) - 1):
        for j in range(len(humans) - i + 1):
            if (is_intersected(humans[i], humans[i + 1])):
                print(humans[i])
                count += 1
                break


                
    
    print("People: " + str(len(humans)))
    print("Collisions: " + str(count))
     
    # Displaying the output Image 
    cv2.imshow("Image", image) 

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows() 

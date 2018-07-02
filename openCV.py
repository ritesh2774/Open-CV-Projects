import cv2
import glob

img_list = glob.glob("*.jpg")
for image in img_list:
    img = cv2.imread(image,0)
    r = cv2.resize(img, (100,100))
    cv2.imshow("frame", r)
    cv2.waitKey(0)
    cv2.destroyWindow("frame")
    cv2.imwrite("resized_"+image, r)



# img = cv2.imread("galaxy.jpg", 1)
# img2 = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 1)
# img3 = cv2.imread("Lighthouse.jpg", 1)
# img4 = cv2.imread("Moon sinking, sun rising.jpg", 1)
#
# print(img.shape)
# print(img.ndim)
#
# # resize_img = cv2.resize(img,((int(img.shape[1]/2)),(int(img.shape[1]/2))))
# resize_img = cv2.resize(img,(100,100))
# resize_img2 = cv2.resize(img2,(100,100))
# resize_img3 = cv2.resize(img3,(100,100))
# resize_img4 = cv2.resize(img4,(100,100))
# # cv2.imshow("ritesh",resize_img)
# #cv2.imshow("ritesh",resize_img2)
# #cv2.imshow("ritesh",resize_img3)
# cv2.imshow("ritesh",resize_img4)
#
# cv2.waitKey(0)
# #cv2.distroyAllWindow()

# cv2.imwrite("resized_galaxy.jpg",resize_img)
#cv2.imwrite("kangaroos-rain-australia_71370_990x742.jpg",resize_img2)
#cv2.imwrite("Lighthouse.jpg",resize_img3)
# cv2.imwrite("Moon sinking, sun rising.jpg",resize_img4)
import cv2

# matplotlib uses RBG  color scheme while Open Cv uses BGR Color scheme

# 1 - reading image from computer
image = cv2.imread("images/image.jpg")

# 2- convert the image from BGR to RBG or a grayscale formate
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 3 - inverting the grey_scale image i.e RGB image
invert_img = cv2.bitwise_not(grey_image)

# 4- blur the image, the numbers are the kernel is the hernel blur ratio that is the larger the numbers the more blurer
bluring_image = cv2.GaussianBlur(invert_img, (21,21), 0)

# 5- invert the blure image
inverted_blur = cv2.bitwise_not(bluring_image)
# or
# inverted_image = 255 - bluring_image
sketch_image = cv2.divide(grey_image, inverted_blur, scale = 256.0)


# saving the sketch file
# cv2.imwrite("sketch.png", sketch_image)

# displaing the sketch file on the screen
cv2.imshow('sketch.jpg', sketch_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
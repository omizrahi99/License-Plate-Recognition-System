from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

car_image = imread("car.jpg", as_gray=True)
print(car_image.shape) #print dimensions of array

gray_car_image = car_image * 255 #instead of pixel range from 0 to 1, pixels will range from 0 to 255

fig, (ax1, ax2) = plt.subplots(1, 2) #create two plots
ax1.imshow(gray_car_image, cmap="gray") #show gray car in left plot
threshold_value = threshold_otsu(gray_car_image) #get threshold from gray_car_image
binary_car_image = gray_car_image > threshold_value #convert grayscale to binary
ax2.imshow(binary_car_image, cmap="gray") #show binary car in right plot
plt.show()

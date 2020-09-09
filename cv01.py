import cv2
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)

# %matplotlib inline

# Import the image
img = cv2.imread('./burano.jpg')

# Convert the image into RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

# Convert the image into gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray, cmap = 'gray')

# Plot the three channels of the image
fig, axs = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 20))
for i in range(0, 3):
    ax = axs[i]
    ax.imshow(img_rgb[:, :, i], cmap = 'gray')
# plt.show()

# Transform the image into HSV and HLS models
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# Plot the converted images
fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 20))
ax1.imshow(img_hsv)
ax2.imshow(img_hls)
# plt.show()

# Copy the image
img2 = cv2.imread('./wall_of_love.jpg')
# Draw a rectangle 
cv2.rectangle(img2, pt1 = (800, 470), pt2 = (980, 530), 
              color = (255, 0, 0), thickness = 5)
plt.imshow(img2)

# Draw a circle 
cv2.circle(img2, center = (950, 50), radius = 50, 
           color = (0, 0, 255), thickness = 5)
plt.imshow(img2)

# Add text 
cv2.putText(img2, text = "the Wall of Love", 
            org = (250, 250),
            fontFace = cv2.FONT_HERSHEY_DUPLEX, 
            fontScale = 2, 
            color = (0, 255, 0), 
            thickness = 2, 
            lineType = cv2.LINE_AA)
plt.imshow(img2)
plt.show()
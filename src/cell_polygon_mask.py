import numpy as np
from matplotlib.path import Path
import matplotlib.pyplot as plt
import random 
from skimage.draw import random_shapes

# create a dictionary of possible cell size and shape (# of vertex)

# image size 
width, height = 1000, 1000

# choose randomly a number of vertices between 10 and 30
#vertex_number = random.choice(range(10, 31))

# choose randomly coordinates for each vertices => how to enforce that vertices should be in circle? 
image, labels = random_shapes((128, 128), max_shapes=1, shape='circle', random_seed=0)
print(f'Image shape: {image.shape}\nLabels: {labels}')

# We can visualize the images.
fig, axes = plt.subplots(nrows=2, ncols=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Grayscale shape')



'''
polygon=[(0.1*width, 0.1*height), (0.15*width, 0.7*height), (0.8*width, 0.75*height), (0.72*width, 0.15*height)]
poly_path=Path(polygon)
x, y = np.mgrid[:height, :width]
coors=np.hstack((x.reshape(-1, 1), y.reshape(-1,1))) # coors.shape is (4000000,2)
mask = poly_path.contains_points(coors)
plt.imshow(mask.reshape(height, width))
plt.show()
'''


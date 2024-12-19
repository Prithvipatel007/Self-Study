import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# import picture
pic = Image.open('D:\Personal\Self-Study\LinearAlgebra\Sec-1-Introduction\Einstein_tongue.jpg')

# Let's have a look
# plt.imshow(pic)
# plt.show()

# We need to convert it to floating point precision
# pic = np.array(pic)
# plt.imshow(pic, cmap='gray')
# plt.show()


# The goal is to look at the image and apply singular value decomposition, to do what's called a low rank approximation. 
# SVD

U, S, V = np.linalg.svd(pic)

# plot the spectrum
# plt.plot(S, 's-')
# plt.xlim([0, 100])
# plt.title('Spectrum of the Picture')
# plt.xlabel('Component Number')
# plt.ylabel('Singular Value (\sigma_i)')
# plt.show()

# Reconstruct the image based on some components

# List the components you want to use to reconstruct the image
comps = np.arange(20,150)

# Reconstruct the low-rant version of the picture
reconPic = U[:,comps] @ np.diag(S[comps]) @ V[comps,:]

# Show the original and reconstructed images for comparison
plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)
plt.imshow(pic, cmap='gray')
plt.title('Original Picture')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(reconPic, cmap='gray')
plt.title('Components %s-%s' % (comps[0], comps[-1]))
plt.axis('off')

plt.show()

# INFO: With the version with only reconstructing the first 5 components, but it looks like its degraded.
# The first 5 components are not enough to capture the essence of the picture.
# So whats interesting is that this picture seems to contain all of the low spatial frequency informations, all like the big contours, 
# but its very blurry. 

# Between 20 and 150, the picture looks different. We see all the sharp edges. These are all high spatial frequency features of the data. 
# In fact, all of these sharp edges are apparent and a lot of kind of smoother features are gone. They just looks like a little bit of gray noise back there. 



import numpy as np
from PIL import Image

# a1 = np.array(1)
# a1 = np.array([1])
# a2 = np.array([1,2,3])
# # a3 = np.array(1,2,3)
#
# print(a1, a2)

img = Image.open("bug.png")
channels = np.atleast_1d(1)
print(type(channels))
print(type(channels[0]))
print(len(channels))
inp = tuple([c for c in channels])
img.putpixel((0,0), inp)
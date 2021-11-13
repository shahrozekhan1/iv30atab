import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

img= Image.open("F:\Data Science Masters\DSSS Exercise\Exercise3\iv30atab\home.jpg")

print(type(img))

numpy= np.array(img)
print(numpy.dtype)
print(numpy.shape)
print(img.size)


resize= img.resize((400,400))
print(resize)
resize.show()
  
 
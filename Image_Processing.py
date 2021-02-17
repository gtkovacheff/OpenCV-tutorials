import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img


image = Image.open('CutePanda.png')

data = img_to_array(image)
samples = np.expand_dims(data, 0)
data_generated = ImageDataGenerator(rotation_range=90)
it = data_generated.flow(samples, batch_size=1)
samples.shape
for i in range(9):
    batch = it.next()
    print(batch.shape)

plt.show()
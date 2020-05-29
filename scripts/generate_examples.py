import tensorflow as tf
import numpy as np
import h5py
from random import randint
import Attacks
import matplotlib.pyplot as plt
from string import ascii_uppercase

images = []
labels = []

model = tf.keras.models.load_model("Chars74K_model.h5")
letters = list(ascii_uppercase)

with h5py.File("Chars74K_data.hdf5", "r") as f:
    ds_length = len(f["x_test"])
    indicies = [randint(0,ds_length) for i in range(5)]
    for index in indicies:
        images.append(f["x_test"][index])
        labels.append(f["y_test"][index])
    labels = tf.keras.utils.to_categorical(labels, 26)

for i, image in enumerate(images):
    img = image / 255.0
    img = img.reshape((-1, 128, 128, 1))
    adv = Attacks.new_mi_fgsm(model, img, labels[i], eps=20, T=25)
    pred = model.predict(adv)
    print(letters[pred.argmax()], pred.max() * 100)
    plt.imsave("./images/n_{}.png".format(i),
              adv.reshape(128, 128),
              cmap="gray")

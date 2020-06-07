import tensorflow as tf
import numpy as np
import h5py
import time

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

# for i, image in enumerate(images):
#     img = image / 255.0
#     img = img.reshape((-1, 128, 128, 1))
#     adv = Attacks.new_mi_fgsm(model, img, labels[i], eps=20, T=25)
#     #adv = Attacks.fgsm(model, img, labels[i], eps=20)
#     pred = model.predict(adv)
#     print(letters[pred.argmax()], pred.max() * 100)
#     plt.imsave("./images/m_{}.png".format(i),
#               adv.reshape(128, 128),
#               cmap="gray")

with tf.compat.v1.Session() as sess:
        #data = images / 255.0
        #data = img.reshape((-1, 128, 128, 1))
        data = images
        #data, model =  MNIST(), MNISTModel("models/mnist", sess)
        attack = Attacks.CarliniL0(sess, model, max_iterations=100, initial_const=10,
                           largest_const=15)

        inputs, targets = generate_data(data, samples=1, targeted=True,
                                        start=0, inception=False)
        timestart = time.time()
        adv = attack.attack(inputs, targets)
        timeend = time.time()

        print("Took",timeend-timestart,"seconds to run",len(inputs),"samples.")

        for i in range(len(adv)):
            print("Valid:")
            show(inputs[i])
            print("Adversarial:")
            show(adv[i])

            print("Classification:", model.model.predict(adv[i:i+1]))

            print("Total distortion:", np.sum((adv[i]-inputs[i])**2)**.5)

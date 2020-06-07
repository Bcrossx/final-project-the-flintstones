import tensorflow as tf
import numpy as np
import h5py
from string import ascii_uppercase
from random import randint
import Attacks

def load_test_data(filename="Chars74K_data.hdf5"):
    with h5py.File(filename, "r") as f:
        x_test = []
        y_test = []
        ds_length = len(f["x_test"])
        # Sample of 250 images from our test dataset
        indices = [randint(0, ds_length) for i in range(250)]
        for index in indices:
            x_test.append(f["x_test"][index])
            y_test.append(f["y_test"][index])
    return np.array(x_test), y_test

def attack_successful(model, attack, img, lbl, epsilon, T):
    # Returns boolean of whether or not attack was successful at fooling model
    truth_lbl = labels[lbl.argmax()]
    if T >= 0: 
        # MI-FGSM
        adv_example = attack(model, img, lbl, eps=epsilon, T=T)
    else:
        # FGSM
        adv_example = attack(model, img, lbl, epsilon)
    prediction_lbl = labels[model.predict(adv_example).argmax()]
    if prediction_lbl is not truth_lbl:
        return True, epsilon
    return False, epsilon
    
def test(model, attack, T=-1):
    eps = 0
    successes = 0
    x_len = len(x_test)
    for idx, img in enumerate(x_test):
        truth_arr = y_test[idx]
        image = img.reshape((-1, 128, 128, 1))
        for epsilon in epsilons:
            found, e = attack_successful(model, attack, image, truth_arr, epsilon, T)
            if found:
                successes += 1
                eps += e
                break
    print("Successes: {}/{}".format(successes, x_len))
    print("Success Rate: ", successes / x_len)
    print("Average Epsilon:", eps / successes)

labels = list(string.ascii_uppercase)
epsilons = [0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

model = tf.keras.models.load_model("Chars74K_model.h5")
x_test, y_test = load_test_data()

x_test = x_test/255
y_test = tf.keras.utils.to_categorical(y_test, len(labels))

print("FGSM Tests")
test(model, Attacks.fgsm)

print("\nMI-FGSM Tests, 10 Iterations")
test(model, Attacks.mi_fgsm, 10)

print("\nMI-FGSM Tests, 20 Iterations")
test(model, Attacks.mi_fgsm, 20)

import tensorflow as tf
import numpy as np

def compute_gradient(model, image, label):
    image = tf.cast(image, tf.float32)
    with tf.GradientTape() as tape:
        tape.watch(image)
        prediction = model(image)
        loss = tf.keras.losses.MSE(label, prediction)
    return tape.gradient(loss, image), loss

def fgsm(model, image, label, eps=0.1):
    gradient, _ = compute_gradient(model, image, label)
    perturbations = tf.sign(gradient).numpy()
    return image + eps*perturbations

def mi_fgsm(model, image, label, decay_factor=1.0, eps=0.1, T=10):
    g = np.zeros((1, 128, 128, 1))
    alpha = eps / T
    adv_x = image
    for t in range(T):
        gradient, _ = compute_gradient(model, adv_x, label)
        L2 = tf.norm(gradient, ord=2)
        g = decay_factor*g + (gradient / L2)
        adv_x = adv_x + alpha * tf.sign(g)
    return adv_x.numpy()

def new_mi_fgsm(model, image, label, decay_factor=1.0, eps=0.1, T=10):
    # This method seems really promising but is also very spotty
    # I would not recommend using this until further notice
    g = np.full((1, 128, 128, 1), 1e-12, dtype=np.float32)
    adv_x = image # 1, 128, 128, 1
    for t in range(T):
        gradient, loss = compute_gradient(model, adv_x, label) # Tensors
        loss = loss.numpy()
        L1 = tf.norm(gradient, ord=1).numpy() # Tensor

        if L1 == 0: L1 = 1e-12

        g = (g * decay_factor) + (loss/L1)

        L2 = tf.norm(g, ord=2).numpy()
        if np.isinf(L2):
            # Dividing by inf gives an error, and x/inf --> 0 so we just set the
            # perturbations to an matrix of zeros
            # It still performed the calculations without this but errors suck
            perturbations = np.full_like(g, 0)
        else:
            perturbations = (eps * (g/L2))
        adv_x = adv_x - perturbations
    return adv_x

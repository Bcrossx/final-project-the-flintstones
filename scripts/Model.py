import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten

def train(x_train, y_train, batch_size, epochs, validation_data,
         save=False, name="model"):
    # validation_data: tuple ex - (x_test, y_test)
    # save: whether or not to save as a file
    model = Sequential([
                Conv2D(32,
                    kernel_size=(5, 5),
                    strides=(1, 1),
                    padding='same',
                    activation='relu',
                    input_shape=(128, 128, 1)),
                Conv2D(64,
                    kernel_size=(5, 5),
                    strides=(1, 1),
                    padding='same',
                    activation='relu'),
                Conv2D(64,
                    kernel_size=(5, 5),
                    strides=(1, 1),
                    padding='same',
                    activation='relu'),
                MaxPooling2D(pool_size=(2, 2)),
                Dropout(0.2),
                Flatten(),
                Dense(32),
                Dropout(0.2),
                Dense(32),
                Dropout(0.2),
                Dense(26, activation='softmax')
            ])
    model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
    model.fit(x_train, y_train,
             batch_size=batch_size,
             epochs=epochs,
             validation_data=validation_data)

    if save: model.save(name + ".h5")

    return model

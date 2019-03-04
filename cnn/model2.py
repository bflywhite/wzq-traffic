import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from sklearn.metrics import classification_report
import pickle

# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape (60,000 28x28), y shape (10,000, )
f = open(r'train.pkl', 'rb')
X_train = pickle.load(f)
X_train = X_train.reshape((-1, 1, 28, 28))
f.close()
f = open(r'train_labels.pkl', 'rb')
y_train = pickle.load(f)
# print(y_train.shape)
f.close()

flag = np.arange(len(X_train))
np.random.shuffle(flag)
X_train = X_train[flag]
y_train = y_train[flag]
print(flag[:10])
f = open(r'test.pkl', 'rb')
X_test = pickle.load(f)
f.close()
X_test = X_test.reshape((-1, 1, 28, 28))
f = open(r'test_labels.pkl', 'rb')
y_test = pickle.load(f)

f.close()

# print(x_train.shape)


# data pre-processing，-1 represents the number of samples;1 represents the num of channels,28&28 represents the length,width respectively


# build neural network

model = Sequential()

model.add(Convolution2D(
    nb_filter=32,
    nb_col=5,
    nb_row=5,
    border_mode='same',  # padding method
    input_shape=(1,  # channels
                 28, 28)  # length and width

))

model.add(Activation('relu'))

model.add(MaxPooling2D(
    pool_size=(2, 2),
    strides=(2, 2),
    border_mode='same',  # padding method
))

model.add(Convolution2D(32, 5, 5, border_mode='same'))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2), border_mode='same'))

model.add(Flatten())

model.add(Dense(1024))

model.add(Activation('relu'))

model.add(Dense(2))

model.add(Activation('softmax'))

adam = Adam(lr=1e-4)

model.compile(
    loss='categorical_crossentropy',
    optimizer=adam,
    metrics=['accuracy'])

print('\nTraining-----------')
model.fit(X_train, y_train, epochs=50, batch_size=64, verbose=1, validation_split=0.2)

model.save("model2class.h5")

print('\nTesting------------')
loss, accuracy = model.evaluate(X_test, y_test)
print()
print('test loss: ', loss)
print('test accuracy: ', accuracy)

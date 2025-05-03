import tensorflow as tf
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test)= tf.keras.datasets.cifar10.load_data()
print("Training data shape",x_train.shape, y_train.shape)

plt.imshow(x_train[1])
plt.show()
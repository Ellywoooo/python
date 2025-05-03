import tensorflow as tf # Load the CIFAR-10 database
import matplotlib.pyplot as plt # Visualizeing data

(x_train,y_train),(x_test,y_test)= tf.keras.datasets.cifar10.load_data()
print("Training data shape",x_train.shape, y_train.shape)

plt.imshow(x_train[1])
plt.show()
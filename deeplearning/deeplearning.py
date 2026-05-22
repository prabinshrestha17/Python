import tensorflow as tf

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


#this guides uses the fashion MNIST dataset which contains, 70,000 grayscale images in a 10 category
#MNIST (Modify National Institute of Standards and Technology Database)

#import and load the fashion MNIST data directly from transflow
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#the labels are an array of integers, ranging from 0 to 9 T
# Define class names for flotting 


classNames = ['Tshirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal','Shirt', 'Sneaker', 'Bag', 'Ankle Boot']
#preprocess the data 
#scale the pixel values from 0-255, to 0-1
train_images = train_images/255.0
test_images = test_images/255.0


model = tf.keras.Sequential([
    #flatten the 28*28 image into a 784 element vector
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    #A fully connected layer with 128 neurons and ReLU activation 
    tf.keras.layers.Dense(128, activation="relu"), 
    # the output layer  with neurons, one for each class
    tf.keras.layers.Dense(10)
])



model.compile(optimizer = "adam", 
             loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True), 
              metrics = ['accuracy']
             )

print("Training the model .......")

model.fit(train_images, train_labels, epochs = 10)

def plot_image_and_prediction(i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

train_images.shape
len(train_labels)
train_labels
test_images.shape
len(test_labels)




plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(True)
plt.show()


train_images = train_images /255.0
test_images = test_images /255.0

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap = plt.cm.binary)
    plt.xlabel(classNames[train_labels[i]])
plt.show()

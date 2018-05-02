# coding: utf-8
import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#hold a input for train dataset
# dataset defined with a "tensor", which means the first dimen indicate dataset "count"
# while the last dimen indicate the dimen's count of each data
x = tf.placeholder(tf.float32, [None, 784])

#weights, and biases
# defined b as 10 size array
# defined W as 784*10 size array
b = tf.Variable(tf.zeros([10]))
W = tf.Variable(tf.zeros([784,10])) 
#--------------------------------------------------------------------------------------------------
# predict step: with softmax regression
#--------------------------------------------------------------------------------------------------
#softmax regression on x.W + b
# in <Neural Network and Deep Learning> it used a Logistic function (sigmoid)
y = tf.nn.softmax(tf.matmul(x,W) + b)

#compare value of y, to calculate the accuracy
y_ = tf.placeholder("float", [None,10])

#---------------------------------------------------------------------------------------------------
# training step: with cost/loss function
#---------------------------------------------------------------------------------------------------
#cost function: cross entropy
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
#Backpropagation, gradient descent, to back propagate W and b
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

#init variables
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
#--------------------------------------------------------------------------------------------------- 
# evaluate step
#--------------------------------------------------------------------------------------------------- 
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

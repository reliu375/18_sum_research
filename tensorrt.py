import tensorflow as tf
# import tensorrt as trt 
# import math

x = tf.constant([[37.0, -23.0],[1.0, 4.0]])
w = tf.Variable(tf.random_uniform([2,2]))
y = tf.matmul(x, w)

output = tf.nn.softmax(y)
init_op = w.initialize

with tf.Session() as sess:
	sess.run(init_op)

	print(sess.run(output))

	y_val, output_val = sess.run([y, output])
import tensorflow as tf
import numpy as np
# import tensorrt as trt 
# import math

a = tf.constant(3.0, dtype = tf.float32)
b = tf.constant(4.0)
y = a + b

print(tf.get_default_graph())
writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())
# events.out.tfevents.{timestamp}.{hostname}
# print(x)
# print(w)
# print(y)
# print(output)
# print(init_op)
'''
with tf.Session() as sess:
	sess.run(init_op)

	print(sess.run(output))

	y_val, output_val = sess.run([y, output])

	print(tf.get_default_graph())
	writer = tf.summary.FileWriter('.')

	writer.add_graph(tf.get_default_graph())
'''
'''
import tensorrt as trt
from tensorrt.parsers import uffparser

uff_model = uff.from_tensorflow(init_op)

G_LOGGER = trt.infer.ConsoleLogger(trt.infer.LogSeverity.ERROR)

parser = uffparser.create_uff_parser()
parser.register_input(x, (2, 2), 0)
parser.register_output(y)

engine = trt.utils.uff_to_trt_engine(G_LOGGER, uff_model, parser)

parser.destroy()

runtime = trt.infer.create_infer_runtime(G_LOGGER)
context = engine.create_execution_context()

output = np.empty(10, dtype = np.float32)

d_input = cuda.mem_alloc(x.nbytes)
d_output = cuda.mem_alloc(output.nbytes)

bindings = [int(d_input), int(d_output)]

stream = cuda.Stream()

context.enquene(1, bindings, stream.handle, None)
# This is to be continued. 
'''

''' An alternative of parsing a TensorFlow graph.



'''


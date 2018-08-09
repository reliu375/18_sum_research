import tensorflow as tf
import numpy as np
import tensorrt as trt 
from tensorrt.parsers import uffparser
import pycuda.driver as cuda
import pycuda.autoinit
import uff
import pdb

# import math
OUTPUT = ["add/result"]

a = tf.constant(3.0, dtype = tf.float32)
b = tf.constant(4.0)
y = a + b
print(y)
pdb.set_trace()
print(tf.get_default_graph())
writer = tf.summary.FileWriter('.')
writer.add_graph(tf.get_default_graph())
writer.close()

init = tf.global_variables_initializer()

session = tf.Session()
session.run(init)

graphdef = tf.get_default_graph().as_graph_def()
frozen_graph = tf.graph_util.convert_variables_to_constants(session, graphdef, OUTPUT)

'''
def cali_graph(fr_gh):
	trt_graph = trt.create_inference_graph(fr_gh, OUTPUT, 16, 4000000000, "INT8")
	return trt_graph

print(cali_graph(frozen_graph))
'''
model = tf.graph_util.remove_training_nodes(frozen_graph)

uff_model = uff.from_tensorflow(model, ["add/result"])

G_LOGGER = trt.infer.ConsoleLogger(trt.infer.LogSeverity.ERROR)

pdb.set_trace()
parser = uffparser.create_uff_parser()
parser.register_output("add/result")

pdb.set_trace()
engine = trt.utils.uff_to_trt_engine(G_LOGGER, uff_model, parser,1, 1 << 20) 
pdb.set_trace()
# TODO: fill in the rest of the arguments
parser.destroy()

pdb.set_trace()
runtime = trt.infer.create_infer_runtime(G_LOGGER)
context = engine.create_execution_context()

output = np.empty(10, dtype = npu.float32)

d_input = 0
d_output = cuda.mem_alloc(1 * output.nbytes)

bindings = [int(d_input), int(d_output)]

stream = cuda.Stream()

context.enquene(1, bindings, stretam.handle, None)

stream.synchronize()
	
# TODO: destroy all the objects to clear memory.
context.destroy()
engine.destroy()
runtime.destroy()


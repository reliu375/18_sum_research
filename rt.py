import tensorflow as tf
import tensorrt as trt

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction = 0.67)

trt_graph = trat.create_inference_graph(input_graph_def=frozen_graph_def,
				outputs=output_node_name,
				max_batch_size=batch_size,
				max_workspace_size_bytes=workspace_size,
				precision_mode=precision)



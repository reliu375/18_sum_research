import PySpin as ps
import cv2 as cv
import os # For deleting images that are saved.
import pdb
import time
 
# NUM_IMAGES = 100
"""
class TriggerType:
	SOFTWARE = 1
	HARDWARE = 2

CHOSEN_TRIGGER = TriggerType.SOFTWARE

def configure_trigger(cam):
	
	THis function configures the camera to use a trigger. Trigger mode is set 
	to off in order to select the trigger source. Once the trigger source is
	selected, trigger mode is then enabled, which has the camera capture only
	a single image upon the execution of the chosen trigger.
		
		:param cam: Camera to configure trigger for.
		:type cam: CameraPtr
		:return: True if successful, False otherwise.
		:rtype: bool
	
	result = True
	
	print('*** CONFIGURING TRIGGER ***\n')

	if CHOSEN_TRIGGER == TriggerType.SOFTWARE:
		print('Software trigger chosen ...')
	elif CHOSEN_TRIGGER == TriggerType.HARDWARE:
		print('Hardware trigger chosen ...')

	try:
		# Ensure trigger mode off
		# The trigger must be disabled to configure whether the source
		# is software or hardware.
		nodemap = cam.GetNodeMap()
		node_trigger_mode = ps.CEnumerationPtr(nodemap.GetNode('TriggerMode'))
		if not ps.IsAvailable(node_trigger_mode) or not ps.IsReadable(node_trigger_mode):
			print('Unable to disable trigger mode (node retrieval). Aborting...')
			return False

		node_trigger_mode_off = node_trigger_mode.GetEntryByName('Off')
		if not ps.IsAvailable(node_trigger_mode_off) or not ps.IsReadable(node_trigger_mode_off):
			print('Unable to disable trigger mode (enum entry retrieval). Aborting...')
			return False
		
		node_trigger_mode.SetIntValue(node_trigger_mode_off.GetValue())
		
		print('Trigger mode disabled...')
		
		# Select trigger source
		# The trigger source must be set to hardware or software while trigger
		# mode is off.
		
		node_trigger_source = ps.CEnumerationPtr(nodemap.GetNode('TriggerSource'))
		if not ps.IsAvailable(node_trigger_source) or not ps.IsWritable(node_trigger_source):
			print('Unable to get trigger source (node retrieval). Aborting...')
			return False

		if CHOSEN_TRIGGER == TriggerType.SOFTWARE:
			node_trigger_source_software = node_trigger_source.GetEntryByName('Software')
			if not ps.IsAvailable(node_trigger_source_software) or not ps.IsReadable(
                    node_trigger_source_software):
				print('Unable to set trigger source (enum entry retrieval). Aborting...')
				return False
			node_trigger_source.SetIntValue(node_trigger_source_software.GetValue())

		elif CHOSEN_TRIGGER == TriggerType.HARDWARE:
			node_trigger_source_hardware = node_trigger_source.GetEntryByName('Line0')
			if not ps.IsAvailable(node_trigger_source_hardware) or not ps.IsReadable(
                    node_trigger_source_hardware):
				print('Unable to set trigger source (enum entry retrieval). Aborting...')
				return False
			node_trigger_source.SetIntValue(node_trigger_source_hardware.GetValue())
			
		# Turn trigger mode on
        # Once the appropriate trigger source has been set, turn trigger mode
        # on in order to retrieve images using the trigger.
        
		node_trigger_mode_on = node_trigger_mode.GetEntryByName('On')
		if not ps.IsAvailable(node_trigger_mode_on) or not ps.IsReadable(node_trigger_mode_on):
			print('Unable to enable trigger mode (enum entry retrieval). Aborting...')
			return False

		node_trigger_mode.SetIntValue(node_trigger_mode_on.GetValue())
		print('Trigger mode turned back on...')
		
	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		return False
	
	return result
	
def grab_next_image_by_trigger(nodemap, cam):
	
	This function acquires an image by executing the trigger node.
	
	:param cam: Camera to acquire images from.
	:param nodemap: Device nodemap.
	:type cam: CameraPtr
	:type nodemap: INodeMap
	:return: True if successful, False otherwise.
	:rtype: bool
	
	
	try:
		result = True
		# Use trigger to capture image
		# The software trigger only feigns being executed by the *Enter key*;
		# By using trigger, one does not have to turn on continuous mode!
		
		if CHOSEN_TRIGGER == TriggerType.SOFTWARE:
			# Get user input
			input('Press the Enter key to initiate software trigger.')

			# Execute software trigger
			node_softwaretrigger_cmd = ps.CCommandPtr(nodemap.GetNode('TriggerSoftware'))
			if not ps.IsAvailable(node_softwaretrigger_cmd) or not ps.IsWritable(node_softwaretrigger_cmd):
				print('Unable to execute trigger. Aborting...')
				return False

			node_softwaretrigger_cmd.Execute()

		elif CHOSEN_TRIGGER == TriggerType.HARDWARE:
			print('Use the hardware to trigger image acquisition.')
		
	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		return False
	
	return result
	
def reset_trigger(nodemap):
	
	This function returns the camera to a normal state by turning off trigger mode.
  
	:param nodemap: Transport layer device nodemap.
	:type nodemap: INodeMap
	:returns: True if successful, False otherwise.
	:rtype: bool
	
	try:
		result = True
		node_trigger_mode = ps.CEnumerationPtr(nodemap.GetNode('TriggerMode'))
		if not ps.IsAvailable(node_trigger_mode) or not ps.IsReadable(node_trigger_mode):
			print('Unable to disable trigger mode (node retrieval). Aborting...')
			return False

		node_trigger_mode_off = node_trigger_mode.GetEntryByName('Off')
		if not ps.IsAvailable(node_trigger_mode_off) or not ps.IsReadable(node_trigger_mode_off):
			print('Unable to disable trigger mode (enum entry retrieval). Aborting...')
			return False

		node_trigger_mode.SetIntValue(node_trigger_mode_off.GetValue())

		print('Trigger mode disabled...')

	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		result = False

	return result 
	"""
		
def acquire_images(cam, nodemap, nodemap_tldevice):
	"""
	This function acquires and saves 10 images from a device.
	:param cam: Camera to acquire images from.
	:param nodemap: Device nodemap.
	:param nodemap_tldevice: Transport layer device nodemap.
	:type cam: CameraPtr
	:type nodemap: INodeMap
	:type nodemap_tldevice: INodeMap
	:return: True if successful, False otherwise.
	:rtype: bool
	"""
	print('*** IMAGE ACQUISITION***\n')    
	try:
		result = True
		
		# Set the acquisition node to continuous.
		# Node entries have to be casted to a pointer type.
		node_acquisition_mode = ps.CEnumerationPtr(nodemap.GetNode('AcquisitionMode'))
		if not ps.IsAvailable(node_acquisition_mode) or not ps.IsWritable(node_acquisition_mode):
			print('node_acquisition_mode is not available or not writable')
			print('Unable to set acquisition mode to continuous. Aborting...')
			return False
		
		# Retrieve entry node from enumeration node.
		node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName('Continuous')
		if not ps.IsAvailable(node_acquisition_mode_continuous) or not ps.IsReadable(node_acquisition_mode_continuous):
			if not ps.IsAvailable(node_acquisition_mode_continuous):
				print('node_acquisition_mode_continuous is not available.')
			
			if not ps.IsReadable(node_acquisition_mode_continuous):
				print('node_acquisition_mode_continuous is not readable.')

			print('')
			print('Unable to set acquisition mode to continuous. Aborting...')
			return False

		# Retrieve integer value from entry node
		acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()

		# Set integer value from entry node as new value of enumeration node
		node_acquisition_mode.SetIntValue(acquisition_mode_continuous)

		print('Acquisition mode set to continuous...')

		# Begin acquiring images.
		# import pdb
		# pdb.set_trace()
		cam.BeginAcquisition()
		print('Acquiring images...')
		# Retrieve device serial number for filename.
		device_serial_number = ''
		node_device_serial_number = ps.CStringPtr(nodemap_tldevice.GetNode('DeviceSerialNumber'))
		if ps.IsAvailable(node_device_serial_number) and ps.IsReadable(node_device_serial_number):
			device_serial_number = node_device_serial_number.GetValue()
			print('Device serial number retrieved as %s...' % device_serial_number)

		# Retrieve, convert, and save images
		# for i in range(NUM_IMAGES):
		begin_time = time.time()
		counter = 0
		while True:
			try:
				# Apply the trigger to capture the image.
				# result &= grab_next_image_by_trigger(nodemap, cam)
				
				
				# Retrieve next received image.
				image_result = cam.GetNextImage()

				# Check for image completion:
				# if image_result.IsIncomplete():
				#	print('Image incomplete with image status %d ...' % image_result.GetImageStatus())

				#else:
				#	# Print image information:
				#	width = image_result.GetWidth()
				#	height = image_result.GetHeight()
				#	print('Grabbed Image, width = %d, height = %d' % (width, height))

				# Getting the image data as a numpy array
				image_data = image_result.GetNDArray()

				# Convert image to mono 8
				# image_converted = image_result.Convert(ps.PixelFormat_Mono8, ps.HQ_LINEAR)
				# import pdb
				# pdb.set_trace()

				# Create file name in case the image is saved.
				'''
				if device_serial_number:
					filename = 'Acquisition-%s-%d.jpg' % (device_serial_number, i)
				else:  # if serial number is empty
					filename = 'Acquisition-%d.jpg' % i
				'''
				# Save the image to the file. The user may decide to delete that image later.
				# image_converted.Save(filename)
				# print('Image saved as %s' % filename)
				
				# Use OpenCV to have the user view the image.
				# current_image = cv.imread(filename, 1)
				cv.imshow('Image', image_data)
				key = cv.waitKey(1)
				counter += 1

				if key == ord('q') or key == ord('Q'):
					end_time = time.time()
					time_difference = end_time - begin_time
					cv.destroyAllWindows()
					print(str(counter) + ' images are displayed.\n')
					print('The time of which the program ran is ' + str(time_difference) + ' seconds.\n')
					efficiency = counter/time_difference
					print(str(efficiency) + 'images are taken per second. ')
					break;				

				'''				
				while key != ord('s') and key != 27:
					print('Invalid entry. Please try again: ')
					key = cv.waitKey(0)
				
				if key == ord('s'):
					cv.destroyAllWindows()
					print('Image is preserved.')
				elif key == 27: # Else if user presses Esc
					try:
						cv.destroyAllWindows()
						os.remove(filename)
					except:
						print('Error: The file that is deleted is in use or does not exist.')
						# Destroy all windows, then try to delete the file. If failed, throw an exception.
				'''
						
				'''
				# Use OpenCV to present and hold up the image. Press 'S' to save and ESC to discard.
				cv.imshow('Image ' + str(i), image_converted)
				key = cv.waitKey(0)
				if key == 27: # Press Esc to discard the image.
					cv.destroyAllWindows()
					print('Image ' + str(i) + ' is discarded.')
				elif key == ord('s'): # Press S to save the image.
					cv.imwrite(filename, 1)
					cv.destroyAllWindows()
					print('Image saved at %s' % filename)
				'''
				# Release the image to clear the camera buffer.
				image_result.Release()

			except ps.SpinnakerException as ex:
				print('Error: %s' % ex)
				return False
		
		# End acquisition.
		cam.EndAcquisition()
	
	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		return False

	return result

def print_device_info(nodemap):
	"""
	This function prints the device information of the camera from the transport
	layer; please see NodeMapInfo example for more in-depth comments on printing
	device information from the nodemap.

	:param nodemap: Transport layer device nodemap.
	:type nodemap: INodeMap
	:returns: True if successful, False otherwise.
	:rtype: bool
	"""

	print('*** DEVICE INFORMATION ***\n')

	try:
		result = True
		node_device_information = ps.CCategoryPtr(nodemap.GetNode('DeviceInformation'))

		if ps.IsAvailable(node_device_information) and ps.IsReadable(node_device_information):
			features = node_device_information.GetFeatures()
			for feature in features:
				node_feature = ps.CValuePtr(feature)
				print('%s: %s' % (node_feature.GetName(),
                                  node_feature.ToString() if ps.IsReadable(node_feature) else 'Node not readable'))

		else:
			print('Device control information not available.')

	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		return False

	return result


def run_single_camera(cam):
	"""
	This function acts as the body of the example; please see NodeMapInfo example
	for more in-depth comments on setting up cameras.

	:param cam: Camera to run on.
	:type cam: CameraPtr
	:return: True if successful, False otherwise.
	:rtype: bool
	"""
	try:
		result = True
		err = False

		# Retrieve TL device nodemap and print device information
		nodemap_tldevice = cam.GetTLDeviceNodeMap()

		result &= print_device_info(nodemap_tldevice)

        # Initialize camera
		cam.Init()

        # Retrieve GenICam nodemap
		nodemap = cam.GetNodeMap()
		
		# Configure trigger
		#if configure_trigger(cam) is False:
		#	return False

        # Acquire images
		result &= acquire_images(cam, nodemap, nodemap_tldevice)
		
		# Reset trigger
		# result &= reset_trigger(nodemap)

        # Deinitialize camera
		cam.DeInit()

	except ps.SpinnakerException as ex:
		print('Error: %s' % ex)
		result = False

	return result

def main():
	"""
	Example entry point; please see Enumeration example for more in-depth
	comments on preparing and cleaning up the system.

	:return: True if successful, False otherwise.
	:rtype: bool
	"""
	result = True

	# Retrieve singleton reference to system object
	system = ps.System.GetInstance()

	# Get current library version
	version = system.GetLibraryVersion()
	print('Library version: %d.%d.%d.%d' % (version.major, version.minor, version.type, version.build))

	# Retrieve list of cameras from the system
	cam_list = system.GetCameras()

	num_cameras = cam_list.GetSize()

	print('Number of cameras detected: %d' % num_cameras)

	# Finish if there are no cameras
	if num_cameras == 0:

		# Clear camera list before releasing system
		cam_list.Clear()

		# Release system instance
		system.ReleaseInstance()

		print('Not enough cameras!')
		input('Done! Press Enter to exit...')
		return False

	# Run example on each camera
	for i, cam in enumerate(cam_list):

		print('Running example for camera %d...' % i)

		result &= run_single_camera(cam)
		print('Camera %d example complete... \n' % i)

    # Release reference to camera
    # NOTE: Unlike the C++ examples, we cannot rely on pointer objects being automatically
    # cleaned up when going out of scope.
    # The usage of del is preferred to assigning the variable to None.
	del cam

    # Clear camera list before releasing system
	cam_list.Clear()

    # Release system instance
	system.ReleaseInstance()

	input('Done! Press Enter to exit...')
	return result

if __name__ == '__main__':
	main()







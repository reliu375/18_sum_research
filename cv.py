import PySpin as ps
import cv2 as cv

# Procedures to implement
# 1: Decide on an acquisition mode. (Multiframe? Continous?)
# 2: Begin taking image.
# 3: Take an image and display it via openCV
# 4: Let user decide whether to retain the file.
# 5: ...

hackMit = cv.imread('test.jpg', 1) 
cv.imshow('Image 1', hackMit)
key = cv.waitKey(0)
if key == 27:
  cv.destroyAllWindows()
elif key == ord('s'):
  cv.imwrite('HackMIT.jpg', hackMit)
  cv.destroyAllWindows()

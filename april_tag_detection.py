from dt_apriltags import Detector
import numpy
import cv2
def detect_tag(img):
    cameraMatrix = numpy.array([ 1060.71, 0, 960, 0, 1060.71, 540, 0, 0, 1]).reshape((3,3))
    camera_params = ( cameraMatrix[0,0], cameraMatrix[1,1], cameraMatrix[0,2], cameraMatrix[1,2] )
    at_detector = Detector(families='tag36h11',
                        nthreads=1,
                        quad_decimate=1.0,
                        quad_sigma=0.0,
                        refine_edges=1,
                        decode_sharpening=0.25,
                        debug=0)
    l = []
    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    tags = at_detector.detect(img, True, camera_params, tag_size = 0.1)
    for tag in tags:
        for idx in range(len(tag.corners)):
            cv2.line(color_img, tuple(tag.corners[idx - 1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)), (0, 255, 0))
            cv2.circle(color_img, (int(tag.center[0].item()),int(tag.center[1].item())), 50, (0, 0, 255), 2)
        l.append((tag.pose_t, tag.pose_R))
    return l
    
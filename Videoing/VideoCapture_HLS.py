# organize imports
import numpy as np
import cv2

# This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_HLS = cv2.VideoWriter('output_hls.avi', fourcc, 20.0, (640, 480))
out_org = cv2.VideoWriter('output_one.avi', fourcc, 20.0, (640, 480))
# loop runs if capturing has been initialized.
while True:
    # reads frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()

    # Converts to HLS color space, OCV reads colors as BGR
    # frame is converted to HLS
    HLS = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

    # output the frame
    out_HLS.write(HLS)

    # The original input frame is shown in the window
    cv2.imshow('Original', frame)

    # The window showing the operated video stream
    cv2.imshow('HLS stream', HLS)

    # Wait for 'a' key to stop the program
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the output
out_HLS.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

import os
import sys
import torch

from face_detection import RealTimeFaceDetector


if __name__ == '__main__':
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Running model on: {device.upper()}')

    rtfd = RealTimeFaceDetector(device=device)

    if len(sys.argv) > 1:  # video mode
        in_path = sys.argv[1]
        if os.path.isfile(in_path):
            rtfd.infer_landmarks_of_video(in_path=in_path)
        else:
            print("Please provide a valid video file path. Exiting ...")
    else:  # camera mode
        rtfd.infer_landmarks_of_video()

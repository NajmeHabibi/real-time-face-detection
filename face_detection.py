from pathlib import Path
import cv2
import face_alignment

from utils import timeit


class RealTimeFaceDetector:
    def __init__(self, device):
        self.model, model_load_time = self._initialize_model(device)
        print(f'Model load time: {model_load_time}')

        self.save_path = './output'
        Path(self.save_path).mkdir(parents=True, exist_ok=True)

    @timeit
    def _initialize_model(self, device):
        return face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device=device)

    @timeit
    def infer_landmarks(self, frame):
        frame_width, frame_height = frame.shape[:2]

        preds = self.model.get_landmarks_from_image(frame) or []
        for face in preds:
            for coordinate in face:
                row, col = int(coordinate[0]), int(coordinate[1])

                if 0 < row < frame_height and 0 < col < frame_width:
                    cv2.circle(frame, (row, col), 2, (0, 0, 255))

        return frame

    def _video_fps(self, video_capture):
        major_ver, minor_ver, subminor_ver = cv2.__version__.split('.')
        fps = video_capture.get(cv2.cv.CV_CAP_PROP_FPS) if int(major_ver) < 3 else video_capture.get(cv2.CAP_PROP_FPS)
        return fps

    def infer_landmarks_of_video(self, in_path=0, save_path=None):
        if save_path is None:
            in_name = 'camera' if in_path == 0 else in_path.split('/')[-1].split('.')[0]
            save_path = f'{self.save_path}/{in_name}.mp4'

        # initialized video capture
        video_capture = cv2.VideoCapture(in_path)
        if not video_capture.isOpened():
            print("Unable to access the camera/video")
            return
        else:
            print("Access to the camera/video was successfully obtained")

        # initialize output writer
        width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
        height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
        input_fps = self._video_fps(video_capture)
        print(f'Setting write fps equal to the input capture fps: {input_fps}')
        writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), input_fps, (width, height))

        i = 0  # loop counter (frame id)
        fps_sum = 0
        while video_capture.isOpened():  # capture loop
            # Capture frame-by-frame
            success, frame = video_capture.read()
            if not success:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # infer and apply landmarks on the frame
            frame, dt = self.infer_landmarks(frame)

            # logging performance measures
            fps = 1 / dt
            fps_sum += fps
            log = f'FPS={fps:.3f}, Avg FPS={fps_sum / (i + 1):.3f}'
            print(f'Frame[{i + 1}]: {log}')

            # putting FPS on the frame
            cv2.putText(frame, log, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 1, cv2.LINE_AA)

            # Display the resulting frame
            cv2.imshow("Face Detector - to quit press ESC or Q", frame)

            # write the frame on save_path
            writer.write(frame)

            # Exit with ESC or q
            key = cv2.waitKey(10)
            if key % 256 == 27 or (key & 0xFF) == ord('q'):
                print('Exiting ...')
                break

            # update the loop counter
            i += 1

        writer.release()
        video_capture.release()
        cv2.destroyAllWindows()

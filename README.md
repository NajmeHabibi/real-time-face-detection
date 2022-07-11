## Real-time face landmarks detection using face-alignment library and opencv
In this Project we used [face-alignment](https://github.com/1adrianb/face-alignment) library and opencv to detect face landmarks on a realtime/offline video. One can use either camera (realtime) or an input video (offline) to do the inference.  

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/42568062/178320643-884ee84a-e351-4732-9a53-5d4e1008aaeb.gif)

### How to run
Instructions to run in linux bash: 
* Having the environment ready:
  * Using conda
    * `conda create -n rtfd_env python=3.9`
    * `conda activate rtfd_env`
  * Using pip
    * `virtualenv -p python3.9 rtfd_env`
    * `source rtfd_env/bin/activate`
* Install dependencies:
  * Using conda
    * `conda install pytorch torchvision cudatoolkit=11.3 -c pytorch` (See [pytorch](https://pytorch.org/get-started/locally/) installation guide)
    * `conda install -c 1adrianb face_alignment` (see [face-alignment](https://github.com/1adrianb/face-alignment) Github repo)
  * Using pip
    * `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113`
    * `pip install face_alignment`
* Run:
  * Inference from camera: `python main.py` 
  * Inference from an input video: `python main.py ./input/v1.MP4`
  
(Alternatively, one can use `run.sh` as a stand-alone script to do the above)
 

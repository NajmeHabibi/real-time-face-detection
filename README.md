## Real-time face landmarks detection using face-alignment library
In this Project we used [face-alignment](https://github.com/1adrianb/face-alignment) library to detect face landmarks on a realtime video. You can use either camera or a video to do the inference.  

<img width="642" alt="Screen Shot 2022-07-11 at 12 24 49 PM" src="https://user-images.githubusercontent.com/42568062/178312052-730ce22e-9f10-461d-aeab-9b5c547de8af.png">

### How to run
Instructions to run from bash in linux:
* Having the environment ready:
  * Using conda
    * `conda create -n rtfd_env python=3.9`
    * `conda activate rtfd_env`
  * Using pip
    * `virtualenv -p python3.9 rtfd_env`
    * `source rtfd_env/bin/activate`
* Install dependencies:
  * Using conda
    * `conda install pytorch torchvision cudatoolkit=11.3 -c pytorch` (See pytorch [instalation guide](https://pytorch.org/get-started/locally/))
    * `conda install -c 1adrianb face_alignment` (see face-alignment [Github repo](https://github.com/1adrianb/face-alignment))
  * Using pip
    * `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113`
    * `pip install face_alignment`
* Run:
  * Infrence from camera: `python main.py` 
  * Inference from an input video: `python main.py ./input/v1.MP4`

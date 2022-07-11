## Face landmarks detection using face_alignment library

### Run:
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
    * `conda install pytorch torchvision cudatoolkit=11.3 -c pytorch` (See pytorch)
    * `conda install -c 1adrianb face_alignment`
  * Using pip
    * `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113`
    * `pip install face_alignment`
* Run:
  * Either do `python main.py` to detect face landmarks from device camera in realtime, 
  * or `python main.py ./input/v1.MP4` to do the inference from an input video passed as the first argument to main.py



# mask-detector
Open-CV project that detects if the person has a face covering or not

## Installation
Download the repo

I suggest to create a virtual env:
If you want to do so follow below steps:

```python
pip install virtualenv
cd <project_folder>
virtualenv venv
```

Assuming you are still in project directory

```python
venv/Scripts/activate
```
This will activate the virtual environment

Run the below command to install the dependencies

```python
pip install requirements.txt
```

## Scripts

- create_data.py : Iterates over a video and extract frames as images to train the model on
- detect_mask_image.py : Pass a single static image to see if the faces in the image have face coverings
- detect_mask_video.py : Runs a video stream and detect mask covering in real time
- train_mask_detector.py : The actual training of the model

## Data

To add your own face data
- Create a 20 second video of yourself *with* and *without* mask
- Place them in a folder of your name in the `dataset` directory in the respective folders
- Run the `create_data.py` script on both the videos
- Run the model file to make the model train on the newly added data

## Usage

```python
# give the path to the video before running
python create_data.py

# Trains and creates the the model
python train_ask_detector.py -d <path/to/dataset>

# Pops up a window with results
python detect_mask_image.py -i <path/to/test_image>

# Pops up a window with live stream
python detect_mask_video.py
```

## Model

The developed model is an improvement on the **MobileNetV2** model of the **`tensorflow`** library

## License
[MIT](https://choosealicense.com/licenses/mit/)

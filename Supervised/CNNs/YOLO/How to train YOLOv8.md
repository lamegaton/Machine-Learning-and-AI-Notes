# How to train YOLOv8
This tutorial will show you how to train or in another word transfer learning the pretrained weight `.pt`

# Install the repo using WSL
> pip install ultralytics

# Get your dataset

These are my togo places to get dataset
1. https://universe.roboflow.com/
2. https://www.kaggle.com/datasets/

# Prepare `.yaml` config file

Let say our project is located at `pipe` folder and below is the structure of it.

```
/pipe
- yolov8_pipe.yaml
- train/
- valid
```

This is how my train folder looks like:

```
pipe/train$ tree | head -n 10
.
├── 0_jpg.rf.13123a2e88dbf811cf2aa783c13b504b.jpg
├── 0_jpg.rf.13123a2e88dbf811cf2aa783c13b504b.txt
├── 0_jpg.rf.2a1a5092988313adc7b2eeca735b5001.jpg
├── 0_jpg.rf.2a1a5092988313adc7b2eeca735b5001.txt
...
```
Valid folder is also similar. All annotations and name should match each other. After gathering all train and valid set, we can setup config file .yaml


```yaml
path: /path/to/pipe
train: 'train/'
val: 'valid/'
 
# class names
names: 
  0: 'pipe'
```
In the example above, I have only one class pipe to detect. To start training we can execute: 
> yolo task=detect mode=train model=yolov8s.pt imgsz=416 data=yolov8_pipe.yaml epochs=50 batch=16 name=yolov8s_v8_pipe

YOLOv8n is the lightest version compare to the others, so I decided to use it for mobile devices.

After your training is completed, you can detect an image with the below command
> yolo predict task=detect model=weights/best_saved_model/best_float16.tflite imgsz=416 source=pipe5.jpg


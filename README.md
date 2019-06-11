# SAMaskRCNN
Image and Semantic Segmentation by Mask RCNN

## Demo of the KITTI Vision Benchmark Suite

<p align="center">
  <img src="./videos/kitti_demo.gif">
</p>

## Setup

```
pip install -r requirements.txt
```

## Usage

Folder structure:  

```
    SAMaskRCNN
    ├── images
    │  ├── 0001
    │  │    ├── data      # Store your images in here 
    │  │    └── results   # Is created during predict.py
    .  .
    .  .
    .  .
```

Execute:  

```
python predict.py --weights mask_rcnn_model.h5 --label coco_labels.txt --images images/0001/
python make_video.py --images images/0001/
```

# SAMaskRCNN
Image and Semantic Segmentation by Mask RCNN

## Demo of the KITTI Vision Benchmark Suite

<p align="center">
  <img src="./kitti_demo.gif">
</p>

## Setup

```
git clone https://github.com/appinho/SAMaskRCNN.git
wget -O file https://drive.google.com/file/d/1ZyfpW2iaZvVNBxVAcb8DW0nBY2iXtSay/view?usp=sharing
pip install -r requirements.txt
```

## Usage

Folder structure:  

```
    SAMaskRCNN
    ├── images              # Folder of images 
    ├── results             # Folder of resulting images after executing predict.py
    ├── mask_rcnn_model.h5  # Neural network parameter file
```

Execute:  

```
python predict.py --weights mask_rcnn_model.h5 --label coco_labels.txt --images images/0001/
python make_video.py --images images/0001/
```

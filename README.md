# SAMaskRCNNKitti
Image and Semantic Segmentation by Mask RCNN of the KITTI Vision Benchmark Suite

## Demo

<p align="center">
  <img src="./demo.gif">
</p>

## Usage

Run following command where images point to a directory in which the images are stored in a `data` subfolder and a resulting folder `results` is created:  

```
python predict.py --weights mask_rcnn_model.h5 --label coco_labels.txt --images images/0001/
python make_video.py --images images/0001/
```

```
    SAMaskRCNNKitti
    ├── images
    │  ├── 0001
    │  │    ├── data 
    │  │    └── results
    .  .
    .  .
    .  .
```

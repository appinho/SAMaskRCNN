# SAMaskRCNNKitti
Image and Semantic Segmentation by Mask RCNN of the KITTI Vision Benchmark Suite

## Demo
## Usage

Run following command where images point to a directory in which the images are stored in a `data` subfolder and a resulting folder `results` is created:  

```
python maskrcnn_predict.py --weights mask_rcnn_model.h5 --label coco_labels.txt --images images/0001/
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

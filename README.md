# SapFruitNet

Official implementation accompanying the manuscript:

**Dynamic estimation of individual *Sapindus mukorossi* Gaertn. fruit counts using multi-temporal drone imagery and deep learning**

## Overview

SapFruitNet is a density-regression-based deep learning framework developed for fruit counting in individual *Sapindus mukorossi* trees from UAV RGB imagery under complex field conditions. The workflow covers UAV image preprocessing, density-map generation, model training, patch-based inference, quantitative evaluation, and density-map visualization.

## Main Features

* UAV-based fruit counting under heterogeneous forest-canopy backgrounds.
* Density-regression-based estimation for small, clustered, and partially occluded fruits.
* Patch-based inference for high-resolution UAV images.
* Visualization of predicted and ground-truth density maps.
* Reproducible training and evaluation scripts.

## Environment

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Dataset Preparation

The dataset used in this study consists of UAV RGB images of *S. mukorossi* trees acquired under different phenological stages, imaging scales, fruit densities, illumination conditions, and canopy backgrounds.

Before training:

1. Prepare the original UAV images and point annotations.
2. Generate the corresponding ground-truth density maps.
3. Split the dataset into training, validation, and test subsets at the original-image level.
4. Apply data augmentation only to the training subset.
5. Update dataset paths in the training and testing scripts.

## Training

```bash
python scripts/train.py
```

Best checkpoint used in the manuscript:

```text
best\_model\_mae-7.50\_epoch-1776.pth
```

## Testing

```bash
python scripts/test.py
```

For high-resolution UAV images, patch-based inference can be used to obtain final density maps and fruit-count estimates.

## Visualization

```bash
python scripts/visualize\_density.py
```

Save visual outputs under:

```text
results/
```

## Experimental Results

|Method|MAE|RMSE|
|-|-:|-:|
|CAN|26.75|37.77|
|CSRNet|16.94|23.82|
|DM-Count|10.43|18.34|
|**SapFruitNet**|**7.50**|**12.57**|

## Dataset and Pretrained Model

The dataset and the best-performing SapFruitNet model checkpoint used in this study are available at the following links.

### Dataset

The dataset used for model training and evaluation can be downloaded from:

- **Baidu Netdisk:** https://pan.baidu.com/s/1Z4eh_S5AkJruwMEQR7IpWQ
- **Extraction code:** `94de`

### Pretrained Model

The best-performing SapFruitNet checkpoint (`best_model_mae-7.50_epoch-1776.pth`) can be downloaded from:

- **Baidu Netdisk:** https://pan.baidu.com/s/1ZqwM0Icov_5SCHbCCneqFw
- **Extraction code:** `w79r`

The pretrained model can be used for model evaluation and fruit-density-map prediction following the instructions provided in the Testing section.

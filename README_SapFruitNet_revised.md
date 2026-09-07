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

## Recommended Repository Structure

```text
SapFruitNet/
├── sapfruitnet/
│   ├── models/                 # Network architectures and model components
│   ├── losses/                 # Loss functions
│   └── utils/                  # Common utilities
├── data\_processing/
│   ├── preprocessing/          # Dataset preprocessing scripts
│   └── density\_maps/           # Density-map generation utilities
├── scripts/
│   ├── train.py                # Model training
│   ├── test.py                 # Model evaluation / patch-based inference
│   └── visualize\_density.py    # Density-map visualization
├── checkpoints/                # Trained model weights
├── results/                    # Predictions and evaluation outputs
├── assets/                     # README figures
├── requirements.txt
├── .gitignore
└── README.md
```

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

## Recommended `.gitignore`

```gitignore
.idea/
.cache/
\_\_pycache\_\_/
\*.pyc

checkpoints/
results/
output/
vis/

\*.pth
\*.pt
```

## Code Attribution

This implementation was developed for UAV-based *S. mukorossi* fruit counting and includes project-specific modifications to the data-processing, training, inference, and evaluation workflow.

If parts of the implementation were adapted from an existing open-source crowd-counting repository, acknowledge the original repository, associated publication, and software license here. Retain all copyright or license notices required by the original license.

Example:

```text
Parts of this implementation were adapted from \[Original Project/Repository].
We thank the original authors for releasing their code.
```

Replace the placeholder with the exact project name, repository link, citation, and license information before public release.

## Citation

```bibtex
@article{SapFruitNet,
  title   = {Dynamic estimation of individual Sapindus mukorossi Gaertn. fruit counts using multi-temporal drone imagery and deep learning},
  author  = {Shao, Wenhao and others},
  journal = {To be updated},
  year    = {To be updated}
}
```

## License

Add a `LICENSE` file that is compatible with any upstream code used in this repository. If the implementation contains adapted third-party code, follow the attribution and redistribution requirements of the corresponding license.


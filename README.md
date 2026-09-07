# SapFruitNet: Simplifying and Improving Crowd Counting with Transformer(Code reproduction)
* Code reproduction

## Overview
* Presentate only the experiment on dataset ShanghaiTech Part A 
* ShanghaiTech Part A 

| Code      | MAE   | MSE      |
|-----------|-------|-------|
| PAPER     | 54.8  | 86.6  |
| This code | 54.20 | 88.97 |

Our code reaches this result with the standard hyperparameter set in code. Trained with batch-size=8 for around 2000 epoch(as said in the paper). Best validation at around epoch 1700
# code framework

# Training
Take a look at the arguments accepted by ```train.py```
* update root "data-dir" in ./train.py.
* load pretrained weights of ImageNet-1k in ./Networks/ALTGVT.py.
* pretrained weights 
* [new] Added [wandb](https://wandb.ai/) integration. If you want to log with wandb, set ```--wandb 1``` in ```train.py``` after having logged in to wandb (```wandb login``` in console)
* launch with ```python train.py```

# Testing
* python test_image_patch.py
* Due to crop training with size of 256x256, the validation image is divided into several patches with size of 256x256, and the overlapping area is averaged.
* The pretrained model best_model_mae-7.50_epoch-1776
# Visualization
* python vis_densityMap.py
* save to ./vis/part_A_final


*Download address of the original data set（https://pan.baidu.com/s/1Z4eh_S5AkJruwMEQR7IpWQ 提取码: 94de）
*SapFruitNet's best model link: https://pan.baidu.com/s/1ZqwM0Icov_5SCHbCCneqFw  提取码:w79r

# Environment
	See requirements.txt
	



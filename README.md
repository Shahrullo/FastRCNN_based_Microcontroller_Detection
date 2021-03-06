# FastRCNN based Microcontroller Detection
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/test_predictions/4.jpg)

## Approach:
  * We trained custom object detection model by applying pre-trained PyTorch Faster RCNN model
  * Microcontroller Detection dataset [from Kaggle](https://www.kaggle.com/tannergi/microcontroller-detection) is applied 
  * New images are tested at last, showing the inference of model
  * Model can be trained on terminal, not Jupyter Notebook

# How to use:
## To Train
```  
  1. Dowload or clone the repo
  2. pip install requirements
  3. cd src
  4. python train.py
```

## To Test
You can test the model after training on any new image source
```
  python inference.py
```

# Results
## Train and Validation Loss
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/outputs/train_loss_100.png)
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/outputs/valid_loss_100.png)

## Detected objects
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/test_predictions/1.jpg)
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/test_predictions/3.jpg)
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/test_predictions/4.jpg)
![](https://github.com/Shahrullo/FastRCNN_based_Microcontroller_Detection/blob/main/test_predictions/8.jpg)

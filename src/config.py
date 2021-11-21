import torch

BATCH_SIZE = 4
RESIZE_TO = 512 # resize the image accordingly
NUM_EPOCHS = 100

DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

TRAIN_DIR = 'C:\\Users\\Shahrullohon\\Desktop\\all\\Computer Vision with Pytorch\\Microcontroller_Detection\\datasets\\train'
VALID_DIR = 'C:\\Users\\Shahrullohon\\Desktop\\all\\Computer Vision with Pytorch\\Microcontroller_Detection\\datasets\\test'

CLASSES = [
    'background', 'Arduino_Nano', 'ESP8266', 'Raspberry_Pi_3', 'Heltec_ESP32_Lora'
]
NUM_CLASSES = 5

VISUALIZE_TRANSFORMED_IMAGES = False

OUT_DIR = '../outputs'
SAVE_PLOTS_EPOCH = 2
SAVE_MODEL_EPOCH = 2
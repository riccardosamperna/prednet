# Where KITTI data will be saved if you run process_kitti.py
# If you directly download the processed data, change to the path of the data.
DATA_DIR = './ego_data/'

# Where model weights and config will be saved if you run kitti_train.py
# If you directly download the trained weights, change to appropriate path.
WEIGHTS_DIR = './ego_model_data/'

# Where results (prediction plots and evaluation file) will be saved.
RESULTS_SAVE_DIR = './ego_results/'

# Decide if you want to use the original dataset or the dataset with augmented training set (+ noise)
NOISE = 0

# Noise ratio of added random noise samples to training set
NOISE_RATIO = 0.1
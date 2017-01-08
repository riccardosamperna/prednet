# Where EgoHands data are saved when you run download_ego.sh
DATA_DIR = './ego_data/'

# Where model weights and config will be saved if you run ego_train.py
# If you directly download the trained weights, change to appropriate path.
WEIGHTS_DIR = './ego_model_data/'

# Where results (prediction plots and evaluation file) will be saved.
RESULTS_SAVE_DIR = './ego_results/'

# Decide if you want to use the dataset with (NOISE = 1)/ without (NOISE = 0) noise in the training set
NOISE = 0

# Noise ratio of added random noise samples to training set
NOISE_RATIO = 0.1
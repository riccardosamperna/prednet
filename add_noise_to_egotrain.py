import os
import numpy as np
from scipy.misc import imread, imresize
import hickle as hkl
from ego_settings import *

NOISE_RATIO = 0.1

train_file = os.path.join(DATA_DIR, 'X_train.hkl')
train_sources = os.path.join(DATA_DIR, 'sources_train.hkl')

X_train = hkl.load(train_file);
sources_train = hkl.load(train_sources);

noise_size = int(X_train.shape[0] * NOISE_RATIO)

if (noise_size): # check if noise_size is not zero
    X_train_wn = np.zeros(((X_train.shape[0] + noise_size), 128, 160, 3))
    noise_samples = np.random.rand(noise_size,128,160,3) * 255
    noise_samples = noise_samples.astype('uint8')
    for i in range(X_train.shape[0]):
        X_train_wn[i] = X_train[i]
    for j in range(noise_samples.shape[0]):
        X_train_wn[i + j + 1] = noise_samples[j]

    sources_train.extend(['noise'] * n_noise_samples) # assign a source also to noise samples

    hkl.dump(X_train_wn, os.path.join(DATA_DIR, 'X_train_wn.hkl'))
    hkl.dump(sources_train, os.path.join(DATA_DIR, 'sources_train_wn.hkl'))


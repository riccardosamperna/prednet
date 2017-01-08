# Adaptation of process_kitty.py file to work with the new dataset

import os
import numpy as np
from scipy.misc import imread, imresize
import hickle as hkl
from ego_settings import *

desired_im_sz = (128, 160)
games = ['cards', 'chess', 'jenga', 'puzzle']

# Recordings used for validation and testing.
val_recordings = [('cards', 'courtyard_B_T')]
test_recordings = [('cards', 'office_B_S'), ('chess', 'livingroom_H_T'), ('jenga', 'office_H_T'), ('puzzle', 'livingroom_H_S')]

# Create image datasets.
# Processes images and saves them in train, val, test splits.
def process_data():
    splits = {s: [] for s in ['train', 'test', 'val']} # creates a 3 key(games)-values(empty) correspondance 
    splits['val'] = val_recordings
    splits['test'] = test_recordings
    not_train = splits['val'] + splits['test']  
    for g in games: 
        g_dir = os.path.join(DATA_DIR, g + '/')
        _, folders, _ = os.walk(g_dir).next()
        splits['train'] += [(g, f) for f in folders if (g, f) not in not_train]

    for split in splits:
        im_list = []
        source_list = []  # corresponds to recording that image came from
        for game, folder in splits[split]:
            im_dir = os.path.join(DATA_DIR, game + '/', folder + '/')
            _, _, files = os.walk(im_dir).next()
            im_list += [im_dir + f for f in sorted(files)[1::3]] #downsample this dataset from 30 to 10 frames a sec
            source_list += [game + '-' + folder] * len(files[1::3])

        print 'Creating ' + split + ' data: ' + str(len(im_list)) + ' images'
        X = np.zeros((len(im_list),) + desired_im_sz + (3,), np.uint8)
        for i, im_file in enumerate(im_list):
            im = imread(im_file)
            X[i] = process_im(im, desired_im_sz)

        hkl.dump(X, os.path.join(DATA_DIR, 'X_' + split + '.hkl'))
        hkl.dump(source_list, os.path.join(DATA_DIR, 'sources_' + split + '.hkl'))


# resize and crop image
def process_im(im, desired_sz):
    target_ds = float(desired_sz[0])/im.shape[0]
    im = imresize(im, (desired_sz[0], int(np.round(target_ds * im.shape[1]))))
    d = (im.shape[1] - desired_sz[1]) / 2
    im = im[:, d:d+desired_sz[1]]
    return im

if __name__ == '__main__':
    process_data()
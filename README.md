# A closer look to the "PredNet": investigation of human attention mechanism on artificial neural networks

## prednet

Code and models accompanying [Deep Predictive Coding Networks for Video Prediction and Unsupervised Learning] (https://arxiv.org/abs/1605.08104) by Bill Lotter, Gabriel Kreiman, and David Cox.

The PredNet is a deep recurrent convolutional neural network that is inspired by the neuroscience concept of predictive coding (Rao and Ballard, 1999; Friston, 2005).
**Check out example prediction videos [here] (https://coxlab.github.io/prednet/).**

The architecture is implemented as a custom layer<sup>1</sup> in [Keras] (http://keras.io/). Tested on Keras 1.0.7 with [theano] (http://deeplearning.net/software/theano/) backend and Python 2.7.
See http://keras.io/ for instructions on installing Keras and its list of dependencies.
For Torch implementation, see [torch-prednet] (https://github.com/e-lab/torch-prednet).

(Text cited directly from Github repository of original project: https://github.com/coxlab/prednet)

<br>

## EgoHands Experiment

Almost all new files in this forked repository are slight adaptations of the original code and follows the same name convention. In this experiment I trained the model on the EgoHands dataset: http://vision.soic.indiana.edu/projects/egohands/, with and without additional noise in the training set. The aim of the project was to investigate the ability of the neural network to filter relevant information (comparable to human attention mechanism). In order to reproduce the experiment please read carefully below.

## Setup

The code was tested with Python 2.7, Keras 1.1.1 and Theano 0.8. Please make sure that in Keras configuration file "image_dim_ordering": "th" and "backend": "theano". To run the training on a GPU please read Keras documentation: https://keras.io/getting-started/faq/#how-can-i-run-keras-on-gpu

1. **Download data**
	```bash
	./download_ego.sh
	```
	Run this script inside the prednet folder. This will download the EgoHands dataset (~8 GB) and it will organise the directories in order for the next steps to work properly.
	<br>
	<br>

2. **Process data**
	```bash
	python process_ego.py
	```
	This will process the images, downsampling the videos from 30 to 10 fps and it will crop the images to 128x160 to comply with the neural network input size.
	<br>
	<br>

3. (Optional) **Add noise samples to training set**
	```bash
	python add_noise_to_egotrain.py
	```
	This will add to the training set a number of noisy samples proportional to the NOISE_RATIO adjustable in the ego_settings.py configuration file. (If you are executing this step, please remember to set also the variable NOISE inside ego_settings.py to 1).
	<br>
	<br>
4. **Train the model**
	```bash
	python ego_train.py
	```
	This will train a PredNet model for t+1 prediction. 
<br>

<sup>1</sup> Note on implementation:  PredNet inherits from the Recurrent layer class, i.e. it has an internal state and a step function. Given the top-down then bottom-up update sequence, it must currently be implemented in Keras as essentially a 'super' layer where all layers in the PredNet are in one PredNet 'layer'. This is less than ideal, but it seems like the most efficient way as of now. We welcome suggestions if anyone thinks of a better implementation.  

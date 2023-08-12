
---
- [Machine Learning and AI Examples](#machine-learning-and-ai-examples)
	- [Status: In Progress](#status-in-progress)
		- [Linear Regression Models](#linear-regression-models)
		- [McCulloch and Pitts](#mcculloch-and-pitts)
		- [Perceptron](#perceptron)
		- [Multilayer Perceptron (MLP) with Backpropagation](#multilayer-perceptron-mlp-with-backpropagation)
		- [Radial Basus Function Network (RBFN)](#radial-basus-function-network-rbfn)
		- [Kohonen’s Self-Organizing Network](#kohonens-self-organizing-network)
		- [Hopfield](#hopfield)
		- [MLP](#mlp)
		- [Convolutional layers](#convolutional-layers)
		- [Recurrent Neural Network](#recurrent-neural-network)
		- [Natural Languague Processing](#natural-languague-processing)
		- [Fuzzy](#fuzzy)
		
---
# Machine Learning and AI Examples

## Status: In Progress

### Linear Regression Models

**Regression**: Mapping inputs to outputs for prediction.
**Classification**: Mapping inputs to categorical outputs for description.

Likelihood refers to the probability of the target given the weight. The maximum likelihood estimate (MLE) is used in multivariable regression.

**Logistic Regression**: Logistic regression is a classification algorithm, not a regression algorithm [1]. One common question is: what are the differences between perceptron and logistic regression? [2]

### McCulloch and Pitts

### Perceptron

The perceptron is an enhanced version of McCulloch and Pitts. It uses the sigmoid activation function instead of a threshold.

Example:

### Multilayer Perceptron (MLP) with Backpropagation

Gradient descent is employed in MLP to update the weights. Having more nodes does not necessarily mean better performance; it can lead to overfitting [5]. MLPs are used in connectionist models [3], where each node represents a neuron, and the weights can be likened to synapses. When the input from a node is multiplied by its weight and passed through the sigmoid function, the information is either fired or transmitted.

Example:

**Note**:
- The derivative of the sigmoid function is relatively small, which can result in the vanishing gradient problem when many layers are used.
- The vanishing gradient problem describes the behavior where all weights become close to 0.


### Radial Basus Function Network (RBFN)
**Characteristic:**
- feedforward NN architecture
- popular kernel in Support Vector Machine (SVM)
- consists of three layers: (1) inputs, (2) hidden, (3) ouputs. 
	- there are no weights between input(s) and hidden layer.
	- there is only one hidden layers
- use Gaussian kernel function as the core. Besides, logistic function is another option.
	- Gaussian kernel has center and width parameters

**Training:**
Step 1: use unsupervised learning (K-means) to get centers and width. 
Step 2: using supervised to adapt the weights. We can use least-squares or gradient method. 

If we want to use RBFN to classify the current dataset, another words, interpolating the data, we can use inverse or psuedo-inverse method to calculate weights.

**Terms**
interpolation: in between the datapoint
extrapolation: beyond the datapoint

StackExchange explains this pretty well with visualization [4]

```
Training procedures:

1. Calculate G by using gausian kernel with input, center, width.

2. Calculate Weight: w=g^-1 dot d
3. Calculate Desired output: d = g dot w

g: gausian kernel

```

Example


### Kohonen’s Self-Organizing Network
**Characteristic:**
- unsupervised learning
- involve competitive learning
- map input to bigger dimension, feature map



### Hopfield 
**Characteristic:**


### MLP 
Fully connected layers is a building block of MLP
All nodes connect to each other then we sum them up and pass through activation function.

### Convolutional layers
Convolution layer using filer or sliding window. 
In communication system, we often convert time domain to frequency domain using FFT (Fast Fouirer Transform).
Then we perform calculation in frequency domain [6]  

**Characteristic:**
- local connectivity: by using sliding window and sum up the results, features are grouped together
- parameter sharing: of the local connectivity, parameters share similar characteristic.

### Recurrent Neural Network

### Natural Languague Processing

### Fuzzy


**References**:  
[1] Deep Learning with Python - Chollet, Francois  
[2] [Link to comparison between logistic regression and perceptron](https://stats.stackexchange.com/questions/162257/whats-the-difference-between-logistic-regression-and-perceptron)  
[3] [Connectionist Models in Cognitive Psychology](https://stanford.edu/~jlmcc/papers/McCCleeremans09CnxMdlsOCC.pdf)  
[4] https://stats.stackexchange.com/a/418814/142439  
[5] https://aws.amazon.com/what-is/overfitting/  
[6] [Application of convolution](https://dspillustrations.com/pages/posts/misc/the-convolution-theorem-and-application-examples.html)  
[7]https://www.deeplearningbook.org/  
[8]http://cs231n.stanford.edu/  
[9]http://neuralnetworksanddeeplearning.com/chap5.html  
[10]https://www.deeplearningbook.org/contents/convnets.html  
[11]https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks  
![unsupervised bot](https://raw.githubusercontent.com/lamegaton/Machine-Learning-and-AI-Examples/08ee1ffa53e0c3c992b62ba0c053107117b75d79/Assets/unsupervised_plain.svg)
---
# Unsupervised learning

### Radial Basis Function Network (RBFN)
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


### Kohonen’s Self-Organizing Network
**Characteristic:**
- unsupervised learning
- involve competitive learning
- map input to bigger dimension, feature map


### Hopfield 
**Characteristic:**
- Mimic human brain's behavior

### Restricted Boltzmann machine (RBM)

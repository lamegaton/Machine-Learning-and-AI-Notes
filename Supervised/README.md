![supervised bot](https://raw.githubusercontent.com/lamegaton/Machine-Learning-and-AI-Examples/b8b14c640610ffa39ee9c1e77d3a33640ac50b4d/Assets/supervised_plain.svg)
---

# Supervised learning

### McCulloch and Pitts model
McCulloch and Pitts model is the foundation of neural network. 


### Perceptron
The perceptron is an enhanced version of McCulloch and Pitts. It uses the sigmoid activation function instead of a threshold.

Example:

### Multilayer Perceptron (MLP) with Backpropagation

Gradient descent is employed in MLP to update the weights. Having more nodes does not necessarily mean better performance; it can lead to overfitting [5]. MLPs are used in connectionist models [3], where each node represents a neuron, and the weights can be likened to synapses. When the input from a node is multiplied by its weight and passed through the sigmoid function, the information is either fired or transmitted.

**Note**:
- The derivative of the sigmoid function is relatively small, which can result in the vanishing gradient problem when many layers are used.
- The vanishing gradient problem describes the behavior where all weights become close to 0.

### Convolutional layers
Convolution layer using filer or sliding window. 
In communication system, we often convert time domain to frequency domain using FFT (Fast Fouirer Transform).
Then we perform calculation in frequency domain [6]  

**Characteristic:**
- local connectivity: by using sliding window and sum up the results, features are grouped together
- parameter sharing: of the local connectivity, parameters share similar characteristic.
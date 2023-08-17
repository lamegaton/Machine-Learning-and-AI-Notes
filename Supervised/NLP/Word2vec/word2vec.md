# word2vec
This is a way to represent relationship of words  

**word2vec** use two methods:  
1. continuous bag of words (CBOW): given context to predict output words  
1. skip-gram: given output word to predict context words  

GloVe and fastText are pretrained models  
Output of softmax can be considered as probability. The sum of it is 1. if you 
remember, sigmoid also map value from 0 to 1; however, sigmoid is used for two class and softmax is used for multiclasses. 

N-Grams: meanig using 1 focus word with N - 1 context words  

Advantages and disadvantage:  
1. Skip-gram: work well with small corpora and rare terms.  
1. CBOW: is faster and has higher accuracies.  


**Good references:**  
https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/  
Natural Language Processing in Action, Second Edition by Hobson Lane, Maria Dyshel  


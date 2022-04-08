# Machine translation

## Machine translation via rotation matrix

Idea: find the matrix that maps the word embeddings of a corpus in a given language to the embeddings of a corpus in a different language. This rotation matrix can then be used to map new words from a language to another.

### Training

1. get the words embeddings for two language corpuses. Each corpus word embedding forms a matrix $M_1$, $M_2$
2. Find the optimal rotation matrix $R$ that approximates $M_2 = M_1 R$. Compute $R$ via gradient descent, optmizing the loss function: $L(R) = {\lVert M_1 R - M_2 \rVert}_{F}^{2}$. The gradient of this function is: $L'(R) = \frac{2}{m} M_1^{T} ( M_1 R - M_2 )$

### Prediction

Compute translations for new words $w_1$ by finding the nearest neigbors of the corresponding predicted mappings $w_1 R$.

You can improve prediction performance by using the [locality sensitive hasing tecnique](misc.html#Locality-sensitive-hashing)
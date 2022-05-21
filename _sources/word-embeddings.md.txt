# Word Embeddings

## Window-base co-occurrence matrix

Steps:
- compute the co-occurrence matrix $ X $.
- Apply SVD on X to get $SVD(X) = USV$
- Select the first $k$ columns of $U$ to get a $k$-dimensional word-embedding matrix
- The ratio between the sum of the eigenvalues corresponding to the selected vectors and the sum of all eigenvalues can be interpreted as the explained variance of those vectors.

Issues:
- the dimensions of the co-occurrence matrix vhange very often
- The matrix $X$ is sparse
- Quadratic cost to train
- Requires the incorporation of some hacks on $X$ to account for the drastic imbalance in the word frequency

## Word2Vec

Word2Vec is a one-hidden-layer no-bias encoder-decoder network in which the hidden layer paramters' matrix represents the word embeddings.

The objective function used is based on the dot-product between the context words embeddings (the hidden layer parameters) and the center words embeddings (the outer layer parameters).

These products are turned into a probability distribution via the softmax activation function.

2 algorithms:
- Continuous bag-of-words: predict a center word from the surrounding countext in terms of word vectors
- Skip-gram: predict the distribution of context words from the center word

Given a training corpus:
- Compute the windows over the corpus sentences
- Compute the pairs (center word, target word)

2 training methods:
- negative sampling: instead of performing backpropagation over the entire vocabulary, sample several negative vectors 
- hierarchical softmax


## Glove

The advantage of GloVe is that, unlike Word2vec, GloVe does not rely just on local statistics (local context information of words), but incorporates global statistics (word co-occurrence) to obtain word vectors.

## Model evaluation

Intrinsic evaluation methods:
- Word vector analogies (semantic, syntactic)
- Word vector distances and their correlation with human judgments

Extrinsic evaluation methods:
- Named entity recognition

Insights:
- Performance is lower for extremely low dimensional word vectors
- Performance increases with larger corpus size
- Performance is heavily dependent on the model used for word embedding
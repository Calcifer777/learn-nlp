# Stanford cs224n

## Resources

- [Home page](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/)
- [Lectures](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ)

### Readings

#### 1: Word Vectors 

- [x] [word2vec paper](https://arxiv.org/pdf/1301.3781.pdf)
- [x] [negative sampling paper](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)

Additional readings:
- [ ] [SLP ch6](https://web.stanford.edu/~jurafsky/slp3/6.pdf)
- [ ] [Medium - Word embedding](https://medium.com/data-science-group-iitr/word-embedding-2d05d270b285)
- [ ] [SVD](https://davetang.org/file/Singular_Value_Decomposition_Tutorial.pdf)
- CS168 SVD
    - [ ] [7](https://web.stanford.edu/class/cs168/l/l7.pdf)
    - [ ] [8](http://theory.stanford.edu/~tim/s15/l/l8.pdf)
    - [ ] [9](https://web.stanford.edu/class/cs168/l/l9.pdf)
- [ ] [Accessing NLTK corpuses](https://www.nltk.org/book/ch02.html)
- [ ] [Gensim docs](https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.FastTextKeyedVectors.most_similar)
- [ ] [The word analogy testing caveat](https://aclanthology.org/N18-2039.pdf)

Other:
- [Analytics Vidhya - word2vec explained](https://medium.com/analytics-vidhya/maths-behind-word2vec-explained-38d74f32726b)


#### 2: Word Vectors 2 and Word Window Classification

- [Glove paper](https://nlp.stanford.edu/pubs/glove.pdf)
- [Improving Distributional Similarity with Lessons Learned from Word Embeddings](https://aclanthology.org/Q15-1016)
- [Evaluation methods for unsupervised word embeddings](https://aclanthology.org/D15-1036)

Additional readings:
- [A Latent Variable Model Approach to PMI-based Word Embeddings](https://aclanthology.org/Q16-1028/)
- [Linear Algebraic Structure of Word Senses, with Applications to Polysemy](https://transacl.org/ojs/index.php/tacl/article/viewFile/1346/320)
- [On the Dimensionality of Word Embedding](https://proceedings.neurips.cc/paper/2018/file/b534ba68236ba543ae44b22bd110a1d6-Paper.pdf)

#### 3: Backprop and Neural Networks

- [Matrix calculus notes](http://web.stanford.edu/class/cs224n/readings/gradient-notes.pdf)
- [Review of differential calculus](http://web.stanford.edu/class/cs224n/readings/review-differential-calculus.pdf)
- [CS231n notes on network architectures](http://cs231n.github.io/neural-networks-1/)
- [CS231n notes on backprop](http://cs231n.github.io/optimization-2/)
- [Derivatives, Backpropagation, and Vectorization](http://cs231n.stanford.edu/handouts/derivatives.pdf)
- [Learning Representations by Backpropagating Errors](http://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf)

Additional Readings:
- [ ] [Yes you should understand backprop](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b)
- [ ] [Natural Language Processing (Almost) from Scratch](http://www.jmlr.org/papers/volume12/collobert11a/collobert11a.pdf)
- [ ] [Vector, Matrix, and Tensor Derivatives](http://cs231n.stanford.edu/vecDerivs.pdf)

Other:
- [ ] [The softmax function and its derivative](https://eli.thegreenplace.net/2016/the-softmax-function-and-its-derivative/)


#### 4: Dependency parsing

- [Incrementality in Deterministic Dependency Parsing](https://www.aclweb.org/anthology/W/W04/W04-0308.pdf)
- [A Fast and Accurate Dependency Parser using Neural Networks](https://www.emnlp2014.org/papers/pdf/EMNLP2014082.pdf)
- [Dependency Parsing](http://www.morganclaypool.com/doi/abs/10.2200/S00169ED1V01Y200901HLT002)
- [Globally Normalized Transition-Based Neural Networks](https://arxiv.org/pdf/1603.06042.pdf)
- [Universal Stanford Dependencies: A cross-linguistic typology](http://nlp.stanford.edu/~manning/papers/USD_LREC14_UD_revision.pdf)
- [Universal Dependencies website](http://universaldependencies.org/)
- [Jurafsky & Martin Chapter 14](https://web.stanford.edu/~jurafsky/slp3/14.pdf)

$$$$ 5: Recurrent Neural Networks and Language Models

- [N-gram Language Models (textbook chapter)](https://web.stanford.edu/~jurafsky/slp3/3.pdf)
- [On Chomsky and the Two Cultures of Statistical Learning](http://norvig.com/chomsky.html)
- [The Unreasonable Effectiveness of Recurrent Neural Networks (blog post overview)](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
- [Sequence Modeling: Recurrent and Recursive Neural Nets (Sections 10.1 and 10.2)](http://www.deeplearningbook.org/contents/rnn.html)

Additional readings:
- [RNN from scratch](https://github.com/topics/backpropagation-through-time)

#### 6: Vanishing Gradients, Fancy RNNs, Seq2Seq

- [Sequence Modeling: Recurrent and Recursive Neural Nets (Sections 10.3, 10.5, 10.7-10.12)](http://www.deeplearningbook.org/contents/rnn.html)
- [Learning long-term dependencies with gradient descent is difficult (one of the original vanishing gradient papers)](http://www.comp.hkbu.edu.hk/~markus/teaching/comp7650/tnn-94-gradient.pdf)
- [On the difficulty of training Recurrent Neural Networks (proof of vanishing gradient problem)](https://arxiv.org/pdf/1211.5063.pdf)
- [Vanishing Gradients Jupyter Notebook (demo for feedforward networks)](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/lectures/vanishing_grad_example.html)
- [Understanding LSTM Networks (blog post overview)](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)


#### 7: Final Projects: Custom and Default; Practical Tips

- [Practical methodology](https://www.deeplearningbook.org/contents/guidelines.html)

#### 8: Transformers

- [Project Handout (IID SQuAD track)](http://web.stanford.edu/class/cs224n/project/default-final-project-handout-squad-track.pdf)
- [Project Handout (Robust QA track)](http://web.stanford.edu/class/cs224n/project/default-final-project-handout-robustqa-track.pdf)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762.pdf)
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Transformer (Google AI blog post)](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
- [Layer Normalization](https://arxiv.org/pdf/1607.06450.pdf)
- [Image Transformer](https://arxiv.org/pdf/1802.05751.pdf)
- [Music Transformer: Generating music with long-term structure](https://arxiv.org/pdf/1809.04281.pdf)


## Other

- [Solutions](https://github.com/fullpower/CS224N-2022)

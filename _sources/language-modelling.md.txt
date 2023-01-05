# Language modelling

## Use cases

- Text summarization
- Translation
- Information extraction
- Dialogue systems

## Basic problems

- Tagging (part of speech tagging, named entity recognition)
- Parsing
- Ambiguity (syntactic, semantic, acousitc, discourse)

## N-gram models

N-gram models define a language model as a Markov process of order N. A common value for N is 3, which yields the **trigram** model.

## Perplexity

Given the (log)likelihood of a sentence defined as:

$l = log_{2}{\prod{p(x_i)}} = \sum{\log_{2}{p(x_i)}}$

, **perplexity** is defined as:

$P = 2^{-\frac{1}{N}l}$

## Estimation techniques

### Linear interpolation

Given the maximum likelihood estimator (in this case of a trigram model):

$q_{ML}(w_i | w_{i-1}, w_{i-2}) = \frac{count(w_i, w_{i-1}, w_{i-2})}{count(w_{i-1}, w_{i-2})}$

the linear interpolation estimator is defined as:

$q(w_i | w_{i-1}, w_{i-2}) = \lambda_{1}q_{ML}(w_i | w_{i-1}, w_{i-2}) + \lambda_{2}q_{ML}(w_i | w_{i-1}) + \lambda_{3}q(w_i)$ 

with $\sum{\lambda_i = 1}$

#### Estimation

Hold out part of training set as “validation” data

Define $c'(w1, w2, w3)$ to be the number of times the trigram $(w1, w2, w3)$ is seen in the validation set

Solve:

$max_{\lambda_{1}, \lambda_{2}, \lambda_{3}} L(\lambda_{1}, \lambda_{2}, \lambda_{3}) = \sum{c'(w_{1}, w_{2}, w_{3}) log\{q(w_{3} | w_{2}, w_{3})\}}$

such that:

$\lambda_{1}, \lambda_{2}, \lambda_{3} = 1$, and $\lambda{i} \gt 0 \forall i$

where:

$q(w_{i} | w_{i−2}, w_{i−1}) = \lambda{1} \cdot q_{ML}(w_{i} | w_{i−2}, w_{i−1}) + \lambda{2} \cdot q_{ML}(w_i | w_{i−1}) + \lambda{3} × q_{ML}(w_i)$

Linear interpolation can be extended by making the $\lambda$ coefficients vary with the frequency of $w_{i-1}, w_{i-2}$, that is.

### Discounting models
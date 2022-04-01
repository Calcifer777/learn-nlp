# Sentiment analysis

## Logistic regression 

- Preprocess the dataset
- For each sentence, compute a vector of $n+1$ elements, where $n$ is the number of categories you want to classify. The $n+1$ element is the bias vector
  - each feature vector represents the frequency of each token for the $nth$ category
- Use a logistic regression for predicting the category of new sentences

## Naive Bayes

[Blog](https://medium.com/analytics-vidhya/sentiment-analysis-with-na%C3%AFve-bayes-131bdc1737e3)

- Preprocess the dataset
- For each sentence, compute a vector of $n+1$ elements, where $n$ is the number of categories you want to classify. The $n+1$ element is the bias vector
  - Each feature vector represents the relative frequency of each token, corrected with *Laplacian smoothing*, that is:

$P(w_i|class) = \frac{freq(w_i|c_i)+1}{|{Class}_i + |Vocabulary|}$
- Predict new sentences with:

$log\{\frac{P(pos)}{P(neg)} \cdot \prod_{i}{\frac{P(w_i|pos)}{P(w_i|neg)}} \} = \log{\frac{P(pos)}{P(neg)}} \cdot \sum_{i}{\log{\frac{P(w_i|pos)}{P(w_i|neg)}}} \lessgtr 0$

### Naive Bayes Assumptions

- Independence between the predictors or features associated with each class:  this will lead to potentially under or over estimates the conditional probabilities of individual words by class
- Relative frequencies in corpus, especially affecting the validation set: Assuming the reality behaves as our “balanced” training dataset would result in a very optimistic or very pessimistic model

### Causes of errors

- Processing as a source of errors
    - Removing punctuation can represent a different meaning
    - Removing words
- Word order can affect a sentence sentiment
- Adversarial attacks
    - sarcasm
    - irony
    - euphemisms

## Vector space models




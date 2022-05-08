# NLP Applications

## Question answering

## Text generation

### Use cases

- Machine translation
- Dialogue systems
- Summarization (document, e-mail, meeting, scholastic papers)
- Data to text
- Visual description
- Creative generation (stories & narratives, poetry)

### Training

#### Maximum Likelihood

Issues:
- Diversity
- Exposure bias: the context that we train on are different from the ones that we see at generation time

#### Unlikelihood training

Given a set of undesired token $C$, lower their likelihood in context

Combine MLE with UL, setting $C$ to be the previous words in the sentext.

#### Exposure bias solutions

- Sequence re-writing
- Reinforcement learning

### Decoding

#### Greedy methods

Types
- argmax
- beam search

Cons
- repetition
- predicted probability of next word has low variance; different from human language patterns


#### Sampling

Types 
- Top-k sampling: sample from a fixed amount of tokens
- Top-p (nucleus): sample from a fixed amount of probability mass
- Softmax temperature: scale the scores by a coefficient $\tau$. The larger $\tau$ the more uniform (i.e. unpredictable) the sampling.

#### Distribution rebalancing

- Retrieval from n-gram phrase statistics
- Backpropagation-based distribution re-balancing

#### Re-ranking

Properties:
- Perplexity
- Style, discourse, entailment/factuality, logical-consistency
- Multi-property

###  Evaluation

#### Automatic evaluation metrics

**Content overlap metrics**

Provide a good starting point for evaluating the quality of generated text, but they are not good enough on their own

- N-gram (e.g. BLUE, ROUGE): do not correlate well with human translation
- Semantic overlap: PYRAMID, SPICE
  
**Model-based metrics**

Can be more correlated with human udgement, but behavior is not interpretable

**Human evaluations**

Only ones that can directly evaluate factuality, that is, "is the model saying correct things"?

But are inconsistent

### Ethical considerations

NLG produces output that is heavily depending on the training data, so it is easy to introduce bias in the models.

NLP models are easy to compromise with adversarial attacks.
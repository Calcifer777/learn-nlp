# Coreference resolution

Find all mentions in a piece of text that refer to the same entity.

## Coreference vs Anaphora (& Cataphora)

Anaphora happens when a term (anaphor) refers to another term (antecedent) in a sentence. Anaphora and coreference are overlapping but distinct objects
- coreference & not anaphora: "Barack Obama ... EOS ; Obama ... EOS"
- coreference & anaphora (pronomial anaphora): ""
- not coreference & anaphora (bridging anaphora): "We went to see a concert last night. The tickets [hidden: of the concert] were really expensive"

Cataphora happens when the referenced term appears after the referencing term.

## Types of coreference resolution

Applications:
- full text understanding
- machine translations
- dialogue systems

### Rule-based (Hobbs' algorithm)

Rule-based algorithms are good but fail to capture knowledge-based schema (Winograd schema).

Semantic-based algorithms are meant to fix these issues.

### Mention-pair

Train a binary classifier that assigns to every pair of mentions a probability of being coreferent.

To account for transitivity, add coreference links between metion pairs.

Issues:
- difficult to resolve distant pair relationships

### Mention-ranking

Assign each mention its highest scoring candidate antecedent according to the model.

Dummy *NA* mention allows the model to decline linking the current mention to anything (*singleton* or *first mention*)

### Clustering

## Approaches

- Non-neural statistical classifier
- Simple NN
- LSTM models, attention models, transformers, etc.

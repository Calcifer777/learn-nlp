# Parsing

## Grammar parsing

Uses phrase structure grammar to organize words into nested constituents.

## Dependency parsing

Dependency structure of sentences shows which words depend on (modify or are arguments of) which other words.

Dependencies are logical asymmetric relations between two words in a sentence, a *head* word and a *dependent* word. Each word can have multiple dependents but only one head.

The dependency parsing proble asks to create a mapping from the input sentence with words $S=w_0 w_1 \cdots w_n$ to its dependency tree graph.

## Approaches

### Transition-based dependency parsing

Relies on a state machine which defines the possible transitions to create the dependency tree. 

The learning problem is to induce a model which can predict the next transition in the state machine based on the transition history.

The parsing problem is to construct the optimial sequence of transitions for the input sequence, give the previously induced model.

### Greedy deterministric transition-based parsing (Nivre 2003)

#### Implementation

For any sentence $S$, a state can be defined with a triple:
- $\sigma$: a stack of words
- $\beta$: a buffer of words
- A set of dependency arcs $A$

The method works by parsing the words in a given sentence with a cursor in order from left to right. 

$\sigma$ represents the words which have been passed by the cursor but which have not been fully processed yet. A word is fully processed when the model finds the relationship connecting it (as depenent) to another word (as head).

$\beta$ represents the words which have not been passed by the cursor.

At any given step, the model can:
- *shift*: move the cursor one step; that is, append the first word in the sentence to the stack
- *left-arc*: create a depenency arc between the last word in the stack (dependent) and the previous word in the stack (head). If the stack is represented as a list of tokens going from left (start) to right (end), this is like drawing a left-to-right dependency arrow from the last to the second-to-last word in the sentence. The last word in the stack is the *dependent* word in this new relationship; so it is fully processed and can be removed from the stack.
- *right-arc*: create a depenency arc between the second-to-last word in the stack (dependent) and the last word in the stack (head).

The parsing process is completed when:
- the cursor has moved to the end of the sentence; that is, the buffer is empty
- all dependency arcs have been processed; that is, the stack is empty and all words are represented in the set of dependency arcs $A$.

### Greedy transition-based parsing with NN

#### Feature selection

The features for a given sentence $S$ generally include:
- Vector embeddings for some of the words in $S$ (and their dependents) at the top of the stack and in the buffer
- Part-of-speech tags for some words in $S$
- Arc labels for some of the words in $S$
# Architectures

## RNN

![rnn](_static/rnn.png)

Applications
- language modelling
- sequence tagging: POS, NER
- sentiment classification
- encoding: question answering, machine translation
- decoding: speech recognition, transation, summarization

Issues
- Vanishing and exploding gradients

## Gated units (LSTM, GRU)

Gated units address the vanishing gradient problem by adding 'direct' connections between the RNN units.

### LSTM

On step $t$, there is a hidden state $h^t$ and a cell state $c^t$:
- Both are vectors of length $n$
- The cell stores long-term information
- The LSTM can read, erase, and write information from the cell
- The selection of which information is erased/Written/read is controlled by three corresponding gates
  - The gates are also vectors of length $n$
  - On each timestep, each element of the gates can be open (1), closed (0), or somewhere in-between
  - The gates are dynaic their value is computed based on the current context

## Seq-to-seq

Seq-to-seq architectures involve two NN components - an encoder and a decoder, where:
- the encoder creates a sparse representation of the input (e.g.sentence, question, piece of text, etc)
- the decoder uses the sparse representation of the input created by the encoder to yield an output (e.g. a translation, answer, summarization, etc)

Use cases:
- Summarization
- Dialogue
- Parsing
- Text generation (e.g. code, music)

### Seq-to-seq with RNN

When doing seq-to-seq with RNN the sparse representation of the input created by the encoder is the hidden state of the model at the last step of the input feed-forward pass.

The decoder starts with this hidden state and the `<START>` token to produce the output.

During training of the decoder, a *teacher-forcing* method is often used. That is, the correct input of the decoded sentence is fed at each step of the feed-forward pass.

### Seq-2-seq with attention

An issue with vanilla seq-2-seq achitectures is that the last hidden state of the encoder needs to capture all the information about the source sentence; this can be seen an information bottleneck.

Attention models aim at reducing this issue by adding a connection between the decoder and the hidden states of each of the encoder steps. This modificaiton allows the NN to focus on a particular part of the source sequence.

For each step $t$ in the decoder, attention models generate a score that captures the similarity between the hidden state at that step and each of the hiddens states in the encoder model.

Then, a probability distribution is derived from these scores via a softmax actiation function. This probability distribution is then used to create a weighted average of the hidden states of the encoder model. 

The result of the weighted average is then combined with the hidden state of the decoder model and finally processed via an activation function.

#### Intuition

Attention models involve a set of *values* (the hidden states of the encoder) and a query (the hidden state of the decoder model).

Attention modes then:
- compute the attention scores, which capture a measure of similarity/relevance between the query and the values
- Derive a probability distribution - the *attention distribution* from the attention scores
- Use the attention distribution to compute a weighted average of the values, the so called *attention output* or *context vector*
- Combine the query with the context vector to generate the decoder output

The attention output is then a selective summary of the information contained in the values, where the query determines which values to focus on. 

Attention is then a way to obtain a fixed-size representation of an arbitrary set of representations - the values - dependent on some other representation - the query.

#### Variants

Ways to derive the attention scores:
- basic dot product: $e_i = s^T h_i$. This assumes that the query and the values have the same dimention.
- multiplicative attention: $e_i = s^T W h_i$, with $W$ a weight matrix
- Reduced rank multiplicative attention: $W = U^T V$, with $U$, $V$ "skinny" matrices; this reduces the number of parameters of $W$
- additive attention: $e_i = v^T tanh(W_1 h_i + W_2 s)$, which effectively uses a dense NN layer to compute the scores

### Self-attention

Issues with recurrent seq-2-seq models:
- linear interaction distance
- lack of parallelizability

### Transformers
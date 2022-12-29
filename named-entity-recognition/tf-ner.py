# https://www.tensorflow.org/datasets/catalog/conll2003#conll2003conll2003_default_config
# %%
import numpy as np
import tensorflow_datasets as tfds
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import Model, Sequential
from keras.losses import SparseCategoricalCrossentropy
from keras.layers import (
  Embedding, 
  TextVectorization, 
  Bidirectional, 
  LSTM,
  Dense,
  Input,
  TextVectorization,
  TimeDistributed,
)

# %%
(ds_train, ds_test), info = tfds.load(
  name="conll2003",
  split=["train", "test"],
  with_info=True,
)

# %%
print(info)
print( "NER tags:", info.features["ner"].feature.names)

# %%
sample_tokens = [x["tokens"].numpy() for x in ds_train.take(20)]

# %%
# Get max sequence length
max_sequence_length = (
  ds_train
  .map(lambda r: len(r['tokens']))
  .reduce(tf.constant(0, tf.int32), lambda t1, t2: tf.math.maximum(t1, t2) )
  .numpy()
)
print("Max sequence length in training set:", max_sequence_length)

# %%
tokens = ds_train.map(lambda r: r['tokens'])

# %%
MAX_VOCAB_SIZE = 10000
MAX_SEQUENCE_LENGTH = 100
vectorizer = TextVectorization(
  max_tokens=MAX_VOCAB_SIZE,
  output_sequence_length=MAX_SEQUENCE_LENGTH,
  standardize="lower",
  output_mode="int",
  split=None,
)

vectorizer.adapt(tokens)

# %%
train_data = (
  tokens
  .map(vectorizer)
  .filter(lambda r: len(r) > 0)
)

# %%
train_arr = np.vstack([x.numpy() for x in train_data])

# %%
EMBEDDING_SIZE = 100
OUTPUT_DIM = len(info.features["ner"].feature.names)

inputs = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype=np.int64)

x = Embedding(
  input_dim=MAX_VOCAB_SIZE, 
  output_dim=EMBEDDING_SIZE,
  mask_zero=True,
)(inputs)
x = Bidirectional(
  layer=LSTM(
    units=5, 
    return_sequences=True, 
    recurrent_dropout=0.2, 
    dropout=0.2
  ),
)(x)
x = TimeDistributed(Dense(units=OUTPUT_DIM, activation="softmax"))(x)

model = Model(inputs=inputs, outputs=x)

model.compile(
  optimizer="adam", 
  loss=SparseCategoricalCrossentropy(),
  metrics=["accuracy"],
)

# %%
# Test the model
"""
output_shape: [records x sequence_length x  possible_tags]

"""
out = model.predict(train_arr[:5])
print(out.shape)

# %%

# Misc

## Preprocessing techniques

When preprocessing, you have to perform the following:
- Tokenizing the string
- Lowercasing
- Removing stop words and punctuation
- Stemming
- Remove other non useful characters (e.g. hyperlinks, Twitter marks and styles)

## Locality sensitive hashing (LSH)

LSH is a technique to hash a set of vectors while attempting to keeping their locallity relationships; that is, close vectors will be hashed in the same hash buckets.

While this algorithm loses in precision, it gains in performance.

### Creating the hash table

1. Given a set of vectors
2. Create a set of hyperplanes in that vector space. Each hyperplanes divides the vector space in 2; $n$ planes will divide the space $2^n$ regions
3. Compute the hash of each vector $v$ as $h(v) = \sum_{i=0}^{n}{2^{I(v \cdot p_i > 0)}}$

### Getting the KNN of a vector

When computing the KNN of a vector, it is sufficient to search among the vectors in the same hash bucket. 

To improve the algorithm's performance, compute several hash tables and search for the KNN in the union of the vectors in each hash table relevant bucket.
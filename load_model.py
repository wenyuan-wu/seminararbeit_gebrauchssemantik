import gensim.models

model = gensim.models.Word2Vec.load('models/1996-model')
word_vectors = model.wv

result = word_vectors.most_similar(positive=['frau', 'könig'], negative=['mann'])
for _ in result:
    print("{}: {:.4f}".format(*_))

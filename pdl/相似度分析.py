from gensim.models import word2vec
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# senteces = word2vec.Text8Corpus("/Users/yujie/Workspaces/Python/offer/pdl/text8")
# model = word2vec.Word2Vec(senteces, size=200)
# model.save("text8.model")
model = word2vec.Word2Vec.load("text8.model")

y1 = model.most_similar("merge",topn=10)

for item in y1:
    print(item[0])
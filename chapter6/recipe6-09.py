# 6.9 単語への重み付け

# 問題
# 観測値に対する重要度で重み付けしたBoWモデルを作りたい。

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# テキストを作成
text_data = np.array([
  'I love Brazil. Brazil!',
  'Sweden is best',
  'Germany beats both'
])

# tf-idf特徴量行列を作成
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

# tf-idf特徴量行列を表示
print(feature_matrix)
print(feature_matrix.toarray())

# 特徴量名を表示
print(tfidf.vocabulary_)

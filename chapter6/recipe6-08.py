# 6.8 Bow(Bag of Words)によるテキストエンコード

# 問題
# テキストデータに対して、
# 個々の観測値テキスト中の特定の単語の出現回数を表す特徴量の集合を作りたい。

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# テキストを作成
text_data = np.array([
  'I love Brazil. Brazil!',
  'Sweden is best',
  'Germany beats both'
])

# Bow特徴量行列を作成
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

# 特徴量行列を表示
print(bag_of_words)
print(bag_of_words.toarray())

# 特徴量名を表示
print(count.get_feature_names())

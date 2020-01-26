# 6.7 品詞タグ付け

# 問題
# テキストデータに対して、単語ごともしくは文字ごとに品詞タグ付けしたい。

import nltk
from nltk import pos_tag, word_tokenize

# nltk.download('averaged_perceptron_tagger')

# テキストを作成
text_data = 'Chris loved outdoor running'

# 訓練済み品詞タグ付け器を適用
text_tagged = pos_tag(word_tokenize(text_data))

# 品詞を表示
print(text_tagged)

# 品詞を用いて単語を選択
print([word for word, tag in text_tagged if tag in ['NN', 'NNS', 'NNP', 'NNPS']])

from sklearn.preprocessing import MultiLabelBinarizer

# テキストを作成
tweets = [
  'I am eating a burrito for beakfast',
  'Political science is an amazing field',
  'San Francisco is an awesome city'
]

# リストを作成
tagged_tweets = []

# ツイート中の単語にタグ付け
for tweet in tweets:
  tweet_tag = pos_tag(word_tokenize(tweet))
  tagged_tweets.append([tag for word, tag in tweet_tag])

# ワンホットエンコードを用いて、タグを特徴量に変換
oen_hot_multi = MultiLabelBinarizer()
print(oen_hot_multi.fit_transform(tagged_tweets))

# 特徴量名を表示
print(oen_hot_multi.classes_)

# 6.6 語幹の抽出

# 問題
# トークン化した単語列を語幹の形に変換したい。

from nltk.stem.porter import PorterStemmer

# 単語トークン列を作成
tokenized_words = ['i', 'am', 'humbled', 'by', 'traditional', 'meeting']

# 語幹抽出器を作成
porter = PorterStemmer()

# 語幹抽出器を適用
print([porter.stem(word) for word in tokenized_words])

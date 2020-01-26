# 6.5 ストップワードの除去

# 問題
# トークン化されたテキストデータから、
# 一般的すぎて有用な情報を持たない(a, is, of, onなど)を取り除きたい。

from nltk.corpus import stopwords

# 最初の1回は下のコメント外してリソースをダウンロード
# import nltk
# nltk.download('stopwords')

# 単語トークン列を作成
tokenized_words = ['i', 'am', 'going', 'to', 'go', 'to', 'the', 'store', 'and', 'park']

# ストップワードをロード
stop_words = stopwords.words('english')

# ストップワードを削除
print([word for word in tokenized_words if word not in stop_words])

# ストップワードの一部を表示
print(stop_words[:5])

# 6.2 HTMLのパースとクリーニング

# 問題
# HTMLの要素として書かれたテキストデータからテキストだけ取り出したい。

from bs4 import BeautifulSoup

# HTMLテキストを生成
html = "<div class='full_name'><span style='font-weight:bold'>Masego</span> Azra</div>"

# HTMLをパース
soup = BeautifulSoup(html, 'lxml')

# classがfull_nameとなっているdivを見つけて、そのテキストを表示
print(soup.find('div', { 'class': 'full_name'}).text.strip())

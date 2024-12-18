# closewords
A library for finding the most similar word from a list of words, supporting Japanese (including kanji). / 最も似た単語を単語群から検索する日本語(漢字含む)対応のライブラリ<br>
[js version(original) / js版(オリジナル)](https://github.com/otoneko1102/closewords/tree/main)
# Example
```py
from closewords import closeWords
word='いぬ'
candidates=['いぬ', 'ねずみ', '猫', 'ねころび']
result=closeWords(word,candidates)
print("結果: {}".format(result[0]["word"]))
print("スコアを含む結果: {}".format(result))
```
# Creator
<img src="https://github.com/zrpy/zrpy/blob/main/kawaii_logo.png"></img>

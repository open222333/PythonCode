# 字串與文字

## 2.1 依據任意的多個定界符來切分字串

問題：

```
需要把一個字串切分(split)成幾個欄位，但字串中界定欄位的定介符(delimiters)以及其周圍的空白數並不一致。
```

解法：

```
字串的split()可解決，若要更多彈性，則可使用re.split()。
```

討論：

```
re.split()，若正則表達式中含有用括號(parentheses)包圍的捕捉組(capture group)，匹配的文字也會出現在結果
```

## 2.2 在一個字串的開頭或結尾比對文字

問題：

```
需要檢查一個字串的開頭(start)或結尾(end)，以找尋特定的文字模式，例如：副檔名(filename extensions)，URL schemes...
```

解法：

```
1. 檢查字串開頭或結尾最簡單方式是startswith()、endswith()。多個選項可用元組放入參數。
2. urllib.request urlopen()函式
```

討論：

```
切片與正則表達式都可以解決這問題。
常見的資料縮減(data reductions)作業。
```

```python
if any(name for name in listdir(os.path.dirname)):
    pass
```

## 2.3 使用Shell的通配模式來比對字串

問題：

```
使用與Unix shell 底下常使用的通配模式(wildcard patterns，例如:*.py、Dat[0-9]*.csv)來比對文字。
```

解法：

```
1. fnmatch模組fnmatch()：與底層的檔案系統(取決於作業系統)相同的大小寫區分規則(case-sensitivity rules)來比對模式。
2. fnmatch模組fnmatchcase()：區分大小寫。
```

討論：

```
fnmatch的能力介於簡單的字串方法以及強大的正規運算式之間。
```

## 2.4 比對與搜尋文字模式

問題：

```
在文字中比對(match)或搜尋特定模式(pattern)。
```

解法：

```
1. 簡單的字面值(literal)：使用字串方法，str.find()、str.endswith()、str.startswith()或類似的方法。
2. 複雜的比對工作：使用正則表達式(regular expressions)。
       - match()：匹配接近字串開頭。
       - findall()：找出所有符合。
       - finditer()：迭代的匹配。
```

討論：

```
正則表達式，使用re.compile()編譯一個模式，再使用match()、findall()、finditer()。
```

## 2.5 搜尋並取代文字

問題：

```
在一個字串搜尋並取代一個文字模式
```

解法：

```
1. str.replace()：簡單的可使用此函式。
2. re模組 sub()函式：較為複雜可使用此函式。
3. calendar模組 month_abbr()函式：更複雜可使用此函式。

subn():可知道替換了多少地方。
```

討論：

```
```

## 2.6 搜尋並取代不區分大小寫的文字

問題：

```
以不區分大小寫(case-insensitive)的方式搜尋並取代文字。
```

解法：

```
re.IGNORECASE(flag)，不區分大小寫的比對。
```

討論：

```
```

## 2.7 為最短匹配指定一個正規表達式

問題：

```
使用一個正規表達式(regular expressions)比對一個文字模式(text pattern)，但所識別出來的是符合一個模式的最長匹配，需改成最短匹配。
```

解法：

```
.*加上？ 就會進行最短匹配。
```

討論：

```
```

## 2.8 為多行的模式撰寫一個正規表達式

問題：

```
試著使用一個正規表達式(reqular expression)來比對一個區塊(block)，希望比對動作能夠跨越數行。
```

解法：

```
正規表達式的. 不匹配換行字元(newline)。(?:.|\n)指定一個非捕捉組。
```

討論：

```
re.compile() 接受一個旗標 re.DOTALL，用處：匹配所有字元，包含(newline)
```

## 2.9 以一種標準表示法正規化Unicode文字

問題：

```
正在處理Unicode字串，得確定所有的字串都使用相同的底層表示法。
```

解法：

```
使用unicodedata模組normalize()函式 將文字正規化。
NFC代表字元應該是組成完整的。
NFD代表字元應該是透過結合字元的使用而完全分解開來。
也支援NFKC NFKD形式的正規化。
```

討論：

```
combining()函式測試一個字元是否為一個結合字元。
```

## 2.10 在正規表達式中處理Unicode字元

問題：

```
使用正規表達式處理文字，但對Unicode有疑慮。
```

解法：

```
re模組，已納入某些Unicode字元類別的基礎知識。
執行比對與搜尋動作時，先把所有的文字正規化或淨化(sanitize)為一種標準行事。(參閱訣竅2.9)
```

討論：

```
若將Unicode與正規表達式混合一起使用，可使用第三方regex程式庫(http://pypi.python.org/pypi/regex)。
```

## 2.11 剝除字串中不想要的字元

問題：

```
想要剝除(strip)不想要的字元。
```

解法：

```
strip() lstrip() rstrip()
```

討論：

```
處理內部的空白，需使用replace()或正規表達式(reqular expression)
運算式lines = (line.strip() for line in f)，有效率的原因，不會先把資料讀到任何暫存器，只會建立一個迭代器(iterator)，而這個迭代器產出的每個文字行都會套用剝除動作。
```

## 2.12 淨化與清理文字


問題：

```
清理奇怪的文字 例如: pythoй
```

解法：

```
str.upper() str.lower() 將文字轉換成標準模式
str.replace() re.sub() 替換特定字元
unicodedata.normalize() 正規化文字 如訣竅2.9
```

討論：

```
類似的訣竅可套用到位元組(byte)
```

## 2.13 對齊文字字串

問題：

```
格式化文字 套用某種對齊(alignment)
```

解法：

```
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

使用format()函式 可用在字串也可用在其他值
```

討論：

```
舊的程式碼使用%來進行格式化 新的應優先使用format()
```

## 2.14 結合與串接字串

問題：

```
```

解法：

```
```

討論：

```
```

## 2.15 在字串中插換變數

問題：

```
```

解法：

```
```

討論：

```
```

## 2.16 將文字重新格式化為固定數目的欄位

問題：

```
```

解法：

```
```

討論：

```
```

## 2.17 在文字中處理HTML與XML的實體

問題：

```
```

解法：

```
```

討論：

```
```

## 2.18 文字的單詞化(Tokenizing)

問題：

```
```

解法：

```
```

討論：

```
```

## 2.19 撰寫一個遞迴下降剖析器(Recursive Descent Parser)

問題：

```
```

解法：

```
```

討論：

```
```

## 2.20 在位元組字串上進行文字作業

問題：

```
```

解法：

```
```

討論：

```
```
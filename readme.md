# 菊韻

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

本作品採用[創意共享 署名-非商業性-相同方式共享 4.0 國際版許可證](cc-by-nc-sa)。

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

部份文件使用其他許可，詳細請見[文件結構・許可](#文件結構・許可)。

**測試階段：預計4月完成**

## 簡介

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入小欖話爲主既粵語方言。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)。

爲適應流動電話鍵盤限制，以及各種新功能，鍵值已於12.0版本進行大規模調整。

更多資訊請閱讀下文竝參攷[Wiki](https://github.com/HoengSaan/rime-gukwan/wiki)。[關於如何安裝](https://github.com/HoengSaan/rime-gukwan/wiki/%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%9D)。

### 多方言適應

菊韻可支持多地方言，但目前僅支持小欖話。已爲各種方言口音預設大量轉換規則同模糊音，方便定製。

- 小欖話
  - 鎮區音
- 廣州話（僅供參攷）
- 分韻音（古代音，僅供參攷）
- 菊韻音（古代音，僅供參攷）

### 字詞

菊韻字庫詞庫以深筆爲準，但可以轉換爲簡筆。隨基本字庫詞庫之外，菊韻亦有小欖話特色詞庫以及廣東地名詞庫。目前準備增添更多詞庫以利打字。

### 功能

菊韻有各類功能以盡量貼近現代輸入法。

- **符號：**RIME特殊符號輸入（粵語版），鍵值爲`/`
- **Unicode：**以Unicode編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲`U`（unicode）
- **數字：**以阿拉伯數字輸入大小寫數字以及大小寫金額，鍵值爲`S`（sauzy）；支持以下7種格式：
  - 二〇二五（數字小寫）
  - 貳零貳伍（數字大寫）
  - 〢〇〢〥（蘇州碼子）
    - 即花碼，由於本身特性不支持亦不需要小數點。[瞭解更多](https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90)。
  - 二千〇二十五（數額小寫）
  - 貳仟零貳拾伍（數額大寫）
  - 二千〇二十五圓整（金額小寫）
  - 貳仟零貳拾伍圓整（金額大寫）
- **農曆：**直出是日農曆，鍵值爲`nl`；亦可以新曆轉舊歷，鍵值爲`N`（nunglik）
- **日期**
- **計數機：**直接在RIME計數，鍵值爲`cC`（calculator）
- **假名：**以細階輸入平假名，大階輸入片假名，鍵值爲`G `（gaaming）
- **顏文字：**以日文輸入各種顏文字，鍵值爲`K`（kaomoji）

**符號須安裝粵拼方可使用**，安裝方法請參攷[如何安裝 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/如何安裝)。

### 反查

多數人士通曉廣州話、普通話卻未必熟識自己鄉下發音，故設各種反查。反查亦可用來打菊韻難以輸入或無收錄既非常用字。

- **粵拼**（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲`J`（jyutping）。
- **明月拼音**（rime-luna_pinyin），官語普通話反查。鍵值爲`P`（pauping）。
- **倉頡五代**（rime-cangjie5），倉頡反查。鍵值爲`C`（congkit）。
- **訓讀**（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀（現代音）反查。鍵值爲`F`（fanduk）。
- **兩分**（[rime-loengfan]([CanCLID/rime-loengfan: Loengfan (粵語兩分) is the Cantonese version of the Liang Fen input method](https://github.com/CanCLID/rime-loengfan))），粵語廣州話兩分拆字反查。鍵值爲`L`(loengfan)。

**粵拼、訓讀、兩分須安裝方可使用**，安裝方法請參攷[如何安裝 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/如何安裝)。如需使用其他方案反查，請自行定製方案。


## 拼音

拼音方案基於[擴展粵拼](https://jyutjam.org/j++/)，現代音同[粵拼](https://jyutping.org/)無區別，直接使用即可。關於古代音請參攷[菊韻拼音表](https://github.com/HoengSaan/rime-gukwan/wiki/%E8%8F%8A%E9%9F%BB%E6%8B%BC%E9%9F%B3%E8%A1%A8)。

<img src="pic\gamjam1.png" style="zoom:50%;" />

<img src="pic\gamjam2.png"/>

|      | 平        | 上     | 去     | 上入  | 下入     |
| ---- | --------- | ------ | ------ | ----- | -------- |
| 陰   | 1 (55/53) | 2 (24) | 3 (33) | 1 (5) | 3 (3)    |
|      | 詩        | 屎     | 試     | 適    | 惜(白讀) |
| 鍵位 | v         | x      | q      | v     | q        |
| 陽   | 4 (32)    | 5 (13) | 6 (21) | 6 (2) | 2* (35)  |
|      | 時        | 市     | 示     | 食    | 食(過去) |
| 鍵位 | vv        | xx     | qq     | v     | q        |

同今時大多數粵拼輸入法一樣，可以輸入聲調以加快蒐字速度。

調值僅供參攷，部份方言僅有9個或8個聲調（含特殊調）。2*並非廣州話「新入」只見於入聲字變調，如「子」白讀zaai2*就同本身陰上調值（24）不一。此調亦用作表達過去、完成之文法意味。

詳細請參攷[小欖話・沙田方言特徵 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/小欖話・沙田方言特徵)


## 特徵

一般用家請無視灰字。恕此處不能盡述，詳細請參攷[小欖話・沙田方言特徵 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/小欖話・沙田方言特徵)。

<img src="pic\dakzhing.png"/>

## 文件結構・許可

部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0許可](cc-by-nc-sa)發佈。

### 方案

**※寬式音標竝不能完全代表實際發音※**

- `gukwan.schema.yaml`：調試用・自用（**請勿刪除**）

#### 預設古代音方案

- `gukwan-default.schema.yaml`：菊韻音（構擬音）
  - 根據菊韻標準所構擬之古音，較分韻複雜。
  - `gukwan-default-ps.schema.yaml`：寬式音標版
- `gukwan-fanwan.schema.yaml`：分韻音
  - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用眞正分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)

#### 預設現代音方案

- `gukwan-siulaam.schema.yaml`：小欖鎮區音
  - 本方案根據小欖鎮區音代表特徵製作。下爲重要特徵：
    - 小欖人多數人不分來孃（l/n）、透曉（t/h），故可以l音打n（如「農」`nung4`可打`lung4`），h音打t（如「偸」`tau1`可打`hau1`）。
    - 小欖人多數人不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
  - 此方案不能代表所有情況，建議仔細閱讀方案竝根據自身口音調整，見[特徵段](https://github.com/HoengSaan/rime-gukwan#特徵)。
  - [關於如何定製適合自己口音既方案](https://github.com/HoengSaan/rime-gukwan/wiki/如何定製)
  - `gukwan-siulaam-ps.schema.yaml`：寬式音標版

- `gukwan-canton.schema.yaml`：廣州音
  - 準確來講此方案係廣州風，並不能準確反映所有廣州發音。若欲使用眞正廣州音打字，可參攷以下方案：[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 字詞

`gukwan.dict.yaml`用於調用字庫詞庫，默認亦調用rime-cantonese部份詞庫同粵語八股文。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字庫
  - `gukwan.chars1.dict.yaml`：廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：今字異字異音訓讀增補
    - 粵字平翹、日以之分參攷梧州話
- 詞庫
  - `gukwan.words.dict.yaml`
    - 基於`jyut6ping3.words.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，隨源文件以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。已去除輸入碼竝改變部份字型。
  - `gukwan.words1.dict.yaml`：部份小欖話辭彙同小欖周邊地名
    - 收錄部份小欖話特有辭彙，小欖周邊地名街名，詳細見[小欖詞庫資料](https://github.com/HoengSaan/rime-gukwan/wiki/小欖詞庫資料)
  - `gukwan.words2.dict.yaml`：
    - 收錄粵拼詞庫所無之特殊辭彙同外來語，部份內容基於`jyut6ping3.lettered.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，隨源文件以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。
  - `gukwan.kwongtung.dict.yaml`：廣東地名（村級）
    - 來源爲[adyliu/china_area: 2024年中国全国5级行政区划（省、市、县、镇、村）](https://github.com/adyliu/china_area)，隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。已繁化。
- [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)

### 依賴

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件請參攷[如何安裝 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/如何安裝)。

- [rime-kanas](https://github.com/HoengSaan/rime-kanas)：用於輸入假名，隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- [rime-cantonese-emoji](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字，隨源文件以[CC 0許可](https://creativecommons.org/public-domain/cc0/)發佈。
- rime-kaomoji：用於輸入顏文字（需以日文輸入），係本人根據[mtripg6666tdr/Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj)字典文件製作，隨源文件以[MIT許可](https://mit-license.org/)發佈。

### LUA腳本

本方案所有LUA腳本均有參攷[iDvel/rime-ice](https://github.com/iDvel/rime-ice)及相關文件，相關文件根據源文件許可發佈。本人僅將其繁化，竝增加小小功能。由於部份腳本源碼已改變，爲避免文件被覆蓋，故改名。

- unicode.lua：UNICODE碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT許可](https://mit-license.org/)發佈。
- lunar.lua：是日農曆，新曆轉舊歷，來自[boomker/rime-fast-xhup](https://github.com/boomker/rime-fast-xhup)，隨源文件以[LGPL 3.0許可](https://www.gnu.org/licenses/lgpl-3.0.en.html)發佈。
- number_gukwan.lua：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense許可](https://unlicense.org/)，本文件亦不設限。
- date_gukwan.lua：以各種格式輸入是日日期時間，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- calc_translator.lua：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之PR。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
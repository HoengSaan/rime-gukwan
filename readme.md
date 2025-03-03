# 菊韻

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

本作品採用[創意共享 署名-非商業性-相同方式共享 4.0 國際版證書](cc-by-nc-sa)。

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

部份文件使用其他證書，詳細請見[文件結構](#文件結構)。

**測試階段：預計4月完成**

## 簡介

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入小欖話爲主既粵語方言。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)。

更多資訊請閱讀下文竝參攷[Wiki](https://github.com/HoengSaan/rime-gukwan/wiki)。關於如何安裝。

### 目前支持方言

- 小欖話鎮區音
- 廣州話（僅供參攷）
- 分韻音（古代音，僅供參攷）
- 菊韻音（古代音，僅供參攷）

詳細可參攷[文件結構](#文件結構)。

## 輸入

字庫詞庫以深筆爲準，但可以轉換爲簡筆。可以粵語輸入繪文字（表情符號），但須手動開啓。

- 反查
  - 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>`</code>
  - 明月拼音（rime-luna_pinyin），官語普通話反查。鍵值爲`X`。
  - 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲`V`。
  - 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi/blob/master/kunyomi.schema.yaml)），和語訓讀（現代音）反查。鍵值爲`K`。
- 特殊（自用）
  - 假名（[rime-kanas](https://github.com/HoengSaan/rime-kanas)），以細階輸入平假名，大階輸入片假名。鍵值爲`J`。
  - 顏文字（rime-kaomoji），以日文輸入顏文字。鍵值爲`L`。

**粵拼、假名、訓讀須安裝方可使用反查**，安裝方法見上方安裝段。如需使用其他方案反查，請自行搜索竝改變方案。

由於粵語兩分以廣州話爲準，故不納入。


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

## 文件結構

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
    - 基於`jyut6ping3.words.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，證書隨源文件爲[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。去除輸入碼竝改變部份字型
  - `gukwan.words1.dict.yaml`：部份小欖話辭彙同小欖周邊地名
    - 收錄部份小欖話特有辭彙，小欖周邊地名街名，詳細見[小欖詞庫資料](https://github.com/HoengSaan/rime-gukwan/wiki/小欖詞庫資料)
  - `gukwan.words2.dict.yaml`：
    - 收錄粵拼詞庫所無之特殊辭彙同外來語，部份內容基於`jyut6ping3.lettered.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，證書隨源文件爲[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
  - `gukwan.kwongtung.dict.yaml`：廣東地名（村級）
    - 來源爲[adyliu/china_area: 2024年中国全国5级行政区划（省、市、县、镇、村）](https://github.com/adyliu/china_area)，證書隨源文件爲[GPL 3.0](https://github.com/HoengSaan/rime-gukwan/blob/main/LICENSE-GPL)。已繁化。
- [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)

### 依賴

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件見[安裝](#安裝)。

- [rime-kanas](https://github.com/HoengSaan/rime-kanas)：用於輸入假名，根據GPL-3.0證書發佈
- [rime-cantonese-emoji](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字
- rime-kaomoji：用於輸入顏文字（需以日文輸入），係本人根據[mtripg6666tdr/Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj)字典文件製作，以MIT證書發佈。
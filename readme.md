# 菊韻

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

部份文件使用其他證書，詳細請見[文件結構段](https://github.com/HoengSaan/rime-gukwan#%E6%96%87%E4%BB%B6%E7%B5%90%E6%A7%8B)。

**測試階段：預計4月完成**

## 簡介

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入小欖話爲主既粵語方言（參攷市誌，以下將稱之爲沙田方言），拼音基於分韻廣韻以兼容各地方音(如師syu1 si1兩音)。爲兼容性同方便整理，輸入碼同實際拼音有所不同，但可直接以粵拼輸入。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。廣韻之外字庫未完成，目前缺少現代字同粵字，缺少部份白讀音。（7.0更新：多數現代字粵字已完成）

菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 方言

雖然好多人講到中山話，多會諗到石歧話，之但是分佈最廣泛其實係所謂沙田方言，人口最爲之多，以中山北部爲主，方音近似順德（尤其北部），故出到去唔少人聞到都以爲係順德話。

| <img src="pic/fongin.jpg" style="zoom:;" /> | <img src="pic/fongin2018.jpg" style="zoom: 75%;" /> |
| ------------------------------------------- | --------------------------------------------------- |
| 圖一：中山方言地圖                          | 圖二：中山方言分佈畧圖                              |

圖一爲本人根據《[中山市誌（2005年版）](http://www.zsdag.cn/list?t_id=96)》所作之粗畧版方言地圖，粵語分爲五類：橙色爲沙田話（近順德話）、紅色爲三角話（近東莞話）、紫色爲古鎮話（近新會話）、紅色爲石歧話、金色則爲中山域外之順德話。綠色爲中山閩語，藍色爲客家話。顏色代表區域主要方言。（板芙鎮：粵語（沙田話）爲主，亦有少數客閩兩語分佈。南蓢鎮：閩語（南蓢話）爲主 ；三鄉鎮：閩語（三鄉話）爲主，亦有少數客粵兩語分佈；坦洲鎮：粵（沙田話）客兩語；神灣鎮：粵（沙田話）客兩語。張家邊鎮（東鄉）：即火炬區，除東莞話皆有。）

加筆：所謂沙田話，多爲文件資料上既講法，實際上無幾個人眞係聽過呢個講法。不過沙田話亦都係貼切既，因爲渠分佈既地方以前基本上眞係田基，呢幾十年工業發展先填起來既，

圖二摘自高然於2019年出版《中山方言誌》，將粵語分爲六類，並無將小欖話（同其周邊方言）、蜑家話歸爲一類。資料較中山市誌詳細許多，但仍不足夠。

加筆：三角鎮白色並非水域，而係三角話。

## 文件結構

### 方案

- `gukwan.schema.yaml`：調試用・自用（**請勿刪除**）

#### 預設古代音方案

- `gukwan-default.schema.yaml`：菊韻音（構擬音）

  - 根據菊韻標準所構擬之古音，較分韻複雜。

  `gukwan-fanwan.schema.yaml`：分韻音

  - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用眞正分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)

#### 預設現代音方案

- `gukwan-siulaam.schema.yaml`：小欖鎮區音
  - 本方案根據小欖鎮區音代表特徵製作，建議仔細閱讀方案竝根據自身口音調整，見[特徵段](https://github.com/HoengSaan/rime-gukwan#特徵)。

- `gukwan-canton.schema.yaml`：廣州音
  - 準確來講此方案係廣州風，並不能準確反映所有廣州發音。若欲使用眞正廣州音打字，可參攷以下方案：[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 字詞

`gukwan.dict.yaml`用於調用字庫詞庫，默認亦調用rime-cantonese部份詞庫同粵語八股文。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字庫
  - `gukwan.chars1.dict.yaml`：增廣一組廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：增廣二組今字異字異音訓讀增補
- 詞庫
  - `gukwan.siulaam.dict.yaml`：小欖話特殊辭彙同小欖周邊地名，詳細見[小欖詞庫資料](https://github.com/HoengSaan/rime-gukwan/wiki/小欖詞庫資料)
  - `gukwan.words.dict.yaml`：`jyut6ping3.words.dict.yaml`無輸入碼版本
    - 作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，證書隨源文件爲[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
  - `gukwan.lettered.dict.yaml`：基於`jyut6ping3.lettered.dict.yaml`
    - 作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，證書隨源文件爲[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。
  - `gukwan.kwongtung.dict.yaml`：廣東地名（村級）
    - 來源爲[adyliu/china_area: 2024年中国全国5级行政区划（省、市、县、镇、村）](https://github.com/adyliu/china_area)，證書隨源文件爲[GPL 3.0](https://github.com/HoengSaan/rime-gukwan/blob/main/LICENSE-GPL)。已繁化。
  - [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)
  

## 安裝

1. 安裝RIME（WINDOWS：[小狼毫](https://github.com/rime/weasel)；MacOS：[鼠鬚管](https://github.com/rime/squirrel)；Linux：[Fcitx5](https://github.com/fcitx/fcitx5)、[Fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)；Android：[同文輸入法](https://github.com/osfans/trime)｜[Fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)、[Fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)）
2. 安裝以下倉庫
   1. [rime-cantonese](https://github.com/rime/rime-cantonese)（**必選**，用於反查廣州話、八股文、部份詞庫）
   2. [rime-kanas](https://github.com/HoengSaan/rime-kanas)（**可選**，用於輸入假名）
   3. [rime-cantonese-emoji](https://github.com/rime/rime-emoji-cantonese)（可選，用於輸入Emoji）
   4. **rime-gukwan**（**本方案**）
   5. [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（若閣下已刪除則須重新安裝，否則無法使用官話反查）
   6. [rime-cangjie](https://github.com/rime/rime-cangjie)（若閣下已刪除則須重新安裝，否則無法使用倉頡反查）

用家可參攷以下文章：

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺）
- [配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)
- [Android 上的 RIME 输入法 trime 同文输入法使用 | Verne in GitHub](https://blog.einverne.info/post/2021/04/use-trime-input-method-rime-on-android.html#安装和基础使用)（Android：同文）

Android亦可選擇小企鵝（fcitx5），但安裝對一般用家來講較爲困難，亦無簡單易明既教程故此簡畧介紹（前提有Windows或其他電腦輔助）。

1. 在電腦安裝RIME並配置好。
2. Download APP同RIME插件即可。手機通常使用arm64-v8a。（Google Play版本更新速度慢，建議從Github [Releases · fcitx5-android/fcitx5-android](https://github.com/fcitx5-android/fcitx5-android/releases) Download）
3. 安裝，須開啓「允許此來源的應用程序」。
4. 於Fcitx5→Addons啓用Rime插件
5. 將電腦端RIME目錄文件（Windows默認：C:\Program Files (x86)\Rime\weasel-0.xx.x\data），壓縮竝送至Android設備，建議使用zip等主流格式即可。
6. 於Android設備解壓文件並送至`/Android/data/org.fcitx.fcitx5.android/files/data/rime/`。
   1. 普通用家須從Fcitx5進入。Fcitx5→Addons→Rime設定（齒輪符號）→User data dir→OK即可移動，左邊即有選單。將解壓後既文件全數Copy，然後送至上述地址（左邊選單→Fcitx5 for Android→rime）。
   1. Root用家直接連接電腦即可傳送文件，毋須經過以上麻煩步驟。
7. 配置文件：開啓Fcitx5鍵盤竝切換至Rime輸入法，用左上角「>」符號開工具列，再撳「…」開輸入法設定，最後撳Reload Config等待輸入法配置完成。 

## 輸入

詳細請參攷[菊韻拼音表](https://github.com/HoengSaan/rime-gukwan/wiki/%E8%8F%8A%E9%9F%BB%E6%8B%BC%E9%9F%B3%E8%A1%A8)。

### 鍵位

<img src="pic\key.png"/>

### 拼音

拼音方案基於[擴展粵拼](https://jyutjam.org/j++/)，現代音同[粵拼](https://jyutping.org/)無區別，直接使用即可。

師韻（現代無此音）菊韻標準爲y，擴展粵拼標準爲ii，須手動開啓轉換式。另有各種簡拼，異拼，詳細請閣下閱讀方案文件。

同今時大多數粵拼輸入法一樣，可以輸入聲調以加快蒐字速度。

<img src="pic\gamjam1.png" style="zoom:50%;" />

<img src="pic\gamjam2.png"/>

|      | 平         | 上     | 去     | 上入  | 下入     |
| ---- | ---------- | ------ | ------ | ----- | -------- |
| 陰   | 1 (55/53)  | 2 (24) | 3 (33) | 1 (5) | 3 (3)    |
|      | 詩         | 矢     | 試     | 適    | 惜(白讀) |
| 鍵位 | v          | x      | q      | v     | q        |
| 陽   | 4 (42/55*) | 5 (13) | 6 (21) | 6 (2) | 2* (35)  |
|      | 時         | 市     | 示     | 食    | 食(過去) |
| 鍵位 | vv         | xx     | qq     | v     | q        |

調值僅供參攷，部份方言僅有9個或8個聲調（含特殊調）。2*並非廣州話「新入」只見於入聲字變調，如「子」白讀zaai2*就同本身陰上調值（24）不一。此調亦用作表達過去、完成之文法意味。

### 反查

目前方案預設四個反查：

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>`</code>
- 明月拼音（rime-luna_pinyin），北語普通話反查。鍵值爲`X`。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲`V`。
- 假名（[rime-kanas](https://github.com/HoengSaan/rime-kanas)），以細階輸入平假名，大階輸入片假名。鍵值爲`R`。

**粵拼同假名須安裝方可使用反查**，安裝方法見上方安裝段。如需使用其他方案反查，請自行搜索竝改變方案。

## 定製

**※請閣下務必閱讀說明（即本頁）同方案文件（即以schema.yaml結尾之文件）方進行方案定製※**

**※定製任何方案務必進行版本備份竝進行測試，以免發生意外※**

**※定製任何方案不應改變現有文件，尤其`gukwan.schema.yaml`※**

定製請參攷[配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)。

方案無法兼顧所有粵語方言，亦竝非本方案之目的。定製本方案需要對音韻學同粵語音韻有基本理解方可進行。

方案本身預設有約百條轉換規則，有簡介其轉換之音位。刪除行頭井號啓用轉換，行頭鍵入井號停止轉換。（即行頭有井號爲停止轉換，行頭無井號爲啓用轉換）若表內無適合規則請自行增添，方法請參攷[SpellingAlgebra · rime/home Wiki](https://github.com/rime/home/wiki/SpellingAlgebra)。

定製方案最好使用新文件，文件必須以`schema.yaml`結尾，如`gukwan-myaccent.schema.yaml`。

以`gukwan-fanwan.schema.yaml`作例，下列部分非常重要，不可或缺。

```yaml
__include: gukwan.schema:/	# 用於調用基底文件

schema:
  schema_id: gukwan-fanwan	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  name: 菊韻分韻音	# 用於區別基底文件「菊韻」，只須同其他方案作出區別即可

###省畧###

speller:
  alphabet: zyxwvutsrqponmlkjihgfedcba
  delimiter: " '"
  algebra:
  # 此部份用於定製，建議以gukwan.schema.yaml爲藍本參攷範例自行調整，表內無敬請自行增添，部分字或要用個人字庫。

translator:
  dictionary: gukwan
  prism: gukwan-fanwan	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  
###省畧###
```

**※注意schema_id必須同其他方案不同，否則無法使用。※**

**※translator下方必須使用prism同基底字庫詞庫進行隔離，否則無法正常打字。※**

### 聲母定製

本方案聲母極其簡單，同分韻竝無大區別，現代音請直接將此部份所有轉換式全數啓用。其他請根據自己口音調整。

```yaml
    #聲母——現代
    #- derive/^(z|c|s)h/$1/                 # 精照合流(zh->z)
    #- derive/^(zj|cj|sj)yo(?=\d)/$1yu/     # 精照合流
    #- derive/^(z|c|s)j(?!yo)/$1/           # 精照合流(ch->c)
    #- derive/^(z|c)r/$1/                   # 精照合流(sj->s)
    #- derive/^nj/j/                        # 日以合流(nj->j)
```

### 韻母定製

7.1更新：最新版已有多數方音轉換式，識粵拼即可自行定製，毋須音韻學智識。建議參攷下特徵段。

### 聲調定製

聲調多用來減少重碼率，無須自己無部分聲調而特登改變。

## 特徵

一般用家請無視灰字。

<img src="pic\dakzhing.png"/>

詳細請參攷[小欖話・沙田方言特徵 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/小欖話・沙田方言特徵)
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

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入小欖話爲主既粵語方言。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 目前支持方言

- 小欖話鎮區音
- 廣州話（僅供參攷）
- 分韻音（古代音，僅供參攷）
- 菊韻音（古代音，僅供參攷）

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
  - 此方案不能代表所有情況，建議仔細閱讀方案竝根據自身口音調整，見[特徵段](https://github.com/HoengSaan/rime-gukwan#特徵)。（[如何定製方案](https://github.com/HoengSaan/rime-gukwan#定製)）
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


## 輸入

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

### 反查

目前方案預設五個反查入口：

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>`</code>
- 明月拼音（rime-luna_pinyin），官語普通話反查。鍵值爲`X`。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲`V`。
- 假名（[rime-kanas](https://github.com/HoengSaan/rime-kanas)），以細階輸入平假名，大階輸入片假名。鍵值爲`R`。
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi/blob/master/kunyomi.schema.yaml)），和語訓讀（現代音）反查。鍵值爲`K`。

**粵拼、假名、訓讀須安裝方可使用反查**，安裝方法見上方安裝段。如需使用其他方案反查，請自行搜索竝改變方案。

由於粵語兩分以廣州話爲準，故不納入。

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

## 定製

**※請閣下務必閱讀說明（即本頁）同方案文件（即以schema.yaml結尾之文件）方進行方案定製※**

**※定製任何方案務必進行版本備份竝進行測試，以免發生意外※**

**※定製任何方案不應改變現有文件，尤其`gukwan.schema.yaml`※**

定製可參攷[配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)。

方案無法兼顧所有粵語方言，亦竝非本方案之目的。

### 定製方法摘要

**※注意schema_id必須同其他方案不同，否則無法使用。※**

**※translator下方必須使用prism同基底字庫詞庫進行隔離，否則無法正常打字。※**

以`gukwan-siulaam.schema.yaml`作例，下列部分非常重要，不可或缺。

```yaml
__include: gukwan.schema:/	# 用於調用基底文件

schema:
  schema_id: gukwan-siulaam	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  name: 菊韻小欖音	# 用於區別基底文件「菊韻」，只須同其他方案作出區別即可

###省畧###

speller:
  alphabet: zyxwvutsrqponmlkjihgfedcba
  delimiter: " '"
  algebra:
  # 此部份用於定製，表內無敬請自行增添，部分字或要用個人字庫。下略。

translator:
  dictionary: gukwan
  prism: gukwan-siulaam	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  
###省畧###
```

定製方案最好使用新文件，文件必須以`schema.yaml`結尾，如`gukwan-myaccent.schema.yaml`。可直接複製`gukwan-siulaam.schema.yaml`或其他文件然後改變以下提到關鍵部份，再進行定製，如下：

```yaml
__include: gukwan.schema:/	# 用於調用基底文件

schema:
  schema_id: gukwan-myaccent	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  name: 菊韻自用定製	# 用於區別基底文件「菊韻」，只須同其他方案作出區別即可

###省畧###

speller:
  alphabet: zyxwvutsrqponmlkjihgfedcba
  delimiter: " '"
  algebra:
  # 此部份用於定製，表內無敬請自行增添，部分字或要用個人字庫。下略。

translator:
  dictionary: gukwan
  prism: gukwan-myaccent	# 用於區別基底文件「gukwan」，只須同其他方案作出區別即可
  
###省畧###
```

方案本身預設有約百條轉換規則，有簡介其轉換之音位。刪除行頭井號啓用轉換，行頭鍵入井號停止轉換。（即行頭有井號爲停止轉換，行頭無井號爲啓用轉換）若表內無適合規則請自行增添。

定製至重要爲發音音，而調教非常簡單，只須以下兩個最重要：`derive`同`xform`。下文摘取自[SpellingAlgebra · rime/home Wiki](https://github.com/rime/home/wiki/SpellingAlgebra)。

```
* 變形／Transformation : 若拼寫（或其子串）與<模式>匹配，則將所匹配的部份改寫爲<替換式>；否則拼寫保持不變。模式、替換式遵循Perl正則表達式語法。

 格式：xform/<模式>/<替換式>/
 實例：算式 xform/^([nl])ue$/$1ve/  運算元 nue  結果 nve
 效果：輸入nve(lve)可以獲得源碼表中與編碼nue(lue)對應的候選；輸入nue(lue)無候選

* 派生／Derivation : 若對拼寫做正則模式匹配、替換而獲得了新的拼寫，則有效拼寫集合同時包含派生前後的拼寫；否則僅保留原拼寫。

 格式：derive/<模式>/<替換式>/
 實例一：算式 derive/^([nl])ue$/$1ve/  運算元 nue  結果 nve
 效果：輸入nve或nue(lve或lue)均可獲得源碼表中與編碼nue(lue)對應的候選

 實例二：算式 derive/^[nl](.*)$/l$1/  運算元 na  結果 la
 效果：輸入la可獲得源碼表中與編碼na、la對應的候選；輸入na，候選仍爲碼表中編碼爲na的候選
```

#### 聲母定製

本方案聲母極其簡單，同分韻竝無大區別，現代音請直接將此部份所有轉換式全數啓用。其他請根據自己口音調整。以下爲較重要部份：

```yaml
	- xform/^hj/j/                          # 口音補充(hj->j)：「賢」讀若jin者
    #- xform/^hj/h/                         # 口音補充(hj->h)：「賢」讀若hin者 順德石歧
    
    - xform/^hwun(?=\d)/hun$1/              # 口音補充(hw->h)：「桓」讀若fun者
    #- xform/^hwun(?=\d)/wun$1/             # 口音補充(hw->w)：「桓」讀若wun者
    
    #- xform/^xu(?=\d)/hu$1/                # 遇攝合口(*u->hu)：「狐」讀作fu4
    - xform/^xu(?=\d)/wu$1/                 # 遇攝合口(*u->wu)：「狐」讀作wu4 多數方音 
    - xform/^vu(?=\d)/hu$1/                 # 遇攝合口(*u->hu)：「護」讀作fu6
    #- xform/^vu(?=\d)/wu$1/                # 遇攝合口(*u->wu)：「護」讀作wu6 多數方音
    
    ###省畧###
    
    #聲母——現代
    #- derive/^(z|c|s)h/$1/                 # 精照合流(zh->z)
    #- derive/^(zj|cj|sj)yo(?=\d)/$1yu/     # 精照合流
    #- derive/^(z|c|s)j(?!yo)/$1/           # 精照合流(ch->c)
    #- derive/^(z|c)r/$1/                   # 精照合流(sj->s)
    #- derive/^nj/j/                        # 日以合流(nj->j)
    
    #FIX
    - derive/^n(?!g|j)/l/                   # 泥來合流(n->l)
    - derive/^t/h/                          # 透曉合流(t->h) 小欖部份
    - xform/^xaa(?=\d)/jaa$1/
```

例如閣下分辨透曉，則可於`- derive/^t/h/ `前面加上井號關閉轉換。

例如閣下將「桓」等字讀成`wun4`，則於`- xform/^hwun(?=\d)/hun$1/`前面加上井號關閉轉換，然後刪除`#- xform/^hwun(?=\d)/wun$1/`井號開啓轉換。

#### 韻母定製

內容過多不能詳述，詳細請參攷[特徵段](https://github.com/HoengSaan/rime-gukwan#特徵)。以下爲較重要部份：

```yaml
    #韻母——現代
    #其他口音請自行調校 不建議關閉打字輔助

    - xform/ooi(?=\d)/eoy/                  # 其他分韻(ooi->eoy)：「脆」讀若ceoy
    #- xform/ooi(?=\d)/oi/                  # 蟹合三止合銳(ooi->oi)「脆」讀若coi 文讀少見，一般白讀先有
    #- xform/ooi(?=\d)/ui/                  # 蟹合三止合銳(ooi->ui)「脆」讀若cui 
    
    - xform/^(b|p|f)i(?=\d)/$1ei/           # 止攝裂化脣音(i->ei) ：「備」讀若bei
    - xform/^(d|t|l|n)i(?=\d)/$1ei/         # 止攝裂化齒音(i->ei)：「地」讀若dei
    #- xform/^(g|k|h)i(?=\d)/$1ei/          # 止攝裂化牙音(i->ei)：「既」讀若gei
    - derive/^(s)(?!j)i(?=\d)/$1ei/         # 止攝心母特音（現代音裂化專用） 
    
    - xform/^ngu(?=\d)/ng/                            # 遇開一單獨成韻(ngu->ng)：「吳」讀若ng
    - xform/^(b|p|m|d|t|n|l|z|c|s|sh)u(?=\d)/$1au/    # 遇攝裂化(u->au)：「渡」讀若dau
    #- xform/^(b|p|m|d|t|n|l|z|c|s|sh)u(?=\d)/$1ou/   # 遇攝裂化(u->ou)：「渡」讀若dou
    #- xform/^(b|p|m|d|t|n|l|z|c|s|sh)u(?=\d)/$1o/    # 遇攝裂化(u->o)：「渡」讀若do
    
    - xform/^(z|c|s|n|l)yo(?=\d)/$1eoy/     # 遇開三(yo->eoy)：「旅」讀若leoy
    #- xform/^(g|k|h)yo(?=\d)/$1eoy/        # 遇開三(yo->eoy)：「去」讀若heoy
    
    - xform/^(z|c|n|l)yu(?=\d)/$1eoy/       # 遇合三裂化(yu->eoy)：「聚」讀若zeoy
    - xform/^(s)yu(?=\d)/$1eoy/             # 遇合三裂化(yu->eoy)：「須」讀若seoy
    #- xform/^(g|k|h)yu(?=\d)/$1eoy/         # 遇合三裂化(yu->eoy)：「巨」讀若geoy
    
    - xform/^(z|c)yi(?=\d)/$1eoy/           # 蟹合一(yi->eoy)：「最」讀若zeoy
    #- xform/^(s)yi(?=\d)/$1eoy/            # 蟹合一(yi->eoy)：「碎」讀若seoy
    - xform/^(s)yi(?=\d)/$1yu/              # 蟹合一(yi->yu)：「碎」讀若syu
    - xform/^(d|t|n|l)yi(?=\d)/$1yu/        # 蟹合一(yi->yu)：「對」讀若dyu
    #- xform/yi(?=\d)/eoy/                  # 蟹合一(yi->eoy)：皆讀作eoy者可用，其他關閉 
    #- xform/yi(?=\d)/yu/                   # 蟹合一(yi->yu)：皆讀作eoy者可用，其他關閉 
    
    - xform/yo(?=\d)/yu/                    # FIX
    
    #- xform/y(?=\d)/i/                     # 止攝師韻展脣(y->i) ：「師」讀若si
    - derive/y(?=\d)/yu/                    # 止攝師韻圓脣(y->yu)：「仕」讀若syu
    #- derive/^(z|c|s)ji(?=\d)/$1ii/        # 止開照組異拼(ji->ii)

    #- derive/eo(n|t)(?=\d)/a$1/            # 臻攝混音(ea->a)：「順」讀若san 多只見於白讀音
    
    - xform/ou(?=\d)/o$1/                   # 效一元音融合(ou->o)：「高」讀若go
    #- xform/ou(?=\d)/au$1/                 # 效一元音(ou->au)：「高」讀若gau
    
    - xform/ia(?=\d)/e$1/                   # 果假元音融合(ia->e)：「車」讀若ce
    - xform/jaa(?=\d)/je$1/                 # 果假元音融合(jaa->je)：「野」讀若je
    
    - xform/oo(ng|k)/o$1/                   # 宕攝開口(oo->o)：「各」讀若gok
    - xform/io(ng|k)/oe$1/                  # 宕攝江攝元音融合(io->oe) ：「量」讀若loeng
    - xform/jo(ng|k)/joe$1/                 # 宕攝江攝元音融合(jo->joe) ：「央」讀央joeng
    
    - derive/ae(u|n|m|t|p)(?=\d)/aa$1/      # 山效咸文(ae->aa)：「關」讀若gwaan
    - derive/ae(u|n|m|t|p)(?=\d)/e$1/       # 山效咸白(ae->e)：「關」讀若gwen 多只見於白讀音
    
    - derive/o(m|p)(?=\d)/a$1/              # 咸攝音變(o->a)：「甘」讀若gam
```

例如閣下將「翠」等字讀成`cooi3`並同`coi3`區分，即「翠」「賽」不同音，則於`- xform/ooi(?=\d)/eoy/`前面加上井號關閉轉換。若不區分`ooi`同`oi`，即「翠」「賽」同音，進行上述操作後刪除`#- xform/ooi(?=\d)/oi/`井號開啓轉換。

#### 聲調定製

聲調多用來減少重碼率，不建議改變聲調。

## 特徵

一般用家請無視灰字。恕此處不能盡述，詳細請參攷[小欖話・沙田方言特徵 · HoengSaan/rime-gukwan Wiki](https://github.com/HoengSaan/rime-gukwan/wiki/小欖話・沙田方言特徵)。

<img src="pic\dakzhing.png"/>
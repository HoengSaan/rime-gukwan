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

日文版菊韻（菊韻和語）：[HoengSaan/rime-kikwan: 日本語輸入方案菊韻 中州韻方案 Japanese IME (RIME Scheme)](https://github.com/HoengSaan/rime-kikwan)

## 簡介

This is a schema based on [Rime Input Method](https://rime.im/).

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入小欖話爲主既粵語方言。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)。

爲適應流動電話鍵盤限制，以及各種新功能，鍵值已於12.0b版本進行大規模調整。

更多資訊請閱讀下文竝參攷[菊韻 – なかやま園](https://zonsan.fc2.page/?cat=123)。[關於如何安裝](#安裝)。

### 多方言適應

菊韻可支持多地方言，但目前僅支持小欖話。已爲各種方言口音預設大量轉換規則同模糊音，方便定製。

- 小欖話
  - `gukwan-siulaam`（鎮區音）
- 廣州話
  - `jyut6ping3-gw`：以菊韻配置調用`rime-cantonese`
- 分韻音（古代音，僅供參攷）
- 菊韻音（古代音，僅供參攷）


### 功能

菊韻有各類功能以盡量貼近現代輸入法。[打開展示圖文件夾](https://github.com/HoengSaan/rime-gukwan/tree/main/pic/showcase)

<img src="pic\showcase.png" style="zoom:50%;" />

- **漢英混打：允許漢字英文混打，基於melt-eng。待完善**
- 繪文字（表情）：可以粵語輸入繪文字，默認關閉
- 符號：特殊符號輸入，鍵值爲`/`。[學習如何使用符號](https://github.com/HoengSaan/rime-gukwan/blob/main/symbols-gukwan.yaml)
- Unicode：以Unicode編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲`U`（unicode）
- 數字：以阿拉伯數字輸入大小寫數字以及大小寫金額，鍵值爲`S`（shuzy）；支持以下7種格式：
  - 二〇二五（數字小寫）
  - 貳零貳伍（數字大寫）
  - 〢〇〢〥（蘇州碼子）
    - 即花碼，由於本身特性不支持亦不需要小數點。[瞭解更多](https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90)
  - 二千〇二十五（數額小寫）
  - 貳仟零貳拾伍（數額大寫）
  - 二千〇二十五圓整（金額小寫）
  - 貳仟零貳拾伍圓整（金額大寫）
- 日期・時間・節日・節氣：
  - 日期（njat ki）：鍵值爲`vrk`或`/rk`或`/date`；有多種格式，部份默認禁用
  - 時間（shi gaen）：鍵值爲`vsg `或`/sg`或`/time`
  - 星期（sing ki）：鍵值爲`vsk`或`/sk`或`/week`
  - 日時（njat shi）：鍵值爲`vrs`或`/rs`或`/datetime`；ISO 8601/RFC 3339格式日期時間，以東八區（UTC+8）爲準
  - 週數（week number）：鍵值爲`vwn`或`/wn`或`/weeknumber`；今年第幾周
  - 時間戳（time stamp），鍵值爲`vts`或`/ts` 或`/timestamp`
  - 農曆（nung lik），鍵值爲`vnl`或`/nl`或`/lunar`
  - 節氣（zit hi）：鍵值爲`vzh`或`/zh`或`/zithi`；廿四節氣同日期
  - 節日（zit njat）：鍵值爲`vzr`或`/zr`或`/festival`；新舊曆節日同日期
  - 直出，鍵值爲`N`+「`YYYYMMDD`」；有四種模式：「新曆」「新曆轉舊曆」「舊曆轉新曆」「新曆轉干支」
  - 日期信息整合，鍵值爲`vday`或`/day`
  - **鍵值已在腳本固定，如需修改須直接改變`date_gukwan.lua`**
- 計數機：直接在RIME計數，鍵值爲`cC`（calculator）。[學習如何使用計數機](https://github.com/gaboolic/rime-shuangpin-fuzhuma/blob/main/md/calc.md)
- 假名：以細階輸入平假名，大階輸入片假名，鍵值爲<code>`G</code> （gaa ming）。輸入方式同其他IME（如Microsoft IME、ATOK等）基本無區別
- 顏文字：以日文輸入各種顏文字，鍵值爲<code>`K</code>（kaomoji）
- 和文：實現半混打日文，基於[rime-kikwin](https://github.com/HoengSaan/rime-kikwan)，鍵值爲<code>`R</code>（njat man）

> [!NOTE]
>
> **顏文字（表情）須安裝粵拼方可使用**，安裝方法請參攷[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。
> 由於和文功能所依賴方案詞庫過大，14.1b版本已將其關閉以防止部分設備無法正常部署。如需使用請自行安裝並手動啓用。

### 字詞

菊韻字庫詞庫以深筆爲準，但可以轉換爲簡筆。隨基本字庫詞庫之外，菊韻亦有小欖話特色詞庫以及廣東地名詞庫。

> [!NOTE]
>
> 菊韻可調用擴展詞庫，但需要手動下載。[gukwan-extended.dict.yaml](https://github.com/HoengSaan/rime-gukwan/blob/main/gukwan-extended.dict.yaml)內有說明如何獲取。由於擴展詞庫過大，低性能設備不建議使用，可能導致部署失敗。

### 反查

多數人士通曉廣州話、普通話卻未必熟識自己鄉下發音，故設各種反查。反查亦可用來打菊韻難以輸入或無收錄既非常用字。

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>` </code>。
- 明月拼音（rime-luna_pinyin），官語普通話反查。鍵值爲<code>`P</code>（pu ping）。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲<code>`C</code>（coong kit）。
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀（現代音）反查。鍵值爲<code>`F</code>（fan duk）。
- 兩分（[rime-loengfan]([CanCLID/rime-loengfan: Loengfan (粵語兩分) is the Cantonese version of the Liang Fen input method](https://github.com/CanCLID/rime-loengfan))），粵語廣州話兩分拆字反查。鍵值爲<code>`L</code>（loeng fan)。

> [!NOTE]
> 
> **粵拼、訓讀、兩分須安裝方可使用**，安裝方法請參攷[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。如需使用其他方案反查，請自行定製方案。

### 問題・未來方向

- 字詞發音：
  - 本人無法亦無有可能去保證所有漢字發音正確。尤其因爲菊韻詞庫多數無輸入碼，有多音字既單詞發音必然有誤。
  - 雖然菊韻支持使用聲調輸入，但本人並不能確保所有字詞聲調正確。尤其考慮到以小欖話等方言變調遠比廣州話豐富，以我一人之力斷無可能完善。
- 地名繁簡：數據來源係簡筆字，本人亦仔細審覈過，但都無法保證三萬幾條地名全數正確。
- <del>漢英混打：由於不明原因gukwan不能使用混打，本人已嘗試多次。將解決詞庫問題後再行處理。</del>**【已解決】**
- 漢英混打開關：待處理。
- 可輸入方言過少：自用爲主，將於未來處理。

## 安裝

以下僅解說大致流程，具體請見[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。

1. 安裝RIME
   1. WINDOWS：[Weasel 小狼毫](https://github.com/rime/weasel)
   2. MacOS：[Squirrel 鼠鬚管](https://github.com/rime/squirrel)｜[fcitx5-macos](https://github.com/fcitx-contrib/fcitx5-macos)
   3. Linux：[ibus](https://github.com/ibus/ibus)→[ibus-rime](https://github.com/rime/ibus-rime)｜[fcitx5](https://github.com/fcitx/fcitx5)→[fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)
   4. Android：[同文輸入法](https://github.com/osfans/trime)｜[fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)→[fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)

> [!NOTE]
>
> Linux版本必須安裝librime-lua否則部分功能無法使用

2. 安裝以下倉庫
   1. **rime-gukwan**（**本方案**）
   2. [rime-cantonese](https://github.com/rime/rime-cantonese)（**必選**，用於廣州話反查、八股文、部份詞庫）
   3. [rime-kunyomi](https://github.com/sgalal/rime-kunyomi/)（**可選**，用於和語訓讀反查）
   4. [rime-loengfan](https://github.com/CanCLID/rime-loengfan)（**可選**，用於廣州話拆字反查）
   5. [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（**可選**，若閣下已刪除則須重新安裝，否則無法使用官話反查）
   6. [rime-cangjie](https://github.com/rime/rime-cangjie)（**可選**，若閣下已刪除則須重新安裝，否則無法使用倉頡反查）
   7. [rime-kikwin](https://github.com/Hoengsaan/rime-kikwin/)（**可選**，用於日文半混打）

> [!WARNING]
>
> 由於`rime-kikwin`詞庫文件巨大，移動設備或低性能電腦不建議使用，可能導致無法部署（即無法正常使用）

3. 設定方案，重新部署

## 定製

定製詳情請參攷[如何定製菊韻 – なかやま園](https://zonsan.fc2.page/?p=1569)。

部份用家可根據自身情況添加以下字音到用戶字庫。

```
虐	hiok6
瘧	hiok6
若	hiok6
螢	hing4
盈	hing4
楹	hing4
蠅	hing4
葉	hip6
業	hip6
頁	hip6
惹	hia5
仰	hiong5
儒	hyu4
蠕	hyu4
孺	hyu4
濡	hyu4
薷	hyu4
夭	hiu1
舀	hiu5
窯	hiu4
姚	hiu4
謠	hiu4
耀	hiu6
遙	hiu4
鷂	hiu6
瑤	hiu4
堯	hiu4
翼	hik6
亦	hek6
贏	heng4
馭	hyo6
禦	hyo6
御	hyo6
驗	him6
芫	him4
筵	hin4
衍	hin5
演	hin5
延	hin4
```

## 拼音

拼音方案基於[擴展粵拼](https://jyutjam.org/j++/)，現代音同[粵拼](https://jyutping.org/)無區別，直接使用即可。關於古代音請參攷[菊韻拼音表 – なかやま園](https://zonsan.fc2.page/?p=1583)。

<img src="pic\gamjam1.png" style="zoom:50%;" />

<img src="pic\gamjam2.png"/>

同今時大多數粵拼輸入法一樣，可以輸入聲調以加快蒐字速度。

調值僅供參攷，部份方言僅有9個或8個聲調（含特殊調）。2*並非廣州話「新入」只見於入聲字變調，如「子」白讀zaai2*就同本身陰上調值（24）不一。此調亦用作表達過去、完成之文法意味。超高陰平只出現於陰平連續變調。

詳細請參攷[小欖話・沙田方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。


## 特徵

一般用家請無視灰字。恕此處不能盡述，詳細請參攷[小欖話・沙田方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。

其他方言未完成，請稍等。[凡例](https://github.com/HoengSaan/rime-gukwan/blob/main/pic/faanlai.png)

<img src="pic\dakzhing.png"/>

## 文件結構・許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0許可](cc-by-nc-sa)發佈。

### 方案

**※寬式音標竝不能完全代表實際發音※**

- `gukwan.schema.yaml`：調試用・自用（**請勿刪除**）
- `jyut6ping3-gw.schema.yaml`：以菊韻配置調用`rime-cantonese`，支持菊韻所有功能。
  - `jyut6ping3-gw-ps.schema.yaml`：寬式音標版

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
  - 此方案不能代表所有情況，建議仔細閱讀方案竝根據自身口音調整，見[小欖話・沙田方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。（內容已過期，待更新）
  - `gukwan-siulaam-ps.schema.yaml`：寬式音標版
  
- `gukwan-canton.schema.yaml`：廣州音
  - 準確來講此方案係廣州風，並不能準確反映所有廣州發音。若欲使用眞正廣州音打字，請使用`jyut6ping3-gw.scheme.yaml`

> [!TIP]
>
> [關於如何定製方案](https://github.com/rime/home/wiki/CustomizationGuide)

### 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用rime-cantonese部份詞庫同粵語八股文。位置爲`/gw_dicts`。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字表
  - `gukwan.chars1.dict.yaml`：廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：今字異字異音訓讀增補
    - 粵字平翹、日以之分參攷梧州話
- 詞庫
  - `gukwan.words.dict.yaml`：粵拼詞庫
    - 基於`jyut6ping3.words.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，隨源文件以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。已去除輸入碼竝改變部份字型。
    - 已開始爲部份詞標音。
  - `gukwan.words1.dict.yaml`：部份小欖話辭彙同小欖周邊地名
    - 收錄部份小欖話特有辭彙，小欖周邊地名街名，詳細見[小欖詞庫資料](https://github.com/HoengSaan/rime-gukwan/wiki/小欖詞庫資料)
  - `gukwan.words2.dict.yaml`：粵拼詞庫增補同外來語
    - 收錄粵拼詞庫所無之特殊辭彙同外來語。
  - `gukwan.lettered.dict.yaml`：粵拼詞庫
    - 基於`jyut6ping3.lettered.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，此部分則以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。
  - `gukwan.kwongtung.dict.yaml`：廣東地名（村級）
    - 來源爲[adyliu/china_area: 2024年中国全国5级行政区划（省、市、县、镇、村）](https://github.com/adyliu/china_area)，隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。已繁化。

> [!NOTE]
>
> `gukwan-extended.dict.yaml`用於調用各種擴展詞庫，以增強輸入體驗。下載並放置於正確位置方可使用，不安裝直接調用將會導致輸入法不能正常使用。故默認情況下將不調用。

> [!TIP]
>
> [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)｜[關於如何使用擴展詞庫](https://github.com/HoengSaan/rime-gukwan/wiki#%E9%97%9C%E6%96%BC%E6%93%B4%E5%B1%95%E8%A9%9E%E5%BA%AB)
### 漢英混打

漢英混打實現是參攷[优化 Rime 英文输入体验 - Dvel's Blog](https://dvel.me/posts/make-rime-en-better/)，基於[tumuyan/melt_eng](https://github.com/tumuyan/rime-melt)（[iDvel/rime-ice](https://github.com/iDvel/rime-ice)版）。隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。

- `gukwan-melt-eng.schema.yaml`：混打方案
- `gukwan-melt-eng.dict.yaml`：混打辭典
  - `en_dicts/en.dict.yaml`
  - `en_dicts/en_ext.dict.yaml`

### LUA腳本

本方案所有LUA腳本均有參攷[iDvel/rime-ice](https://github.com/iDvel/rime-ice)及相關文件，相關文件根據源文件許可發佈。

- unicode.lua：UNICODE碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT許可](https://mit-license.org/)發佈。
- lunar.lua：是日農曆，新曆轉舊歷，來自[boomker/rime-fast-xhup](https://github.com/boomker/rime-fast-xhup)，隨源文件以[LGPL 3.0許可](https://www.gnu.org/licenses/lgpl-3.0.en.html)發佈。
- calc_translator.lua：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之PR。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- autocap_filter.lua：自動大寫英文詞彙，作者爲@abcdefg233同@Mirtle，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。

以下腳本繁化並增添小小功能。爲避免文件被覆蓋，故改名。

- number_gukwan.lua：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense許可](https://unlicense.org/)，本文件亦不設限。
- time_gukwan.lua：以各種格式輸入是日日期時間，來自[amzxyz/rime_wanxiang](amzxyz/rime_wanxiang)。隨源文件以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。

### 其他

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件請參攷[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。

- [rime-cantonese-emoji](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字，隨源文件以[CC 0許可](https://creativecommons.org/public-domain/cc0/)發佈。
- `symbols-gukwan.yaml`：菊韻定製標點符號（類似Microsoft 日本語 IME）同特殊符號輸入。
- `菊韻.trime.yaml`：同文輸入法主題，基於[Wenti-D/Astralwelkin](https://github.com/Wenti-D/Astralwelkin)，隨源文件以[MIT許可](https://mit-license.org/)發佈。不同點如下：
  - 鍵值更改，允許一鍵反查（q鍵、p鍵、a鍵）。
  - 專用配色，參攷小欖特色菊花，但未夠膽用黃色驚太鮮豔，結果做變成屎黃色((o(；□；`)o))。如下：

<img src="pic\gukwan_trime.jpg" alt="gukwan_trime" style="zoom:25%;" />

## 銘謝

在此特別致謝於上文中所提及方案、字表、詞庫同腳本創作者，亦感謝以下書籍及網站的作者和編者。若無諸位努力，本人亦無法製作菊韻。

- 高然《中山方言誌》
- 何惠玲、馮國強《中山市沙田族羣的方音傳承及其民俗變遷》
- 中山市地方誌編撰委員會《中山市志(1979-2005)》
- 葉卉時《廣府方言順德話》
- [poem《廣韻字音表》](https://zhuanlan.zhihu.com/p/20430939)
- [嶺南粵音《泛粵大典》](https://jyutdict.org/)
- [zi.tools 字統网](https://zi.tools/)




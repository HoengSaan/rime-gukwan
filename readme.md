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

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，是爲改善粵語輸入體驗，支持漢英混打（中英混打），輸入日期・時間・節日・節氣等各種功能。菊韻亦可以用於輸入小欖話（含中山其他順德系方言）・順德話・蜑家話。

更多資訊請閱讀下文竝參攷[菊韻 – なかやま園](https://zonsan.fc2.page/?cat=123)。[關於如何安裝](#安裝)。

## 功能

### 多方言適應

菊韻可支持多地方言。已爲各種方言口音預設大量轉換規則同模糊音，方便定製。[具體異同](https://github.com/HoengSaan/rime-gukwan#%E6%96%B9%E6%A1%88)。

- 順德系（中山）
  - `gukwan-siulaam`（<ruby>小<rp>(</rp><rt>siu2</rt><rp>)</rp></ruby><ruby>欖<rp>(</rp><rt>laam5</rt><rp>)</rp></ruby>音）：以小欖話比較有代表性特徵製作，兼容新派發音，適合大多數小欖人。
    - `gukwan-siulaam-bofung`（<ruby>小<rp>(</rp><rt>siu2</rt><rp>)</rp></ruby><ruby>欖<rp>(</rp><rt>laam5</rt><rp>)</rp></ruby><ruby>寶<rp>(</rp><rt>bo2</rt><rp>)</rp></ruby><ruby>豐<rp>(</rp><rt>fung1</rt><rp>)</rp></ruby>音）：小欖鎮寶豐村，兼容新派發音。
  - `gukwan-waanglaan`（<ruby>橫<rp>(</rp><rt>waang4</rt><rp>)</rp></ruby><ruby>欄<rp>(</rp><rt>laan4</rt><rp>)</rp></ruby>音）：以橫欄鎮比較有代表性特徵製作，適合大多數橫欄人。
  - `gukwan-naamtau-naamsing`（<ruby>南<rp>(</rp><rt>naam4</rt><rp>)</rp></ruby><ruby>頭<rp>(</rp><rt>tau4</rt><rp>)</rp></ruby><ruby>南<rp>(</rp><rt>naam4</rt><rp>)</rp></ruby><ruby>城<rp>(</rp><rt>sing4</rt><rp>)</rp></ruby>音）：南頭鎮南城村
- 順德系（順德）
  - `gukwan-daailoeng`（<ruby>大<rp>(</rp><rt>daai6</rt><rp>)</rp></ruby><ruby>良<rp>(</rp><rt>loeng1</rt><rp>)</rp></ruby>音）：以大良比較有代表性特徵製作。
- 蜑家話
- 廣州話
  - `jyut6ping3-gw`：`rime-cantonese`菊韻版，增添菊韻所有功能以改善打字體驗
  - `gukwan-canton`：不建議使用
- 古代音
  - `gukwan-default`：構擬音，僅供參攷。
  - `gukwan-fanwan`：不完全正確，僅供參攷。

> [!NOTE]
>
> 除小欖音以外均以老派音製作，可能已不貼合實際情況，故：
>
> - 曉匣喻母細音字部份字跟廣州讀`j`，但未變齊。
>   - 如「爺」讀`he4`，但係「園」讀`jyun4`（本應讀`hyun4`）
>   - 由於個個方言都變化程度唔同，我一個人絕無辦法去執晒，只能設定兩種音都出到字。
>   - 如小欖話只有極少數作爲白讀音殘留，例如「穴」`hyut6`，「嫌」`him4`。則可以特例處理。
> - 師韻讀`y`定讀`i`？
>   - 其實理論上全部應該讀`y`，但係不能避免的人遇到隻唔識既字，就直情跟廣州音。此處不作改變，如不能辨別者，請手動更改方案。
> - 見系咸攝字`om`同`am`不分。
>   - 由於個個方言都變化程度唔同，我一個人絕無辦法去執晒，只能設定兩種音都出到字。
> - 各種白讀字
>   - 「螺」「朵」「蓑」「坐」等字讀`-oe`
>   - 「山」「斬」「減」「咸」等字讀`-e`
>   - 「應」讀`ing`
>   - 以上字對輸入影響不大，全部收錄在主字庫，不再另立。
>   - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
>   - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
>   - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`（「剩」`zing6`「嘥」`caai1`「贖」`zuk6`「煠」`zep6`已收錄在主字庫）
>   - 「婆」「茶」「糖」「田」等少部分送氣字無氣化（「柿」`zy2`「淡」`daam6`已收錄在主字庫）
>   - 「件」「解」「揀」「掛」等少部分無氣字送氣化（「舊」`kau6`已收錄在主字庫）
>   - 以上收錄在`gukwan-alt.dict.yaml`。

### 三拼輸入

菊韻支持竝默認開啓三拼，即所有漢字皆可以三鍵輸入（不含聲調），但用家仍然可以使用全拼（即輸入拼音完整形式——聲母+韻母+聲調）輸入。 學習成本較低。

寬式音標版：由於菊韻同時支持三拼同全拼，爲避免輸入全拼時發生轉換錯誤，故輸入三拼時不能顯示正確音標。

<img src="pic\key.png"/>

#### 子音

- 多數方言
  - 以`q`輸入`kw`：如「裙」`kwan`則爲`qan`
  - 以`x`輸入`gw`：如「轟」`gwang`則爲`xar`
  - 以`r`輸入`ng`：如「我」`ngo`則爲`ngo`（不支持單獨成韻，即「吳」`ng`無法以`r`輸入）
- 區分平翹日以之方言
  - 以`z`輸入`zh`（實質模糊音，默認關閉）
  - 以`c`輸入`ch`（實質模糊音，默認關閉）
  - 以`s`輸入`sh`（實質模糊音，默認關閉）
  - 以`q`輸入`kw`
  - 以`x`輸入`gw`
  - 以`r`輸入`ng`｜`ngi`｜`nj`：如「言」`ngin`則爲`rin`，如「仍」`njing`則爲`rir`

#### 母音

- 無韻尾情況（如`laa`，`loe`等）
  - 以`a`輸入`aa`：如「瓜」`gwaa`則爲`xa`
  - 以`y`輸入`yu`（`jyu`）：如「擧」`gyu`則爲`gy`
- 有韻尾情況（如`laang`，`loeng`等）
  - 以`e`輸入`oe`：如「涼」`loeng`則爲`ler`
  - 以`r`輸入`aa`：如「逛」`gwaang`則爲`xrr`
  - 以`y`輸入`yu`（`jyu`）:如「血」`hyut`則爲`hyt`
  - 以`u`輸入`eo`：如「論」`leon`則爲`lun`；
  - 以`r/e`輸入`ae`：如「斬」`zhaem`則爲`z(h)aam`｜`z(h)rm`｜`z(h)em`（僅`gukwan-default`）
  - 以`ui`輸入`ooi`如「淚」`looi`則爲`lui`（部份方言）

以`e`輸入`oe`是考慮`e`系韻母本身以白讀音爲主，較少使用。而`u`同`eo/oo`在多數方言下都爲互補，不影響輸入。

#### 其他

以下兩個簡拼默認關閉，無論開啓關閉都可以以三拼形式輸入。

- `ji`簡拼`j`：如「影」`jing`則爲`jr`（`jir`）
- `nji`簡拼`nj`：如「仍」`njing`則爲`njr`（`rir`｜`njir`）
- `wu`簡拼`u`：如「換」`wun`則爲`un`

<img src="pic\srmpir.png"/>

### 特殊輸入

支持漢英混打，各種特殊符號輸入，日期時間輸入等。

<img src="pic\showcase.png"/>

- **漢英混打：允許漢字英文混打，基於melt-eng。待完善**
- 繪文字（表情）：可以粵語輸入繪文字，默認關閉
- 符號：特殊符號輸入，鍵值爲`/`。[學習如何使用符號](https://github.com/HoengSaan/rime-gukwan/blob/main/symbols-gukwan.yaml)
- Unicode：以Unicode編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲`U`（unicode）
- 數字：以阿拉伯數字輸入大小寫數字以及大小寫金額，鍵值爲`S`（SHuZy/SauZy）；支持以下7種格式：
  - 二〇二五（數字小寫）
  - 貳零貳伍（數字大寫）
  - 〢〇〢〥（蘇州碼子）
    - 即花碼，由於本身特性不支持亦不需要小數點。[瞭解更多](https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90)
  - 二千〇二十五（數額小寫）
  - 貳仟零貳拾伍（數額大寫）
  - 二千〇二十五圓整（金額小寫）
  - 貳仟零貳拾伍圓整（金額大寫）
- 日期・時間・節日・節氣：
  - 【`/date`】日期（NJatKi/JatKi）：現代鍵值爲`vjk`｜`/jk`；古代鍵值爲`vrk`｜`/rk`；有多種格式，部份默認禁用
  - 【`/time`】時間（SHiGaen/SiGaan）：鍵值爲`vsg`｜`/sg`
  - 【`/week`】星期（SingKi）：鍵值爲`vsk`｜`/sk`
  - 【`/datetime`】日時（NJatSHi/JatSi）：現代鍵值爲`vjs`｜`/js`｜；古代鍵值爲`vrs`｜`/rs`；ISO 8601/RFC 3339格式日期時間，以東八區（UTC+8）爲準
  - 【`/weeknumber`】週數（Week Number）：鍵值爲`vwn`｜`/wn`；今年第幾周
  - 【`/timestamp`】時間戳（Time Stamp），鍵值爲`vts`｜`/ts`
  - 【`/lunar`】農曆（NungLik），鍵值爲`vnl`｜`/nl`
  - 【`/zithi`】節氣（ZitHi）：鍵值爲`vzh`｜`/zh`｜；廿四節氣同日期
  - 【`/festival`】節日（ZitNJat/ZitJat）：現代鍵值爲`vzj`｜`/zj`；古代鍵值爲`vzr`｜`/zr`；新舊曆節日同日期
  - 【`/info`】日期信息整合，鍵值爲`vday`｜`/day`（電話版中州韻多數不能正常顯示）
  - 直出，鍵值爲`N`+「`YYYYMMDD`」；有四種模式：「新曆」「新曆轉舊曆」「舊曆轉新曆」「新曆轉干支」
  - **鍵值已在腳本固定，如需修改須直接改變`time_gukwan.lua`或`time_gukwan_modern.lua`**
- 計數機：直接在RIME計數，鍵值爲`cC`（Calculator）。[學習如何使用計數機](https://github.com/gaboolic/rime-shuangpin-fuzhuma/blob/main/md/calc.md)
- 假名：以細階輸入平假名，大階輸入片假名，鍵值爲<code>`G</code> （gaa ming）。輸入方式同其他IME（如Microsoft IME、ATOK等）基本無區別
- 顏文字：以日文輸入各種顏文字，鍵值爲<code>`K</code>（kaomoji）
- 和文：實現半混打日文，基於[rime-kikwin](https://github.com/HoengSaan/rime-kikwan)，鍵值爲<code>`R</code>（romaji）

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
- 明月拼音（rime-luna_pinyin），官語普通話反查。鍵值爲<code>`P</code>（PuPing/PouPing）。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲<code>`C</code>（CoongKit/CongKit ）。
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀（現代音）反查。鍵值爲<code>`F</code>（FanDuk）。
- 兩分（[rime-loengfan](https://github.com/CanCLID/rime-loengfan)），粵語廣州話兩分拆字反查。鍵值爲<code>`L</code>（LoengFan）。

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
- 可輸入方言過少：自用爲主，將於未來處理。【正在處理】

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

## 方案

> [!NOTE]
>
> `xxx.xxx-ps.scheme.yaml`爲寬式音標版，寬式音標並不能完全代表實際發音。所有寬式音標版存儲在`/ps`。如需使用請自行將其移出。
>
> 以下方案並不能完全代表當地發音，請根據自身實際情況調整。

- `gukwan.schema.yaml`：調試用・自用（**請勿刪除，刪除後無法使用**）
- `jyut6ping3-gw.schema.yaml`：以菊韻配置調用`rime-cantonese`，支持菊韻所有功能。默認開啓三拼。

### 順德系方案

#### 順德系方言共通特徵

詳細可見[小欖話・沙田方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。（內容已過期，待更新）

- 多數不分來孃，即「南」`naam4`讀作「藍」`laam4`、「農」`nung4`讀作「龍」`lung4`。
- 古匣母（含少數云母合口字）部份字：即今時廣州話聲母`w`同韻腹`u/o`結合者，順德系方言聲母則爲`f`。
  - 大多數中山方言點只是部份符合規律，將「胡」「戶」「護」三小韻讀作`fu`。「垣」小韻讀作`fun`。但其他則全部廣州話，同廣州一樣，聲母爲`w`。
- 見組止攝開口三等字未裂化讀作`i`而非`ei`，如「其」`ki4`「起」`hi2`「機」`gi1`「紀」`gi3`等。
- 師韻字（即精莊組止攝開口三等字）讀作`y`而非`i`，如「資」`zy1`「師」`sy1`「字」`zy6`「此」`cy2`等。
- 見系遇攝三等字未裂化讀作`yu`而非`eoy`，如「區」`ky1`「去」`hy3`「車」`gy1`「巨」`gy6`等。
- 蟹攝合口一等字部份方言將部份字讀作`yu`而非`eoy`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
- 遇攝合口一等字除見系之外裂化爲`au`而非`ou`，如「度」`dau6`「無」`mau4`「做（作）」`zau6`「粗」`cau1`等。
- 效攝一等字發生元音融合，讀`o`，如「高」`go1`「刀」`do1`「毛」`mo4`「草」`co2`。
- 咸攝見系字依舊讀`om`，如「鴿」`gop3`「合」`hop6`「敢」`gom2`「柑」`gom1`等。
  - 但實際情況連多數中年人亦不分`om/op`同`am/ap`，同方言記錄有差別。故菊韻允許以`am/ap`音輸入`om/op`字。
- 白讀音豐富。
- 變調豐富，有一定規律但其豐富性導致方案無法完全還原其實態。尤其陽平字特殊變調之多，本人已放棄收錄。

以上特徵如無重申即無異。

### 小欖

- `gukwan-siulaam.schema.yaml`：小欖音
  - 本方案根據小欖鎮代表特徵製作。下爲重要特徵：
    - 小欖人多數人不分透曉（t/h），故可以h音打t（如「偸」`tau1`可打`hau1`）。
    - 小欖人多數人不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
    - 蟹攝合口一等字，廣州話讀`eoy`者，小欖話多讀作`yu`：
      - 端組、來母同心母讀作`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
      - 精組（除心母）多數人已裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`「催」`ceoy1`等，故不納入。
      - 此類字讀`ui`爲棺材音，故方案不採用。
- `gukwan-siulaam-bofung.schema.yaml`：小欖寶豐音
  - 本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖音主要區別：
    - 分辨透曉，ong/ok同oeng/oek可不分；eng/ek同en/et可不分。實際打字兩者皆可。
    - 蟹攝合口一等字變化同廣州話一樣，但有部分讀`oe`（見`gukwan-siulaam-bofung.dict.yaml`）

### 大良

- `gukwan-daailoeng.schema.yaml`：大良音
  - 本方案根據陳村音代表特徵製作。下爲重要特徵：
    - 不分來孃之外不分疑影，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
    - 不分`ing/ik`同`in/it`，故可以ing/it音打in/it（如「迫」`bik1`可打`bit1`）。
    - `yun/yt`老派讀`un/ut`，但因同`eon/eot`簡拼衝突故不採用。
    - 蟹攝合口一等字，廣州話讀`eoy`者，大良老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 廣州話聲母`w`同韻腹`u/o`結合者，大良聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

### 陳村

- `gukwan-cancyn.schema.yaml`：陳村音
  - 本方案根據陳村音代表特徵製作。下爲重要特徵：
    - 不分來孃之外不分疑影，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
    - 陳村音止攝字無發生裂化，故廣州話讀`ei`者，陳村仍舊讀`i`，如「皮」`pi4`「鼻」`bi6`「地」`di6`「四」`si3`。
    - 蟹攝合口一等字，廣州話讀`eoy`者，陳村老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 廣州話聲母`w`同韻腹`u/o`結合者，陳村聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

### 橫欄

- `gukwan-waanglaan.schema.yaml`：橫欄音
  - 本方案綜合橫欄各地鄉音——四沙（兩書合作人皆爲貼邊人）・六沙・橫東。
    - ong/ok歸oeng/oek，即「江」「薑」不分，皆讀`goeng1`。實際打字兩者皆可。
      - 橫東方面，兩個脣化聲母遇oeng/oek即展脣化。故「光」「江」「薑」不分，皆讀`goeng1`（「黃」則讀`woeng4`，不讀作`oeng4`）。
      - /oe/實際發音爲[yø]，如有需要可自行將方案調整爲yo或yoe以貼合實際發音。
    - 蟹攝合口一等字同廣州一樣爲`eoy`，並不讀作`yu`。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 《沙田方言》中，效攝一等記作`o`，但《中山方言誌》全部紀錄點都爲`ou`。此處採用《中山方言誌》記錄，請根據實際情況自行調整。（如需改請刪除146行、427行、503行井號）
    - 「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，橫欄仍保持其對`eoy`同`oi`對立。其中以六沙最爲完整。即「趣」`ceoy3`「菜」`coi3`「脆」`cooi3`不同音。
      - 其他方言點之中，蟹攝三等合口字讀`eoy`而非`ooi`。（如需改請在152行、429行、505行添加井號，竝刪除153行、430行、506行井號）
      - /ooi/實際發音爲[oø]，如有需要可自行將方案調整爲`ooy`以貼合實際發音。
      - /eoy/實際發音爲[øy]。
      - 《沙田方言》並無記載此對立。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將107行井號刪除，竝將107~110行裏邊個`xform`改成`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，橫欄聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。

### 南頭

- `gukwan-naamtau-naamsing.schema.yaml`：南頭南城音（或將刪除同其他南頭音合併）
  - 本方案根據《沙田方言》製作。下爲重要特徵：
    - ong/ok歸oeng/oek，而兩個脣化聲母遇oeng/oek即展脣化，故「光」「江」「薑」不分，皆讀`goeng1`（「黃」則讀`woeng4`，不讀作`oeng4`）。實際打字兩者皆可。
    - 蟹攝合口一等字，廣州話讀`eoy`者，南城音有部份讀作作`yu`：
      - 端組同來母讀`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「雷」`sy3`等。
      - 精組多數人則裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`「催」`ceoy1`等。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。

### 參攷用方案

- `gukwan-default.schema.yaml`：菊韻音（構擬音）根據菊韻標準所構擬之古音，較分韻複雜。
- `gukwan-fanwan.schema.yaml`：分韻音
  - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用眞正分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)
- `gukwan-canton.schema.yaml`：廣州音
  - 準確來講此方案係廣州風，並不能準確反映所有廣州發音。若欲使用眞正廣州音打字，請使用`jyut6ping3-gw.scheme.yaml`

> [!TIP]
>
> [關於如何定製方案](https://github.com/rime/home/wiki/CustomizationGuide)

## 文件結構・許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0許可](cc-by-nc-sa)發佈。下列擧除方案文件外其他重要文件。

### 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用rime-cantonese部份詞庫同粵語八股文。位置爲`/gw_dicts`。`gukwan-alt.dict.yaml`同`gukwan-alt-asp.dict.yaml`特供部份方言使用。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字表
  - `gukwan.chars1.dict.yaml`：廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：近代字異體字異音訓讀增補
    - 粵字平翹、日以之分參攷梧州話
  - `gukwan.chars3.dict.yaml`：廣韻字近代字非通用增補（特供部份方言使用）
  - `gukwan.chars4.dict.yaml` ：廣韻字近代字非通用增補（特供部份方言使用）
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
- 何惠玲、馮國強《中山市沙田族羣的方音傳承及其民俗變遷》（以上皆簡稱爲《沙田方言》
- 中山市地方誌編撰委員會《中山市志(1979-2005)》
- 葉卉時《廣府方言順德話》
- [poem《廣韻字音表》](https://zhuanlan.zhihu.com/p/20430939)
- [嶺南粵音《泛粵大典》](https://jyutdict.org/)
- [zi.tools 字統网](https://zi.tools/)




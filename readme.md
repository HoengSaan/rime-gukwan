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

# 簡介

This is a schema based on [Rime Input Method](https://rime.im/).

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，是爲改善粵語輸入體驗，支持漢英混打（中英混打），輸入日期・時間・節日・節氣等各種功能。

菊韻本身是爲輸入順德系方言設計，可用於輸入小欖話・順德話等順德系方言。

菊韻自用爲主。

更多資訊請閱讀下文竝參攷[菊韻 – なかやま園](https://zonsan.fc2.page/?cat=123)。[關於如何安裝](#安裝)。

## 功能

### 多方言適應

菊韻可支持多地方言。已爲各種方言口音預設大量轉換規則同模糊音，方便自行定製。（需對Regex同音韻學有基本瞭解）[具體異同](https://github.com/HoengSaan/rime-gukwan#%E6%96%B9%E6%A1%88)。

- 順德系——中山市
  - `gukwan-siulaam`【<ruby>小<rp>(</rp><rt>siu2</rt><rp>)</rp>欖<rp>(</rp><rt>laam5</rt><rp>)</rp></ruby>鎮】：以小欖話比較有代表性特徵製作，兼容新派發音。
    - `gukwan-siulaam-bofung`（小欖<ruby>寶<rp>(</rp><rt>bo2</rt><rp>)</rp>豐<rp>(</rp><rt>fung1</rt><rp>)</rp></ruby>音）：小欖鎮寶豐村，兼容新派發音。
  - `gukwan-dungsing`：（東昇音）：舊東昇鎮
  - `gukwan-waanglaan`【<ruby>橫<rp>(</rp><rt>waang4</rt><rp>)</rp>欄<rp>(</rp><rt>laan4</rt><rp>)</rp></ruby>鎮】：以橫欄鎮比較有代表性特徵製作。
  - `gukwan-naamtau`【<ruby>南<rp>(</rp><rt>naam4</rt><rp>)</rp></ruby><ruby>頭<rp>(</rp><rt>tau4</rt><rp>)</rp></ruby>鎮】：
    - `gukwan-naamtau-naamsing`（南頭<ruby>南<rp>(</rp><rt>naam4</rt><rp>)</rp>城<rp>(</rp><rt>sing4</rt><rp>)</rp></ruby>音）：南頭鎮南城村
    - `gukwan-naamtau-paaihom`（南頭<ruby>排<rp>(</rp><rt>naam4</rt><rp>)</rp>坎<rp>(</rp><rt>sing4</rt><rp>)</rp></ruby>音）：南頭鎮排坎村
  - `gukwan-guzan-hoizau`【古鎮海洲音】：古鎮海洲音
- 順德系——順德市
  - `gukwan-daailoeng`（<ruby>大<rp>(</rp><rt>daai6</rt><rp>)</rp>良<rp>(</rp><rt>loeng1</rt><rp>)</rp></ruby>音）：以大良話比較有代表性特徵製作。
  - `gukwan-cancyn`（<ruby>陳<rp>(</rp><rt>can4</rt><rp>)</rp>村<rp>(</rp><rt>cyun1</rt><rp>)</rp></ruby>音）：以陳村話比較有代表性特徵製作。
  - `gukwan-gwanon`（<ruby>均<rp>(</rp><rt>gwan1</rt><rp>)</rp>安<rp>(</rp><rt>on1</rt><rp>)</rp></ruby>音）【未製作】
- 香山系
  - `gukwan-sekki`（<ruby>石<rp>(</rp><rt>sek6</rt><rp>)</rp>歧<rp>(</rp><rt>ki4</rt><rp>)</rp></ruby>音）：以石歧話新派音製作。（老派音建議自行製作字表）
- 廣州話
  - `jyut6ping3-gw`：完全使用`rime-cantonese`字表詞庫，增添菊韻所有功能以改善打字體驗

> 除小欖音以外均以老派音製作，方案不能直接同新派音兼容，可能已不貼合實際情況，故：
>
> - 曉匣喻母細音字部份字跟廣州讀`j`，但未變齊。
>  - 如「爺」讀`he4`，但係「園」讀`jyun4`（本應讀`hyun4`）
>   - 由於個個方言都變化程度唔同，我一個人絕無辦法去執晒，只能設定兩種音都出到字。
>   - 如小欖話只有極少數作爲白讀音殘留，例如「穴」`hyut6`，「嫌」`him4`。則可以特例處理。
> - 師韻讀`y`定讀`i`？
>   - 其實理論上全部應該讀`y`，但係不能避免的人遇到隻唔識既字，就直情跟廣州音。此處不作改變，如不能辨別者，請手動更改方案。
> - 見系咸攝字`om`同`am`不分。
>   - 由於個個方言都變化程度不一，以我
> - 關於白讀字請見[方案](https://github.com/HoengSaan/rime-gukwan#方案)

### 三拼輸入

菊韻支持竝默認開啓三拼，即所有漢字皆可以三鍵輸入（不含聲調）。

**三拼輸入不影響聲調輸入**，用家仍然可以使用傳統打法——即全拼，輸入拼音完整形式：聲母+韻母+聲調，聲調可以省畧。

如不能接受三拼輸入，下文有解說如何關閉三拼。

<img src="pic\key.png"/>

#### 子音

- 不區分平翹日以之方言（多數方言）
  - 以`q`輸入`kw`：如「裙」`kwan`則爲`qan`
  - 以`x`輸入`gw`：如「轟」`gwang`則爲`xar`
  - 以`r`輸入`ng`：如「我」`ngo`則爲`ngo`（不支持單獨成韻，即「吳」`ng`無法以`r`輸入）
- 區分平翹日以之方言（僅`gukwan-default`同`gukwan-fanwan`）
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
  - 以`u`輸入`eo`：如「論」`leon`則爲`lun`
  - 以`r/e`輸入`ae`：如「斬」`zhaem`則爲`z(h)aam`｜`z(h)rm`｜`z(h)em`（僅`gukwan-default`）
  - 以`u`輸入`oo`【僅限`ooi`】：如「淚」`looi`則爲`lui`（部份方言）
  - 以`o`輸入`oo`【僅限`oong/ook`】：如「朗」`loong`則爲`lor`（部份方言）

以`e`輸入`oe`是考慮`e`系韻母本身以白讀音爲主，較少使用。而`u`同`eo/oo`；`o`同`oo`在多數方言下都爲互補，不影響輸入。

#### 其他

以下兩個簡拼默認關閉，無論開啓關閉都可以以三拼形式輸入。

- `ji`簡拼`j`：如「影」`jing`則爲`jr`（`jir`）
- `nji`簡拼`nj`：如「仍」`njing`則爲`njr`（`rir`｜`njir`）
- `wu`簡拼`u`：如「換」`wun`則爲`un`

<img src="pic\srmpir.png"/>

#### 關閉三拼

三拼是本人代替全拼之做法，其會影響首拼出字之效率。若不想使用三拼，可在方案文件關閉以下選項（行頭加井號）：

```yaml
    - derive/^kw/q/                         # 簡拼(kw->q)
    - derive/^gw/x/                         # 簡拼(gw->q)
    #- derive/^nj/r/                         # 簡拼(nj->r)
    - derive/^ng([aeiouy])/r$1/             # 簡拼(ng->r)
    - derive/([aeiouy])ng/$1r/              # 簡拼(ng->r)

    - derive/aa(?=\d)/a/                    # 簡拼(aa->a)【毋須關閉】
    - derive/aa([iumnptkr]|ng)/r$1/         # 簡拼(aa->r)
    - derive/^jy?([aeiou])/y$1/             # 簡拼(jy->y)【毋須關閉】
    - derive/yu(?!ng|k)/y/                  # 簡拼(yu->y)【毋須關閉】
    - derive/oe(ng|k|r)/e$1/                # 簡拼(oe->e)
    - derive/eo([ntiy])/u$1/               # 簡拼(eo->u)
    - derive/oo(i|y)/u$1/                   # 簡拼(oo->u)
```



### 特殊輸入

**支持漢英混打**，各種特殊符號輸入，日期時間輸入等。

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

### 字表詞庫

菊韻字表詞庫以深筆爲準，但可以轉換爲簡筆。隨基本字表詞庫之外，菊韻亦有小欖話特色詞庫以及廣東地名詞庫。

> [!NOTE]
>
> 菊韻可調用擴展詞庫，但需要手動下載。[gukwan-extended.dict.yaml](https://github.com/HoengSaan/rime-gukwan/blob/main/gukwan-extended.dict.yaml)內有說明如何獲取。由於擴展詞庫過大，低性能設備不建議使用，可能導致部署失敗。

### 反查支持

多數人士通曉廣州話、普通話卻未必熟識自己鄉下發音，故設各種反查。反查亦可用來打菊韻難以輸入或無收錄既非常用字。

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>` </code>。
- 明月拼音（rime-luna_pinyin），官語普通話反查 。鍵值爲<code>`P</code>（PuPing/PouPing）。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲<code>`C</code>（CoongKit/CongKit ）。
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀（現代音）反查。鍵值爲<code>`F</code>（FanDuk）。
- 兩分（[rime-loengfan](https://github.com/CanCLID/rime-loengfan)），粵語廣州話兩分拆字反查。鍵值爲<code>`L</code>（LiongFan/LoengFan）。

> [!NOTE]
> 
> **粵拼、訓讀、兩分須安裝方可使用**，安裝方法請參攷[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。如需使用其他方案反查，請自行定製方案。

### 問題・未來方向

- 字詞發音：
  - 本人無法亦無有可能去保證所有漢字發音正確。尤其因爲菊韻詞庫多數無輸入碼，有多音字既單詞發音必然有誤。
  - 雖然菊韻支持使用聲調輸入，但本人並不能確保所有字詞聲調正確。尤其考慮到以小欖話等方言變調遠比廣州話豐富，以我一人之力斷無可能完善。
- 簡轉繁問題：
  - `gukwan.kwongtung.dict.yaml`數據來源係簡筆字，本人亦仔細審覈過，但都無法保證三萬幾條地名全數正確。
  - jyut6ping3部份詞庫（例如`jyut6ping3.phrase.dict.yaml`）有明顯簡轉繁痕跡，已超出本人處理範圍。
- 語言模型：
  - 語言模型是改善輸入體驗最有效方法，但粵語同官話語言模型不能完全通用，需自行訓練，已超出本人能力範圍。
- <del>漢英混打：由於不明原因gukwan不能使用混打，本人已嘗試多次。將解決詞庫問題後再行處理。</del>**【已解決】**
- 漢英混打開關：待處理。
- 可輸入方言過少：自用爲主，將於未來處理。【正在處理】

## 安裝

以下僅解說大致流程，具體請見[如何在RIME輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。d

1. 安裝RIME
   1. WINDOWS：[Weasel 小狼毫](https://github.com/rime/weasel)
   2. MacOS：[Squirrel 鼠鬚管](https://github.com/rime/squirrel)｜[fcitx5-macos](https://github.com/fcitx-contrib/fcitx5-macos)
   3. Linux：[ibus](https://github.com/ibus/ibus)→[ibus-rime](https://github.com/rime/ibus-rime)｜[fcitx5](https://github.com/fcitx/fcitx5)→[fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)
   4. Android：[同文輸入法](https://github.com/osfans/trime)｜[fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)→[fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)

2. 安裝以下倉庫
   1. **rime-gukwan**（**本方案**）
   2. [rime-cantonese](https://github.com/rime/rime-cantonese)（**必選**，用於廣州話反查、八股文、部份詞庫）
   3. [rime-kunyomi](https://github.com/sgalal/rime-kunyomi/)（**可選**，用於和語訓讀反查）
   4. [rime-loengfan](https://github.com/CanCLID/rime-loengfan)（**可選**，用於廣州話拆字反查）
   5. [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（**可選**，若閣下已刪除則須重新安裝，否則無法使用官話反查）
   6. [rime-cangjie](https://github.com/rime/rime-cangjie)（**可選**，若閣下已刪除則須重新安裝，否則無法使用倉頡反查）
   7. [rime-kikwin](https://github.com/Hoengsaan/rime-kikwin/)（**可選**，用於日文半混打，低性能設備建議關閉，只使用`rime-kanas`同`rime-kaomoji`）

3. 設定方案，重新部署

## 定製

部份用家可根據自身情況添加以下字音到用戶字庫。

### 必讀參攷文章

定製可參攷[如何定製菊韻 – なかやま園](https://zonsan.fc2.page/?p=1569)，但當真要定製中州韻方案，<b style="color:red;">懇請閣下閱讀以下文章</b>：

- [中州韻維基 - SpellingAlgebra](https://github.com/rime/home/wiki/SpellingAlgebra)
- [amzxyz - Patch方法论](https://github.com/amzxyz/rime_wanxiang_pro/blob/main/custom/patch%E6%96%B9%E6%B3%95%E8%AE%BA.md)
- [oh-my-rime - 配置教程](https://www.mintimate.cc/zh/guide/)

## 拼音

打字方式仍遵從當年`rime-jyutping`基本原則。

<img src="pic\gamjam1.png" style="zoom:50%;" />

<img src="pic\gamjam2.png"/>

以上調值爲小欖話，僅供參攷。部份方言僅有9個或8個聲調（含特殊調），香山系方言只有6個甚至更少。

古代音請參攷[菊韻拼音表 – なかやま園](https://zonsan.fc2.page/?p=1583)，其他可參攷[順德系方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。

### 粵拼同擴展粵拼

菊韻拼音方案基於[擴展粵拼](https://jyutjam.org/j++/)，現代音可直接以[粵拼](https://jyutping.org/)輸入。

不少方音同一音位發音同廣州竝不盡同，但爲方便輸入，如果粵拼可以表達，則全部用粵拼表達。只有粵拼不可表達之音位，方用擴展粵拼。

以南頭排坎話爲例子，其江攝宕攝仍保留有介音：

- 「江」韻母讀/ong/，對應廣州話ong，故可直接用粵拼現有`ong`。
- 「鋼」韻母讀/yoong/，廣州話無對應音位，故使用擴展粵拼`oong`。爲打字方便，`ong`亦可使用。
- 「薑」韻母讀/yong/，對應廣州話oong，故可直接用粵拼現有`oeng`。而擴展粵拼`iong`亦可使用。
- 「廣」韻母讀/wong/，對應廣州話wong，故可直接用粵拼現有`wong`。

### `gu/ku`同`gwu/kwu`

【以下僅限擁有圓脣聲母方言】

雖然絕大多數字典同記音不分辨`gu/ku`同`gwu/kwu`，但兩者並非同音位。`gwu`同`kwu`最爲常見，多數字都讀作圓脣而非展脣。而`gu`同`ku`一般爲擬聲擬態詞所用，非常少見。

亦有部份方言將效攝讀作`u`，聲母仍爲展脣。即「高」讀`gu1`而「姑」讀`gwu1`。菊韻目前無此類方言。

因以上兩種原因，菊韻目前不分，皆作`gu/ku`。

### 特殊調

【以下僅適用於部份中山市順德系方言】

2\*並不如廣州話「新入」，只見於入聲字變調，如「子」白讀`zaai2*`就同陰上調值（通常爲24，而特殊調多爲35）不一。此調亦用作表達過去、完成之文法意味。超高陰平只出現於陰平連續變調。

爲免麻煩，特殊調打字同2（陰上）通用。

# 方案

> [!NOTE]
>
> <del>`xxx.xxx-ps.scheme.yaml`爲寬式音標版，寬式音標並不能完全代表實際發音。所有寬式音標版存儲在`/ps`。如需使用請自行將其移出。</del>**音標版方案已被放棄，不再維護。**
>
> **以下方案並不能完全代表當地發音，請根據自身實際情況調整。**
>
> <b style="color:red;">由於本人所寫轉換規則有缺陷，導致拼音提示不準確，敬請見諒。</b>

- `gukwan.schema.yaml`：基底文件（<b style="color:red;">請勿刪除，刪除後所有方案都無法使用</b>）
- `jyut6ping3-gw.schema.yaml`：三拼版`rime-cantonese`（廣州話），支持菊韻所有功能。
- `jyut6ping3-gw-cp.schema.yaml`：關閉三拼功能，支持菊韻除三拼以外一切功能。

### 白讀字

以下白讀字竝非適用於所有方言。

- 以下字較爲共通，且對輸入影響不大，全部收錄在主字庫，不再另立。
  - 「螺」「朶」「鏟」「墮」等字讀`-oe`
  - 「邊」「扁」「癲」「見」等字讀`-e`
  - 「山」「斬」「減」「咸」等字讀`-e`（統一爲ae再轉換，故拼音提示仍爲ae，此爲菊韻輸入法遺留問題）
  - 「應」「拎」「煙」等字讀零聲母（此字現代少見，而香山系方言老派無論文白皆讀零聲母）
  - 短`a`變長`a`（aa）：「第」`daai6`「仔」`zaai2`「洗」`saai2`；「某・畝」`maau5`「謀・繆・謬」`maau4`「貿・茂」`maau6`；「侄・姪」`zaat2`「甩」`laat1`
  - 不成規模：「現」`ngin6`「鏟」`coen2`「玩」`faan2`「閂」`soen1`「凝・迎」讀`nging4`「處」`syu3`「姊」`zei2`等，不勝枚擧。
- 以下字收錄在`gukwan-alt.dict.yaml`同`gukwan-alt-asp.dict.yaml`
  - 「虐」「若」「業」「仰」等疑日母字讀`h`
  - 「亦」「姚」「盈」「芫」等字補全
- 以下字收錄在`gukwan-asp.dict.yaml`同`gukwan-alt-asp.dict.yaml`
  - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
  - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
  - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`（「剩」`zing6`「嘥」`caai1`「贖」`zuk6`「煠」`zep6`「塞」`zak1`已收錄在主字庫）
  - 「婆」「茶」「糖」「田」等少部分送氣字無氣化（「柿」`zy2`「淡」`daam6`已收錄在主字庫）
  - 「件」「解」「揀」「掛」等少部分無氣字送氣化（「舊」`kau6`已收錄在主字庫）

## 順德系方言

順德系方言主要分佈於順德市同其周邊，如中山，南海，番禺等。

順德市方面主要可分爲四種，①以大良爲中心，同周邊容奇、桂州、倫敎、勒流爲一類；②以陳村爲中心，同周邊北滘、樂從爲一類；③以龍江爲中心，同周邊龍山、里海爲一類，部份音韻特徵同小欖有共通點；④均安鎮。

中山市方面則有兩種，①以小欖爲中心爲一類；②遠離小欖竝帶有一定蜑家特徵爲一類。

南海，番禺方面目前無計劃。

### 順德系方言共通特徵

主要指出同廣州話異同，以小欖話爲準：

- 多數不分來孃，即「南」`naam4`讀作「藍」`laam4`、「農」`nung4`讀作「龍」`lung4`。
- 古匣母（含少數云母合口字）部份字：即今時廣州話聲母`w`同韻腹`u/o`結合者，順德系方言聲母則爲`f`。
  - 大多數中山方言點只是部份符合規律，將「胡」「戶」「護」三小韻讀作`fu`。「垣」小韻讀作`fun`。其他已大幅向廣州貼近，聲母讀`w`。
- 見組止攝開口三等字未裂化讀作`i`而非`ei`，如「其」`ki4`「起」`hi2`「機」`gi1`「紀」`gi3`等。而陳村則完全無裂化。
- 師韻字（即精莊組止攝開口三等字）讀作`y`而非`i`，如「資」`zy1`「師」`sy1`「字」`zy6`「此」`cy2`等。
- 見系遇攝三等字未裂化讀元本發音`yu`而非廣州發音`eoy`，如「區」`ky1`「去」`hy3`「車」`gy1`「巨」`gy6`等。
- 蟹攝合口一等字本應讀`ui`，部份方言則變作`yu`，而非廣州發音`eoy`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
  - 通常精母先變`eoy`，清母兩種情況都有，而其他則變`yu`。
- 部份方言遇攝合口一等字除見系之外裂化爲`au`而非`ou`，如「度」`dau6`「無」`mau4`「做（作）」`zau6`「粗」`cau1`等。
  - 亦有部份方言低化爲`o`。
- 部份方言效攝一等字發生元音融合，讀`o`，如「高」`go1`「刀」`do1`「毛」`mo4`「草」`co2`。
  - 亦有部份方言讀`au`，或同廣州發音一樣讀`ou`。有甚者讀`oo`，同`o`保持對立（需檢查）。均安則同官話一樣讀`aau`。
- 咸攝見系字仍讀`om`，如「鴿」`gop3`「合」`hop6`「敢」`gom2`「柑」`gom1`等。
  - 但實際情況連多數中年人亦不分`om/op`同`am/ap`，同方言記錄有差別。故菊韻允許以`am/ap`音輸入`om/op`字。
- 【老派】順德市大良、陳村、均安以及中山市小欖等無`ak`，皆讀`aak`。
- 白讀音豐富。
- 變調豐富，有一定規律但其豐富性導致方案無法完全還原其實態。尤其陽平字特殊變調之多，本人已放棄收錄。

以上特徵如無重申即無異。

### 中山

#### 小欖

小欖鎮位於中山市北部，亦名菊城、欖鎮。同順德市均安鎮接壤，爲中山工業重鎮。小欖多數人講小欖話（順德系方言），僅沙口講蜑家話（受小欖話嚴重影響）。

- `gukwan-siulaam.schema.yaml`：小欖音
  - 本方案根據小欖鎮代表特徵製作。下爲重要特徵：
    - 多數人不分透曉（t/h），故可以h音打t（如「偸」`tau1`可打`hau1`）。
    - 「胡」「戶」「護」三小韻`wu/fu`混讀。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 蟹攝合口一等字，廣州話讀`eoy`者，小欖話多讀作`yu`：
      - 端組、來母同心母讀作`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
      - 精組（除心母）多數人讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`「催」`ceoy1`等。
      - 此類字讀`ui`爲棺材音，故方案不採用。
- `gukwan-siulaam-bofung.schema.yaml`：小欖寶豐音
  - 本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖音主要區別：
    - 分辨透曉，ong·ok同oeng·oek可不分；eng·ek同en·et可不分。實際打字兩者皆可。
    - 「胡」「戶」「護」三小韻讀`fu`。
    - 蟹攝合口一等字變化同廣州話一樣，但有部分讀`oe`（見`gukwan-siulaam-bofung.dict.yaml`）

##### 東昇

東昇本屬小欖，86年被劃出，21年被劃返去小欖鎮。

坦背本分屬欖鎮同隆鎮，新中國後分去沙蓢，84年設區，86年設鎮，99年併入東昇，21年跟東昇一同併入欖鎮。

- `gukwan-dungsing.schema.yaml`：東昇音

  - 本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖話主要區別：
    - 分辨透曉
    - ong·ok同oeng·oek不分，全部讀`oe`。實際打字兩者皆可。
    - 「胡」「戶」「護」三小韻讀`fu`，無混。
    - 蟹攝合口一等字精組全面變化爲`eoy`。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 曉匣喻細音字讀`h`而非`j`，但已大幅廣州化。
  - 根據《中山方言誌》高沙音同東昇音區別爲：
    - 遇攝合口一等字裂化同小欖一樣爲`au`，而非`ou`。
      - 請符合此項用家在98行添加井號，竝刪除97行井號。
    - 分辨ong·ok同oeng·oek /yø/。
      - 請符合此項用家在170行、171行、374行添加井號

  - 根據《中山方言誌》太平音同東昇音主要區別：
    - 廣州話聲母`w`同韻腹`u/o`結合者，太平聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 請符合此項用家刪除42行、43行、313行、314行井號
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。
    - 江攝除莊組外讀`ong /yong/`，江攝莊組同宕攝開口讀`oeng /yeong/`，宕攝合口讀`wong /wyong/`。
      - 請符合此項用家先在130行、170行、171行、374行添加井號，竝刪除179行同375行井號。
  - 根據《中山方言誌》坦背音同東昇音主要區別：
    - 曉谿合口不讀脣齒，如「灰」讀`hui1`，「戶」讀`hu6`、不同「父」`fu6`混。
      - 請符合此項用家在62行、63行、324行、325行添加井號。
    - 部份古全濁字不送氣，即「盤」讀`bun4`等
      - 請符合此項用家刪除221行井號。
    - 江攝除莊組外讀`ong /yong/`，江攝莊組同宕攝開口讀`oeng /yeong/`，宕攝合口讀`wong /wyong/`。即「鋼」讀`goeng1`但「江」讀`gong1`，其他音位不變。
      - 請符合此項用家先在130行、170行、171行、374行添加井號，竝刪除179行同375行井號。

#### 橫欄

- `gukwan-waanglaan.schema.yaml`：橫欄音
  - 本方案綜合橫欄各地鄉音——四沙（兩書合作人皆爲貼邊人）・六沙・橫東。
    - ong/ok歸oeng/oek，即「江」「薑」不分，皆讀`goeng1`。實際打字兩者皆可。
      - 橫東方面，兩個脣化聲母遇oeng/oek即展脣化。故「光」「江」「薑」不分，皆讀`goeng1`（「黃」則讀`woeng4`，不讀作`oeng4`）。
      - /oe/實際發音爲[yø]，如有需要可自行將方案調整爲yo或yoe以貼合實際發音。
        - 如需修改鍵值，需同時修改三拼規矩。
    - 蟹攝合口一等字同廣州一樣爲`eoy`，並不讀作`yu`。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 《沙田方言》中，效攝一等記作`o`，但《中山方言誌》全部紀錄點都爲`ou`。此處採用《中山方言誌》記錄，請根據實際情況自行調整。（如需改請刪除77行、335行井號）
    - 「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，橫欄仍保持其對`eoy`同`oi`對立。其中以六沙最爲完整。即「趣」`ceoy3`「菜」`coi3`「脆」`cooi3`不同音。
      - 其他方言點之中，蟹攝三等合口字讀`eoy`而非`ooi`。（如需改請在81行、337行添加井號，竝刪除82行、338行井號）
      - /ooi/實際發音爲[oø]，如有需要可自行將方案調整爲`ooy`以貼合實際發音。
      - /eoy/實際發音爲[øy]。
      - 《沙田方言》並無記載此對立。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37行井號刪除，竝將37~40行`xform`改成`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，橫欄聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。

參攷：《沙田方言》《中山方言誌》

#### 古鎮

古鎮亦被稱之爲燈都，顧名思義，其主要產業即爲燈。古鎮臨近江門，只有海洲係講順德系方言，曹步同古鎮則主要講四邑系方言。

由於菊韻本意是爲順德系方言製作方案，故目前竝無考慮製作四邑系方言。

- `gukwan-guzan-hoizau.schema.yaml`：海洲音
  - 本方案根據海洲音代表特徵製作。下爲重要特徵：
    - 區分來孃。
    - 脣化聲母遇o消失，即「過」「個」不分，皆讀`go3`
    - 見系遇攝三等字裂化，讀`eoy /øy/`，如「區」`keoy1`「去」`heoy3`「車」`geoy1`「巨」`geoy6`等。
    - 「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，海洲止攝同廣州一樣變`eoy`但蟹攝同`oi`合流。
    - 效攝一等字讀`au`而非`ou`，如「高」`gau1`「刀」`dau1`「掃」`sau3`「毛」`mau4`
  - 以下竝非出自《中山方言誌》，而爲本人所知：
    - 遇攝合口一等字除見系之外裂化爲`ou`，但亦有讀`au`話者。
      - 請讀`au`用家在98行添加井號，竝刪除97行井號。
    - 見組止攝開口三等字已裂化讀`ei`，如「其」`kei4`「起」`hei2`「機」`gei1`「紀」`gei3`等。
  - 以下並無資料證明，僅爲猜測：
    - 其蟹攝合口一等字變化應同小欖。

參攷：《中山方言誌》

#### 東鳳

#### 阜沙

#### 三角

#### 南頭

- `gukwan-naamtau-naamsing.schema.yaml`：南頭南城音
  - 本方案根據《沙田方言》製作。下爲重要特徵：
    - ong/ok歸oeng/oek，而兩個脣化聲母遇oeng/oek即展脣化，故「光」「江」「薑」不分，皆讀`goeng1`（注意：「黃」仍讀`woeng4`，不讀作`oeng4`）。實際打字兩者皆可。
    - 蟹攝合口一等字，廣州話讀`eoy`者，南城音有部份讀作作`yu`：
      - 端組同來母讀`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「雷」`sy3`等。
      - 精組多數人則裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`「催」`ceoy1`等。
    - 脣化聲母遇o消失，即「過」「個」不分，皆讀`go3`
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
- `gukwan-naamtau-paaihom.schema.yaml`：南頭排坎音
  - 本方案根據《中山市誌》製作。下爲重要特徵：
    - 本人所有資料中唯一江攝宕攝分四種：「江<sup>江攝</sup>」讀`ong`「窗<sup>江攝莊組・宕攝開三</sup>」讀`yong`（僅作顯示，默認不用`yong`，鍵值爲`iong/oeng`）「宕<sup>宕攝</sup>」讀`yoong`（僅作顯示，默認不用，鍵值爲`oong`打）「廣<sup>宕攝合口</sup>」讀`wong`
      - 如需修改鍵值，需同時修改三拼規矩。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 效攝一等字發音同廣州一樣爲`ou`：「好」`hou2`「逃」`tou4`「早」`zou2`「掃」`sou3`等。
    - 廣州話聲母`w`同韻腹`u/o`結合者，排坎聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。
    - 少部分送氣字無氣化
  - 以下並無資料證明，僅爲猜測：
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37行井號刪除，竝將37~40行`xform`改成`derive`。

參攷：《沙田方言》《中山方言誌》

#### 浪網

#### 黃圃

#### 沙蓢

#### 港口

### 順德

#### 大良

- `gukwan-daailoeng.schema.yaml`：大良音
  - 本方案根據大良音代表特徵製作。下爲重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 不分`ing/ik`同`in/it`，故可以in/it音打ing/ik（如「迫」`bik1`可打`bit1`）。
    - `yun/yt`老派讀`un/ut`，但因同`eon/eot`簡拼衝突故不採用。
    - 蟹攝合口一等字，廣州話讀`eoy`者，大良老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37行井號刪除，竝將37~40行`xform`改成`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，大良聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

#### 陳村

- `gukwan-cancyn.schema.yaml`：陳村音
  - 本方案根據陳村音代表特徵製作。下爲重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 陳村音止攝字無發生裂化，故廣州話讀`ei`者，陳村仍舊讀`i`，如「皮」`pi4`「鼻」`bi6`「地」`di6`「四」`si3`。
    - 蟹攝合口一等字，廣州話讀`eoy`者，陳村老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已裂化讀`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37行井號刪除，竝將37~40行`xform`改成`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，陳村聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

#### 均安【未製作】

- `gukwan-gwanon.schema.yaml`：均安音

  - 下爲均安話重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以aak音打ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 效攝一等字讀`aau`，如「高」`gaau1`「刀」`daau1`「掃」`saau3`「毛」`maau4`
    - 山攝開口一等字陽聲韻見系不讀`on`讀`aan`，如「漢」`haan3`「岸」`ngaan6`「安」`aan3`「乾」`gaan1`，但入聲中新派同廣州話一樣，只有少數作爲白讀字保留，如「割」`gaat3`「渴」`haat3`。
    - 蟹攝合口一等字，廣州話讀`eoy`者，均安話多讀作`yu`：
      - 端組、來母同心母讀作`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
      - 精組（除心母）多數人則讀`ooi`（同`oi`無對立），如「最」`zoi3`「罪」`zoi6`「催」`coi1`等。
    - 遇攝三等字裂化者同`ooi音`，即廣州話讀`eoy`者，均安話均讀作`ooi`（同`oi`無對立），如「女」`noi5`「旅」`loi5`「醉」`zoi3`「隨」`coi4`
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37行井號刪除，竝將37~40行`xform`改成`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，均安聲母則爲`f`，如「黃」`fong4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 均安有部份讀`h`，如「慌」`hong1`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將42~44行`xform`改成`derive`。
    - 「火」「過」讀`u`
    - 「我」「個」等白讀讀`oi`，均安則讀`aai`。

    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

## 香山系方言

香山系方言今時勢微，主要分佈在石岐鎮（今石歧街道）、南區（環城）、東區、張家邊（今中山港街道），石歧周邊地區亦有分佈。中山以外，珠海部份地區，如唐家、金<ruby>鼎<rp>(</rp><rt>deng2</rt><rp>)</rp></ruby>、前山、南屏亦有分佈。澳門曾經亦是講香山系方言，由於歷史因素，今時絕大多數人都操廣州話。

高然將一部份方音（主要爲三鄉同珠海部份地區）再細分爲下方話。

菊韻本意是爲順德系方言製作方案，對香山系方言部份音韻特徵水土不服。

### 香山系方言共通特徵

主要指出同廣州話異同。主要參攷《中山方言誌》《澳門粵語音系的歷史變遷及其成因》，以石歧鎮（岐江河內）爲準：

- 聲母
  - 區分來孃，故「南」`naam4`不可讀作「藍」`laam4`、「農」`nung4`不可讀作「龍」`lung4`。
  - 鼻音`m`｜`ng`可發生塞化，讀成`mb [ᵐb] `｜`ngg [ᵑg]`或`bb [b]`｜`gg [g]`（擴展粵拼中，準確來講爲`rb`｜`rg`），竝無對立，爲自由變體。此現象多見於閩南語，而少見於粵語。
  - 古非敷奉讀重脣較多，如「斧」`pu2`「扶」`pu4`等。
  - 古非敷奉合口字多數讀`h`而非脣齒音`f`，此現象極少見於粵語。今時只有同韻腹`u`結合者有此現象，如「風」`hung1`「福」`huk1`「符」`hu4`「鳳」`hung3`。而同韻腹`o`結合者則最遲見於1897年，如「方」`hong1`。根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。
  - 根據《中山方言誌》疑母細音字仍讀疑母，如「魚」`ngy4`「語」`ngy2`「嚴」`ngim4`「月」`ngyt6`等。甚至日母細音字亦讀作`ng`，如「耳」`ngi4`「繞」`ngiu3`「熱」`ngit6`「如」`ngi4`等。而有部份字廣州化讀`j`，如「儒」`jy4`（本應讀`ngy4`）「柔」`jau4`（本應讀`ngiau4`）「日」`jit2`（本應讀`ngit2`等，變化極不規律。
  - 古谿母字不少字仍讀作`k`而非`h`，此現象極少見於粵語。如「可」`ko2` 「庫」`ku3`「筷」`kwaai3`「枯」`ku1`等。根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。
  - 兩個脣化聲母遇o系韻腹即展脣化，故「光」「江」不分，皆讀`gong1`，「過」「個」不分，皆讀`go3`。
  - 根據近代資料（直至1987年），曉匣喻細音應該同順德系一樣讀`h`（小欖除外），如「爺」`he4`「賢」`hin4`「雨」`hy5`「頁」`hip6`。但根據《中山方言誌》《中山市誌》《泛粵典》資料，並無此現象，而係同小欖一樣讀`j`。推測此廣州化現象（曉匣喻細音字讀`j`）至少在20世紀中葉開始，小欖話應該亦是類似時間開始。
    - 補充：根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。
  - 影以日母廣州話讀`j`，石歧話則讀作零聲母，「英」則讀作`ing1`「翼」則讀作`ik6`。新派則同廣州一樣。此現象亦見於老派順德系方言（以白讀音保留）。
- 韻母
  - 假攝三等字有嚴重混讀現象，有部份的而且保留介音讀`ia`，如「椰」`jaa4`「爺」`jaa4`「夜」`jaa3`「惹」`jaa3`（日母字），但部份字卻跟周邊其他方言讀`e`，如「社」`se2`「借」`ze3`。（應爲以`j`爲聲母者存古）
  - 石歧話止攝字無發生裂化，故廣州話讀`ei`者，石歧仍讀`i`，如「皮」`pi4`「鼻」`bi6`「地」`di6`「四」`si3`。
    - 師韻字並無如順德系方言常見讀`y`之現象。
  - 遇攝合口一等字無發生裂化，故廣州話讀`ou`者，石歧仍讀`u`，如「補」`bu2`「都」`du1`「盧」`lu4`「府」`hu2`；廣州話讀`eoy`者，石歧仍讀`yu`，如「女」`ny2`「區」`ky1`「去」`hy3`「車」`gy1`。
  - 果攝開口三等字讀`oe`而非`e`，如「茄」`koe2`。新派音同廣州一樣。
  - 根據《泛粵典》《澳門粵語音系的歷史變遷及其成因》蟹攝合口一等字，廣州話讀`eoy`者，石歧則讀`ui`，新派音同廣州一樣：
    - 如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`「最」`zui3`。同順德系方言一樣，精母最早開始變化。順德兩個方言亦是精母最早變作`eoy`。
  - 宕攝江攝，廣州話讀`oeng/oek`，根據《中山方言誌》，石歧仍保留介音讀`iong/iok`，如「孃」`niong4`，「畧」`liok6`「窗」`ciong1`「張」`ziong1`，僅有少數讀`oeng/oek`。
    - 根據《泛粵典》同《中山市誌》資料，石歧話已無`io`，全讀`oe`。可能因爲《中山方言誌》記錄多爲老派音。而《澳門粵語音系的歷史變遷及其成因》，老派音都`io`，新派音則爲兩者混讀。
  - 梗攝白讀音，石歧話老派音仍保留介音讀`iang/iak`而非新派音`eng/ek`，如「平」`piang4`「命」`miang3`「驚」`giang1`「石」`siak6`。
  - 咸攝見系字依舊讀`om`，如「鴿」`gop3`「合」`hop6`「敢」`gom2`「柑」`gom1`等。而新派音稍爲高化，不讀`o [ɔ]`，而讀`oo [o]`。（音位無別）
  - 關於攝口韻
    - 根據《中山方言誌》所說石歧話之中攝口韻（`yu/yun/yut/eoy`）極少，而石歧鎮外香山系方言並無攝口韻，如「雨」石歧讀`jy2`、其他方言讀`ji2`；「水」石歧讀`seoy2`，唐家讀`sui2`等。故高然先生認爲無攝口韻方是存古，今時石歧話攝口韻是因爲北部粵語遷入，甚至爲廣州話影響。
    - 蟹攝三等合口字同止攝合口銳音字，近代確實讀`ooi`。現代石歧話同廣州一樣讀`eoy`，而石歧鎮以外香山系方言多爲`ui`或：如「淚」`leoy3`「水」`seoy2`「嘴」`zeoy2`等。
    - `eon/eot`同`an/at`（兩者本身來源同一個音韻）分佈於1939年開始接近廣州，但「晉」等字仍讀`an`。而新派音則徹底被廣州同化。
  - 《中山方言誌》雖無提及，但根據近代石歧話資料，推測石歧話見系流攝三等字本應讀`iau`，如「舊」`giau3`「求」`kiau4`。（1897年爲`ieu`，部份介音脫落變作`au`，1939年全數脫落）
- 聲調
  - 聲調在粵語中較少，只有平聲、入聲分陰陽。上陰入歸陽入。
  - 陰平（1｜55）、陽平（4｜51）、上聲（2｜213）、去聲（3｜33）、陰入（1｜5）、陽入（6｜2）

推測石歧話「廣州化」早於19世紀晚期開始，於20世紀中葉加劇。羅言發先生亦持相同意見。

《澳門粵語音系的歷史變遷及其成因》亦有提及前山音（1987年記錄）、北山音（2010年老派）同唐家音（2011年老派）。

以上三個方音同石歧話主要區別爲無`om/op`，無`eon/eot`，無脣化聲母`gw/kw`。而廣州話讀`ng`，三個珠海方音則同近代石歧話一樣讀`ung`。

此外，唐家音同北山音有其他共同現象：無`eoy`亦無`oi`，全部歸`ui`。`ia`系韻母元音融合，讀`e`。`i`音同`y`音混亂。亦不分`ou`同`au`，皆讀`au`，即「島」「斗」不分。甚至完全無`ing/ik`音，故梗攝全部讀`ang/ak`。

雖然三個方音同樣只有六個調，但唐家音同北山音下陰入歸陰入而非陽入。

但三個方音所有疑母細音字同日母字不約而同出現混亂（即部份讀`ng`，部份讀`j`，部份零聲母），前山音`ngj`音脫落最爲嚴重。曉母亦出現不同程度弱化，同時間非敷奉母開始脣齒化。基本上可以確定近四十年來各地廣州化明顯，但程度不等。

### 石歧

由於本人非香山系方言母語者，或闕不少字音。<b style="color:red;">警告：請勿以本輸入法作爲石歧話標準參攷。</b>

- `gukwan-sekki.schema.yaml`：由於石歧話老派變化並不均等，菊韻難以處理。故採用廣州化程度更深之新派音，標準如下：
  - 允許疑日母細音以`j`輸入。
  - 曉匣喻細音全面廣州化，讀`j`，即「爺」不讀`he4`讀`je4`「賢」不讀`hin4`讀`jin4`「樣」不讀`hiong3`讀`joeng3`。
  - 谿母字全面廣州化，讀`f`或者`h`，即「可」不讀`ko2`讀`ho2` 「庫」不讀`ku3`讀`hu3`「筷」不讀`kwaai3`讀`faai3`「枯」不讀`ku1`讀`hu1`。
  - 蟹攝合口一等字全面廣州化，讀`eoy`，即「對」不讀`dui3`讀`deoy3`「腿」不讀`tui2`讀`teoy2`「催」不讀`cui1`讀`ceoy1`「碎」不讀`sui3`讀`seoy3`「最」不讀`zui3`讀`zeoy3`，但仍可以用老派音`ui`輸入。
  - 臻攝分佈徹底廣州化，但仍可以用老派音`an/at`輸入。
  - 江攝宕攝讀`iong/iok`者可以用新派音`oeng/oek`輸入。
  - 梗攝白讀音讀`eng/ek`，如「平」`peng4`「命」`meng3`「驚」`geng1`「石」`sek6`。
  - 陽入作`3`，鍵值爲`q`。

## 參攷用方案

- `gukwan-default.schema.yaml`：菊韻音（構擬音）根據菊韻標準所構擬之古音，較分韻複雜。
- `gukwan-fanwan.schema.yaml`：<del>分韻音</del>**【已移除】**
  - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用眞正分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)
- `gukwan-canton.schema.yaml`：<del>廣州音</del>**【已移除】**
  - 並不能準確反映所有廣州發音，廣州話請用`jyut6ping3-gw`或`jyut6ping3-gw-cp`

### 構擬音特徵

構擬音是本人基於順德系方言所構擬之古音，主要指出其對分韻異同。<b style="color:red;">警告：本構擬音僅供參攷。</b>

- 聲母
  - 【同】區分精照（照組默認爲`-h`：`zh/ch/sh`）
  - 【同】區分日以（日母默認爲`-j`：`nj`）
  - 【異】疑母細音未歸日母，如「堯」讀`ngiu4`「仰」讀`ngiong5`「原」讀`ngyun4`「凝」讀`nging4`
  - 【異】疑母合口字聲母未脫，即「玩」讀`ngun6`「頑」讀`ngwaen4`
  - 【異】曉匣谿母合口字未脣齒化，如「薰」讀`hwan1`「黃」讀`hwong3`「苦」讀`hu2`「戶」讀`hu6`
  - 【異】匣喻細音讀`h`，「賢」讀`hin4`「樣」讀`hiong6`「蠅」讀`hing4`「爺」讀`hia4`
  - 【異】曉母接韻腹`a`讀`hj`，如「欣」讀`hjan1`「欽」讀`hjam1`「休」讀`hjau1`「釁」`hjan3`（未變調）
- 韻母
  - 【異】江攝照系字・宕攝開口三等字（除莊組）讀`iong/iok`，如「薑」讀`giong1`「畧」讀`liok6`「張」讀`zhiong1`「上」讀`shiong5`
  - 【異】其他宕攝字讀`oong`，同`ong`對立。如「鋼」讀`goong1`「忙」讀`moong4`「藏」讀`zoong6`「牀」讀`choong4`
  - 【異】師韻分精照，讀舌尖前圓唇元音（`y`），如「字」讀`zy6`「此」讀`cy2`「師」讀`shy1`「廁」讀`chy3`
  - 【異】遇攝開口三等字讀`yo`，合口讀`yu`。
  - 【異】蟹攝合口三等字除疑母皆讀`ui`。
  - 【異】止攝合口銳音・蟹攝合口三四等字讀`ooi`
  - 【異】臻攝竝無`eon/eot`同`an/at`之分，皆讀`an/at`
  - 【異】山開字・刪合字・效攝二等字・咸攝二等字韻腹讀`ae`
  - 【異】果攝開口三等字・假攝三等字讀`ia`
  - 【異】流攝三等字讀`iau`
  - 【同】咸攝見系字讀`om`
  - 【異】`e`系白讀字除`ei`之外韻腹讀`ia`

# 文件結構・許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0許可](cc-by-nc-sa)發佈。下列擧除方案文件外其他重要文件。

## 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用rime-cantonese部份詞庫同粵語八股文。位置爲`/gw_dicts`。`gukwan-alt.dict.yaml`・`gukwan-asp.dict.yaml`・`gukwan-alt-asp.dict.yaml`爲部份方言專用。

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
  - `gukwan.macau.dict.yaml`：澳門地名
    - 自製，澳門地名街名政府部門名，基於WIKIPEDIA。

> [!NOTE]
>
> `gukwan-extended.dict.yaml`用於調用各種擴展詞庫，以增強輸入體驗。下載並放置於正確位置方可使用，不安裝直接調用將會導致輸入法不能正常使用。故默認情況下將不調用。
>
> 默認不調用方言字表（`char3.dict`・`char4.dict`），需手動設置。

> [!TIP]
>
> [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)｜[關於如何使用擴展詞庫](https://github.com/HoengSaan/rime-gukwan/wiki#%E9%97%9C%E6%96%BC%E6%93%B4%E5%B1%95%E8%A9%9E%E5%BA%AB)
## 漢英混打

漢英混打實現是參攷[优化 Rime 英文输入体验 - Dvel's Blog](https://dvel.me/posts/make-rime-en-better/)，基於[tumuyan/melt_eng](https://github.com/tumuyan/rime-melt)（[iDvel/rime-ice](https://github.com/iDvel/rime-ice)版）。隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。

- `gukwan-melt-eng.schema.yaml`：混打方案
- `gukwan-melt-eng.dict.yaml`：混打辭典
  - `en_dicts/en.dict.yaml`
  - `en_dicts/en_ext.dict.yaml`

## LUA腳本

本方案所有LUA腳本均有參攷[iDvel/rime-ice](https://github.com/iDvel/rime-ice)及相關文件，相關文件根據源文件許可發佈。

- `unicode.lua`：UNICODE碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT許可](https://mit-license.org/)發佈。
- `lunar.lua`：是日農曆，新曆轉舊歷，來自[boomker/rime-fast-xhup](https://github.com/boomker/rime-fast-xhup)，隨源文件以[LGPL 3.0許可](https://www.gnu.org/licenses/lgpl-3.0.en.html)發佈。
- `calc_translator.lua`：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之PR。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `autocap_filter.lua`：自動大寫英文詞彙，作者爲@abcdefg233同@Mirtle，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `en_spacer.lua`：優化英文輸入體驗（自動空格），來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。

以下腳本繁化並增添小小功能。爲避免文件被覆蓋，故改名。

- `number_gukwan.lua`：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense許可](https://unlicense.org/)，本文件亦不設限。
- `time_gukwan.lua`：以各種格式輸入是日日期時間，來自[amzxyz/rime_wanxiang](amzxyz/rime_wanxiang)。隨源文件以[CC BY 4.0許可](https://creativecommons.org/licenses/by/4.0/)發佈。

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
- 羅言發《澳門粵語音系的歷史變遷及其成因》
- [poem《廣韻字音表》](https://zhuanlan.zhihu.com/p/20430939)
- [嶺南粵音《泛粵大典》](https://jyutdict.org/)
- 嶺南粵音《泛粵表》（非公開版本）
- [zi.tools 字統网](https://zi.tools/)




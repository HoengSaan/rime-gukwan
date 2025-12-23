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

### 其他菊韻項目

- 菊韻同文主題：[trime-gukwan: 同文輸入法36鍵鍵盤主題 Trime IME 36 Keys Keyboard Theme](https://github.com/HoengSaan/trime-gukwan/)
- 菊韻和語【停止維護】：[rime-kikwin: 菊韻日本語入力法 基於中州韻 Japanese IME (RIME Scheme)](https://github.com/HoengSaan/rime-kikwin)

# 簡介

This is a schema based on [Rime Input Method](https://rime.im/).

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，是爲改善粵語輸入體驗，支持三拼，漢英混打（中英混打），輸入日期・時間・節日・節氣等各種功能。

菊韻支持輸入除廣州話之外粵語方言，如小欖話、順德話、石歧話（新派）等。更多資訊請閱讀下文竝參攷[菊韻 – なかやま園](https://zonsan.fc2.page/?cat=123)。[關於如何安裝](#安裝)。

菊韻爲本人自用，只要一日未有更合本人之粵語輸入方案，則維護不停。

加筆：閣下可提供自己方言之音韻特徵同字音表，本人可爲閣下製作方案。

# 功能

支持各類方言、三拼輸入、漢英混打，各種特殊符號、日期時間輸入，各類反查等。

- 以下功能出廠自帶：
  - **漢英混打：允許漢字英文混打，基於 melt-eng。**
  - 繪文字（表情）：可以粵語輸入繪文字，默認關閉
  - 符號：特殊符號輸入，鍵值爲`/`。[學習如何使用符號](https://github.com/HoengSaan/rime-gukwan/blob/main/symbols-gukwan.yaml)
  - Unicode腳本：以 Unicode 編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲`U`（unicode）
  - 數字腳本：以阿拉伯數字輸入大小寫數字以及大小寫金額，鍵值爲`S`（SHuZy/SauZy）；
    - 二〇二五（數字小寫）
    - 貳零貳伍（數字大寫）
    - 〢〇〢〥（蘇州碼子）
      - 即花碼，由於本身特性不支持亦不需要小數點。[瞭解更多](https://zh.wikipedia.org/zh-tw/苏州码子)
    - 二千〇二十五（數額小寫）
    - 貳仟零貳拾伍（數額大寫）
    - 二千〇二十五圓整（金額小寫）
    - 貳仟零貳拾伍圓整（金額大寫）
  - 日期・時間・節日・節氣輸入腳本（**鍵值已在腳本固定，如需修改須直接改變`time_gukwan.lua`**）：
    - 【`/date`】日期（NJatKi/JatKi）：`vjk`｜`/jk`｜`vrk`｜`/rk`；有多種格式，部份默認禁用
    - 【`/time`】時間（SHiGaen/SiGaan）：`vsg`｜`/sg`
    - 【`/week`】星期（SingKi）：`vsk`｜`/sk`
    - 【`/datetime`】日時（NJatSHi/JatSi）：`vjs`｜`/js`｜`vrs`｜`/rs`；ISO 8601/RFC 3339 格式日期時間，以東八區（UTC+8）爲準
    - 【`/weeknumber`】週數（Week Number）：`vwn`｜`/wn`；今年第幾周
    - 【`/timestamp`】時間戳（Time Stamp），`vts`｜`/ts`
    - 【`/lunar`】農曆（NungLik），`vnl`｜`/nl`
    - 【`/zithi`】節氣（ZitHi）：`vzh`｜`/zh`｜；廿四節氣同日期
    - 【`/festival`】節日（ZitNJat/ZitJat）：`vzj`｜`/zj`｜`vzr`｜`/zr`；新舊曆節日同日期
    - 【`/info`】日期信息整合，鍵值爲`vday`｜`/day`（電話版中州韻多數不能正常顯示）
    - 【`N`+「`YYYYMMDD`】日期輸出：「新曆」「新曆轉舊曆」「舊曆轉新曆」「新曆轉干支」
  - 計數機：直接在 RIME 計數，鍵值爲`cC`（Calculator）。[學習如何使用計數機](https://github.com/gaboolic/rime-shuangpin-fuzhuma/blob/main/md/calc.md)
  - 打字統計：`/rtj`日統計｜`/ztj`週統計｜`/ytj`月統計｜`/ntj`年統計｜`/tj`生涯。
  - 防止連續Backspacee在編碼爲空時刪除已上屏內容
  - 允許輸入時，使用Ctrl+1~0直接上屏首個候前N個字（1即爲1隻字，0即爲10隻字），剩餘編碼保留並按音節拆分。可有效增強打字效率。
  - **新增功能：九宮格輸入（仍在測試）**
    - 參攷霧凇拼音。請以jyut6ping3-gw-t9.schema.yaml（廣州話）同trime-gukwan主題文件進行測試。由於九宮格同Rime先天劣勢，會導致：出詞效率差（極難解決）；無法實現漢英混打（解決方案如下）；聲調輸入麻煩（解決方案如下）
      - 九宮格聲調輸入不再使用字母代替（即vxz等），而係直接輸入數字（1鍵由於被用作分詞，須下劃輸入）。
      - 漢英混打直接新增一個36鍵鍵盤，以便輸入英文。（最好直接切換方案）
- 以下功能依賴`rime-kikwin`（<mark>無日文輸入需求不建議使用</mark>）： 
  - 假名：羅馬字方式，細階輸入平假名，大階輸入片假名，鍵值爲<code>`G</code> （gaa ming）。
  - 顏文字：以日文輸入各種顏文字，鍵值爲<code>`K</code>（kaomoji）
  - 和文：允許半混打日文，鍵值爲<code>`R</code>（romaji）

## Trime主題

Android使用同文輸入法可用自帶主題（`gukwan~.trime.yaml`），使用各種功能更加方便。基於[Wenti-D/Astralwelkin](https://github.com/Wenti-D/Astralwelkin)，源文件以[MIT 許可](https://mit-license.org/)發佈，菊韻以[CC BY NC SA 4.0 許可](cc-by-nc-sa)發佈。主題介紹請見：[trime-gukwan: 同文輸入法36鍵鍵盤主題 Trime IME 36 Keys Keyboard Theme](https://github.com/HoengSaan/trime-gukwan/)

## 多方言適應

菊韻可支持多地方言。由於衆口難調，已爲各種方言口音預設大量轉換規則同模糊音，方便自行定製。（需對 Regex 同音韻學有基本瞭解）

### 支持方言列表（部份）

- `jyut6ping3-gw`【廣州話（廣州系）】：使用`rime-cantonese`字表同詞庫，增添菊韻所有功能以改善打字體驗。**適合穗港澳等操廣州話人士。**
- `jyut6ping3-gw-cp`【廣州話（廣州系）】：同上，**全拼版本**。
- `gukwan-siulaam`【小欖話（順德系）】：以小欖話比較有代表性特徵製作，兼容部份新派發音。
- `gukwan-daailoeng`【大良話（順德系）】：以大良話比較有代表性特徵製作，兼容部份新派發音。
- `gukwan-cancyn`【陳村話（順德系）】：以陳村話比較有代表性特徵製作，兼容部份新派發音。
- `gukwan-gwanaan`【均安話（順德系）】：以均安話比較有代表性特徵製作，兼容部份新派發音。
- `gukwan-sekki`【石岐話（香山系）】：以石歧話新派音製作。（老派音需要自行製作字表，菊韻字表不能轉換）

詳細列表同方案細節請參攷`readme-dialect.md`（[Link](https://github.com/HoengSaan/rime-gukwan/blob/main/readme-dialect.md)）

## 輸入

打字方式仍遵從當年`rime-jyutping`基本原則。輸入廣州話時同`rime-cantonese`竝無分別，故此不贅述。多數方案使用粵拼，部份方言使用擴展粵拼，詳細請參攷`readme-dialect.md`（[Link](https://github.com/HoengSaan/rime-gukwan/blob/main/readme-dialect.md)）。

菊韻支持竝**默認開啓三拼**，即所有漢字皆可以三鍵輸入（不含聲調）。**三拼輸入不影響聲調輸入**，用家仍然可以使用傳統打法。如不能接受，下文有解說如何關閉三拼。

<img src="pic\key.png"/>

### 三拼鍵值

#### 子音（聲母）

- 不區分平翹日以之方言（多數方言）
  - 以`q`輸入`kw`：如「裙」`kwan`則爲`qan`
  - 以`x`輸入`gw`：如「轟」`gwang`則爲`xar`
  - 以`r`輸入`ng`：如「我」`ngo`則爲`ro`（不支持單獨成韻，即「吳」`ng`無法以`r`輸入）
- 區分平翹日以之方言增補（僅`gukwan-default`，可參攷此三拼並自行適配梧州話等方言）
  - 以`z/c/s`輸入`zh/ch/sh`（實質模糊音，默認關閉）
  - 以`r`輸入`ng`｜`ngi`｜`nj`：如「言」`ngin`則爲`rin`，如「仍」`njing`則爲`rir`

#### 母音（韻母）

- 以`e`輸入`oe`（`io`）：如「涼」`loeng`則爲`ler`
- 以`r`輸入`aa`：如「逛」`gwaang`則爲`xrr`
- 以`y`輸入`yu`（`jyu`）:如「血」`hyut`則爲`hyt`
- 以`u`輸入`eo`：如「論」`leon`則爲`lun`
- 以`r/e`輸入`ae`：如「斬」`zhaem`則爲`z(h)aam`｜`z(h)rm`｜`z(h)em`以`e`輸入`ia`：如「名」`miang`則爲`meng`（僅`gukwan-default`）
- 以`e`輸入`ia`：如「名」`miang`則爲`meng`（僅`gukwan-default`同`gukwan-sekki`）
- 以`u`輸入`oo`【僅限`ooi`】：如「淚」`looi`則爲`lui`
- 以`o`輸入`oo`【僅限`oong/ook`】：如「朗」`loong`則爲`lor`

以`e`輸入`oe`是考慮`e`系韻母本身以白讀音爲主，較少使用。而`u`同`eo/oo`；`o`同`oo`兩對音在多數方言可基本互補，不影響輸入。

<img src="pic\srmpir.png"/>

### 關閉三拼

三拼雖能加速全拼輸入，但對首拼出字有影響。（首拼效率本身低，實則無必要閂）若當不想使用三拼，可在方案中關閉以下選項（行頭加井號）：

```yaml
- derive/^kw/q/ # 簡拼(kw->q)
- derive/^gw/x/ # 簡拼(gw->q)
#- derive/^nj/r/                         # 簡拼(nj->r)
- derive/^ng([aeiouy])/r$1/ # 簡拼(ng->r)
- derive/([aeiouy])ng/$1r/ # 簡拼(ng->r)

- derive/aa(?=\d)/a/ # 簡拼(aa->a)【毋須關閉】
- derive/aa([iumnptkr]|ng)/r$1/ # 簡拼(aa->r)
- derive/^jy?([aeiou])/y$1/ # 簡拼(jy->y)【毋須關閉】
- derive/yu(?!ng|k)/y/ # 簡拼(yu->y)【毋須關閉】
- derive/oe(ng|k|r)/e$1/ # 簡拼(oe->e)
- derive/eo([ntiy])/u$1/ # 簡拼(eo->u)
#- derive/oo(i|y)/u$1/ # 簡拼(oo->u)
```

## 反査支持

多數人士通曉廣州話、普通話卻未必熟識自己鄉下發音，故設各種反査。反査亦可用來各種疑難雜字。

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反査。鍵值爲<code>` </code>
- 朙月拼音（rime-luna_pinyin），官話普通話反査 。鍵值爲<code>`P</code>（PuPing/PouPing）
- 倉頡五代（rime-cangjie5），倉頡反査。鍵值爲<code>`C</code>（CoongKit/CongKit）
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀反査。鍵值爲<code>`F</code>（FanDuk）
- 兩分（[rime-loengfan](https://github.com/CanCLID/rime-loengfan)），粵語廣州話兩分拆字反査。鍵值爲<code>`L</code>（LiongFan/LoengFan）

Android建議使用Trime並使用**菊韻主題**（`菊韻.trime.yaml`），使用功能更加方便。

> [!NOTE]
>
> **粵拼、訓讀、兩分須安裝方可使用**，如需使用其他方案反査，請自行定製方案。

## 已知問題・未來方向

- 簡轉繁問題：
  - `gukwan.kwongtung.dict.yaml`數據來源係簡筆字，本人亦仔細審覈過，但都無法保證三萬幾條地名全數正確。
  - jyut6ping3 部份詞庫（例如`jyut6ping3.phrase.dict.yaml`）有明顯簡轉繁痕跡，已超出本人處理範圍。
- 語言模型：
  - 語言模型是改善輸入體驗有效方法之一，**但粵語同官話語言模型不能完全通用，且現有大模型，即萬象模型因基於簡體字表，菊韻等繁體字表不能使用**。繁體模型目前我所知僅有[八股文](https://github.com/lotem/rime-octagram-data/)一個（注意：自帶八股文爲簡化版），可參攷`補靪範例`自行打補靪使用。
- 聯想・預測功能：粵語無現成可用。無法解決。現有全部聯想皆基於官話。（其實rime啲聯想本身都唔好用）


### 字詞收錄之標準

菊韻字表爲本人獨自製作，收錄數量係不如部份音碼輸入法，更不能同形碼輸入法比較。發音自然更是不能保證無任何謬誤。以下爲菊韻字詞收錄標準：

- 漢字：
  - 收錄廣韻全本，共二萬六千一百九十四個字。 
  - 收錄廣韻無收錄之近代字、現代字、粵語、少許異體字，共一萬〇九百七十五個字。
- 發音：
  - 廣韻有收錄者，統一推導至近代順德系粵語音（菊韻標準），再行轉換。例外小韻統一處理，不保留推導音。
  - 其他字如有韻書，處理同上。
  - 例外字，即不符合音韻規律，但不成規模者，則單獨記音。
  - 白讀音，儘量記載齊全。
  - 順德系方言單字變調（如「哭」`huk6`「錢」`cin1`等），亦儘量記錄。
  - 【注意】多音字由於無單獨調整，不能保證發音準確。

# 安裝

此處僅簡畧說明安裝方法，具體請見[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。更詳細教程或其他平臺可參攷以下文章：

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺，粵語）
- [配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)（多平臺，官話）
- [Android 上的 RIME 输入法 trime 同文输入法使用 | Verne in GitHub](https://blog.einverne.info/post/2021/04/use-trime-input-method-rime-on-android.html#安装和基础使用)（Android同文，官話）

安裝後請自行從`gw_dialects`複製所需方案。<mark>默認狀態下只有廣州話同基底方案可用。</mark>

> [!WARNING]
>
> 必須安裝[rime-cantonese](https://github.com/rime/rime-cantonese)，否則無法使用。

### 簡略安裝流程

1. 安裝 RIME：[Weasel 小狼毫](https://github.com/rime/weasel)（WINDOWS）[Squirrel 鼠鬚管](https://github.com/rime/squirrel)｜[fcitx5-macos](https://github.com/fcitx-contrib/fcitx5-macos)（MacOS）[ibus](https://github.com/ibus/ibus)→[ibus-rime](https://github.com/rime/ibus-rime)｜[fcitx5](https://github.com/fcitx/fcitx5)（Linux）[同文輸入法](https://github.com/osfans/trime)｜[fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)（Android）｜[倉輸入法](https://github.com/imfuxiao/Hamster)（iOS）
2. 安裝菊韻同所需依賴
   1. **rime-gukwan**（**本方案**）
   2. [rime-cantonese](https://github.com/rime/rime-cantonese)（**必選**，用於廣州話反査、粵語八股文、調用部份詞庫）
   3. [rime-kunyomi](https://github.com/sgalal/rime-kunyomi/)（**可選**，用於和語訓讀反査）
   4. [rime-loengfan](https://github.com/CanCLID/rime-loengfan)（**可選**，用於廣州話拆字反査）
   5. [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（**可選**，若閣下已刪除則須重新安裝，否則無法使用官話反査）
   6. [rime-cangjie](https://github.com/rime/rime-cangjie)（**可選**，若閣下已刪除則須重新安裝，否則無法使用倉頡反査）
   7. [rime-kikwin](https://github.com/Hoengsaan/rime-kikwin/)（**可選**，用於日文半混打，假名輸入，顏文字輸入）
3. 設定方案，重新部署

## 定製

定製可參攷[如何定製菊韻 – なかやま園](https://zonsan.fc2.page/?p=1569)，但當真要定製中州韻方案，<mark>懇請閣下閱讀以下文章</mark>：[中州韻維基 - SpellingAlgebra](https://github.com/rime/home/wiki/SpellingAlgebra)｜[amzxyz - Patch 方法论](https://github.com/amzxyz/rime_wanxiang_pro/blob/main/custom/patch%E6%96%B9%E6%B3%95%E8%AE%BA.md)｜[oh-my-rime - 配置教程](https://www.mintimate.cc/zh/guide/)

<mark>定製方案不應修改方案本身，閣下應使用補靪或根據原方案自製方案文件。</mark>

### 漢英混打大詞庫

大詞庫增加40萬條詞條，將大大增加英文輸入體驗。多數情況下並不影響打字，但並非完全無影響，故默認只調用小詞庫。

若想使用大詞庫，只需將`gw_custom/Easy English Super`內文件覆蓋默認方案即可，同正常安裝無誤。反之，若想用返小詞庫，則用`gw_custom/Easy English Nano`內文件覆蓋大詞庫方案即可。

### 添加新詞庫

隨基本字表詞庫之外，菊韻亦有特色詞庫以及廣東地名詞庫若嫌不足，菊韻有腳本（<mark>須安裝Python</mark>）輔助閣下，自動修改詞庫文件以適用菊韻。**<mark>強烈建議手動修改文件。</mark>**

菊韻添加新詞庫必須符合以下兩個要求： 

1. 無輸入碼：使用前請解壓`OpenCC.zip`至`gw_custom`，亦可自行編譯（[BYVoid/OpenCC](https://github.com/BYVoid/OpenCC)）。之後將**需要去除輸入碼之詞庫**，放在`Dict_Source`，然後使用`去除輸入碼.py`即可去除輸入碼。文件默認輸出至`Dict_Removed`
2. 詞庫必須使用繁體（OpenCC 標準）：將**需要繁化詞庫**放在`Dict_Removed`，然後使用`繁簡轉換.cmd`，選擇`s2t.json`即可繁化。文件默認輸出至`Dict_Removed`。

符合要求者，可直接將詞庫放在`Dict_Converted`。毋須使用以上兩個腳本。

##### 詞庫調用

`詞庫調用.py`將自動尋找在`Dict_Removed`同`Dict_Converted`內所有詞庫文件，閣下可自行選擇要調用詞庫。

選擇後將自動執行，將已配置詞庫放於`data`。用家只需將`data`內所有文件放置於中州韻程序文件夾即可。

### 補靪範例

`gw_custom`內有本人使用補靪之範例，示範如何調用定製詞庫，語法模型，打字預測等。（**<mark>請勿直接使用</mark>**）

# 文件結構・許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0 許可](cc-by-nc-sa)發佈。下列擧除方案文件外其他重要文件。

## 方案

> [!NOTE]
>
> **所有放棄維護方案存儲於`/gw_archive。`**

- `gukwan.schema.yaml`：基底文件（**<u><mark>請勿刪除，刪除後所有方案都無法使用</mark></u>**）
- `jyut6ping3-gw.schema.yaml`：三拼版`rime-cantonese`（廣州話），支持菊韻所有功能。
- `jyut6ping3-gw-cp.schema.yaml`：關閉三拼功能，支持菊韻除三拼以外一切功能。

關於非廣州話方案以及參攷用方案請見`readme-dialect.md`（[Link](https://github.com/HoengSaan/rime-gukwan/blob/main/readme-dialect.md)）。

## 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用 rime-cantonese 部份詞庫同粵語八股文。**位置爲`/gw_dicts`。**
`gukwan-alt.dict.yaml`・`gukwan-asp.dict.yaml`・`gukwan-alt-asp.dict.yaml`爲方言專用。`jyut6ping3-gw.dict.yaml`爲廣州專用。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字表
  - `gukwan.chars1.dict.yaml`：廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：近代字異體字異音訓讀增補（粵字平翹、日以之分參攷梧州話）
  - `gukwan.chars3.dict.yaml`：[alt] 廣韻字近代字非通用增補（方言專用）
  - `gukwan.chars4.dict.yaml` ：[asp] 廣韻字近代字非通用增補（方言專用）
- 詞庫
  - `gukwan.words.dict.yaml`：粵拼詞庫
    - 基於`jyut6ping3.words.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，隨源文件以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈。已去除輸入碼竝改變部份字型。已開始人工爲部份詞標音。
  - `gukwan.words1.dict.yaml`：地方詞增補
  - `gukwan.words2.dict.yaml`：粵拼詞庫增補同外來語
  - `gukwan.wordsjp.dict.yaml`：廣州話專用
  - `gukwan.lettered.dict.yaml`：粵拼詞庫
    - 基於`jyut6ping3.lettered.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，此部分則以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈。
  - `gukwan.kwongtung.dict.yaml`：廣東地名（村級）
    - 來源爲[adyliu/china_area: 2024 年中国全国 5 级行政区划（省、市、县、镇、村）](https://github.com/adyliu/china_area)，隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。已繁化。
  - `gukwan.macau.dict.yaml`：澳門地名
    - 自製，澳門地名街名政府部門名，基於 WIKIPEDIA。

> [!TIP]
>
> [關於如何製作用戶詞庫](https://github.com/rime/home/wiki/UserGuide#%E7%94%A8%E6%88%B6%E8%A9%9E%E5%85%B8%E7%AE%A1%E7%90%86)｜[關於如何使用擴展詞庫](https://github.com/HoengSaan/rime-gukwan/wiki#%E9%97%9C%E6%96%BC%E6%93%B4%E5%B1%95%E8%A9%9E%E5%BA%AB)

## 漢英混打

漢英混打實現是參攷[优化 Rime 英文输入体验 - Dvel's Blog](https://dvel.me/posts/make-rime-en-better/)，基於[tumuyan/melt_eng](https://github.com/tumuyan/rime-melt)（[iDvel/rime-ice](https://github.com/iDvel/rime-ice)版）。隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。英文大詞庫基於[Easy English Super](https://github.com/oniondelta/Onion_Rime_Files/tree/main)（字典：[skywind3000/ECDICT](https://github.com/skywind3000/ECDICT)，隨源文件以[MIT License](https://mit-license.org/)發佈，並禁止商用。）

- `gukwan-melt-eng.schema.yaml`：混打方案
- `gukwan-melt-eng.dict.yaml`：混打辭典
  - `en_dicts/en.dict.yaml`
  - `en_dicts/en_ext.dict.yaml`
  - `en_dicts/en_sup.dict.yaml`：英文大詞庫

##  腳本

相關文件根據源文件許可發佈。**位置爲`/lua`。**

- `unicode.lua`：UNICODE 碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT 許可](https://mit-license.org/)發佈。
- `calc_translator.lua`：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之 PR（非此repo）。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `autocap_filter.lua`：自動大寫英文詞彙，作者爲@abcdefg233 同@Mirtle，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `en_spacer.lua`：優化英文輸入體驗（自動空格），同上。
- `number_gukwan.lua`：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense 許可](https://unlicense.org/)，本文件亦不設限。

以下腳本來自來自[amzxyz/rime_wanxiang](amzxyz/rime_wanxiang)。隨源文件以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈：

- `time_gukwan.lua`：以各種格式輸入是日日期時間，菊韻用，繁化。
- `input_statistics.lua`：萬象拼音用（可被覆蓋），新增文本「你已击败了全国87％的用户」。
- `input_statistics_gw.lua`：同`input_statistics.lua`，菊韻用，繁化，新增文本「閣下已擊敗全國87％個用戶」。
- `backspace_limit.lua`：防止連續Backspacee在編碼爲空時刪除已上屏內容
- `partial_commit.lua`：此腳本允許輸入時，使用Ctrl+1~0直接上屏首個候前N個字（1即爲1隻字，0即爲10隻字），剩餘編碼保留並按音節拆分。可有效增強打字效率。
- `lib/userdb.lua`｜`wanxiang.lua`：依賴

以下 Python 同 CMD 腳本，爲本人借助AI所作。位置爲`/gw_custom`

- `去除輸入碼.py`：自動去除詞庫輸入碼。
- `繁簡轉換.cmd`：使用 OpenCC 進行繁簡轉換。
- `詞庫調用.py`：自動修改詞庫文件。

## 其他

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件請參攷[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。

- [`rime-cantonese-emoji`](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字，並無進行修改，隨源文件以[CC 0 許可](https://creativecommons.org/public-domain/cc0/)發佈。
- `symbols-gukwan.yaml`：菊韻定製標點符號（類似 Microsoft 日本語 IME）同特殊符號輸入。
- `trime-gukwan`：源文件以[MIT 許可](https://mit-license.org/)發佈，菊韻以[CC BY NC SA 4.0 許可](cc-by-nc-sa)發佈。主題介紹請見：[trime-gukwan: 同文輸入法36鍵鍵盤主題 Trime IME 36 Keys Keyboard Theme](https://github.com/HoengSaan/trime-gukwan/)
  - WD-XL Lubrifont / WD-XL 滑油字：僅用於按鍵，來源爲[NightFurySL2001/WD-XL-font](https://github.com/HoengSaan/trime-gukwan/blob/main/NightFurySL2001/WD-XL-font)。由於**滑油字**闕失部份字符，部分佈局有闕字現象，不能接受者可使用其他字型。
  - Shanggu / 尚古：僅用於候選欄，來源爲[GuiWonder/Shanggu](https://github.com/GuiWonder/Shanggu)。由於**尚古**闕失部分罕有字，不能接受者可使用**字雲**、**天珩字庫**或其他字型。（亦可作爲後備字型設置）
  - Chocolate Classical Sans / 朱古力黑體：除按鍵・按鍵註釋・候選欄之外，來源爲[MoonlitOwen/ChocolateSans](https://github.com/MoonlitOwen/ChocolateSans)。
- `OpenCC 開放中文轉換`：開箱即用，用於繁簡轉換，隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。位置爲`/gw_custom`。

## 銘謝

在此特別致謝於上文中所提及方案、字表、詞庫同腳本創作者，亦感謝以下書籍及網站的作者和編者。若無諸位努力，本人亦無法製作菊韻。

- 高然《中山方言誌》
- 何惠玲、馮國強《中山市沙田族羣的方音傳承及其民俗變遷》（簡稱爲《沙田方言》）
- 中山市地方誌編撰委員會《中山市志(1979-2005)》
- 葉卉時《廣府方言順德話》
- 羅言發《澳門粵語音系的歷史變遷及其成因》
- [poem《廣韻字音表》](https://zhuanlan.zhihu.com/p/20430939)
- [嶺南粵音《泛粵大典》](https://jyutdict.org/)
- 嶺南粵音《泛粵表》（非公開版本）
- [zi.tools 字統网](https://zi.tools/)


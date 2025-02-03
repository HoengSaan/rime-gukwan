# 菊韻

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

`gukwan.temp.dict.yaml`爲`jyut6ping3.words.dict.yaml`無輸入碼版本，作者爲粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，證書跟隨源文件爲[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)。

**測試階段：預計4月完成**

## 簡介

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入粵語之所謂沙田方言，拼音基於分韻廣韻以兼容各地方音(如師syu1 si1兩音)同廣州化(如弧本讀fu4受廣州影響讀wu4)既情況。爲兼容性同方便整理，輸入碼同實際拼音有所不同，但可直接以粵拼輸入。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。廣韻之外字庫未完成，目前缺少現代字同粵字，缺少部份白讀音。由於方案竝無詞庫，建議以粵拼詞庫代替之（須去除輸入碼）。

菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。本方案並非廣州話方案，廣州話（穗港澳）請用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 沙田方言

所謂沙田方言，多爲文件資料上既講法，實際上無幾個人眞係聽過呢個講法。不過沙田話亦都係貼切既，因爲渠分佈既地方以前基本上眞係田基，呢幾十年工業發展先填起來既。

雖然好多人講到中山既語言，多會諗到石歧話，之但是分佈最廣泛其實係所謂沙田方言，人口最爲之多：詳細爲小欖、東昇、坦背、沙蓢、橫欄、東鳳、阜沙、南頭、黃圃、民眾、浪網、港口、板芙、張家邊（部份）、南蓢（部份）、坦洲（部份）鎮。

方音近似順德（尤其北部），故出到去唔少人聞到都以爲係順德話。（其實無錯因爲眞係好多人都係順德落來既）

### 中山方言地圖

以粵語爲主，另有客閩兩語。中山粵語可分四類方言：分佈最爲廣泛之沙田方言（小欖話、沙田話、水上話），分佈在市區周圍既石歧話（石歧話、環城話），分佈在三角既東莞話，同近四邑既古鎮話、海州話。閩語主要分佈在隆都，即今日既沙溪大涌兩鎮（隆都話），南蓢三鄉亦有分佈。客語（梅縣）則多分佈在五桂山鎮周邊。

![fongin](/pic/fongin.jpg)

審圖號：粵TS（2023）第032號

#### 補充

- 板芙鎮：粵語（沙田話）爲主，亦有少數客閩兩語分佈。
- 南蓢鎮：閩語（南蓢話）爲主 。
- 三鄉鎮：閩語（三鄉話）爲主，亦有少數客粵兩語分佈。
- 坦洲鎮：粵（沙田話）客兩語。
- 神灣鎮：粵（沙田話）客兩語。
- 張家邊鎮（東鄉）：即火炬區，除東莞話皆有。

## 文件結構

### 方案

- `gukwan.schema.yaml`：調試用・自用
- 古代音
  - `gukwan-fanwan.schema.yaml`：分韻音
    - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用完全分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)
- 現代音
  - `gukwan-fanwan.schema.yaml`：廣州音
    - 準確來講此方案係廣州風，並不能準確反映所有廣州發音。若欲使用完全廣州音打字，可參攷以下方案：[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)

### 字詞

`gukwan.dict.yaml`用於調用字庫詞庫，默認亦調用rime-cantonese部份詞庫。

- 字庫
  - `gukwan.basic.dict.yaml`：廣韻字庫
  - `gukwan.one.dict.yaml`：增廣一組廣韻異音訓讀增補
  - `gukwan.two.dict.yaml`：增廣二組今字異字異音訓讀增補
- 詞庫
  - `gukwan.temp.dict.yaml`：`jyut6ping3.words.dict.yaml`無輸入碼版本

## 安裝

1. 安裝RIME（WINDOWS：[小狼毫](https://github.com/rime/weasel)；MacOS：[鼠鬚管](https://github.com/rime/squirrel)；Linux：[Fcitx5](https://github.com/fcitx/fcitx5)、[Fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)；Android：[同文輸入法](https://github.com/osfans/trime)｜[Fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)、[Fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)）
2. 安裝以下倉庫
   1. [rime-cantonese](https://github.com/rime/rime-cantonese)（必選，用於反查廣州話、八股文、部份詞庫）
   2. [rime-kanas](https://github.com/HoengSaan/rime-kanas)（可選，用於輸入假名）
   3. [rime-cantonese-emoji](https://github.com/rime/rime-emoji-cantonese)（可選，用於輸入Emoji）
   4. **rime-gukwan**（本方案）

用家可參攷以下文章：

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺）
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

拼音方案基於擴展粵拼，現代音（今音）同粵拼無區別，直接使用即可。

註：師韻默認y，擴展粵拼標準爲ii，須手動開啓轉換式。

### 鍵位

<img src="pic\key.png"/>

### 聲調

同大多數粵拼輸入法一樣，可以輸入聲調以加快蒐字速度。

- 陰：單擊
  - 陰平（1｜55/53）：`v` 
  - 陰上（2｜24）：`x`
  - 陰去（3｜33）：`q`
    - 應歸陽平
  - 上陰入（1｜5）：`v`
  - 新入（2｜24）：`x`
  - 下陰入（3｜3）：`q`
- 陽：雙擊
  - 陽平（4｜42）：`vv`
  - 陽上（5｜13）：`xx`
  - 陰去（6｜21）：`qq`
  - 陽入（6｜6）：`qq`

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

方案無法兼顧所有粵語方言，亦竝非本方案之目的。定製本方案需要對音韻學同粵語音韻有基本理解方可進行。

方案本身預設有約百條轉換規則，有簡介其轉換之音位。刪除行頭井號啓用轉換，行頭鍵入井號停止轉換。（即行頭有井號爲停止轉換，行頭無井號爲啓用轉換）若表內無適合規則請自行增添，方法請參攷[SpellingAlgebra · rime/home Wiki](https://github.com/rime/home/wiki/SpellingAlgebra)。

<img src="pic\ref1.png"/>

### 聲母定製

本方案聲母極其簡單，同分韻竝無大區別，現代音請直接將此部份所有轉換規全數啓用。

```yaml
    #聲母——現代
    #- derive/^(z|c|s)h/$1/                 # 精照合流(zh->z)
    #- derive/^(zj|cj|sj)yo(?=\d)/$1yu/     # 精照合流
    #- derive/^(z|c|s)j(?!yo)/$1/           # 精照合流(ch->c)
    #- derive/^(z|c)r/$1/                   # 精照合流(sj->s)
    #- derive/^nj/j/                        # 日以合流(nj->j)
```

### 韻母定製

請閣下詳細閱讀下方韻母段。

## 特徵表

關於韻母區別對比詳細見韻母表段。

| 特徵表             | 例              | 菊韻 | 沙田     | 分韻 | 廣州^穗港澳^ |
| ------------------ | --------------- | ---- | -------- | ---- | ------------ |
| 區分精照           | 精(z)貞(zh)     | 是   | 否       | 是   | 否           |
| 區分來孃(l/n)      | 靈(l)寧(n)      | 是   | 方音有別 | 是   | 老派         |
| 區分透曉(t/h)      | 聽(t)輕(h)      | 是   | 方音有別 | 是   | 是           |
| 疑母細音齶化       | 疑(ng)兒(nj)    | 否   | 是       | 是   | 是           |
| 區分日以(nj/j)     | 日(nj)逸(j)     | 是   | 否       | 是   | 否           |
| 曉合口讀脣齒(hw/f) | 虎(fu)化(faa)   | 否   | 是       | 是   | 是           |
| 匣母遇攝讀wu       | 壺護互(hu/wu)   | 否   | 方音有別 | 是   | 是           |
| 有無師韻(y)        | 詩(i)師(y)      | 有   | 無(i/yu) | 有   | 無(i)        |
| 有無介音(io/iaa)   | 良(iong)茄(iaa) | 有   | 無       | 有   | 無           |
| 山咸效攝是否有白讀 | 扁(aan/en)      |      | 是       |      | 否           |
| 區分見系咸一深攝   | 甘(om)今(am)    | 是   | 老派     | 否   | 否           |
| 陰去歸陽平         |                 | 否   | 方音有別 | 否   | 否           |

## 拼音表

<img src="pic\gujam1.png"/>

<img src="pic\gujam2.png"/>

## 韻母表

<img src="pic\wanmaubiu.png" style="zoom: 150%;" />
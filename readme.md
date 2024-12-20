# 菊韻

**測試階段**

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入粵語沙田方言，拼音基於分韻廣韻以兼容各地方音(如師讀作si1)同廣州化(如弧讀作wu4)既情況。爲兼容性同方便整理，輸入碼同實際拼音有所不同，但可直接以粵拼輸入。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。廣韻之外字庫未完成，目前缺少現代字同粵字，缺少部份白讀音。由於方案竝無詞庫，建議以粵拼詞庫代替之（須去除輸入碼）。

此方案無法兼顧所有粵語方言，亦竝非本方案之目的。目前可以以小欖話、廣州話、分韻音輸入。

## 示範

![showcase](pic\showcase.gif)

## 安裝

1. 安裝RIME（WINDOWS：[小狼毫](https://github.com/rime/weasel)；MacOS：[鼠鬚管](https://github.com/rime/squirrel)；Linux：[Fcitx5](https://github.com/fcitx/fcitx5)、[Fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)；Android：[同文輸入法](https://github.com/osfans/trime)｜[Fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)、[Fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)）

2. 安裝以下方案
   1. [rime-cantonese](https://github.com/rime/rime-cantonese)（必選，反查八股文用）
   2. [rime-kanas](https://github.com/HoengSaan/rime-kanas)（可選，假名用）
   3. **rime-gukwan**（本方案）

用家可參攷以下文章，先安裝RIME，再安裝方案。

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺）
- [Android 上的 RIME 输入法 trime 同文输入法使用 | Verne in GitHub](https://blog.einverne.info/post/2021/04/use-trime-input-method-rime-on-android.html#安装和基础使用)（Android：同文）

Android亦可選擇小企鵝（fcitx5），但安裝對一般用家來講較爲困難，亦無簡單易明既教程故此簡畧介紹（前提有Windows或其他電腦輔助）。

1. 在電腦安裝RIME並配置好。
2. Download [Releases · fcitx5-android/fcitx5-android](https://github.com/fcitx5-android/fcitx5-android/releases)，APP同RIME即可。手機通常使用arm64-v8a。
   1. 唔建議從Google Play中下載。
3. 安裝，須開啓「允許此來源的應用程序」。
4. 於Fcitx5→Addons啓用Rime插件
5. 將電腦端RIME目錄文件（Windows默認：C:\Program Files (x86)\Rime\weasel-0.xx.x\data），壓縮竝送至Android設備，建議使用zip等主流格式即可。
6. 於Android設備解壓文件並送至`/Android/data/org.fcitx.fcitx5.android/files/data/rime/`。
   1. 普通用家須從Fcitx5進入。Fcitx5→Addons→Rime設定（齒輪符號）→User data dir→OK即可移動，左邊即有選單。將解壓後既文件全數Copy，然後送至上述地址（左邊選單→Fcitx5 for Android→rime）。
7. 配置文件：開啓Fcitx5鍵盤竝切換至Rime輸入法，用左上角「>」符號開工具列，再撳「…」開輸入法設定，最後撳Reload Config等待輸入法配置完成。

## 輸入

方案無法兼顧所有粵語方言，亦竝非本方案之目的。目前可以以菊韻音、小欖話、廣州話、分韻音（勳小韻除外）輸入。其他方音須自行調整轉換規則。刪除行頭井號啓用轉換，行頭鍵入井號停止轉換。若表內無適合規矩請自行增添，方法參考請參攷[SpellingAlgebra · rime/home Wiki](https://github.com/rime/home/wiki/SpellingAlgebra)。

其他方音目前須自行製作模糊音規矩。

### 預設方案

- 古音
  - `gukwan.schema.yaml` 菊韻音（自用）
  - `gukwan_fanwan.schema.yaml` 分韻音
    - 勳小韻應讀若fan1，本方案爲kwan1。
- 小欖話
  - 不能辨別透（t）曉（h）者須手動開啓模糊音，請刪除第29行頭井號
    - 如「肚餓」讀作hau5 ngo6而非tau5 ngo6
  - 不能辨別透（t）曉（h）者須手動開啓模糊音，請刪除第30行頭井號
    - 如「南方」讀作laam4 fong1而非naam4 fong1
  - 不能辨別om/op同am/at者須手動開啓模糊音，請刪除第116行頭井號
    - 如「乳鴿」讀作jyu5 gap3而非jyu5 gop3
  - 如能辨別ak同aak者可關閉模糊音，請在第121行頭加井號
    - 如「勒索」讀作lak6 sok3而非laak6 sok3
  - `gukwan_sl1.schema.yaml` 小欖話——口音一
    - 見下方小欖話段默認，若部分不符合可自行更改方案。
  - `gukwan_sl2.schema.yaml` 小欖話——口音二
    - 見下方小欖話段異音，若部分不符合可自行更改方案。
    - 師韻讀作i者
      - 如「師資」讀成si1 zi1而非syu1 zyu1
      - 如「廁所」讀成ci3 so2而非cyu so2
    - 蟹合一等音，同心來兩母組合時，不讀yu而讀作eoy者 
      - 如「碎片」讀成seoy3 pin3而非syu3 pin3
      - 如「行雷」讀成haang4 leoy6而非haang4 lyu4
    - 遇開三等音，同心母組合時，不讀yu而讀作eoy者 
      - 如「需求」讀成seoy1 kau4而非syu1 kau4
  - `gukwan_canton.schema.yaml` 廣州話（未測試或不能用）
    - 臻小韻爲zeon1，本方案爲zan1。
    - 廣州話建議閣下使用[rime/rime-cantonese: Rime Cantonese input schema | 粵語拼音輸入方案](https://github.com/rime/rime-cantonese)，官網爲[粵語拼音輸入法 Jyutping IME](https://jyutping.net/)。

### 注意

※請閣下務必閱讀方案文件（即以schema.yaml結尾之文件）※

爲貼合閣下口音，請閱讀方案文件，尤其`#聲母——菊韻`同`#韻母——菊韻`部份並進行調整。

### 反查

目前方案預設四個反查：

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲`。
- 明月拼音（rime-luna_pinyin），北語普通話反查。鍵值爲x。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲v。
- 假名（[rime-kanas](https://github.com/HoengSaan/rime-kanas)），以細階輸入平假名，大階輸入片假名。鍵值爲R。

**粵拼同假名須安裝方可使用反查**，安裝方法見上方安裝段。如需使用其他方案反查，請自行搜索竝改變方案。

## 今音輸入

### 聲母

<img src="pic\shingmau.png" style="zoom: 50%;" />

### 韻母

<img src="pic\wanmau.png" style="zoom: 67%;" />

### 聲調

聲調同大多數粵拼輸入法一樣：v爲平、x爲上、q爲去。單擊爲陰聲，雙擊爲陽聲。上陰入同陰平，下陰入同陰去，陽入同陽去。

## 古音輸入

進階用家用。韻母表複雜全爲兼容，實際擬音並無如此複雜。寬式音標本考慮作爲IPA版既輸出，但係太過離地，應該唔會整。毋須理會，正常打字即可。

<img src="pic\shingmaushingdiu.png" style="zoom: 67%;" />

<img src="pic\wanmaufull.png" style="zoom: 67%;" />

## 小欖話

本處僅列擧同現今廣州話既異同。如有繆誤，敬請見諒。

### 聲母

- 透曉合流
  - 小欖不少人將透母讀作曉母，無法分辨。
  - 如「肚」讀若hau5、「臺」讀若hoi4。廣州話則讀若tou5、toi4。
- 來孃合流
  - 部份人不能分辨。
  - 如「囊」讀若long4、「泥」讀若lai4。廣州話則讀若nong4、nai4。
- 遇攝匣母字
  - 如「戶」讀若fu6、「湖」讀若fu4。廣州話則讀若wu6、wu4。今受廣州影響，亦讀若wu6、wu4。

### 韻母

- 止攝
  - 小欖**見組**未裂化。
    - 如「機」讀gi1、「希」讀hi1。廣州話則讀若gei1、hei1。
    - 「地」「離」等則同廣州相同，讀若dei6、lei4。
    - 「祕」白讀bai3（bai4）、「米」白讀（單位）mei5、「批」異讀爲pei1、「厲」異讀爲lei6。
  - 開口**精莊兩組**，即分韻師韻讀若yu。但部份地方亦同廣州相同亦讀作i。
    - 如「思」讀syu1、「字」讀zyu6。廣州話則讀若si1、zi6。

  - 開口**章組**理論應讀i，但有部分常用字亦被讀作yu。此現象少見，應爲誤讀。
    - 常見如「時」有讀syu4、「詩」有讀syu1、「持」有讀cyu4、「嗜」有讀syu3、「視」有讀syu6、「示」有讀syu6、「試」有讀syu3、「侍」有讀syu6。而「是」「氏」兩字讀若syu6。
    - 四小韻共「死」一字同廣州亦爲例外。如「四」讀sei3、「死」讀sei2。

- 遇攝
  - 分韻u音，若廣州裂化爲ou，小欖則裂化爲au。
    - 如「都」讀dau1、「素」讀sau3（sau4）。廣州話則讀若dou1、sou3。
    - 「都」白讀do1、實爲「多」訛。

  - 三等字分韻讀yu者，開口只有**精組**同**孃來**讀作eoy，合口則爲**從精清來**四母。
    - 如「鋸」讀gyu3（gyu4）、「去」讀hyu3（hyu4）。廣州話則讀作geoy3（文讀，小欖話無goe3音）、heoy3。
    - 有部分地方合口心母，如「須」「需」會同廣州話相同讀eoy。
  - 蟹合一等音、同**心來**兩母同**端組**聲母則發生元音融合讀yu。
    - 如「對」讀dyu3、「推」讀tyu1。廣州話則讀deoy3、teoy1。
    - 有部分地方**心來**兩母，如「雷」「碎」同廣州話相同讀eoy。

- 臻攝
  - 「順」白讀（順氣）讀san5、「𨳍」又讀ceot6、「出」白讀cyut1。
  - 廣州話臻小韻爲例外，讀若zeon1。小欖話則無此例外，讀若zan1。
- 山攝
  - 山開刪合兩韻有白讀讀若en。
    - 如「八」白讀（數詞）bet3、「關」白讀（動詞）gwen1。部分白讀音如「山」白讀（拜山）sen1今少見。

  - 三四等開口有白讀讀若en。
    - 如「邊」白讀（不定詞）ben1、如「扁」白讀（形容詞）ben2。

- 效攝
  - 一等字小欖話發生元音融合，讀若o。
    - 如「毛」讀mo4、「逃」讀to4。廣州話則讀若mou4、tou4。

  - 二等字白讀讀若eu。
    - 如「包」白讀（名詞）beu1、「覺」白讀（睏覺）geu3（geu4）。

- 咸攝
  - 一等字見系依舊讀若om。
    - 如「甘」讀gom1、「鴿」讀gop3。廣州話則讀若gam1、gap3。今受廣州影響，亦讀gam1、gap3。

  - 二等字白讀讀若em。
    - 如「鹹」白讀hem4、「餡」白讀（動詞）hem2。


### 聲調

本應陰去歸陽平，常用字詞亦符合此現象「睏覺」則爲fan4 geu4，但受廣州影響，單字讀時（讀書音）同廣州同。

<img src="pic\shingdiudyibi.png" alt="shingdiudyibi" style="zoom:50%;" />

### 小項

關於異讀白讀可讀一組文件（未發佈未完成）。

- 小欖音多將ak讀若aak，尤其老人則全無ak音，疑是辨別長短音殘留？
- 「齒」白讀（馬齒莧）讀若si2。
- 「在」coi5音保留，多讀coi2。
- 「仔」白讀zaai2。
- 「朶」白讀（量詞）讀若doe2、「頂」白讀（量詞）讀若doeng2、「多」白讀（的多）讀若doe1、「剁」白讀讀若doek1。
- 「隨」文讀同廣州亦讀若ceoy4，但白讀則爲coi4。「脆」亦有白讀（乾脆）coi3。
- 聲旁爲「亘」者，如廣州話讀若wun4，小欖話則讀若fun4。
- ……

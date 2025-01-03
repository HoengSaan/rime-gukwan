# 菊韻

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

**測試階段：預計4月完成**

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，用於輸入粵語沙田方言，拼音基於分韻廣韻以兼容各地方音(如師讀作si1)同廣州化(如弧讀作wu4)既情況。爲兼容性同方便整理，輸入碼同實際拼音有所不同，但可直接以粵拼輸入。

現有字庫根據excel大批量轉換，有不少紕漏，敬請見諒。廣韻之外字庫未完成，目前缺少現代字同粵字，缺少部份白讀音。由於方案竝無詞庫，建議以粵拼詞庫代替之（須去除輸入碼）。

菊韻無法兼顧所有粵語方言，亦竝非本方案之目的。目前可以以小欖話、廣州話、分韻音輸入。

## 示範

<img src="pic\showcase.gif" alt="showcase" style="zoom:100%;" />

## 安裝

**由於拼法變動，方案需要大改，若要試用請用此版本https://github.com/HoengSaan/rime-gukwan/releases/tag/v1.6-beta。在字庫完成前除測試用方案`gukwan.schema.yaml`之外都唔會有update。**

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
2. Download APP同RIME插件即可。手機通常使用arm64-v8a。（Google Play版本更新速度慢，建議從Github [Releases · fcitx5-android/fcitx5-android](https://github.com/fcitx5-android/fcitx5-android/releases) Download）
3. 安裝，須開啓「允許此來源的應用程序」。
4. 於Fcitx5→Addons啓用Rime插件
5. 將電腦端RIME目錄文件（Windows默認：C:\Program Files (x86)\Rime\weasel-0.xx.x\data），壓縮竝送至Android設備，建議使用zip等主流格式即可。
6. 於Android設備解壓文件並送至`/Android/data/org.fcitx.fcitx5.android/files/data/rime/`。
   1. 普通用家須從Fcitx5進入。Fcitx5→Addons→Rime設定（齒輪符號）→User data dir→OK即可移動，左邊即有選單。將解壓後既文件全數Copy，然後送至上述地址（左邊選單→Fcitx5 for Android→rime）。
   1. Root用家直接連接電腦即可傳送文件，毋須經過以上麻煩步驟。
7. 配置文件：開啓Fcitx5鍵盤竝切換至Rime輸入法，用左上角「>」符號開工具列，再撳「…」開輸入法設定，最後撳Reload Config等待輸入法配置完成。

## 輸入

拼音方案基於粵拼，現代音（今音）同粵拼無區別，直接使用即可。

### 聲調

同大多數粵拼輸入法一樣，可以輸入聲調以加快蒐字速度。

- 陰：單擊
  - 陰平（1｜55/53）：`v` 
  - 陰上（2｜24）：`x`
  - 陰去（3｜33）：`q`
    - 應歸陽平
  - 上陰入（1｜5）：`v`
  - 新入（2｜24）：`x`
    - 目前字表無收變調音
  - 下陰入（3｜3）：`q`
- 陽：雙擊
  - 陽平（4｜42）：`vv`
  - 陽上（5｜13）：`xx`
  - 陰去（6｜21）：`qq`
  - 陽入（6｜6）：`qq`

### 反查

目前方案預設四個反查：

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反查。鍵值爲<code>`</code>
- 明月拼音（rime-luna_pinyin），北語普通話反查。鍵值爲`x`。
- 倉頡五代（rime-cangjie5），倉頡反查。鍵值爲`v`。
- 假名（[rime-kanas](https://github.com/HoengSaan/rime-kanas)），以細階輸入平假名，大階輸入片假名。鍵值爲`R`。

**粵拼同假名須安裝方可使用反查**，安裝方法見上方安裝段。如需使用其他方案反查，請自行搜索竝改變方案。

### 注意

※請閣下務必閱讀方案文件（即以schema.yaml結尾之文件）※

方案無法兼顧所有粵語方言，亦竝非本方案之目的。

刪除行頭井號啓用轉換，行頭鍵入井號停止轉換。（即行頭有井號爲停止轉換，行頭無井號爲啓用轉換）若表內無適合規矩請自行增添，方法請參攷[SpellingAlgebra · rime/home Wiki](https://github.com/rime/home/wiki/SpellingAlgebra)。

<img src="pic\ref1.png"/>

爲貼合閣下口音，請閱讀方案文件，尤其`#聲母——菊韻`同`#韻母——菊韻`部份並進行調整。其他方音目前須自行製作模糊音規矩。

### 預設方案

**由於拼法變動，方案需要大改，若要試用請用此版本https://github.com/HoengSaan/rime-gukwan/releases/tag/v1.6-beta。在字庫完成前除測試用方案`gukwan.schema.yaml`之外都唔會有update。**

## 拼音表

<img src="pic\gujam1.png"/>

<img src="pic\gujam2.png"/>

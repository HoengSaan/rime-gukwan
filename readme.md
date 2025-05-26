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

此爲[RIME | 中州韻輸入法引擎](https://rime.im/)方案，是爲改善粵語輸入體驗，支持三拼，漢英混打（中英混打），輸入日期・時間・節日・節氣等各種功能。

菊韻本身是爲輸入順德系方言設計，可用於輸入小欖話・順德話等順德系方言，亦支持輸入廣州話。

更多資訊請閱讀下文竝參攷[菊韻 – なかやま園](https://zonsan.fc2.page/?cat=123)。[關於如何安裝](#安裝)。

## 功能

### 多方言適應

菊韻可支持多地方言。已爲各種方言口音預設大量轉換規則同模糊音，方便自行定製。（需對 Regex 同音韻學有基本瞭解）[具體異同](https://github.com/HoengSaan/rime-gukwan#%E6%96%B9%E6%A1%88)。

<details>
	<summary>菊韻支持方言</summary>
	<ul>
		<li>順德系——中山市
			<ul>
				<li><code>gukwan-siulaam</code>【小欖鎮】：以小欖話比較有代表性特徵製作，兼容新派發音。
					<ul>
						<li><code>gukwan-siulaam-bofung</code>（小欖寶豐音）：小欖鎮寶豐村，兼容新派發音。</li>
						<li><code>gukwan-dungsing</code>：（東昇音）：舊東昇鎮（今屬小欖）各口音</li>
					</ul>
				</li>
				<li><em><code>gukwan-guzan</code></em>【古鎮鎮】：
					<ul>
						<li><code>gukwan-guzan-hoizau</code>（古鎮海洲音）：古鎮鎮海洲村</li>
					</ul>
				</li>
                <li><code>gukwan-dungfau</code></li>【東鳳・阜沙鎮】：東阜兩鎮各口音
				<li><code>gukwan-waanglaan</code>【橫欄鎮】：橫欄鎮各口音</li>
				<li><code>gukwan-naamtau</code>【南頭鎮】：南頭鎮各口音
					<ul>
						<li><code>gukwan-naamtau-naamsing</code>（南頭南城音）：南頭鎮南城村</li>
					</ul>
				</li>
                <li><code>gukwan-wongpou</code>【黃圃鎮】：黃圃鎮各口音</li>
				<li><em><code>gukwan-manzung</code></em>【民衆鎮】：
					<ul>
						<li><code>gukwan-longmong</code>（浪網音）：舊浪網鎮（今屬民衆）各口音。</li>
					</ul>
				</li>
                <li><em><code>gukwan-saalong</code></em>【沙蓢鎮】：有出入請用東昇音改</li>
                <li><em><code>gukwan-gonghau</code></em>【港口鎮】：有出入請用東昇音改</li>
			</ul>
		</li>
		<li>順德系——順德市
			<ul>
				<li><code>gukwan-daailoeng</code>【大良】：以大良話比較有代表性特徵製作。</li>
				<li><code>gukwan-cancyn</code>【陳村】：以陳村話比較有代表性特徵製作。</li>
				<li><code>gukwan-gwanon</code>【均安鎮】：【未製作】</li>
			</ul>
		</li>
		<li>香山系
			<ul>
				<li><code>gukwan-sekki</code>【石岐鎮】：以石歧話新派音製作。（老派音需要自行製作字表，菊韻字表不能轉換）</li>
			</ul>
		</li>
		<li>廣州話
			<ul>
				<li><code>jyut6ping3-gw</code>【穗港澳】：完全使用<code>rime-cantonese</code>字表詞庫，增添菊韻所有功能以改善打字體驗。適合穗港澳。</li>
			</ul>
		</li>
	</ul>
	<blockquote>
		<p>除小欖音以外均以老派音製作，方案不能直接同新派音兼容，可能已不貼合實際情況，如：</p>
		<ul>
			<li>曉匣喻母細音字部份字跟廣州讀<code>j</code>，但未變齊。</li>
			<li>如「爺」讀<code>he4</code>，但係「園」讀<code>jyun4</code>（本應讀<code>hyun4</code>）</li>
			<li>由於個個方言都變化程度唔同，我一個人絕無辦法去執晒，只能設定兩種音都出到字。</li>
			<li>如小欖話只有極少數作爲白讀音殘留，例如「穴」<code>hyut6</code>，「嫌」<code>him4</code>。則可以特例處理。</li>
			<li>師韻讀<code>y</code>定讀<code>i</code>？
				<ul>
					<li>其實理論上全部應該讀<code>y</code>，但係不能避免的人遇到隻唔識既字，就直情跟廣州音。此處不作改變，如不能辨別者，請手動更改方案。</li>
				</ul>
			</li>
			<li>關於白讀字請見<a href="https://github.com/HoengSaan/rime-gukwan#%E6%96%B9%E6%A1%88">方案</a></li>
		</ul>
	</blockquote>
</details>

<mark>部份地方音須根據說明自行修改方案。</mark>

### 輸入方式

菊韻支持竝默認開啓三拼，即所有漢字皆可以三鍵輸入（不含聲調）。

**三拼輸入不影響聲調輸入**，用家仍然可以使用傳統打法——即全拼，輸入拼音完整形式：聲母+韻母+聲調，聲調可以省畧。

如不能接受三拼輸入，下文有解說如何關閉三拼。

<img src="pic\key.png"/>

<details>
	<summary>鍵值詳細說明</summary>
	<h4>子音（聲母）</h4>
	<ul>
		<li>不區分平翹日以之方言（多數方言）
			<ul>
				<li>以<code>q</code>輸入<code>kw</code>：如「裙」<code>kwan</code>則爲<code>qan</code></li>
				<li>以<code>x</code>輸入<code>gw</code>：如「轟」<code>gwang</code>則爲<code>xar</code></li>
				<li>以<code>r</code>輸入<code>ng</code>：如「我」<code>ngo</code>則爲<code>ngo</code>（不支持單獨成韻，即「吳」<code>ng</code>無法以<code>r</code>輸入）</li>
			</ul>
		</li>
		<li>區分平翹日以之方言（僅<code>gukwan-default</code>同<code>gukwan-fanwan</code>）
			<ul>
				<li>以<code>z</code>輸入<code>zh</code>（實質模糊音，默認關閉）</li>
				<li>以<code>c</code>輸入<code>ch</code>（實質模糊音，默認關閉）</li>
				<li>以<code>s</code>輸入<code>sh</code>（實質模糊音，默認關閉）</li>
				<li>以<code>q</code>輸入<code>kw</code></li>
				<li>以<code>x</code>輸入<code>gw</code></li>
				<li>以<code>r</code>輸入<code>ng</code>｜<code>ngi</code>｜<code>nj</code>：如「言」<code>ngin</code>則爲<code>rin</code>，如「仍」<code>njing</code>則爲<code>rir</code>
				</li>
			</ul>
		</li>
	</ul>
	<h4>母音（韻母）</h4>
	<ul>
		<li>無韻尾情況（如<code>laa</code>，<code>loe</code>等）
			<ul>
				<li>以<code>a</code>輸入<code>aa</code>：如「瓜」<code>gwaa</code>則爲<code>xa</code></li>
				<li>以<code>y</code>輸入<code>yu</code>（<code>jyu</code>）：如「擧」<code>gyu</code>則爲<code>gy</code></li>
			</ul>
		</li>
		<li>有韻尾情況（如<code>laang</code>，<code>loeng</code>等）
			<ul>
				<li>以<code>e</code>輸入<code>oe</code>：如「涼」<code>loeng</code>則爲<code>ler</code></li>
				<li>以<code>r</code>輸入<code>aa</code>：如「逛」<code>gwaang</code>則爲<code>xrr</code></li>
				<li>以<code>y</code>輸入<code>yu</code>（<code>jyu</code>）:如「血」<code>hyut</code>則爲<code>hyt</code></li>
				<li>以<code>u</code>輸入<code>eo</code>：如「論」<code>leon</code>則爲<code>lun</code></li>
			</ul>
		</li>
		<li>以下三拼僅部分方案適用
			<ul>
				<li>以<code>r/e</code>輸入<code>ae</code>：如「斬」<code>zhaem</code>則爲<code>z(h)aam</code>｜<code>z(h)rm</code>｜<code>z(h)em</code>（僅<code>gukwan-default</code>）</li>
				<li>以<code>u</code>輸入<code>oo</code>【僅限<code>ooi</code>】：如「淚」<code>looi</code>則爲<code>lui</code>（部份方案）</li>
				<li>以<code>o</code>輸入<code>oo</code>【僅限<code>oong/ook</code>】：如「朗」<code>loong</code>則爲<code>lor</code>（部份方案）</li>
			</ul>
		</li>
	</ul>
	<p>以<code>e</code>輸入<code>oe</code>是考慮<code>e</code>系韻母本身以白讀音爲主，較少使用。而<code>u</code>同<code>eo/oo</code>；<code>o</code>同<code>oo</code>在多數方言下都爲互補，不影響輸入。</p>
	<h4>其他</h4>
	<p>以下兩個簡拼默認關閉，無論開啓關閉都可以以三拼形式輸入。</p>
	<ul>
		<li><code>ji</code>簡拼<code>j</code>：如「影」<code>jing</code>則爲<code>jr</code>（<code>jir</code>）</li>
		<li><code>nji</code>簡拼<code>nj</code>：如「仍」<code>njing</code>則爲<code>njr</code>（<code>rir</code>｜<code>njir</code>）</li>
		<li><code>wu</code>簡拼<code>u</code>：如「換」<code>wun</code>則爲<code>un</code></li>
	</ul>
</details>
<img src="pic\srmpir.png"/>

#### 關閉三拼

三拼是本人加速輸入全拼之做法，其會影響首拼出字之效率。若不想使用三拼，可在方案文件關閉以下選項（行頭加井號）：

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
- derive/oo(i|y)/u$1/ # 簡拼(oo->u)
```

### 特殊輸入

**支持漢英混打**，各種特殊符號輸入，日期時間輸入等。

<img src="pic\showcase.png"/>

<ul>
	<li>以下功能出廠自帶：
		<ul>
			<li><strong>漢英混打：允許漢字英文混打，基於 melt-eng。待完善</strong></li>
			<li>繪文字（表情）：可以粵語輸入繪文字，默認關閉</li>
			<li>符號：特殊符號輸入，鍵值爲<code>/</code>。<a href="https://github.com/HoengSaan/rime-gukwan/blob/main/symbols-gukwan.yaml">學習如何使用符號</a></li>
			<li>Unicode：以 Unicode 編號直接輸入字符，適合輸入組合字符，空白字符等難複製特殊字符，鍵值爲<code>U</code>（unicode）</li>
			<li>數字大小寫：以阿拉伯數字輸入大小寫數字以及大小寫金額，鍵值爲<code>S</code>（SHuZy/SauZy）；
				<details>
					<summary>支持以下 7 種格式：</summary>
					<ul>
						<li>二〇二五（數字小寫）</li>
						<li>貳零貳伍（數字大寫）</li>
						<li>〢〇〢〥（蘇州碼子）</li>
						<li>即花碼，由於本身特性不支持亦不需要小數點。<a href="https://zh.wikipedia.org/zh-tw/%E8%8B%8F%E5%B7%9E%E7%A0%81%E5%AD%90">瞭解更多</a></li>
						<li>二千〇二十五（數額小寫）</li>
						<li>貳仟零貳拾伍（數額大寫）</li>
						<li>二千〇二十五圓整（金額小寫）</li>
						<li>貳仟零貳拾伍圓整（金額大寫）</li>
					</ul>
				</details>
			</li>
			<li>日期・時間・節日・節氣輸入；
				<details>
					<summary>支持以下 11 種格式：</summary>
					<ul>
						<li>【<code>/date</code>】日期（NJatKi/JatKi）：現代鍵值爲<code>vjk</code>｜<code>/jk</code>；古代鍵值爲<code>vrk</code>｜<code>/rk</code>；有多種格式，部份默認禁用</li>
						<li>【<code>/time</code>】時間（SHiGaen/SiGaan）：鍵值爲<code>vsg</code>｜<code>/sg</code></li>
						<li>【<code>/week</code>】星期（SingKi）：鍵值爲<code>vsk</code>｜<code>/sk</code></li>
						<li>【<code>/datetime</code>】日時（NJatSHi/JatSi）：現代鍵值爲<code>vjs</code>｜<code>/js</code>｜；古代鍵值爲<code>vrs</code>｜<code>/rs</code>；ISO 8601/RFC 3339 格式日期時間，以東八區（UTC+8）爲準</li>
						<li>【<code>/weeknumber</code>】週數（Week Number）：鍵值爲<code>vwn</code>｜<code>/wn</code>；今年第幾周</li>
						<li>【<code>/timestamp</code>】時間戳（Time Stamp），鍵值爲<code>vts</code>｜<code>/ts</code></li>
						<li>【<code>/lunar</code>】農曆（NungLik），鍵值爲<code>vnl</code>｜<code>/nl</code></li>
						<li>【<code>/zithi</code>】節氣（ZitHi）：鍵值爲<code>vzh</code>｜<code>/zh</code>｜；廿四節氣同日期</li>
						<li>【<code>/festival</code>】節日（ZitNJat/ZitJat）：現代鍵值爲<code>vzj</code>｜<code>/zj</code>；古代鍵值爲<code>vzr</code>｜<code>/zr</code>；新舊曆節日同日期</li>
						<li>【<code>/info</code>】日期信息整合，鍵值爲<code>vday</code>｜<code>/day</code>（電話版中州韻多數不能正常顯示）</li>
						<li>直出，鍵值爲<code>N</code>+「<code>YYYYMMDD</code>」；有四種模式：「新曆」「新曆轉舊曆」「舊曆轉新曆」「新曆轉干支」</li>
						<li><strong>鍵值已在腳本固定，如需修改須直接改變<code>time_gukwan.lua</code></strong></li>
					</ul>
				</details>
			</li>
			<li>計數機：直接在 RIME 計數，鍵值爲<code>cC</code>（Calculator）。<a href="https://github.com/gaboolic/rime-shuangpin-fuzhuma/blob/main/md/calc.md">學習如何使用計數機</a></li>
		</ul>
	</li>
	<li>以下功能須安裝<code>rime-kikwin</code>方可使用：
		<ul>
			<li><mark>無日文輸入需求不建議使用</mark></li>
			<li>假名：以細階輸入平假名，大階輸入片假名，鍵值爲&lt;code&gt;`G&lt;/code&gt; （gaa ming）。輸入方式同其他 IME（如 Microsoft IME、ATOK 等）基本無區別</li>
			<li>顏文字：以日文輸入各種顏文字，鍵值爲&lt;code&gt;`K&lt;/code&gt;（kaomoji）</li>
			<li>和文：允許半混打日文，鍵值爲&lt;code&gt;`R&lt;/code&gt;（romaji）</li>
		</ul>
	</li>
</ul>

### 反査支持

多數人士通曉廣州話、普通話卻未必熟識自己鄉下發音，故設各種反査。反査亦可用來各種疑難雜字。

- 粵拼（[rime-cantonese](https://github.com/rime/rime-cantonese)），粵語廣州話反査。鍵值爲<code>` </code>。
- 朙月拼音（rime-luna_pinyin），官語普通話反査 。鍵值爲<code>`P</code>（PuPing/PouPing）。
- 倉頡五代（rime-cangjie5），倉頡反査。鍵值爲<code>`C</code>（CoongKit/CongKit ）。
- 訓讀（[rime-kunyomi](https://github.com/sgalal/rime-kunyomi)），和語訓讀（現代音）反査。鍵值爲<code>`F</code>（FanDuk）。
- 兩分（[rime-loengfan](https://github.com/CanCLID/rime-loengfan)），粵語廣州話兩分拆字反査。鍵值爲<code>`L</code>（LiongFan/LoengFan）。

> [!NOTE]
>
> **粵拼、訓讀、兩分須安裝方可使用**，安裝方法請參攷[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。如需使用其他方案反査，請自行定製方案。

### 問題・未來方向

- 字詞發音：
  - 本人無法亦無有可能去保證所有漢字發音正確。尤其因爲菊韻詞庫多數無輸入碼，有多音字既單詞發音必然有誤。
  - 雖然菊韻支持使用聲調輸入，但本人並不能確保所有字詞聲調正確。尤其考慮到以小欖話等方言變調遠比廣州話豐富，以我一人之力斷無可能完善。
- 簡轉繁問題：
  - `gukwan.kwongtung.dict.yaml`數據來源係簡筆字，本人亦仔細審覈過，但都無法保證三萬幾條地名全數正確。
  - jyut6ping3 部份詞庫（例如`jyut6ping3.phrase.dict.yaml`）有明顯簡轉繁痕跡，已超出本人處理範圍。
- 語言模型：
  - 語言模型是改善輸入體驗最有效方法，但粵語同官話語言模型不能完全通用，需自行訓練，已超出本人能力範圍。

## 安裝

此處僅簡畧說明安裝方法，具體請見[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。更詳細教程或其他平臺可參攷以下文章：

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺，粵語）
- [配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)（多平臺，官話）
- [Android 上的 RIME 输入法 trime 同文输入法使用 | Verne in GitHub](https://blog.einverne.info/post/2021/04/use-trime-input-method-rime-on-android.html#安装和基础使用)（Android同文，官話）

若無法使用Python，安裝後請自行從`gw_dialects`複製需要使用方案。<mark>默認狀態下只有廣州話同基底方案可用。</mark>

**識者不難，難者不識。**<mark>若有不明，可問AI。</mark>

### 簡略安裝流程

1. 安裝 RIME
   1. WINDOWS：[Weasel 小狼毫](https://github.com/rime/weasel)
   2. MacOS：[Squirrel 鼠鬚管](https://github.com/rime/squirrel)｜[fcitx5-macos](https://github.com/fcitx-contrib/fcitx5-macos)
   3. Linux：[ibus](https://github.com/ibus/ibus)→[ibus-rime](https://github.com/rime/ibus-rime)｜[fcitx5](https://github.com/fcitx/fcitx5)→[fcitx5-Rime](https://github.com/fcitx/fcitx5-rime)
   4. Android：[同文輸入法](https://github.com/osfans/trime)｜[fcitx5-Android](https://github.com/fcitx5-android/fcitx5-android)→[fcitx5-Android-Rime](https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime)
2. 安裝菊韻同所需依賴
   1. **rime-gukwan**（**本方案**）
   2. [rime-cantonese](https://github.com/rime/rime-cantonese)（**必選**，用於廣州話反査、粵語八股文、調用部份詞庫）
   3. [rime-kunyomi](https://github.com/sgalal/rime-kunyomi/)（**可選**，用於和語訓讀反査）
   4. [rime-loengfan](https://github.com/CanCLID/rime-loengfan)（**可選**，用於廣州話拆字反査）
   5. [rime-luna-pinyin](https://github.com/rime/rime-luna-pinyin)（**可選**，若閣下已刪除則須重新安裝，否則無法使用官話反査）
   6. [rime-cangjie](https://github.com/rime/rime-cangjie)（**可選**，若閣下已刪除則須重新安裝，否則無法使用倉頡反査）
   7. [rime-kikwin](https://github.com/Hoengsaan/rime-kikwin/)（**可選**，用於日文半混打，低性能設備建議關閉，只使用`rime-kanas`同`rime-kaomoji`）
3. 設定方案，重新部署

## 定製

部份用家可根據自身情況添加以下字音到用戶字庫。

### 必讀參攷文章

定製可參攷[如何定製菊韻 – なかやま園](https://zonsan.fc2.page/?p=1569)，但當真要定製中州韻方案，<mark>懇請閣下閱讀以下文章</mark>：

- [中州韻維基 - SpellingAlgebra](https://github.com/rime/home/wiki/SpellingAlgebra)
- [amzxyz - Patch 方法论](https://github.com/amzxyz/rime_wanxiang_pro/blob/main/custom/patch%E6%96%B9%E6%B3%95%E8%AE%BA.md)
- [oh-my-rime - 配置教程](https://www.mintimate.cc/zh/guide/)

### 漢英混打大詞庫

大詞庫增加40萬條詞條，將大大增加英文輸入體驗。多數情況下並不影響打字，但並非完全無影響，故默認只調用小詞庫。

若想使用大詞庫，只需將`gw_custom/Easy English Super`內文件覆蓋默認方案即可，同正常安裝無誤。反之，若想用返小詞庫，則用`gw_custom/Easy English Nano`內文件覆蓋大詞庫方案即可。

### 添加新詞庫

隨基本字表詞庫之外，菊韻亦有特色詞庫以及廣東地名詞庫若嫌不足，菊韻有腳本（<mark>須安裝Python</mark>）輔助閣下，自動修改詞庫文件以適用菊韻。

菊韻添加新詞庫必須符合以下兩個要求： 

1. 無輸入碼，菊韻輸入碼無法同其他方案通用。
   - 使用前請解壓`OpenCC.zip`至`gw_custom`，亦可自行編譯（[BYVoid/OpenCC](https://github.com/BYVoid/OpenCC)）。
   - 將需要去除輸入碼之詞庫，放在`Dict_Source`，然後使用`去除輸入碼.py`即可去除輸入碼。
   - 去除輸入碼版本默認輸出至`Dict_Removed`
2. 詞庫必須使用繁體（OpenCC 標準），否則無法打字。
   - 將需要繁化詞庫放在`Dict_Removed`，然後使用`繁簡轉換.cmd`，選擇`s2t.json`即可繁化。
   - 轉換後默認輸出至`Dict_Removed`。

若閣下詞庫已符合以上兩個要求，可直接將詞庫放在`Dict_Converted`。毋須使用以上兩個腳本。

##### 詞庫調用

`詞庫調用.py`將自動尋找在`Dict_Removed`同`Dict_Converted`內所有詞庫文件，閣下可自行選擇要調用詞庫。

選擇後將自動執行，將已配置詞庫放於`data`。用家只需將`data`內所有文件放置於中州韻程序文件夾即可。

**建議打補靪（`~custom.yaml`）或自行修改文件。**

### 補靪範例

`gw_custom`內有本人使用補靪之範例，以供參攷。

## 拼音

打字方式仍遵從當年`rime-jyutping`基本原則。輸入廣州話時同`rime-cantonese`竝無分別，故此不贅述。

# 方案

> [!NOTE]
>
> <del>`xxx.xxx-ps.scheme.yaml`爲寬式音標版，寬式音標並不能完全代表實際發音。所有寬式音標版存儲在`/ps`。如需使用請自行將其移出。</del>**音標版方案已被放棄，不再維護。所有放棄維護方案存儲於`/gw_archive。`**
>
> <mark>以下方案並不能完全代表當地發音，請根據自身實際情況調整。</mark>
>
> 由於本人所寫轉換規則有缺陷，導致部份字拼音提示不準確，敬請見諒。

- `gukwan.schema.yaml`：基底文件（**<u><mark>請勿刪除，刪除後所有方案都無法使用</mark></u>**）
- `jyut6ping3-gw.schema.yaml`：三拼版`rime-cantonese`（廣州話），支持菊韻所有功能。
- `jyut6ping3-gw-cp.schema.yaml`：關閉三拼功能，支持菊韻除三拼以外一切功能。

非廣州話方案以及參攷用方案請見`readme-dialect.md`（[Link](https://github.com/HoengSaan/rime-gukwan/blob/main/readme-dialect.md)）有詳細介紹

# 文件簡介 許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0 許可](cc-by-nc-sa)發佈。下列擧除方案文件外其他重要文件。

## 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用 rime-cantonese 部份詞庫同粵語八股文。位置爲`/gw_dicts`。

`gukwan-alt.dict.yaml`・`gukwan-asp.dict.yaml`・`gukwan-alt-asp.dict.yaml`爲部份方言專用。

`jyut6ping3-gw.dict.yaml`爲廣州話專用。

`gukwan-extended.dict.yaml`用於調用各種擴展詞庫，以增強輸入體驗。下載並放置於正確位置方可使用，不安裝直接調用將會導致輸入法不能正常使用。故默情況下將不調用。默認不調用方言字表（`char3.dict`・`char4.dict`），需手動設置。

- 字庫
  - `gukwan.chars.dict.yaml`：廣韻字表
  - `gukwan.chars1.dict.yaml`：廣韻異音訓讀增補
  - `gukwan.chars2.dict.yaml`：近代字異體字異音訓讀增補
    - 粵字平翹、日以之分參攷梧州話
  - `gukwan.chars3.dict.yaml`：[alt] 廣韻字近代字非通用增補（特供部份方言使用）
  - `gukwan.chars4.dict.yaml` ：[asp] 廣韻字近代字非通用增補（特供部份方言使用）
- 詞庫
  - `gukwan.words.dict.yaml`：粵拼詞庫
    - 基於`jyut6ping3.words.dict.yaml`，作者爲「粵語計算語言學基礎建設組」([@CanCLID](https://github.com/CanCLID)) ，隨源文件以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈。已去除輸入碼竝改變部份字型。
    - 已開始爲部份詞標音。
  - `gukwan.words1.dict.yaml`：部份小欖話辭彙同小欖周邊地名
    - 收錄部份小欖話特有辭彙，小欖周邊地名街名，詳細見[小欖詞庫資料](https://github.com/HoengSaan/rime-gukwan/wiki/小欖詞庫資料)
  - `gukwan.words2.dict.yaml`：粵拼詞庫增補同外來語
    - 收錄粵拼詞庫所無之特殊辭彙同外來語。
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

漢英混打實現是參攷[优化 Rime 英文输入体验 - Dvel's Blog](https://dvel.me/posts/make-rime-en-better/)，基於[tumuyan/melt_eng](https://github.com/tumuyan/rime-melt)（[iDvel/rime-ice](https://github.com/iDvel/rime-ice)版）。隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。
英文大詞庫基於[Easy English Super](https://github.com/oniondelta/Onion_Rime_Files/tree/main)（字典：[skywind3000/ECDICT](https://github.com/skywind3000/ECDICT)，隨源文件以[MIT License](https://mit-license.org/)發佈，並禁止商用。

- `gukwan-melt-eng.schema.yaml`：混打方案
- `gukwan-melt-eng.dict.yaml`：混打辭典
  - `en_dicts/en.dict.yaml`
  - `en_dicts/en_ext.dict.yaml`
  - `en_dicts/en_sup.dict.yaml`：英文大詞庫

##  腳本

本方案多數 LUA 腳本均有參攷[iDvel/rime-ice](https://github.com/iDvel/rime-ice)及相關文件，相關文件根據源文件許可發佈。

- `unicode.lua`：UNICODE 碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT 許可](https://mit-license.org/)發佈。
- `lunar.lua`：是日農曆，新曆轉舊歷，來自[boomker/rime-fast-xhup](https://github.com/boomker/rime-fast-xhup)，隨源文件以[LGPL 3.0 許可](https://www.gnu.org/licenses/lgpl-3.0.en.html)發佈。
- `calc_translator.lua`：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之 PR。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `autocap_filter.lua`：自動大寫英文詞彙，作者爲@abcdefg233 同@Mirtle，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `en_spacer.lua`：優化英文輸入體驗（自動空格），來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。

以下 LUA 腳本繁化並增添小小功能。爲避免文件被覆蓋，故改名。

- `number_gukwan.lua`：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense 許可](https://unlicense.org/)，本文件亦不設限。
- `time_gukwan.lua`：以各種格式輸入是日日期時間，來自[amzxyz/rime_wanxiang](amzxyz/rime_wanxiang)。隨源文件以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈。

以下 Python 同 CMD 腳本，爲本人借助AI所作。

- `去除輸入碼.py`：自動去除詞庫輸入碼。
- `繁簡轉換.cmd`：使用 OpenCC 進行繁簡轉換。
- `詞庫調用.py`：自動修改詞庫文件。

## 其他

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件請參攷[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。

- [`rime-cantonese-emoji`](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字，隨源文件以[CC 0 許可](https://creativecommons.org/public-domain/cc0/)發佈。
- `symbols-gukwan.yaml`：菊韻定製標點符號（類似 Microsoft 日本語 IME）同特殊符號輸入。
- `菊韻.trime.yaml`：同文輸入法主題，基於[Wenti-D/Astralwelkin](https://github.com/Wenti-D/Astralwelkin)，隨源文件以[MIT 許可](https://mit-license.org/)發佈。不同點如下：
  - 鍵值更改，允許一鍵反査（q 鍵、p 鍵、a 鍵）。
  - 專用配色，參攷小欖特色菊花，但未夠膽用黃色驚太鮮豔，結果就變成屎黃色((o(；□；`)o))。
- `OpenCC 開放中文轉換`：開箱即用，用於繁簡轉換，隨源文件以[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)發佈。

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

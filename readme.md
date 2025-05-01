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

<mark>Update：將方言點方案移至`gw_dialects`。</mark>

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
				<li><em><code>gukwan-manzung</code></em>【民衆鎮】：
					<ul>
						<li><code>gukwan-longmong</code>（浪網音）：舊浪網鎮（今屬民衆）各口音。</li>
					</ul>
				</li>
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
		<p>除小欖音以外均以老派音製作，方案不能直接同新派音兼容，可能已不貼合實際情況，故：</p>
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
			<li>見系咸攝字<code>om</code>同<code>am</code>不分。
				<ul>
					<li>由於個個方言都變化程度不一，以我</li>
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

### 字表詞庫

菊韻字表詞庫以深筆爲準，但可以轉換爲簡筆。隨基本字表詞庫之外，菊韻亦有小欖話特色詞庫以及廣東地名詞庫。

> [!NOTE]
>
> 菊韻可調用擴展詞庫，但需要手動下載。[gukwan-extended.dict.yaml](https://github.com/HoengSaan/rime-gukwan/blob/main/gukwan-extended.dict.yaml)內有說明如何獲取。由於擴展詞庫過大，低性能設備不建議使用，可能導致部署失敗。

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
- <del>漢英混打：由於不明原因 gukwan 不能使用混打，本人已嘗試多次。將解決詞庫問題後再行處理。</del>**【已解決】**
- 可輸入方言過少：自用爲主，將於未來處理。【正在處理】
- 英文單詞過少：實際使用下英文單詞過少，將於未來處理。

## 安裝

此處僅簡畧說明安裝方法，具體請見[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。更詳細教程或其他平臺可參攷以下文章：

- [Home · rime/rime-cantonese Wiki](https://github.com/rime/rime-cantonese/wiki)（多平臺，粵語）
- [配置教程 | oh-my-rime输入法](https://www.mintimate.cc/zh/guide/)（多平臺，官話）
- [Android 上的 RIME 输入法 trime 同文输入法使用 | Verne in GitHub](https://blog.einverne.info/post/2021/04/use-trime-input-method-rime-on-android.html#安装和基础使用)（Android同文，官話）

**識者不難，難者不識。**

<details>
	<summary>簡略安裝流程</summary>
	<ol>
		<li>
			<p>安裝 RIME</p>
			<ol>
				<li>WINDOWS：<a href="https://github.com/rime/weasel">Weasel 小狼毫</a></li>
				<li>MacOS：<a href="https://github.com/rime/squirrel">Squirrel 鼠鬚管</a>｜<a href="https://github.com/fcitx-contrib/fcitx5-macos">fcitx5-macos</a></li>
				<li>Linux：<a href="https://github.com/ibus/ibus">ibus</a>→<a href="https://github.com/rime/ibus-rime">ibus-rime</a>｜<a href="https://github.com/fcitx/fcitx5">fcitx5</a>→<a href="https://github.com/fcitx/fcitx5-rime">fcitx5-Rime</a></li>
				<li>Android：<a href="https://github.com/osfans/trime">同文輸入法</a>｜<a href="https://github.com/fcitx5-android/fcitx5-android">fcitx5-Android</a>→<a href="https://github.com/fcitx5-android/fcitx5-android/blob/master/plugin/rime">fcitx5-Android-Rime</a> </li>
			</ol>
		</li>
		<li>
			<p>安裝以下倉庫</p>
			<ol>
				<li><strong>rime-gukwan</strong>（<strong>本方案</strong>）</li>
				<li><a href="https://github.com/rime/rime-cantonese">rime-cantonese</a>（<strong>必選</strong>，用於廣州話反査、八股文、部份詞庫）</li>
				<li><a href="https://github.com/sgalal/rime-kunyomi/">rime-kunyomi</a>（<strong>可選</strong>，用於和語訓讀反査）</li>
				<li><a href="https://github.com/CanCLID/rime-loengfan">rime-loengfan</a>（<strong>可選</strong>，用於廣州話拆字反査）</li>
				<li><a href="https://github.com/rime/rime-luna-pinyin">rime-luna-pinyin</a>（<strong>可選</strong>，若閣下已刪除則須重新安裝，否則無法使用官話反査）</li>
				<li><a href="https://github.com/rime/rime-cangjie">rime-cangjie</a>（<strong>可選</strong>，若閣下已刪除則須重新安裝，否則無法使用倉頡反査）</li>
				<li><a href="https://github.com/Hoengsaan/rime-kikwin/">rime-kikwin</a>（<strong>可選</strong>，用於日文半混打，低性能設備建議關閉，只使用<code>rime-kanas</code>同<code>rime-kaomoji</code>）</li>
			</ol>
		</li>
		<li>
			<p>設定方案，重新部署</p>
		</li>
	</ol>
</details>

## 定製

部份用家可根據自身情況添加以下字音到用戶字庫。

### 必讀參攷文章

定製可參攷[如何定製菊韻 – なかやま園](https://zonsan.fc2.page/?p=1569)，但當真要定製中州韻方案，<mark>懇請閣下閱讀以下文章</mark>：

- [中州韻維基 - SpellingAlgebra](https://github.com/rime/home/wiki/SpellingAlgebra)
- [amzxyz - Patch 方法论](https://github.com/amzxyz/rime_wanxiang_pro/blob/main/custom/patch%E6%96%B9%E6%B3%95%E8%AE%BA.md)
- [oh-my-rime - 配置教程](https://www.mintimate.cc/zh/guide/)

## 拼音

打字方式仍遵從當年`rime-jyutping`基本原則。

<img src="pic\gamjam1.png" style="zoom:50%;" />

<img src="pic\gamjam2.png"/>

以上調值爲小欖話，僅供參攷。部份方言僅有 9 個或 8 個聲調（含特殊調），香山系方言只有 6 個甚至更少。

古代音請參攷[菊韻拼音表 – なかやま園](https://zonsan.fc2.page/?p=1583)，其他可參攷[順德系方言特徵 – なかやま園](https://zonsan.fc2.page/?p=1580)。

### 粵拼同擴展粵拼

菊韻拼音方案基於[擴展粵拼](https://jyutjam.org/j++/)，現代音可直接以[粵拼](https://jyutping.org/)輸入。

不少方音同一音位發音同廣州竝不盡同，但爲方便輸入，如果粵拼可以表達，則全部用粵拼表達。只有粵拼不可表達之音位，方用擴展粵拼。

以南頭排坎音爲例子，其江攝宕攝仍保留有介音：

- 「江」韻母讀/ong/，對應廣州話 ong，故可直接用粵拼現有`ong`。
- 「鋼」韻母讀/yoong/，廣州話無對應音位，故使用擴展粵拼`oong`。爲打字方便，`ong`亦可使用。
- 「薑」韻母讀/yong/，對應廣州話 oong，故可直接用粵拼現有`oeng`。而擴展粵拼`iong`亦可使用。
- 「廣」韻母讀/wong/，對應廣州話 wong，故可直接用粵拼現有`wong`。

### `gu/ku`同`gwu/kwu`

【以下僅限擁有圓脣聲母方言】

雖然絕大多數字典同記音不分辨`gu/ku`同`gwu/kwu`，但兩者並非同音位。`gwu`同`kwu`最爲常見，多數字都讀作圓脣而非展脣。而`gu`同`ku`一般爲擬聲擬態詞所用，非常少見。

亦有部份方言將效攝讀作`u`，聲母仍爲展脣。即「高」讀`gu1`而「姑」讀`gwu1`。菊韻目前無此類方言。

因以上兩種原因，菊韻目前不分，皆作`gu/ku`。

### 特殊調

【以下僅適用於部份中山市順德系方言】

2\*並不如廣州話「新入」，只見於入聲字變調，如「子」白讀`zaai2*`就同陰上調值（通常爲 24，而特殊調多爲 35）不一。此調亦用作表達過去、完成之文法意味。超高陰平只出現於陰平連續變調。

爲免麻煩，特殊調打字同 2（陰上）通用。

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

### 白讀字

<details>
	<summary>以下白讀字竝非適用於所有方言：</summary>
	<ul>
		<li>以下字較爲共通，且對輸入影響不大，全部收錄在主字庫，不再另立。
			<ul>
				<li>「螺」「朶」「鏟」「墮」等字讀<code>-oe</code></li>
				<li>「邊」「扁」「癲」「見」等字讀<code>-e</code></li>
				<li>「山」「斬」「減」「咸」等字讀<code>-e</code>（統一爲 ae 再轉換，故拼音提示仍爲 ae，此爲菊韻輸入法遺留問題）</li>
				<li>「應」「拎」「煙」等字讀零聲母（此字現代少見，而香山系方言老派無論文白皆讀零聲母）</li>
				<li>短<code>a</code>變長<code>a</code>（aa）：「第」<code>daai6</code>「仔」<code>zaai2</code>「洗」<code>saai2</code>；「某・畝」<code>maau5</code>「謀・繆・謬」<code>maau4</code>「貿・茂」<code>maau6</code>；「侄・姪」<code>zaat2</code>「甩」<code>laat1</code></li>
				<li>不成規模：「現」<code>ngin6</code>「鏟」<code>coen2</code>「玩」<code>faan2</code>「閂」<code>soen1</code>「凝・迎」讀<code>nging4</code>「處」<code>syu3</code>「姊」<code>zei2</code>等，不勝枚擧。</li>
			</ul>
		</li>
		<li>以下字收錄在<code>gukwan-alt.dict.yaml</code>同<code>gukwan-alt-asp.dict.yaml</code>
			<ul>
				<li>「虐」「若」「業」「仰」等疑日母字讀<code>h</code></li>
				<li>「亦」「姚」「盈」「芫」等字補全</li>
			</ul>
		</li>
		<li>以下字收錄在<code>gukwan-asp.dict.yaml</code>同<code>gukwan-alt-asp.dict.yaml</code>
			<ul>
				<li>「花」「輝」「快」「筷」等少部分曉母合口字讀<code>w-</code></li>
				<li>「蠅」「業」「惹」「仰」等少部分細音字讀<code>h-</code></li>
				<li>「船」「射」「繩」「蛇」等少部分擦音字塞化讀<code>c-</code>或者<code>z-</code>（「剩」<code>zing6</code>「嘥」<code>caai1</code>「贖」<code>zuk6</code>「煠」<code>zep6</code>「塞」<code>zak1</code>已收錄在主字庫）</li>
				<li>「婆」「茶」「糖」「田」等少部分送氣字無氣化（「柿」<code>zy2</code>「淡」<code>daam6</code>已收錄在主字庫）</li>
				<li>「件」「解」「揀」「掛」等少部分無氣字送氣化（「舊」<code>kau6</code>已收錄在主字庫）</li>
			</ul>
		</li>
	</ul>
</details>

## 順德系方言

順德系方言主要分佈於順德市同其周邊，如中山，南海，番禺等。

順德市方面主要可分爲四種：

1. 以大良爲中心，同周邊容奇、桂州、倫敎、勒流爲一類；
2. 以陳村爲中心，同周邊北滘、樂從爲一類；
3. 以龍江爲中心，同周邊龍山、里海爲一類；
4. 以均安爲一類。

中山市方面則有兩種：

1. 以小欖爲中心，同周邊海洲、東昇、東鳳爲一類；
2. 遠離小欖竝帶有一定蜑家特徵爲一類。

南海，番禺方面目前無計劃。

### 順德系方言共通特徵

<details>
	<summary>主要指出同廣州話異同，以小欖話爲準：</summary>
	<ul>
		<li>多數不分來孃，即「南」<code>naam4</code>讀作「藍」<code>laam4</code>、「農」<code>nung4</code>讀作「龍」<code>lung4</code>。</li>
		<li>古匣母（含少數云母合口字）部份字：即今時廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，順德系方言聲母則爲<code>f</code>。
			<ul>
				<li>大多數中山方言點只是部份符合規律，將「胡」「戶」「護」三小韻讀作<code>fu</code>。「垣」小韻讀作<code>fun</code>。其他已大幅向廣州貼近，聲母讀<code>w</code>。</li>
			</ul>
		</li>
		<li>見組止攝開口三等字未裂化讀作<code>i</code>而非<code>ei</code>，如「其」<code>ki4</code>「起」<code>hi2</code>「機」<code>gi1</code>「紀」<code>gi3</code>等。而陳村則完全無裂化。</li>
		<li>師韻字（即精莊組止攝開口三等字）讀作<code>y</code>而非<code>i</code>，如「資」<code>zy1</code>「師」<code>sy1</code>「字」<code>zy6</code>「此」<code>cy2</code>等。</li>
		<li>見系遇攝三等字未裂化讀元本發音<code>yu</code>而非廣州發音<code>eoy</code>，如「區」<code>ky1</code>「去」<code>hy3</code>「車」<code>gy1</code>「巨」<code>gy6</code>等。</li>
		<li>蟹攝合口一等字本應讀<code>ui</code>，部份方言則變作<code>yu</code>，而非廣州發音<code>eoy</code>，如「對」<code>dy3</code>「腿」<code>ty2</code>「堆」<code>dy1</code>「碎」<code>sy3</code>等。
			<ul>
				<li>通常精母先變<code>eoy</code>，清母兩種情況都有，而其他則變<code>yu</code>。</li>
			</ul>
		</li>
		<li>部份方言遇攝合口一等字除見系之外裂化爲<code>au</code>而非<code>ou</code>，如「度」<code>dau6</code>「無」<code>mau4</code>「做（作）」<code>zau6</code>「粗」<code>cau1</code>等。
			<ul>
				<li>亦有部份方言低化爲<code>o</code>。</li>
			</ul>
		</li>
		<li>部份方言效攝一等字發生元音融合，讀<code>o</code>，如「高」<code>go1</code>「刀」<code>do1</code>「毛」<code>mo4</code>「草」<code>co2</code>。
			<ul>
				<li>亦有部份方言讀<code>au</code>，或同廣州發音一樣讀<code>ou</code>。有甚者讀<code>oo</code>，同<code>o</code>保持對立（需檢査）。均安則同官話一樣讀<code>aau</code>。</li>
			</ul>
		</li>
		<li>咸攝見系字仍讀<code>om</code>，如「鴿」<code>gop3</code>「合」<code>hop6</code>「敢」<code>gom2</code>「柑」<code>gom1</code>等。
			<ul>
				<li>但實際情況連多數中年人亦不分<code>om/op</code>同<code>am/ap</code>，同方言記錄有差別。故菊韻允許以<code>am/ap</code>音輸入<code>om/op</code>字。</li>
			</ul>
		</li>
		<li>【老派】順德市大良、陳村、均安以及中山市小欖等無<code>ak</code>，皆讀<code>aak</code>。</li>
		<li>白讀音豐富。</li>
		<li>變調豐富，有一定規律但其豐富性導致方案無法完全還原其實態。尤其陽平字特殊變調之多，本人已放棄收錄。</li>
	</ul>
	<p>以上特徵如無重申即無異。</p>
</details>

### 中山

#### 小欖・東昇

小欖鎮位於中山市北部，亦名菊城、欖鎮。同順德市均安鎮接壤，爲中山工業重鎮。小欖多數人講小欖話（順德系方言），僅沙口講蜑家話（受小欖話嚴影響）。

東昇本屬小欖，86 年被劃出，21 年被劃回小欖鎮。

坦背本分屬欖鎮同隆鎮，新中國後分去沙蓢，84 年設區，86 年設鎮，99 年併入東昇，21 年跟東昇一同併入欖鎮。

<details>
	<summary><code>gukwan-siulaam.schema.yaml</code>：小欖音</summary>
	<ul>
		<li>本方案根據小欖鎮代表特徵製作。下爲重要特徵：
			<ul>
				<li>多數人不分透曉（t/h），故曉母（h）可通透母（t）：如「偸」<code>tau1</code>可打<code>hau1</code>，「聽」<code>ting1</code>可打<code>hing1</code>。</li>
				<li>「胡」「戶」「護」三小韻<code>wu/fu</code>混讀。</li>
				<li>不分<code>ak</code>同<code>aak</code>，故<code>aak</code>音可通ak：如「勒」<code>lak6</code>可打<code>laak6</code>，「得」<code>dak1</code>可打<code>daak1</code>。
					<ul>
						<li>老派只有<code>aak</code>，無<code>ak</code>。</li>
					</ul>
				</li>
				<li>蟹攝合口一等字，廣州話讀<code>eoy</code>者，小欖話多讀作<code>yu</code>：
					<ul>
						<li>端組、來母同心母讀作<code>yu</code>，如「對」<code>dy3</code>「腿」<code>ty2</code>「堆」<code>dy1</code>「碎」<code>sy3</code>等。</li>
						<li>精組（除心母）多數人讀<code>eoy</code>，如「最」<code>zeoy3</code>「罪」<code>zeoy6</code>「催」<code>ceoy1</code>等。</li>
						<li>此類字讀<code>ui</code>爲棺材音，故方案不採用。</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
</details>

<details>
	<summary><code>gukwan-siulaam-bofung.schema.yaml</code>：小欖寶豐音</summary>
	<ul>
		<li>本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖音主要區別：
			<ul>
                <li>分辨透曉</li>
                <li>ong·ok 同 oeng·oek 不分；eng·ek 同 en·et 不分。實際打字兩者皆可。</li>
				<li>「胡」「戶」「護」三小韻讀<code>fu</code>，並無混讀。</li>
				<li>蟹攝合口一等字變化同廣州話一樣，但有部分讀<code>oe</code>（見<code>gukwan-siulaam-bofung.dict.yaml</code>）</li>
			</ul>
		</li>
	</ul>
</details>

<details>
	<summary><code>gukwan-dungsing.schema.yaml</code>：東昇音</summary>
	<ul>
		<li>本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖話主要區別：
			<ul>
				<li>分辨透曉</li>
				<li>ong·ok 同 oeng·oek 不分，全部讀<code>oe</code>。實際打字兩者皆可。
					<ul>
						<li>【高沙】分辨 ong·ok 同 oeng·oek /yø/。
							<ul>
								<li>請符合此項用家在 170 行、171 行、374 行添加井號</li>
							</ul>
						</li>
						<li>【太平】【坦背】江攝除莊組外讀<code>ong /yong/</code>，江攝莊組同宕攝開口讀<code>oeng /yeong/</code>，宕攝合口讀<code>wong /wyong/</code>。
							<ul>
								<li>請符合此項用家先在 130 行、170 行、171 行、374 行添加井號，竝刪除 179 行同 375 行井號。</li>
							</ul>
						</li>
					</ul>
				</li>
				<li>「胡」「戶」「護」三小韻讀<code>fu</code>，無混。</li>
				<li>蟹攝合口一等字精組全面變化爲<code>eoy</code>。</li>
				<li>遇攝合口一等字裂化同廣州一樣爲<code>ou</code>：「度」<code>dou6</code>「無」<code>mou4</code>「做（作）」<code>zou6</code>「粗」<code>cou1</code>等。
					<ul>
						<li>【高沙】遇攝合口一等字裂化同小欖一樣爲<code>au</code>，而非<code>ou</code>。
							<ul>
								<li>請符合此項用家在 98 行添加井號，竝刪除 97 行井號。</li>
							</ul>
						</li>
					</ul>
				</li>
				<li>曉匣喻細音字讀<code>h</code>而非<code>j</code>，但已大幅廣州化。</li>
                <li>分<code>ak</code>同<code>aak</code>。</li>
			</ul>
		</li>
		<li>補充：
			<ul>
				<li>【太平】廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，太平聲母則爲<code>f</code>，如「黃」<code>foeng4</code>「換」<code>fun6</code>「會」<code>fui6</code>「活」<code>fut6</code>。
					<ul>
						<li>請符合此項用家刪除 42 行、43 行、313 行、314 行井號</li>
						<li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>w</code>。如已不能分辨者，請將 42~44 行<code>xform</code>改爲<code>derive</code>。</li>
					</ul>
				</li>
				<li>【坦背】曉谿合口不讀脣齒，如「灰」讀<code>hui1</code>，「戶」讀<code>hu6</code>、不同「父」<code>fu6</code>混。
					<ul>
						<li>請符合此項用家在 62 行、63 行、324 行、325 行添加井號。</li>
					</ul>
				</li>
				<li>【坦背】並母字有不送氣現象，即「盤」讀<code>bun4</code>等
					<ul>
						<li>請符合此項用家將 dictionary 值改爲<code>gukwan-alt-asp</code>。</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
</details>

#### 古鎮（海洲）

古鎮位於中山市北部、小欖西邊，臨近江門。古鎮亦被稱之爲燈都，顧名思義，其主要產業即爲燈。

古鎮只有海洲操順德系方言，曹步同古鎮則主要講四邑系方言。由於菊韻本意是爲順德系方言製作方案，故目前竝無考慮製作四邑系方言。

<details>
	<summary><code>gukwan-guzan-hoizau.schema.yaml</code>：海洲音</summary>
	<ul>
		<li>本方案根據海洲音代表特徵製作。下爲同小欖音主要區別：
			<ul>
				<li>區分來孃・區分透曉</li>
				<li>脣化聲母遇 o 消失，即「過」「個」不分，皆讀<code>go3</code></li>
				<li>見系遇攝三等字裂化，讀<code>eoy /øy/</code>，如「區」<code>keoy1</code>「去」<code>heoy3</code>「車」<code>geoy1</code>「巨」<code>geoy6</code>等。</li>
				<li>「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，海洲止攝同廣州一樣變<code>eoy</code>但蟹攝則同<code>oi</code>合流，如「脆」<code>coi3</code>「銳」<code>joi6</code>「稅」<code>soi3</code>「歲」<code>soi3</code>等。</li>
				<li>效攝一等字讀<code>au</code>而非<code>ou</code>，如「高」<code>gau1</code>「刀」<code>dau1</code>「掃」<code>sau3</code>「毛」<code>mau4</code></li>
			</ul>
		</li>
		<li>以下竝非出自《中山方言誌》，而爲本人所知：
			<ul>
				<li>遇攝合口一等字除見系之外裂化爲<code>ou</code>，但亦有讀<code>au</code>話者。
					<ul>
						<li>請讀<code>au</code>用家在 98 行、339行添加井號，竝刪除 97 行、338行井號。</li>
					</ul>
				</li>
				<li>見組止攝開口三等字已裂化讀<code>ei</code>，如「其」<code>kei4</code>「起」<code>hei2</code>「機」<code>gei1</code>「紀」<code>gei3</code>等。</li>
			</ul>
		</li>
		<li>以下並無資料證明，僅爲猜測：
			<ul>
				<li>其蟹攝合口一等字變化應同小欖。</li>
                <li>分<code>ak</code>同<code>aak</code>。</li>
			</ul>
		</li>
	</ul>
</details>

#### 東鳳・阜沙

東鳳鎮位於中山市北部、小欖東邊，上接容桂、下接阜沙。工業較爲發達，亦是中山北部物流中心。

阜沙鎮位於中山市北部，上接東鳳，臨近欖鎮、黃圃、三角等地。

<details>
  <summary><code>gukwan-dungfau.schema.yaml</code>：東阜音</summary>
  <ul>
    <li>本方案根據《沙田方言》《中山方言誌》製作。下爲同小欖音主要區別：
      <ul>
        <li>區分透曉</li>
        <li>「胡」「戶」「護」三小韻讀<code>fu</code>;，無混。</li>
        <li>遇攝合口一等字除見系之外裂化爲<code>ou</code>，【西罟埗】則同小欖一樣讀<code>au</code>。
          <ul>
            <li>請讀<code>au</code>;用家在 98 行添加井號，竝刪除 97 行井號。</li>
          </ul>
        </li>
        <li>效攝一等字有人讀<code>ou</code>，亦有同小欖一樣讀<code>o</code>，根據《沙田方言》記載，【東罟埗】有混讀現象。東阜音方案默認作<code>ou</code>.
          <ul>
            <li>請讀<code>o</code>用家刪除 77 行、332 行井號。</li>
            <li>請混讀用家刪除 77 行、332 行井號後，將 77行中<code>xform</code>改爲<code>derive</code>。</li>
          </ul>
        </li>
        <li>分<code>ak</code>同<code>aak</code>。</li>
      </ul>
    </li>
    <li>補充：
      <ul>
        <li>【同安】【羅松】廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，排坎聲母則爲<code>f</code>，如「黃」<code>foeng4</code>「換」<code>fun6</code>「會」<code>fui6</code>「活」<code>fut6</code>。
          <ul>
            <li>請符合此項用家刪除 42 行、43 行、311行、312行井號。</li>
            <li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>w</code>。如已不能分辨者，請將42~44 行<code>xform</code>改爲<code>derive</code>。</li>
          </ul>
        </li>
        <li>江宕兩攝讀法異同：
          <ul>
            <li>【東罟埗】根據《中山方言誌》記載，江宕兩攝除合口皆讀<code>oeng /yœŋ/</code>，合口讀<code>woeng /wyœŋ/</code>。但《沙田方言》記載，其讀音同小欖別無二致。</li>
            <li>【大有圍】則將江宕兩攝除合口讀作<code>oeng /œŋ/</code>，合口讀<code>woeng /wœŋ/</code>。</li>
            <li>【羅松】則將江宕兩攝除合口讀作<code>oeng /yoŋ/</code>，合口讀<code>woeng /wyoŋ/</code>。</li>
            <li>以上情況有兩種方法：
              <ul>
                <li>刪除 170 行、171 行、372行井號開啓混打。</li>
                <li>刪除 170 行、374 行井號，竝將170行<code>derive</code>改爲<code>xform</code>，將所有<code>ong/ok</code>轉換爲<code>oeng/oek</code>。</li>
              </ul>
            </li>
            <li>【西罟埗】【同安】讀音基本同小欖一樣，但讀<code>oeng</code>時有合口介音<code>/y/</code>。</li>
          </ul>
        </li>
        <li>【同安】並母字有不送氣現象，即「盤」讀<code>bun4</code>等。
          <ul>
            <li>請符合此項用家將 dictionary 值改爲<code>gukwan-asp</code>。</li>
          </ul>
        </li>
        <li>【羅松】幫組接un·ut時讀on·ot。
          <ul>
			<li>請符合此項用家刪除 199 行、373 行井號。
		  </ul>
        </li>
      </ul>
    </li>
  </ul>
</details>

#### 橫欄

橫欄鎮位於中山市西部，毗鄰欖鎮、隆都。西邊即爲新會。

<details>
	<summary><code>gukwan-waanglaan.schema.yaml</code>：橫欄音</summary>
	<ul>
		<li>本方案綜合橫欄各地鄉音——四沙（兩書合作人皆爲貼邊人）・六沙・橫東。
			<ul>
				<li>ong/ok 歸 oeng/oek，即「江」「薑」不分，皆讀<code>goeng1</code>。實際打字兩者皆可。
					<ul>
						<li>橫東方面，兩個脣化聲母遇 oeng/oek 即展脣化。故「光」「江」「薑」不分，皆讀<code>goeng1</code>（「黃」則讀<code>woeng4</code>，不讀作<code>oeng4</code>）。</li>
						<li>/oe/實際發音爲[yø]，如有需要可自行將方案調整爲 yo 或 yoe 以貼合實際發音。
							<ul>
								<li>如需修改鍵值，需同時修改三拼規矩。</li>
							</ul>
						</li>
					</ul>
				</li>
				<li>蟹攝合口一等字同廣州一樣爲<code>eoy</code>，並不讀作<code>yu</code>。</li>
				<li>遇攝合口一等字裂化同廣州一樣爲<code>ou</code>：「度」<code>dou6</code>「無」<code>mou4</code>「做（作）」<code>zou6</code>「粗」<code>cou1</code>等。</li>
				<li>《沙田方言》中，效攝一等記作<code>o</code>，但《中山方言誌》全部紀錄點都爲<code>ou</code>。此處採用《中山方言誌》記錄，請根據實際情況自行調整。（如需改請刪除 77 行、335 行井號）</li>
				<li>「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，橫欄仍保持其對<code>eoy</code>、<code>oi</code>、<code>ooi</code>之對立。其中以六沙最爲完整。即「趣」<code>ceoy3</code>「菜」<code>coi3</code>「脆」<code>cooi3</code>不同音。
					<ul>
						<li>其他方言點之中，蟹攝三等合口字讀<code>eoy</code>而非<code>ooi</code>。（如需改請在 81 行、337 行添加井號，竝刪除 82 行、338 行井號）</li>
						<li>/ooi/實際發音爲[oø]，如有需要可自行將方案調整爲<code>ooy</code>以貼合實際發音。</li>
						<li>/eoy/實際發音爲[øy]。</li>
						<li>《沙田方言》並無記載此對立。</li>
					</ul>
				</li>
				<li>曉匣喻細音字讀<code>h</code>而非<code>j</code>，如「爺」<code>he4</code>「賢」<code>hin4</code>「雨」<code>hy5</code>「藥」<code>hoek6</code>。
					<ul>
						<li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>j</code>。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將 37 行井號刪除，竝將 37~40 行<code>xform</code>改爲<code>derive</code>。</li>
					</ul>
				</li>
				<li>廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，橫欄聲母則爲<code>f</code>，如「黃」<code>foeng4</code>「換」<code>fun6</code>「會」<code>fui6</code>「活」<code>fut6</code>。
					<ul>
						<li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>w</code>。如已不能分辨者，請將 42~44 行<code>xform</code>改爲<code>derive</code>。</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
  <p>參攷：《沙田方言》《中山方言誌》</p>
</details>

#### 南頭

南頭鎮位於中山市北部，同桂州對望，毗鄰東鳳鎮、黃圃鎮。工業較爲發達。

<details>
<summary><code>gukwan-naamtau.schema.yaml</code>：南頭音</summary>
<ul>
  <li>本方案根據《中山方言誌》製作。下爲重要特徵：
    <ul>
      <li>本人所有資料中唯一江攝宕攝分四種：「江<sup>江攝</sup>」讀<code>ong</code>「窗<sup>江攝莊組・宕攝開三</sup>」讀<code>yong</code>（僅作顯示，默認不用<code>yong</code>，鍵值爲<code>iong/oeng</code>）「宕<sup>宕攝</sup>」讀<code>yoong</code>（僅作顯示，默認不用，鍵值爲<code>oong</code>打）「廣sup>宕攝合口</sup>」讀<code>wong</code><ul>
          <li>如需修改鍵值，需同時修改三拼規矩。</li>
        </ul>
      </li>
      <li>遇攝合口一等字裂化同廣州一樣爲<code>ou</code>：「度」<code>dou6</code>「無」<code>mou4</code>「做（作）」<code>zou6</code>「粗」<code>cou1</code>等。</li>
      <li>效攝一等字發音同廣州一樣爲<code>ou</code>：「好」<code>hou2</code>「逃」<code>tou4</code>「早」<code>zou2</code>「掃」<code>sou3</code>等。</li>
      <li>廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，排坎聲母則爲<code>f</code>，如「黃」<code>foeng4</code>「換」<code>fun6</code>「會」<code>fui6</code>「活」<code>fut6</code>。
        <ul>
          <li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>w</code>。如已不能分辨者，請將42~44 行<code>xform</code>改爲<code>derive</code>。</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>以下並無資料證明，僅爲猜測：
    <ul>
      <li>曉匣喻細音字讀<code>h</code>而非<code>j</code>，如「爺」<code>he4</code>「賢」<code>hin4</code>「雨」<code>hy5</code>「藥」<code>hoek6</code>。
        <ul>
          <li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>j</code>。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將37 行井號刪除，竝將 37~40 行<code>xform</code>改爲<code>derive</code>。</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>以上均以排坎音爲基準，以下爲地方音補充：
    <ul>
      <li>【滘心】幫組接un·ut時讀yn·yt。
        <ul>
          <li>請符合此項用家刪除 201 行、378 行井號。</li>
        </ul>
      </li>
      <li>【滘心】「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，滘心止攝同廣州一樣變<code>eoy</code>但蟹攝則同<code>oi</code>合流，如「脆」<code>coi3</code>「銳」<code>joi6</code>「稅」<code>soi3</code>「歲」<code>soi3</code>等。<ul>
          <li>請符合此項用家在 82 行、336 行添加井號，竝刪除 83 行、337 行井號</li>
        </ul>
      </li>
      <li>【滘心】【低沙】江宕兩攝除合口皆讀<code>ong /yoŋ/</code>，合口讀<code>wong /woŋ/</code>。
        <ul>
          <li>請符合此項用家將 130~131 行、171 行<code>derive</code>改爲<code>xform</code>，在 132 行、361~363 行添加井號，竝刪除 171 行、364~366 行井號。</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
</details>

<details>
<summary><code>gukwan-naamtau-naamsing.schema.yaml</code>：南頭南城音</summary>
<ul>
  <li>本方案根據《沙田方言》製作。下爲重要特徵：
    <ul>
      <li>ong/ok 歸 oeng/oek，而兩個脣化聲母遇 oeng/oek 即展脣化，故「光」「江」「薑」不分，皆讀<code>goeng1</code>（注意：「黃」仍讀<code>woeng4</code>，不讀作<code>oeng4</code>）。實際打字兩者皆可。</li>
      <li>蟹攝合口一等字，廣州話讀<code>eoy</code>者，南城音有部份讀作作<code>yu</code>：
        <ul>
          <li>端組同來母讀<code>yu</code>，如「對」<code>dy3</code>「腿」<code>ty2</code>「堆」<code>dy1</code>「雷」<code>sy3</code>等。</li>
          <li>精組多數人則裂化讀<code>eoy</code>，如「最」<code>zeoy3</code>「罪」<code>zeoy6</code>「催」<code>ceoy1</code>等。</li>
        </ul>
      </li>
      <li>脣化聲母遇 o 消失，即「過」「個」不分，皆讀<code>go3</code></li>
      <li>遇攝合口一等字裂化同廣州一樣爲<code>ou</code>：「度」<code>dou6</code>「無」<code>mou4</code>「做（作）」<code>zou6</code>「粗」<code>cou1</code>等。</li>
    </ul>
  </li>
</ul>
</details>

#### 三角【未製作】

三角鎮位於中山市東部，同南沙對望。三角山四周操三角話，是莞寶系方言。其他地方則講順德系方言。

`gukwan-saamgok-punlung.schema.yaml`：三角蟠龍音

- 本方案根據《中山方言誌》製作。下爲重要特徵：
  - 區分來孃
  - 遇攝合口一等字除見系之外低化爲`o`，如「度」`do6`「無」`mo4`「做（作）」`zo6`「粗」`co1`等。
  - 「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，止攝合口銳音歸`eoy`，但蟹攝三等合口字仍保持其同`eoy`、`oi`兩音之對立。即「趣」`ceoy3`「菜」`coi3`「脆」`cooi3 /ʦʰuoi`不同音。
  - 其韻母`oe`仍帶有少許介音，讀`/iœ/`。

#### 黃圃【未製作】

黃圃鎮位於中山市東北部，同桂州對望，毗鄰三角鎮、南頭鎮。以臘味聞名。

#### 西區（沙蓢）【未製作】

沙蓢今屬西區（鄉級），是市區附近除港口少有講順德系方言地區。

#### 港口【未製作】

港口鎮位於市區北邊。

#### 民衆（浪網）

民眾鎮位於中山市東部，與南沙對望。

由於民衆鎮其他音屬蜑家話，此處不收，僅收浪網音。浪網鎮於 2000 年撤鎮，劃入民衆鎮。民衆鎮除舊浪網鎮轄地皆操蜑家話。

<details>
	<summary><code>gukwan-longmong.schema.yaml</code>：浪網音</summary>
	<ul>
		<li>本方案根據浪網音代表特徵製作。下爲重要特徵：
			<ul>
				<li>曉匣喻細音字讀<code>h</code>而非<code>j</code>，如「爺」<code>he4</code>「賢」<code>hin4</code>「雨」<code>hy5</code>「藥」<code>hoek6</code>。
					<ul>
						<li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>j</code>。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將 37 行井號刪除，竝將 37~40 行<code>xform</code>改爲<code>derive</code>。</li>
					</ul>
				</li>
				<li>師韻字讀作<code>i</code>而非<code>y</code>，如「資」<code>zi1</code>「師」<code>si1</code>「字」<code>zi6</code>「此」<code>ci2</code>等。</li>
				<li>蟹攝合口一等字，廣州話讀<code>eoy</code>者，浪網音全數讀<code>yu</code>，如「對」<code>dy3</code>「腿」<code>ty2</code>「催」<code>cui1</code>「最」<code>zy3</code>。</li>
				<li>「ooi音」，來自於蟹攝三等合口字同止攝合口銳音，浪網止攝同廣州一樣變<code>eoy</code>但蟹攝則同<code>oi</code>合流，如「脆」<code>coi3</code>「銳」<code>joi6</code>「稅」<code>soi3</code>「歲」<code>soi3</code>等。</li>
				<li>遇攝合口一等字裂化同廣州一樣爲<code>ou</code>：「度」<code>dou6</code>「無」<code>mou4</code>「做（作）」<code>zou6</code>「粗」<code>cou1</code>等。</li>
				<li>效攝一等字發音同廣州一樣爲<code>ou</code>：「好」<code>hou2</code>「逃」<code>tou4</code>「早」<code>zou2</code>「掃」<code>sou3</code>等。但根據《沙田方言》，此類字讀<code>o</code>而非<code>ou</code>。菊韻採用《中山方言誌》記錄。</li>
				<li>根據《中山方言誌》，其韻母<code>oe</code>仍帶有少許介音，讀<code>oe /iœ/</code>。群安則讀作<code>io /io/</code>。默認設定上，僅韻腹可oe·io混打。</li>
				<li>根據《沙田方言》，遇三所有無裂化字均讀作<code>i</code>，如「語」<code>ji5</code>「處」<code>ci3</code>「擧」<code>gi2</code>「書」<code>si1</code>等，此爲蜑家話特徵。但根據《中山方言誌》，此類字仍讀攝口（y）。菊韻採用《中山方言誌》記錄。</li>
				<li>並母字有不送氣現象，即「盤」讀<code>bun4</code>等</li>
				<li>【群安】廣州話聲母<code>w</code>同韻腹<code>u/o</code>結合者，群安聲母則爲<code>f</code>，如「黃」<code>foeng4</code>「換」<code>fun6</code>「會」<code>fui6</code>「活」<code>fut6</code>。
					<ul>
						<li>請符合此項用家刪除 42 行、43 行、313 行、314 行井號</li>
						<li>此類字往往越接近現代，就會有越多字跟廣州一樣讀<code>w</code>。如已不能分辨者，請將 42~44 行<code>xform</code>改爲<code>derive</code>。</li>
					</ul>
				</li>
			</ul>
		</li>
	</ul>
	<p>參攷：《沙田方言》《中山方言誌》</p>
</details>

### 順德

#### 大良

- `gukwan-daailoeng.schema.yaml`：大良音
  - 本方案根據大良話代表特徵製作。下爲重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以 aak 音打 ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 不分`ing/ik`同`in/it`，故可以 in/it 音打 ing/ik（如「迫」`bik1`可打`bit1`）。
    - `yun/yt`老派讀`un/ut`，但因同`eon/eot`簡拼衝突故不採用。
    - 蟹攝合口一等字，廣州話讀`eoy`者，大良老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已讀作`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將 37 行井號刪除，竝將 37~40 行`xform`改爲`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，大良聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將 42~44 行`xform`改爲`derive`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

#### 陳村

- `gukwan-cancyn.schema.yaml`：陳村音
  - 本方案根據陳村話代表特徵製作。下爲重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以 aak 音打 ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 陳村音止攝字無發生裂化，故廣州話讀`ei`者，陳村仍舊讀`i`，如「皮」`pi4`「鼻」`bi6`「地」`di6`「四」`si3`。
    - 蟹攝合口一等字，廣州話讀`eoy`者，陳村老派音讀`ui`，新派音讀`yu`：
      - 端組、來母、清母、心母讀作`ui`（新派讀`yu`），如「對」`dui3`「腿」`tui2`「催」`cui1`「碎」`sui3`等。
      - 精組（除清母、心母）多數人已讀作`eoy`，如「最」`zeoy3`「罪」`zeoy6`等，故不納入。
    - 遇攝合口一等字裂化同廣州一樣爲`ou`：「度」`dou6`「無」`mou4`「做（作）」`zou6`「粗」`cou1`等。
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將 37 行井號刪除，竝將 37~40 行`xform`改爲`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，陳村聲母則爲`f`，如「黃」`foeng4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將 42~44 行`xform`改爲`derive`。
    - 「花」「輝」「快」「筷」等少部分曉母合口字讀`w-`
    - 「蠅」「業」「惹」「仰」等少部分細音字讀`h-`
    - 「船」「射」「繩」「蛇」等少部分擦音字塞化讀`c-`或者`z-`
    - 「婆」「茶」「糖」「田」等少部分送氣字無氣化
    - 「件」「解」「揀」「掛」等少部分無氣字送氣化

#### 均安【未製作】

- `gukwan-gwanon.schema.yaml`：均安音
  - 下爲均安話重要特徵：
    - 不分來孃且疑母脫落，故疑母字可作零聲母（如「我」`ngo5`可打`o5`）。
    - 不分`ak`同`aak`，故可以 aak 音打 ak（如「勒」`lak6`可打`laak6`）。
      - 老派只有`aak`，無`ak`
    - 效攝一等字讀`aau`，如「高」`gaau1`「刀」`daau1`「掃」`saau3`「毛」`maau4`
    - 山攝開口一等字陽聲韻見系不讀`on`讀`aan`，如「漢」`haan3`「岸」`ngaan6`「安」`aan3`「乾」`gaan1`，但入聲中新派同廣州話一樣，只有少數作爲白讀字保留，如「割」`gaat3`「渴」`haat3`。
    - 蟹攝合口一等字，廣州話讀`eoy`者，均安話多讀作`yu`：
      - 端組、來母同心母讀作`yu`，如「對」`dy3`「腿」`ty2`「堆」`dy1`「碎」`sy3`等。
      - 精組（除心母）多數人則讀`ooi`（同`oi`無對立），如「最」`zoi3`「罪」`zoi6`「催」`coi1`等。
    - 遇攝三等字裂化者同`ooi音`，即廣州話讀`eoy`者，均安話均讀作`ooi`（同`oi`無對立），如「女」`noi5`「旅」`loi5`「醉」`zoi3`「隨」`coi4`
    - 曉匣喻細音字讀`h`而非`j`，如「爺」`he4`「賢」`hin4`「雨」`hy5`「藥」`hoek6`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`j`。例如小欖就基本剩低極少數白讀字。如已不能分辨者，請將 37 行井號刪除，竝將 37~40 行`xform`改爲`derive`。
    - 廣州話聲母`w`同韻腹`u/o`結合者，均安聲母則爲`f`，如「黃」`fong4`「換」`fun6`「會」`fui6`「活」`fut6`。
      - 均安有部份讀`h`，如「慌」`hong1`。
      - 此類字往往越接近現代，就會有越多字跟廣州一樣讀`w`。如已不能分辨者，請將 42~44 行`xform`改爲`derive`。
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

<details>
	<summary>主要指出同廣州話異同，以石歧鎮（岐江河內）爲準：</summary>
	<ul>
		<li>聲母
			<ul>
				<li>區分來孃，故「南」<code>naam4</code>不可讀作「藍」<code>laam4</code>、「農」<code>nung4</code>不可讀作「龍」<code>lung4</code>。
				</li>
				<li>鼻音<code>m</code>｜<code>ng</code>可發生塞化，讀成<code>mb [ᵐb]</code>｜<code>ngg [ᵑg]</code>或<code>bb [b]</code>｜<code>gg [g]</code>（擴展粵拼中，準確來講爲<code>rb</code>｜<code>rg</code>），竝無對立，爲自由變體。此現象多見於閩南語，而少見於粵語。
				</li>
				<li>古非敷奉讀重脣較多，如「斧」<code>pu2</code>「扶」<code>pu4</code>等。</li>
				<li>古非敷奉合口字多數讀<code>h</code>而非脣齒音<code>f</code>，此現象極少見於粵語。今時只有同韻腹<code>u</code>結合者有此現象，如「風」<code>hung1</code>「福」<code>huk1</code>「符」<code>hu4</code>「鳳」<code>hung3</code>。而同韻腹<code>o</code>結合者則最遲見於1897年，如「方」<code>hong1</code>。根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。
				</li>
				<li>根據《中山方言誌》疑母細音字仍讀疑母，如「魚」<code>ngy4</code>「語」<code>ngy2</code>「嚴」<code>ngim4</code>「月」<code>ngyt6</code>等。甚至日母細音字亦讀作<code>ng</code>，如「耳」<code>ngi4</code>「繞」<code>ngiu3</code>「熱」<code>ngit6</code>「如」<code>ngi4</code>等。而有部份字廣州化讀<code>j</code>，如「儒」<code>jy4</code>（本應讀<code>ngy4</code>）「柔」<code>jau4</code>（本應讀<code>ngiau4</code>）「日」<code>jit2</code>（本應讀<code>ngit2</code>等，變化極不規律。
				</li>
				<li>古谿母字不少字仍讀作<code>k</code>而非<code>h</code>，此現象極少見於粵語。如「可」<code>ko2</code>
					「庫」<code>ku3</code>「筷」<code>kwaai3</code>「枯」<code>ku1</code>等。根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。</li>
				<li>兩個脣化聲母遇o系韻腹即展脣化，故「光」「江」不分，皆讀<code>gong1</code>，「過」「個」不分，皆讀<code>go3</code>。</li>
				<li>根據近代資料（直至1987年），曉匣喻細音應該同順德系一樣讀<code>h</code>（小欖除外），如「爺」<code>he4</code>「賢」<code>hin4</code>「雨」<code>hy5</code>「頁」<code>hip6</code>。但根據《中山方言誌》《中山市誌》《泛粵典》資料，並無此現象，而係同小欖一樣讀<code>j</code>。推測此廣州化現象（曉匣喻細音字讀<code>j</code>）至少在20世紀中葉開始，小欖話應該亦是類似時間開始。
					<ul>
						<li>補充：根據《澳門粵語音系的歷史變遷及其成因》，新派音此現象已消失。</li>
					</ul>
				</li>
				<li>影以日母廣州話讀<code>j</code>，石歧話則讀作零聲母，「英」則讀作<code>ing1</code>「翼」則讀作<code>ik6</code>。新派則同廣州一樣。此現象亦見於老派順德系方言（以白讀音保留）。
				</li>
			</ul>
		</li>
		<li>韻母
			<ul>
				<li>假攝三等字有嚴重混讀現象，有部份的而且保留介音讀<code>ia</code>，如「椰」<code>jaa4</code>「爺」<code>jaa4</code>「夜」<code>jaa3</code>「惹」<code>jaa3</code>（日母字），但部份字卻跟周邊其他方言讀<code>e</code>，如「社」<code>se2</code>「借」<code>ze3</code>。（應爲以<code>j</code>爲聲母者存古）
				</li>
				<li>石歧話止攝字無發生裂化，故廣州話讀<code>ei</code>者，石歧仍讀<code>i</code>，如「皮」<code>pi4</code>「鼻」<code>bi6</code>「地」<code>di6</code>「四」<code>si3</code>。
					<ul>
						<li>師韻字並無如順德系方言常見讀<code>y</code>之現象。</li>
					</ul>
				</li>
				<li>遇攝合口一等字無發生裂化，故廣州話讀<code>ou</code>者，石歧仍讀<code>u</code>，如「補」<code>bu2</code>「都」<code>du1</code>「盧」<code>lu4</code>「府」<code>hu2</code>；廣州話讀<code>eoy</code>者，石歧仍讀<code>yu</code>，如「女」<code>ny2</code>「區」<code>ky1</code>「去」<code>hy3</code>「車」<code>gy1</code>。
				</li>
				<li>果攝開口三等字讀<code>oe</code>而非<code>e</code>，如「茄」<code>koe2</code>。新派音同廣州一樣。</li>
				<li>根據《泛粵典》《澳門粵語音系的歷史變遷及其成因》蟹攝合口一等字，廣州話讀<code>eoy</code>者，石歧則讀<code>ui</code>，新派音同廣州一樣：
					<ul>
						<li>如「對」<code>dui3</code>「腿」<code>tui2</code>「催」<code>cui1</code>「碎」<code>sui3</code>「最」<code>zui3</code>。同順德系方言一樣，精母最早開始變化。順德兩個方言亦是精母最早變作<code>eoy</code>。
						</li>
					</ul>
				</li>
				<li>宕攝江攝，廣州話讀<code>oeng/oek</code>，根據《中山方言誌》，石歧仍保留介音讀<code>iong/iok</code>，如「孃」<code>niong4</code>，「畧」<code>liok6</code>「窗」<code>ciong1</code>「張」<code>ziong1</code>，僅有少數讀<code>oeng/oek</code>。
					<ul>
						<li>根據《泛粵典》同《中山市誌》資料，石歧話已無<code>io</code>，全讀<code>oe</code>。可能因爲《中山方言誌》記錄多爲老派音。而《澳門粵語音系的歷史變遷及其成因》，老派音都<code>io</code>，新派音則爲兩者混讀。
						</li>
					</ul>
				</li>
				<li>梗攝白讀音，石歧話老派音仍保留介音讀<code>iang/iak</code>而非新派音<code>eng/ek</code>，如「平」<code>piang4</code>「命」<code>miang3</code>「驚」<code>giang1</code>「石」<code>siak6</code>。
				</li>
				<li>咸攝見系字依舊讀<code>om</code>，如「鴿」<code>gop3</code>「合」<code>hop6</code>「敢」<code>gom2</code>「柑」<code>gom1</code>等。而新派音稍爲高化，不讀<code>o [ɔ]</code>，而讀<code>oo [o]</code>。（音位無別）
				</li>
				<li>關於攝口韻
					<ul>
						<li>根據《中山方言誌》所說石歧話之中攝口韻（<code>yu/yun/yut/eoy</code>）極少，而石歧鎮外香山系方言並無攝口韻，如「雨」石歧讀<code>jy2</code>、其他方言讀<code>ji2</code>；「水」石歧讀<code>seoy2</code>，唐家讀<code>sui2</code>等。故高然先生認爲無攝口韻方是存古，今時石歧話攝口韻是因爲北部粵語遷入，甚至爲廣州話影響。
						</li>
						<li>蟹攝三等合口字同止攝合口銳音字，近代確實讀<code>ooi</code>。現代石歧話同廣州一樣讀<code>eoy</code>，而石歧鎮以外香山系方言多爲<code>ui</code>或：如「淚」<code>leoy3</code>「水」<code>seoy2</code>「嘴」<code>zeoy2</code>等。
						</li>
						<li><code>eon/eot</code>同<code>an/at</code>（兩者本身來源同一個音韻）分佈於1939年開始接近廣州，但「晉」等字仍讀<code>an</code>。而新派音則徹底被廣州同化。
						</li>
					</ul>
				</li>
				<li>《中山方言誌》雖無提及，但根據近代石歧話資料，推測石歧話見系流攝三等字本應讀<code>iau</code>，如「舊」<code>giau3</code>「求」<code>kiau4</code>。（1897年爲<code>ieu</code>，部份介音脫落變作<code>au</code>，1939年全數脫落）
				</li>
			</ul>
		</li>
		<li>聲調
			<ul>
				<li>聲調在粵語中較少，只有平聲、入聲分陰陽。上陰入歸陽入。</li>
				<li>陰平（1｜55）、陽平（4｜51）、上聲（2｜213）、去聲（3｜33）、陰入（1｜5）、陽入（6｜2）</li>
			</ul>
		</li>
	</ul>
	<p>推測石歧話「廣州化」早於19世紀晚期開始，於20世紀中葉加劇。羅言發先生亦持相同意見。</p>
	<p>《澳門粵語音系的歷史變遷及其成因》亦有提及前山音（1987年記錄）、北山音（2010年老派）同唐家音（2011年老派）。</p>
	<p>以上三個方音同石歧話主要區別爲無<code>om/op</code>，無<code>eon/eot</code>，無脣化聲母<code>gw/kw</code>。而廣州話讀<code>ng</code>，三個珠海方音則同近代石歧話一樣讀<code>ung</code>。
	</p>
	<p>此外，唐家音同北山音有其他共同現象：無<code>eoy</code>亦無<code>oi</code>，全部歸<code>ui</code>。<code>ia</code>系韻母元音融合，讀<code>e</code>。<code>i</code>音同<code>y</code>音混亂。亦不分<code>ou</code>同<code>au</code>，皆讀<code>au</code>，即「島」「斗」不分。甚至完全無<code>ing/ik</code>音，故梗攝全部讀<code>ang/ak</code>。
	</p>
	<p>雖然三個方音同樣只有六個調，但唐家音同北山音下陰入歸陰入而非陽入。</p>
	<p>但三個方音所有疑母細音字同日母字不約而同出現混亂（即部份讀<code>ng</code>，部份讀<code>j</code>，部份零聲母），前山音<code>ngj</code>音脫落最爲嚴重。曉母亦出現不同程度弱化，同時間非敷奉母開始脣齒化。基本上可以確定近四十年來各地廣州化明顯，但程度不等。
	</p>
</details>

### 石歧

由於本人非香山系方言母語者，或闕不少字音。<mark>警告：請勿以本輸入法作爲石歧話標準參攷。</mark>

<details>
	<summary><code>gukwan-sekki.schema.yaml</code>：由於石歧話老派變化並不均等，菊韻難以處理。故採用廣州化程度更深之新派音，標準如下：</summary>
	<ul>
		<li>允許疑日母細音以<code>j</code>輸入。</li>
		<li>曉匣喻細音全面廣州化，讀<code>j</code>，即「爺」不讀<code>he4</code>讀<code>je4</code>「賢」不讀<code>hin4</code>讀<code>jin4</code>「樣」不讀<code>hiong3</code>讀<code>joeng3</code>。
		</li>
		<li>谿母字全面廣州化，讀<code>f</code>或者<code>h</code>，即「可」不讀<code>ko2</code>讀<code>ho2</code>
			「庫」不讀<code>ku3</code>讀<code>hu3</code>「筷」不讀<code>kwaai3</code>讀<code>faai3</code>「枯」不讀<code>ku1</code>讀<code>hu1</code>。
		</li>
		<li>蟹攝合口一等字全面廣州化，讀<code>eoy</code>，即「對」不讀<code>dui3</code>讀<code>deoy3</code>「腿」不讀<code>tui2</code>讀<code>teoy2</code>「催」不讀<code>cui1</code>讀<code>ceoy1</code>「碎」不讀<code>sui3</code>讀<code>seoy3</code>「最」不讀<code>zui3</code>讀<code>zeoy3</code>，但仍可以用老派音<code>ui</code>輸入。
		</li>
		<li>臻攝分佈徹底廣州化，但仍可以用老派音<code>an/at</code>輸入。</li>
		<li>江攝宕攝讀<code>iong/iok</code>者可以用新派音<code>oeng/oek</code>輸入。</li>
		<li>梗攝白讀音讀<code>eng/ek</code>，如「平」<code>peng4</code>「命」<code>meng3</code>「驚」<code>geng1</code>「石」<code>sek6</code>。
		</li>
		<li>陽入作<code>3</code>，鍵值爲<code>q</code>。</li>
	</ul>
</details>

## 參攷用方案

- `gukwan-default.schema.yaml`：菊韻音（構擬音）根據菊韻標準所構擬之古音，較分韻複雜。
- `gukwan-fanwan.schema.yaml`：<del>分韻音</del>**【已移除】**
  - 準確來講此方案係分韻風，並不能準確反映所有分韻發音。若欲使用眞正分韻音打字，可參攷以下方案：[leimaau/old-Cantonese: Rime Old Cantonese Input Scheme | 《分韻撮要》音系及輸入方案](https://github.com/leimaau/old-Cantonese)
- `gukwan-canton.schema.yaml`：<del>廣州音</del>**【已移除】**
  - 並不能準確反映所有廣州發音，廣州話請用`jyut6ping3-gw`或`jyut6ping3-gw-cp`

### 構擬音特徵

<mark>警告：本構擬音僅供參攷。</mark>

構擬音是本人基於順德系方言所構擬之古音。

<details>
	<summary>主要指出其對分韻異同：</summary>
	<ul>
		<li>聲母
			<ul>
				<li>【同】區分精照（照組默認爲<code>-h</code>：<code>zh/ch/sh</code>）</li>
				<li>【同】區分日以（日母默認爲<code>-j</code>：<code>nj</code>）</li>
				<li>【異】疑母細音未歸日母，如「堯」讀<code>ngiu4</code>「仰」讀<code>ngiong5</code>「原」讀<code>ngyun4</code>「凝」讀<code>nging4</code></li>
				<li>【異】疑母合口字聲母未脫，即「玩」讀<code>ngun6</code>「頑」讀<code>ngwaen4</code></li>
				<li>【異】曉匣谿母合口字未脣齒化，如「薰」讀<code>hwan1</code>「黃」讀<code>hwong3</code>「苦」讀<code>hu2</code>「戶」讀<code>hu6</code></li>
				<li>【異】匣喻細音讀<code>h</code>，「賢」讀<code>hin4</code>「樣」讀<code>hiong6</code>「蠅」讀<code>hing4</code>「爺」讀<code>hia4</code></li>
				<li>【異】曉母接韻腹<code>a</code>讀<code>hj</code>，如「欣」讀<code>hjan1</code>「欽」讀<code>hjam1</code>「休」讀<code>hjau1</code>「釁」<code>hjan3</code>（未變調）</li>
			</ul>
		</li>
		<li>韻母
			<ul>
				<li>【異】江攝照系字・宕攝開口三等字（除莊組）讀<code>iong/iok</code>，如「薑」讀<code>giong1</code>「畧」讀<code>liok6</code>「張」讀<code>zhiong1</code>「上」讀<code>shiong5</code></li>
				<li>【異】其他宕攝字讀<code>oong</code>，同<code>ong</code>對立。如「鋼」讀<code>goong1</code>「忙」讀<code>moong4</code>「藏」讀<code>zoong6</code>「牀」讀<code>choong4</code></li>
				<li>【異】師韻分精照，讀舌尖前圓唇元音（<code>y</code>），如「字」讀<code>zy6</code>「此」讀<code>cy2</code>「師」讀<code>shy1</code>「廁」讀<code>chy3</code></li>
				<li>【異】遇攝開口三等字讀<code>yo</code>，合口讀<code>yu</code>。</li>
				<li>【異】蟹攝合口三等字除疑母皆讀<code>ui</code>。</li>
				<li>【異】止攝合口銳音・蟹攝合口三四等字讀<code>ooi</code></li>
				<li>【異】臻攝竝無<code>eon/eot</code>同<code>an/at</code>之分，皆讀<code>an/at</code></li>
				<li>【異】山開字・刪合字・效攝二等字・咸攝二等字韻腹讀<code>ae</code></li>
				<li>【異】果攝開口三等字・假攝三等字讀<code>ia</code></li>
				<li>【異】流攝三等字讀<code>iau</code></li>
				<li>【同】咸攝見系字讀<code>om</code></li>
				<li>【異】<code>e</code>系白讀字除<code>ei</code>之外韻腹讀<code>ia</code></li>
			</ul>
		</li>
	</ul>
</details>

# 文件結構・許可

> [!IMPORTANT]
>
> 部份文件竝非我所作，故許可授權不同，使用前請注意。若無備註則皆以[CC BY NC SA 4.0 許可](cc-by-nc-sa)發佈。下列擧除方案文件外其他重要文件。

## 字詞

`gukwan.dict.yaml`用於調用字表詞庫，默認亦調用 rime-cantonese 部份詞庫同粵語八股文。位置爲`/gw_dicts`。

`gukwan-alt.dict.yaml`・`gukwan-asp.dict.yaml`・`gukwan-alt-asp.dict.yaml`爲部份方言專用。

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

- `gukwan-melt-eng.schema.yaml`：混打方案
- `gukwan-melt-eng.dict.yaml`：混打辭典
  - `en_dicts/en.dict.yaml`
  - `en_dicts/en_ext.dict.yaml`

## LUA 腳本

本方案所有 LUA 腳本均有參攷[iDvel/rime-ice](https://github.com/iDvel/rime-ice)及相關文件，相關文件根據源文件許可發佈。

- `unicode.lua`：UNICODE 碼直接輸入字符，來自[shewer/librime-lua-script](https://github.com/shewer/librime-lua-script/tree/main)，隨源文件以[MIT 許可](https://mit-license.org/)發佈。
- `lunar.lua`：是日農曆，新曆轉舊歷，來自[boomker/rime-fast-xhup](https://github.com/boomker/rime-fast-xhup)，隨源文件以[LGPL 3.0 許可](https://www.gnu.org/licenses/lgpl-3.0.en.html)發佈。
- `calc_translator.lua`：計數機，來自[ChaosAlphard](https://github.com/ChaosAlphard)之 PR。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `autocap_filter.lua`：自動大寫英文詞彙，作者爲@abcdefg233 同@Mirtle，來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。
- `en_spacer.lua`：優化英文輸入體驗（自動空格），來自[iDvel/rime-ice](https://github.com/iDvel/rime-ice)。隨源文件以[GPL 3.0 許可](https://www.gnu.org/licenses/gpl-3.0.en.html)發佈。

以下腳本繁化並增添小小功能。爲避免文件被覆蓋，故改名。

- `number_gukwan.lua`：以阿拉伯數字輸入轉換漢語數字，來自[yanhuacuo/98wubi-tables](https://github.com/yanhuacuo/98wubi-tables)。增加轉換蘇州碼子功能。增加直接轉換功能。由於源文件採取[Unlicense 許可](https://unlicense.org/)，本文件亦不設限。
- `time_gukwan.lua`：以各種格式輸入是日日期時間，來自[amzxyz/rime_wanxiang](amzxyz/rime_wanxiang)。隨源文件以[CC BY 4.0 許可](https://creativecommons.org/licenses/by/4.0/)發佈。

### 其他

以下爲本倉庫自帶，毋須額外下載。關於其他依賴文件請參攷[如何在 RIME 輸入法安裝菊韻輸入法 – なかやま園](https://zonsan.fc2.page/?p=1563)。

- [`rime-cantonese-emoji`](https://github.com/rime/rime-emoji-cantonese)：用於輸入繪文字，隨源文件以[CC 0 許可](https://creativecommons.org/public-domain/cc0/)發佈。
- `symbols-gukwan.yaml`：菊韻定製標點符號（類似 Microsoft 日本語 IME）同特殊符號輸入。
- `菊韻.trime.yaml`：同文輸入法主題，基於[Wenti-D/Astralwelkin](https://github.com/Wenti-D/Astralwelkin)，隨源文件以[MIT 許可](https://mit-license.org/)發佈。不同點如下：
  - 鍵值更改，允許一鍵反査（q 鍵、p 鍵、a 鍵）。
  - 專用配色，參攷小欖特色菊花，但未夠膽用黃色驚太鮮豔，結果做變成屎黃色((o(；□；`)o))。

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

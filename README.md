
# Table of Contents

1.  [概要](#orgfaeeed5)
    1.  [これは何？](#org5a602e3)
    2.  [事前準備](#org17ce749)
        1.  [.envの作成](#org1f005dc)
        2.  [関連パッケージのインストール](#org8974a92)
        3.  [テーブルの作成](#orgf5ae558)
    3.  [稼働](#orgfb8c081)
    4.  [参考](#org86cdcd5)



<a id="orgfaeeed5"></a>

# 概要


<a id="org5a602e3"></a>

## これは何？

このコードはFTXにwebsocketをつないで、MySQLに保存します。


<a id="org17ce749"></a>

## 事前準備


<a id="org1f005dc"></a>

### .envの作成

MySQLでftxのデータを保存するためのデータベースを作成してください。

.envファイルを作成してください。中身は.env.exampleを参考にします。

必要な情報はFTXのAPIキーとMySQLのURLです。


<a id="org8974a92"></a>

### 関連パッケージのインストール

ubuntu を使っている場合は次のコマンドを実行します。

sudo apt install libssl-dev pkg-config

sudo apt-get install -y default-libmysqlclient-dev


<a id="orgf5ae558"></a>

### テーブルの作成

データベースにsave\_data\_listというテーブルを作成してください。カラムは下のように作成します。

exchange\_name: "FTX"にしてください

symbol\_name: FTXで配信しているシンボル名にしてください

table\_name: 自由に決めてください

このテーブルに次のようにINSERTしてください。
ここに記述したものが記録されていきます。

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">exchange_name</th>
<th scope="col" class="org-left">symbol_name</th>
<th scope="col" class="org-left">table_name</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">FTX</td>
<td class="org-left">BTC-PERP</td>
<td class="org-left">tickdata_ftx_btc_perp</td>
</tr>


<tr>
<td class="org-left">FTX</td>
<td class="org-left">ETC-PERP</td>
<td class="org-left">tickdata_ftx_etc_perp</td>
</tr>


<tr>
<td class="org-left">FTX</td>
<td class="org-left">XRP-PERP</td>
<td class="org-left">tickdata_ftx_xrp_perp</td>
</tr>


<tr>
<td class="org-left">&#x2026;</td>
<td class="org-left">&#x2026;</td>
<td class="org-left">&#x2026;</td>
</tr>
</tbody>
</table>

次に、各銘柄を保存するためのテーブルを作成してください。テーブル名はsave\_data\_listにあるtable\_nameと同じ名前にする必要があります。

必要なカラムはid, timestamp, price, amount, directionです。

例: tickdata\_ftx\_btc\_perpを次のようにする

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">id</th>
<th scope="col" class="org-left">timestamp(integer)</th>
<th scope="col" class="org-left">price(float)</th>
<th scope="col" class="org-left">amount(float)</th>
<th scope="col" class="org-left">direction(string)</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>

これで準備は完了です。

これらの作業がめんどくさい場合は、適切にpip installしてから create\_database.pyを実行してください。


<a id="orgfb8c081"></a>

## 稼働

cargo build &#x2013;releaseでコンパイルして./target/release/FTX\_to\_MySQLなどをする

このコードが実行されると次のように約定データが保存されていきます。

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-right">id</th>
<th scope="col" class="org-right">timestamp(integer)</th>
<th scope="col" class="org-right">price(float)</th>
<th scope="col" class="org-right">amount(float)</th>
<th scope="col" class="org-left">direction(string)</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-right">0</td>
<td class="org-right">1000000000</td>
<td class="org-right">100</td>
<td class="org-right">1.4</td>
<td class="org-left">Buy</td>
</tr>


<tr>
<td class="org-right">1</td>
<td class="org-right">1000000010</td>
<td class="org-right">90</td>
<td class="org-right">50</td>
<td class="org-left">Sell</td>
</tr>


<tr>
<td class="org-right">&#x2026;</td>
<td class="org-right">&#x2026;</td>
<td class="org-right">&#x2026;</td>
<td class="org-right">&#x2026;</td>
<td class="org-left">&#x2026;</td>
</tr>
</tbody>
</table>


<a id="org86cdcd5"></a>

## 参考

以下のモジュールを使用した
<https://github.com/fabianboesiger/ftx>


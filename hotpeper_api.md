リクルート
リクルートWEBサービスお問い合わせ利用規約プライバシーポリシー(2021年4月改定)
ホームリクルートWEBサービスについてよくある質問退会申請
新規登録
サービス一覧 
 ・ホットペッパーグルメ
ホットペッパーグルメ　ご利用案内
ホットペッパーグルメ　APIリファレンス
ご要望・お問合せ
サービス一覧
ホットペッパー.jpホットペッパー リファレンス
refグルメサーチAPI
URL
検索クエリ
サンプルクエリ
レスポンスフィールド
ref店名サーチAPI
URL
検索クエリ
サンプルクエリ
レスポンスフィールド
ref検索用ディナー予算マスタAPI
ref大サービスエリアマスタAPI
refサービスエリアマスタAPI
ref大エリアマスタAPI
ref中エリアマスタAPI
ref小エリアマスタAPI
refジャンルマスタAPI
refクレジットカードマスタAPI
ref特集マスタAPI
ref特集カテゴリマスタAPI
refエラー時のレスポンス


ref
refグルメサーチAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/gourmet/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	 
id	お店ID	お店に割り当てられた番号で検索します。	*1	(例) J999999999
20個まで指定可。*2
name	掲載店名	お店の名前で検索(部分一致)します。	 
name_kana	掲載店名かな	お店の読みかなで検索(部分一致)します。	 
name_any	掲載店名 OR かな	お店の名前または読みかな両方をOR検索(部分一致)します。	 
tel	電話番号	お店の電話番号で検索します。半角数字(ハイフンなし)	(例) 035550000
address	住所	お店の住所で検索(部分一致)します。	 	 
special	特集	特集コードをANDで絞り込みができます。
特集コードは特集マスタAPI参照。
複数指定可能*2	*1	LT0086
special_or	特集	特集コードをORで絞り込みができます。
特集コードは特集マスタAPI参照。
複数指定可能*2	*1	LT0086,LT0045
special_category	特集カテゴリ	特集カテゴリコードをANDで絞り込みができます。
特集カテゴリコードは特集カテゴリマスタAPI参照。
複数指定可能*2	 	SPD1
special_category_or	特集カテゴリ	特集カテゴリコードをORで絞り込みができます。
特集カテゴリコードは特集カテゴリマスタAPI参照。
複数指定可能*2	 	SPD1,SPD3
large_service_area	大サービスエリアコード	エリアに割り当てられたコード番号で検索します。指定できるコード番号はエリアマスタAPIを参照。	*1	 
service_area	サービスエリアコード	3個まで指定可。*2
large_area	大エリアコード	3個まで指定可。*2
middle_area	中エリアコード	5個まで指定可。*2
small_area	小エリアコード	5個まで指定可。*2
keyword	キーワード	店名かな、店名、住所、駅名、お店ジャンルキャッチ、キャッチのフリーワード検索(部分一致)が可能です。文字コードはUTF8。半角スペース区切りの文字列を渡すことでAND検索になる。複数指定可能*2	*1	 
lat	緯度	ある地点からの範囲内のお店の検索を行う場合の緯度です。	*1	(例) 35.669220
lng	経度	ある地点からの範囲内のお店の検索を行う場合の経度です。	(例) 139.761457
range	検索範囲	ある地点からの範囲内のお店の検索を行う場合の範囲を5段階で指定できます。たとえば300m以内の検索ならrange=1を指定します	1: 300m
2: 500m
3: 1000m (初期値)
4: 2000m
5: 3000m
(例) 1
datum	測地系	緯度・経度の測地系を指定できます。world: 世界測地系、tokyo: 旧日本測地系。初期値は world。	 	(例) world
ktai_coupon	携帯クーポン掲載	携帯クーポンの有無で絞り込み条件を指定します。		1：携帯クーポンなし
0：携帯クーポンあり
指定なし：絞り込みなし
genre	お店ジャンルコード	お店のジャンル(サブジャンル含む)で絞込むことができます。指定できるコードについてはジャンルマスタAPI参照	 	*2
budget	検索用ディナー予算コード	ディナー予算で絞り込むことができます。指定できるコードについてはディナー予算マスタAPI参照	 	2個まで指定可。*2
party_capacity	宴会収容人数	宴会収容人数で絞り込むことができます。指定数より大きな収容人数のお店を検索します	 	(例) 50
wifi	WiFi 有無	WiFi 経由によるインターネット利用が可能なお店を絞り込みます。	 	0:絞り込まない（初期値）
1:絞り込む
wedding	ウェディング二次会等	ウェディング・二次会等のお問い合わせが可能なお店を絞り込みます。	 	0:絞り込まない（初期値）
1:絞り込む
course	コースあり	「コースあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
free_drink	飲み放題	「飲み放題」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
free_food	食べ放題	「食べ放題」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
private_room	個室あり	「個室あり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
horigotatsu	掘りごたつあり	「掘りごたつあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
tatami	座敷あり	「座敷あり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
cocktail	カクテル充実	「カクテル充実」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
shochu	焼酎充実	「焼酎充実」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
sake	日本酒充実	「日本酒充実」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
wine	ワイン充実	「ワイン充実」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
card	カード可	「カード可」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
non_smoking	禁煙席	「禁煙席」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
charter	貸切	「貸切可」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
ktai	携帯電話OK	「携帯電話OK」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
parking	駐車場あり	「駐車場あり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
barrier_free	バリアフリー	「バリアフリー」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
sommelier	ソムリエがいる	「ソムリエがいる」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
night_view	夜景がキレイ	「夜景がキレイ」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
open_air	オープンエア	「オープンエア」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
show	ライブ・ショーあり	「ライブ・ショーあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
equipment	エンタメ設備	「エンタメ設備」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
karaoke	カラオケあり	「カラオケあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
band	バンド演奏可	「バンド演奏可」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
tv	TV・プロジェクター	「TV・プロジェクター」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
lunch	ランチあり	「ランチあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
midnight	23時以降も営業	「23時以降も営業」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
midnight_meal	23時以降食事OK	「23時以降食事OK」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
english	英語メニューあり	「英語メニューあり」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
pet	ペット可	「ペット可」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
child	お子様連れOK	「お子様連れOK」という条件で絞り込むかどうかを指定します。	 	0:絞り込まない（初期値）
1:絞り込む
credit_card	クレジットカード	クレジットカードの種別ごとに絞り込むことができます。指定できるコードについてはクレジットカードマスタAPI参照。(2008/02/08追加)	 	複数指定可
type	出力タイプ	レスポンス項目の項目数を指定できます。
liteを指定すると、主要項目のみ出力されます。出力項目はレスポンスフィールドを参照してください。
credit_card、specialを指定することで、クレジットカード、特集をレスポンスに付加できます。 +でつないで指定することで、複数指定が可能です。 例:type=credit_card+specialと指定することで、クレジットカードと特集両方をレスポンスに付加可能です。	 	lite:主要項目のみ
credit_card:クレジットカードをレスポンスに付加
special:特集をレスポンスに付加
指定なし:クレジットカード、特集以外をすべて出力（初期値）
order	ソート順	検索結果の並び順を指定します。おススメ順は定期的に更新されます。
※ 位置検索の場合、「4:オススメ順」以外は指定に関係なく、強制的に距離順でソートされます。	 	1:店名かな順
2:ジャンルコード順
3:小エリアコード順
4:おススメ順
初期値はおススメ順。位置から検索を行った場合は距離順
start	検索の開始位置	検索結果の何件目から出力するかを指定します。	 	初期値:1
count	1ページあたりの取得数	検索結果の最大出力データ数を指定します。	 	初期値：10、最小1、最大100
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*1　いずれか最低1つが必要
*2 複数可のパラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...
個数の上限が指定されてる場合は、その数を超えたパラメータは無視されます。
ページトップへ
サンプルクエリ
大エリアコード=Z011(東京)のお店を検索

http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=[APIキー]&large_area=Z011
■地点を指定して、その範囲にあるお店をオススメ順に取得

http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=[APIキー]&lat=34.67&lng=135.52&range=5&order=4
※実際にご利用いただくには新規登録をした上で、取得したご自身のAPIキーをGETパラメータに加えていただく必要があります。

ページトップへ
レスポンスフィールド
フィールド	説明	例	lite*1
results	 	 	○
api_version	APIのバージョン	1.20	○
results_available	クエリー条件にマッチする、検索結果の全件数	47	○
results_returned	このＸＭＬに含まれる検索結果の件数	47	○
results_start	検索結果の開始位置	1	○
shop	[複数要素]	 	○
id	お店ID	J999999999	○
name	掲載店名	居酒屋 ホットペッパー	○
logo_image	ロゴ画像	URL	-
name_kana	掲載店名かな	いざかや　ほっとぺっぱー	-
address	住所	東京都中央区銀座８－４－１７	○
station_name	最寄駅名	銀座	-
ktai_coupon	携帯用クーポン掲載
0:あり、1:なし	0	-
large_service_area	大サービスエリア	 	-
code	大サービスエリアコード	SS10	-
name	大サービスエリア名	関東	-
service_area	サービスエリア	 	-
code	サービスエリアコード	SA11	-
name	サービスエリア名	東京	-
large_area	大エリア	 	-
code	大エリアコード	Z011	-
name	大エリア名	東京	-
middle_area	中エリア	 	-
code	中エリアコード	Y005	-
name	中エリア名	銀座・有楽町・新橋・築地・月島	-
small_area	小エリア	 	-
code	小エリアCD	X010	-
name	小エリア名	銀座5～8丁目	-
lat	緯度（測地系は検索時に指定したもの）	35.6608183454	○
lng	経度（測地系は検索時に指定したもの）	139.7754267645	○
genre	お店ジャンル	 	○
code	お店ジャンルコード	G001	-
name	お店ジャンル名	居酒屋	○
catch	お店ジャンルキャッチ	一口餃子専門店	○
sub_genre	お店サブジャンル	マスタはジャンルと同じです。	-
code	お店サブジャンルコード	G001	-
name	お店サブジャンル名	居酒屋	-
budget	ディナー予算	 	-
code	検索用ディナー予算コード	B001	-
name	検索用ディナー予算	～1000	-
average	平均ディナー予算	「900円」「フリー2500円　宴会3500円」など	-
budget_memo	料金備考	お通し代300円	-
catch	お店キャッチ	TVの口コミランキングで堂々1位に輝いた一口餃子専門店！！	○
capacity	総席数	300	-
access	交通アクセス	銀座駅A2出口でて､みゆき通り右折､徒歩1分	○
mobile_access	携帯用交通アクセス	銀座一丁目駅10番出口徒歩3分	-
urls	店舗URL	 	○
pc	PC向けURL	 	○
photo	写真	 	○
pc	PC向け	 	○
l	店舗トップ写真(大）画像URL	 	○
m	店舗トップ写真(中）画像URL	 	○
s	店舗トップ写真(小）画像URL	 	○
mobile	携帯向け	 	-
l	店舗トップ写真(大）画像URL	 	-
s	店舗トップ写真(小）画像URL	 	-
open	営業時間	月～金／11：30～14：00	-
close	定休日	日	-
party_capacity	最大宴会収容人数	185	-
wifi	WiFi 有無	あり、なし、未確認 のいずれか	-
wedding	ウェディング･二次会	応相談	-
course	コース	あり	-
free_drink	飲み放題	あり	-
free_food	食べ放題	あり	-
private_room	個室	あり	-
horigotatsu	掘りごたつ	なし	-
tatami	座敷	なし	-
card	カード可	利用可	-
non_smoking	禁煙席	一部禁煙	-
charter	貸切可	貸切不可	-
ktai	携帯電話OK	つながりにくい	-
parking	駐車場	なし	-
barrier_free	バリアフリー	なし	-
other_memo	その他設備	プロジェクターあります。	-
sommelier	ソムリエ	いる	-
open_air	オープンエア	あり	-
show	ライブ・ショー	なし	-
equipment	エンタメ設備	なし	-
karaoke	カラオケ	なし	-
band	バンド演奏可	不可	-
tv	TV・プロジェクター	なし	-
english	英語メニュー	あり	-
pet	ペット可	可	-
child	お子様連れ	お子様連れ歓迎	-
lunch	ランチ	あり	-
midnight	23時以降も営業	営業している	-
shop_detail_memo	備考	プロジェクター利用可	-
coupon_urls	クーポンURL	 	-
pc	PC向けURL	 	-
sp	スマートフォン向けURL	 	-
*1 ○印がついている項目のみが、type=liteを指定したときに出力される。

レスポンスフィールド - 特集
type指定にspecialが含まれるときに、レスポンスに付加されます。
例1: type=specialと指定すると、特集がレスポンスに付加されます
例2: type=special+credit_cardと指定すると、特集とクレジットカードがレスポンスに付加されます

フィールド	説明	例
special	特集[複数要素]	
code	特集コード	LV0069
name	特集名	家族でがっつり焼肉を食べよう♪
special_category	特集カテゴリ	
code	特集カテゴリコード	SPC0
name	特集カテゴリ名	宴会で盛り上がろう！
title	タイトル - お店ごとの特集に関連した、キャッチコピーで、お店ごとに異なります	個室風テーブル席で食べ飲み放題


レスポンスフィールド - クレジットカード
type指定にcredit_cardが含まれるときに、レスポンスに付加されます。
例1: type=credit_cardと指定すると、クレジットカードがレスポンスに付加されます。
例2: type=lite+credit_cardと指定すると、lite対象の項目にクレジットカードがレスポンスに付加されます。

フィールド	説明	例
credit_card	クレジットカード	[複数要素]
code	クレジットカードコード	c99
name	クレジットカード名	○○カード
ページトップへ


ページトップへ
ref
ref店名サーチAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/shop/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
keyword	キーワード	お店の名前・読みがな・住所で検索（部分一致）します。文字コードはUTF8。半角スペース区切りの文字列を渡すことでAND検索になる。複数指定可能*2。	*1	
tel	電話番号	お店の電話番号で検索(完全一致)します。半角数字(ハイフンなし)	*1	
start	検索の開始位置	検索結果の何件目から出力するかを指定します。	 	初期値:1
count	1ページあたりの取得数	検索結果の最大出力データ数を指定します。	 	初期値：30、最小1、最大30
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*1 いずれか最低1つが必要
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...
*3 検索条件にヒットする店舗が30件より多い場合はエラーになり「条件を絞り込んでください。」とメッセージがレスポンスされます。条件を追加して30件以内の店緒がヒットするようにしてください。店舗名や住所、電話番号等の一部がある程度わかっている場合にご利用いただける仕様となっております。
ページトップへ
サンプルクエリ
キーワード「オーガニック,東京」で店名を検索

http://webservice.recruit.co.jp/hotpepper/shop/v1/?key=[APIキー]&keyword=%E3%82%AA%E3%83%BC%E3%82%AC%E3%83%8B%E3%83%83%E3%82%AF%2C%E6%9D%B1%E4%BA%AC
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	47
results_returned	このＸＭＬに含まれる検索結果の件数	47
results_start	検索結果の開始位置	1
shop	[複数要素]	
id	お店ID	J999999999
name	掲載店名	居酒屋 ホットペッパー
name_kana	掲載店名かな	いざかや　ほっとぺっぱー
address	住所	東京都中央区銀座８－４－１７
genre	お店ジャンル	 
name	お店ジャンル名	居酒屋
urls	店舗URL	 
pc	PC向けURL	 
desc	詳細フラグ。1の場合グルメサーチAPI対象店舗	0:なし、1:あり
ページトップへ
サンプルレスポンス
<?xml version="1.0" encoding="UTF-8" ?> 
<results xmlns="http://webservice.recruit.co.jp/HotPepper/">
  <api_version>1.20</api_version> 
  <results_available>47</results_available> 
  <results_returned>1</results_returned> 
  <results_start>1</results_start>
   <shop> 
    <id>J000000000</id>
    <name>リクルートカフェ</name>
    <name_kana>りくるーとかふぇ</name_kana>
    <address>東京都中央区新橋</address>
    <genre>
        <name>カフェ・喫茶</name>
    </genre>
    <urls>
        <pc>http://www.hotpepper.jp/...</pc>
    </urls>
    <desc>0</desc>
  </shop>
ページトップへ
ref
ref検索用ディナー予算マスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/budget/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。

ページトップへ
サンプルクエリ
検索用ディナー予算マスタを検索

http://webservice.recruit.co.jp/hotpepper/budget/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	6
results_returned	このＸＭＬに含まれる検索結果の件数	6
results_start	検索結果の開始位置	1
budget	[複数要素]	
code	検索用ディナー予算コード	B001
name	検索用ディナー予算テキスト	～2000円
ページトップへ
ref
ref大サービスエリアマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/large_service_area/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。

ページトップへ
サンプルクエリ
大サービスエリアマスタを検索

http://webservice.recruit.co.jp/hotpepper/large_service_area/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	9
results_returned	このＸＭＬに含まれる検索結果の件数	9
results_start	検索結果の開始位置	1
large_service_area	[複数要素]	
code	大サービスエリアコード	SS20
name	大サービスエリア名	関西
ページトップへ
ref
refサービスエリアマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/service_area/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。

ページトップへ
サンプルクエリ
サービスエリアマスタを検索

http://webservice.recruit.co.jp/hotpepper/service_area/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	47
results_returned	このＸＭＬに含まれる検索結果の件数	47
results_start	検索結果の開始位置	1
service_area	[複数要素]	
code	サービスエリアコード	SA11
name	サービスエリア名	東京
large_service_area		 
code	大サービスエリアコード	SS10
name	大サービスエリア名	関東
ページトップへ
ref
ref大エリアマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/large_area/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
large_area	大エリアコード	大エリアコードで検索(完全一致)します。（3個まで指定可、4個以上指定すると4個目以降無視します）*2		Y005
keyword	大エリア名	大エリア名で検索(部分一致)します。UTF8(URLエンコード)で指定		神奈川
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
大エリアマスタを検索

http://webservice.recruit.co.jp/hotpepper/large_area/v1/?key=[APIキー] 
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	47
results_returned	このＸＭＬに含まれる検索結果の件数	47
results_start	検索結果の開始位置	1
large_area	[複数要素]	
code	大エリアコード	Z011
name	大エリア名	東京
service_area		 
code	サービスエリアコード	SA11
name	サービスエリア名	東京
large_service_area		 
code	大サービスエリアコード	SS10
name	大サービスエリア名	関東
ページトップへ
ref
ref中エリアマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/middle_area/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
middle_area	中エリアコード	中エリアコードで検索(完全一致)します。（5個まで指定可、6個以上指定すると6個目以降無視します）*2		Y005
large_area	大エリアコード	大エリアコードで検索(完全一致)します。（3個まで指定可、4個以上指定すると4個目以降無視します）*2		Z011
keyword	中エリア名	中エリア名で検索(部分一致)します。UTF8(URLエンコード)で指定		飯田橋
start	検索の開始位置	検索結果の何件目から出力するかを指定します。	 	初期値:1
count	1ページあたりの取得数	検索結果の最大出力データ数を指定します。	 	初期値：なし、最小1、最大：なし（すべて取得）
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
中エリアマスタを検索

http://webservice.recruit.co.jp/hotpepper/middle_area/v1/?key=[APIキー]&middle_area=Y005
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	47
results_returned	このＸＭＬに含まれる検索結果の件数	47
results_start	検索結果の開始位置	1
middle_area	[複数要素]	
code	中エリアコード	Y055
name	中エリア名	新宿
large_area		 
code	大エリアコード	Z011
name	大エリア名	東京
service_area		 
code	サービスエリアコード	SA11
name	サービスエリア名	東京
large_service_area		 
code	大サービスエリアコード	SS10
name	大サービスエリア名	関東
ページトップへ
ref
ref小エリアマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/small_area/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
small_area	小エリアコード	小エリアコードで検索(完全一致)します。（5個まで指定可、6個以上指定すると6個目以降無視します）*2		X005
middle_area	中エリアコード	中エリアコードで検索(完全一致)します。（5個まで指定可、6個以上指定すると6個目以降無視します）*2		Y005
keyword	小エリア名	小エリア名で検索(部分一致)します。UTF8(URLエンコード)で指定		銀座
start	検索の開始位置	検索結果の何件目から出力するかを指定します。	 	初期値:1
count	1ページあたりの取得数	検索結果の最大出力データ数を指定します。	 	初期値：なし、最小1、最大：なし（すべて取得）
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
小エリアマスタを検索

http://webservice.recruit.co.jp/hotpepper/small_area/v1/?key=[APIキー]&middle_area=Y005
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	530
results_returned	このＸＭＬに含まれる検索結果の件数	530
results_start	検索結果の開始位置	1
small_area	[複数要素]	
code	小エリアコード	X150
name	小エリア名	東口・歌舞伎町方面
middle_area		 
code	中エリアコード	Y055
name	中エリア名	新宿
large_area		 
code	大エリアコード	Z011
name	大エリア名	東京
service_area		 
code	サービスエリアコード	SA11
name	サービスエリア名	東京
large_service_area		 
code	大サービスエリアコード	SS10
name	大サービスエリア名	関東
ページトップへ
ref
refジャンルマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/genre/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
code	ジャンルコード	ジャンルコードで検索(完全一致)します。（２個まで指定可、3個以上指定すると3個目以降無視します）*2		G002
keyword	ジャンル名	ジャンル名で検索(部分一致)します。 UTF8(URLエンコード)で指定		バー
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
ジャンルマスタを検索

http://webservice.recruit.co.jp/hotpepper/genre/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	15
results_returned	このＸＭＬに含まれる検索結果の件数	15
results_start	検索結果の開始位置	1
genre	[複数要素]	
code	ジャンルコード	G002
name	ジャンル名	ダイニングバー
ページトップへ
ref
11クレジットカードマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/credit_card/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。

ページトップへ
サンプルクエリ
クレジットカードマスタを検索

http://webservice.recruit.co.jp/hotpepper/credit_card/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	47
results_returned	このＸＭＬに含まれる検索結果の件数	47
results_start	検索結果の開始位置	1
credit_card	[複数要素]	
code	クレジットカードコード	c99
name	クレジットカード名	○○カード
ページトップへ
ref
ref特集マスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/special/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
special	特集コード	特集コードで検索(完全一致)します。複数指定可能*2		LJ0028
special_category	特集カテゴリコード	特集カテゴリコードで検索(完全一致)します。複数指定可能*2		SPC0
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
特集マスタを特集カテゴリSPG6で絞り込み検索

http://webservice.recruit.co.jp/hotpepper/special/v1/?key=[APIキー]&special_category=SPG6
ページトップへ
レスポンスフィールド
フィールド	説明	例
special	特集[複数要素]	
code	特集コード	LV0069
name	特集名	家族でがっつり焼肉を食べよう♪
special_category	特集カテゴリ	
code	特集カテゴリコード	SPC0
name	特集カテゴリ名	宴会で盛り上がろう！
ページトップへ
ref
ref特集カテゴリマスタAPI
リクエストURL
http://webservice.recruit.co.jp/hotpepper/special_category/v1/
ページトップへ
検索クエリ
パラメータ	項目名	説明	必須	値
key	APIキー	APIを利用するために割り当てられたキーを設定します。	○	
special_category	特集カテゴリコード	特集カテゴリコードで検索(完全一致)します。複数指定可能*2		X005
format	レスポンス形式	レスポンスをXMLかJSONかを指定します。	 	初期値:xml。xml または json。
*2 複数指定可能パラメータの指定方法
name=value1&name=value2&...または name=value1,value2,...

ページトップへ
サンプルクエリ
特集カテゴリマスタを検索

http://webservice.recruit.co.jp/hotpepper/special_category/v1/?key=[APIキー]
ページトップへ
レスポンスフィールド
フィールド	説明	例
results	 	 
api_version	APIのバージョン	1.20
results_available	クエリー条件にマッチする、検索結果の全件数	5
results_returned	このＸＭＬに含まれる検索結果の件数	5
results_start	検索結果の開始位置	1
special_category	[複数要素]	
code	特集カテゴリコード	SPX0
name	特集カテゴリ名	特典・サービスで選ぶ
ページトップへ
ref
12エラー時のレスポンス
<?xml version="1.0" encoding="UTF-8"?>
<results xmlns="http://webservice.recruit.co.jp/hotpepper/">
  <api_version>1.00</api_version>
  <error>
    <message>keyは必須パラメーターです</message>
    <code>3000</code>
  </error>
</results>
エラーの際でも、HTTPレスポンスステータスは常に "200 OK" が返ります。実装側では常にレスポンスXMLの内容を見てエラー判断を行ってください。

codeが取りうる値は、以下のとおりです。

1000：サーバ障害エラー
2000：APIキーまたはIPアドレスの認証エラー
3000：パラメータ不正エラー
ページトップへ
コピーライトお問い合わせ利用規約プライバシーポリシー(2021年4月改定)
# ascomments-dl
ASOBISTAGEの配信ライブのアーカイブコメントをダウンロードするツールとそれをニコニココメントxml形式に変換するツールです。  
ASOBISTAGE Comments Downloader and Converter (to niconico xml)  
  
このプログラムはpython3によって作成されています。websocketsモジュールが必要です。  
This program is written by python3. You need the websockets module.  

## ascomments-dl
ASOBISTAGEの配信ライブのアーカイブコメントをダウンロードし、そのままの形式でjsonに保存するツールです。  
イベント名_dayx_comments.json"の形式で保存されます。上書き確認あり。  
  
It is a tool that downloads the archive comments of ASOBISTAGE live broadcasts and saves them in json as they are.  
It will be saved in the event name_dayx_comments.json format. Overwrite confirmation.  

### 使用方法 Usage
```
ascomments-dl [ASOBISTAGE LIVE Archive Page URL]
```
例 for example
```
ascomments-dl https://asobistage.asobistore.jp/event/cinderella_cg_kagayaki_yomatsuri/archive/day1
```

## asobi2nico
ダウンロードしたASOBISTAGEコメントファイルをニコニココメントxml形式に変換するツールです。(現在エラー処理未実装)  
入力ファイル名.xmlの形式で保存されます。コメントファイルをドラッグアンドドロップすることでも実行可能です。すでにファイルが存在する場合エラーになります。  
  
This is a tool to convert the downloaded ASOBISTAGE comment file into niconico comment xml format. (currently error handling not implemented)  
It is saved in the input file name.xml format. It can also be executed by dragging and dropping the comment file.An error will occur if the file already exists.  

### 使用方法 Usage
```
asobi2nico [path to ASOBISTAGE comment file]
```
例 for example
```
ascomments-dl "cinderella_cg_kagayaki_yomatsuri_day1_comments.json"
```

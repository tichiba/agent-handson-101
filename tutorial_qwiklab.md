# はじめての AI エージェントハンズオン

## ハンズオンの概要

あなたは、とある企業の開発者です。最近話題の AI エージェントを開発して、社内の業務を自動化したいと考えています。しかし、何から始めれば良いかわかりません。

そこで、あなたは Google Cloud の Agentspace と Agent Development Kit (ADK) を使って、簡単な AI エージェントを開発してみることにしました。

### このラボの内容
*   Agentspace の初期設定を行う
*   Agent Designer でノーコードでエージェントを作成する (現在準備中)
*   ADK を使って AI エージェントを作成し、作成したエージェントと対話する

## ハンズオンの開始
<walkthrough-tutorial-duration duration=5></walkthrough-tutorial-duration>
まずはハンズオンに利用するファイルをダウンロードします。
<walkthrough-info-message>既に実施済の方はこの手順をスキップできます。</walkthrough-info-message>

1. Cloud Shell 
<walkthrough-cloud-shell-icon></walkthrough-cloud-shell-icon> を開きます。

2. 次のコマンドを実行してハンズオン資材をダウンロードし、チュートリアルを開きます。
```bash
git clone https://github.com/tichiba/agent-handson-101.git
cd ~/agent-handson-101/
teachme tutorial_qwiklab.md
```

<!-- ## Google Cloud プロジェクトの設定
次に、ターミナルの環境変数にプロジェクトIDを設定します。
```bash
export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
```
<walkthrough-info-message>**Tips:** コードボックスの横にあるボタンをクリックすることで、クリップボードへのコピーおよび Cloud Shell へのコピーが簡単に行えます。</walkthrough-info-message> -->

次に、このハンズオンで利用するAPIを有効化します。

<walkthrough-enable-apis apis=
  "discoveryengine.googleapis.com,aiplatform.googleapis.com">
</walkthrough-enable-apis>

最後に、このハンズオンで利用する Google ADK をインストールします。
```bash
pip install google-adk
```

## **[シナリオ1] Agentspace の初期設定**

<walkthrough-tutorial-duration duration=15></walkthrough-tutorial-duration>

まずは、AI エージェントを開発・実行するための基盤となる Agentspace 環境をセットアップします。

### IDプロバイダの設定

1.  ナビゲーションメニュー <walkthrough-nav-menu-icon></walkthrough-nav-menu-icon> から **[AI Applications]** に移動します。
<walkthrough-menu-navigation sectionid="VERTEX_AI_SEARCH_AND_CONVERSATION"></walkthrough-menu-navigation>
<walkthrough-info-message>コンソール上部の検索バーで「AI Applications」を検索することもできます。</walkthrough-info-message>

2.  初めて利用する場合は、「**CONTINUE AND ACTIVATE THE API**」をクリックしてAPIを有効化します。

3.  左のナビゲーションペインから「**設定**」を選択します。

4.  `global` ロケーションの行にある>**鉛筆アイコン（編集ボタン）**をクリックします。

5.  IDプロバイダとして「**Google Identity**」を選択します。

6.  「**SAVE**」をクリックします。

### Google Cloud Storage データストアの作成

1.  左のナビゲーションペインで「**データストア**」を選択します。

2.  「**データストアの作成**」を選択します。

3.  「**Cloud Storage**」カードを見つけて「**SELECT**」をクリックします。

4.  Cloud Shell で以下のコマンドを実行し、プロジェクトIDと同じ名前のGCSバケットを作成します。
```bash
export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
gsutil mb gs://$PROJECT_ID
```

5.  **バケット名またはフォルダパス** に、先ほど作成したバケット名（`gs://<walkthrough-project-id/>`）を入力し、「**続行**」をクリックします。

6.  データストアに `GCS Data Store` という名前を付けます。

7.  「**作成**」を選択します。作成したデータストアが一覧に表示されます。
### Agentspace アプリのデプロイ

1.  左のナビゲーションペインで「**アプリ**」を選択します。

2.  「**+ アプリを作成する**」を選択します。

3.  「**Agentspace**」カードを見つけて「**作成**」を選択します。

4.  アプリに `My Agentspace` という名前を付け、「**作成**」を選択します。

5. 左のナビゲーションペインで「**接続されたデータストア**」を選択します。

6. 「**既存のデータストアを追加**」を選択します。

7.  接続するデータストアとして、先ほど作成した「**GCS Data Store**」データストアのチェックボックスを選択します。

8.  「**接続**」を選択します。

これでエージェントを開発する準備が整いました。

## **[シナリオ2] ADK を使ったエージェントの実行とカスタマイズ**

<walkthrough-tutorial-duration duration=20></walkthrough-tutorial-duration>

次に、Agent Development Kit (ADK) を使って、サンプルエージェントをローカルで実行し、プロンプトを書き換えて応答の変化を体験します。

### .env ファイルの作成

1. まず、Cloud Shell エディタ <walkthrough-cloud-shell-editor-icon></walkthrough-cloud-shell-editor-icon> を開きます。

1.  サンプルエージェントのディレクトリ `dawasa-agent` に移動して、`agent.py` ファイルを開きます。

2.  このファイルには、エージェントの名前、説明、およびエージェントに与えられたインストラクションが記載されています。

3. 次に、`env.example` ファイルを開きます。このファイルには、エージェントが使用する API キーなどの設定を記述します。

4. `GOOGLE_CLOUD_PROJECT` に Google Cloud プロジェクト ID `<walkthrough-project-id/>` を設定してください。

5. `env.example` ファイルを `.env` という名前に変更します。

### エージェントのローカル実行と対話

1. ターミナルを開く を選択して、Cloud Shell を開きます。

1.  `adk web` コマンドを実行して、エージェントをローカルで起動します。
```bash
adk web
```
このコマンドは、エージェントと対話するためのWebサーバーを起動します。

2.  コマンドの出力に表示されるURLを開くには、Webプレビュー<walkthrough-web-preview-icon></walkthrough-web-preview-icon> をクリックします。

3. 「**ポートを変更**」を選択し、コマンドの出力に表示されたURLのポート番号を入力してください。

3.  Web UIが開いたら、利用可能なエージェントの一覧から `dawasa-agent` を選択します。

4.  テキストボックスに「日本の首都は？」と入力して、Enterキーを押してみましょう。エージェントから「東京です。」のような応答が返ってくることを確認してください。

### プロンプトのカスタマイズ

次に応答メッセージをカスタマイズしてみましょう。

1.  Cloud Shellで `Ctrl+C` を押して、Webサーバーを停止します。

2.  Cloud Shell エディタ <walkthrough-cloud-shell-editor-icon></walkthrough-cloud-shell-editor-icon> を開き、 `dawasa-agent/agent.py` ファイルを開きます。

3.  ファイル内の `prompt` の内容を変更してください。例えば、武士のキャラクターになりきって「ござる」と応答するように変更します。

4.  ファイルを保存し、再度 `adk web` コマンドを実行してエージェントを起動します。
```bash
adk web
```

5.  Web UIをブラウザでリロードし、もう一度「日本の首都は？」と入力します。エージェントの応答が「東京でござる。」のように変化したことを確認してください。

## **[シナリオ3] 製品・サービス仕様QAエージェントの作成**

<walkthrough-tutorial-duration duration=20></walkthrough-tutorial-duration>

今度は、シナリオ1で作成した Google Cloud Storage のデータストアをRAG (Retrieval Augmented Generation) として利用する `rag-agent` を動かしてみましょう。このエージェントは、Google Cloud Storage 内の**製品仕様書**を検索し、その内容に基づいて質問に回答します。

### GCSへのファイル準備

まず、RAGの検索対象となるサンプルファイルをGCSバケットにアップロードします。

1.  Cloud Shellで、前のシナリオで使用したWebサーバーを `Ctrl+C` で停止します。

2.  Cloud Shellで以下のコマンドを実行し、サンプルファイルをシナリオ1で作成したGCSバケットにアップロードします。
```bash
gsutil cp agent-handson-101/rag-agent/files/product_spec_model_x.txt gs://<walkthrough-project-id/>/
```
<walkthrough-info-message>GCSバケットにファイルがアップロードされると、データストアが自動的にファイルをインデックスに登録します。これには数分かかる場合があります。</walkthrough-info-message>

### エージェントの設定と対話

次に、エージェントが接続するデータストアのIDを設定し、エージェントと対話します。

1.  ナビゲーションメニュー <walkthrough-nav-menu-icon></walkthrough-nav-menu-icon> から **[AI Applications]** > **[データストア]** に移動します。

2.  シナリオ1で作成した `GCS Data Store` データストアをクリックします。

3.  データストアの詳細ページで、**データストアの ID** をコピーします。

4.  Cloud Shellエディタ <walkthrough-cloud-shell-editor-icon></walkthrough-cloud-shell-editor-icon> で `rag-agent/agent.py` ファイルを開き、`your-datastore-id` の値を、先ほどコピーしたご自身のデータストアIDに書き換えます。

5. 次に、`your-gcp-project-id` の値を、ご自身の Google Cloud プロジェクト ID `<walkthrough-project-id/>` に書き換えます。

6.  `adk web` コマンドを実行して、エージェントをローカルで起動します。
    ```bash
    adk web
    ```

7.  Webプレビュー機能を使って、表示されたURLを開き、`rag-agent` を選択します。

8.  テキストボックスに、アップロードしたファイルの内容に関する質問を入力してみましょう。例えば、「製品Model-Xのバッテリー駆動時間は？」と入力してEnterキーを押します。

9.  エージェントがGoogle Cloud Storageの製品仕様書を検索し、ファイルの内容に基づいた回答をすることを確認してください。


## Congratulations!
<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

おめでとうございます！ハンズオンはこれで完了です。ご参加ありがとうございました。

ADK を使って、AI エージェントの開発、デプロイ、実行までの一連の流れを体験することができました。
# はじめての AI アプリケーションハンズオン

## ハンズオンの概要

あなたは、とある企業の開発者です。社内のGoogle Driveにあるドキュメントを、自然言語で検索・要約できるAIアプリケーションを構築したいと考えています。

そこで、あなたは Google Cloud の **Vertex AI Search and Conversation** を使って、コーディングなしで簡単に対話型AIアプリケーションを開発してみることにしました。

### このラボの内容
*   Vertex AI Search and Conversation の初期設定を行う
*   Google Drive をデータストアとして接続する
*   対話型のAIアプリケーションを作成する
*   （次のシナリオ）作成したAIアプリケーションをテストする

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

## Google Cloud プロジェクトの設定
次に、ターミナルの環境変数にプロジェクトIDを設定します。
```bash
export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
```
<walkthrough-info-message>**Tips:** コードボックスの横にあるボタンをクリックすることで、クリップボードへのコピーおよび Cloud Shell へのコピーが簡単に行えます。</walkthrough-info-message>

次に、このハンズオンで利用するAPIを有効化します。
<walkthrough-enable-apis apis=
  "discoveryengine.googleapis.com,drive.googleapis.com">
</walkthrough-enable-apis>

## **[シナリオ1] Vertex AI Search and Conversation の設定**

<walkthrough-tutorial-duration duration=15></walkthrough-tutorial-duration>

まずは、AI アプリケーションを開発・実行するための基盤となる **Vertex AI Search and Conversation** 環境をセットアップします。

### IDプロバイダの設定

1.  ナビゲーションメニュー <walkthrough-nav-menu-icon></walkthrough-nav-menu-icon> から [**Vertex AI Search and Conversation**] に移動します。コンソール上では「AI Applications」と表示されている場合があります。
<walkthrough-menu-navigation sectionid="VERTEX_AI_SEARCH_AND_CONVERSATION"></walkthrough-menu-navigation>

2.  初めて利用する場合は、「**CONTINUE AND ACTIVATE THE API**」をクリックしてAPIを有効化します。

3.  左のナビゲーションペインから「**Settings**」を選択します。

4.  `global` ロケーションの行にある<walkthrough-spotlight-pointer cssselector="[aria-label='Edit Identity provider']" single="true">**鉛筆アイコン（編集ボタン）**</walkthrough-spotlight-pointer>をクリックします。

5.  IDプロバイダとして「**Google Identity**」を選択します。

6.  「**SAVE**」をクリックします。

### Google Drive データストアの作成

1.  左のナビゲーションペインで「**Data Stores**」を選択します。

2.  「**+ NEW DATA STORE**」を選択します。

3.  「**Google Drive**」カードを見つけて「**SELECT**」をクリックします。

4.  「**All drives**」が選択されたままで、「**CONTINUE**」をクリックします。

5.  データストアに `Google Drive` という名前を付けます。

6.  「**CREATE**」を選択します。作成したデータストアが一覧に表示されます。

### アプリの作成

1.  左のナビゲーションペインで「**Apps**」を選択します。

2.  「**+ NEW APP**」を選択します。

3.  「**Search**」カードを見つけて「**CREATE**」を選択します。

4.  アプリに `Cymbal Shops Agentspace` という名前を付けます。

5.  会社名として `Cymbal Shops` を使用します。

6.  「**CONTINUE**」を選択します。

7.  接続するデータストアとして、先ほど作成した「**Google Drive**」データストアのチェックボックスを選択します。

8.  「**CREATE**」を選択します。

これで、Google Drive内のドキュメントを検索・要約する準備が整いました。

## **[シナリオ2] 作成したアプリとの対話**

<walkthrough-tutorial-duration duration=20></walkthrough-tutorial-duration>

シナリオ1で作成したAIアプリケーションをテストし、実際にGoogle Drive内のドキュメントについて質問してみましょう。
（このセクションは後続のステップで作成します）

## Congratulations!
<walkthrough-conclusion-trophy></walkthrough-conclusion-trophy>

おめでとうございます！ハンズオンはこれで完了です。ご参加ありがとうございました。

Vertex AI Search and Conversation を使って、AI アプリケーションの基盤を構築することができました。
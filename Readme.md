# AI エージェント開発ハンズオン (agent-handson-101)

## 概要

このリポジトリは、Google Cloud の Agentspace と Agent Development Kit (ADK) を用いた AI エージェント開発のハンズオンです。
簡単なエージェントの作成から、RAG (Retrieval Augmented Generation) を利用したエージェントまで、一連の開発フローを体験することができます。

## ハンズオンの内容

このハンズオンは、以下の3つのシナリオで構成されています。

-   **シナリオ1: Agentspace の初期設定**
    -   AI エージェントを開発・実行するための基盤となる Agentspace 環境をセットアップします。

-   **シナリオ2: ADK を使ったエージェントの実行とカスタマイズ**
    -   サンプルエージェント (`dawasa-agent`) をローカルで実行し、プロンプトを書き換えて応答の変化を体験します。

-   **シナリオ3: 製品・サービス仕様QAエージェントの作成**
    -   Google Cloud Storage のドキュメントをRAGとして利用する `rag-agent` を動かし、製品仕様に関する質問応答を体験します。

## 始め方

ハンズオンの詳しい手順は、[tutorial_qwiklab.md](./tutorial_qwiklab.md) を参照してください。

Cloud Shell を利用してチュートリアルを開始するには、以下の手順を実行します。

1.  **Google Cloud Console を開き、Cloud Shell をアクティブにします。**
    [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com)

2.  **リポジトリをクローンし、ディレクトリに移動します。**
    ```bash
    git clone https://github.com/tichiba/agent-handson-101.git
    cd agent-handson-101
    ```

3.  **次のコマンドでチュートリアルを開始します。**
    ```bash
    teachme tutorial_qwiklab.md
    ```

## ディレクトリ構成

```
.
├── dawasa-agent/      # シナリオ2で利用するシンプルなエージェント
│   ├── agent.py
│   └── ...
├── rag-agent/         # シナリオ3で利用するRAGエージェント
│   ├── agent.py
│   └── ...
├── files/             # RAGで利用するサンプルドキュメント
│   └── product_spec_model_x.txt
└── tutorial_qwiklab.md # ハンズオンのチュートリアル
```

import vertexai
from google.adk.agents import LlmAgent
from google.adk.tools import VertexAiSearchTool

MODEL = 'gemini-2.5-flash'

vertex_search_tool = VertexAiSearchTool(
    data_store_id='projects/{project_id}/locations/{location}/collections/default_collection/dataStores/{data_store_id}'.format(
        # TODO: ご自身のプロジェクトIDとデータストアIDに書き換えてください
        project_id='your-gcp-project-id',
        location='global',
        data_store_id='your-datastore-id'
    )
)

root_agent = LlmAgent(
    model=MODEL,
    name="product_spec_qa_agent",
    description="製品仕様書を検索し、技術的な質問に回答するエージェントです。",
    instruction="""あなたは製品仕様に詳しいテクニカルサポート担当者です。
Vertex AI Search ツールを使って、Cloud Storageに保存されている製品仕様書を検索し、ユーザーからの技術的な質問に答えます。

ユーザーからの質問に対して、関連する仕様を正確に引用して回答してください。
仕様書に記載がない情報については、無理に回答せず、「仕様書には該当する記載がありませんでした。」と正直に伝えてください。
""",
    tools=[vertex_search_tool]
)

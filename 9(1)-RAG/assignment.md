[9회차] RAG 과제

발제자: 윤희찬

기간
마감: 2월 9일 23시 59분
지각 제출: 2월 10일 23시 59분

intro
이번 과제는 개인 과제입니다.

본 과제의 목적은 와빅이라면 누구나 갖춰야할 기본 소양, 에이전트의 시작이자 기본인 RAG
를 직접 다양한 형태로 구현하는 것에 있습니다.
이번 과제의 개요는 다음과 같습니다.

1. 인덱싱을 위한 pinecone / elastic cloud / algolia 를 구축합니다. (벡터 / 하이브리드
   검색 / 텍스트)
2. 미리 열어둔 DB들에 필요한 인덱스 (임베딩 등) 를 생성하고 적재합니다.
3. RAG 파이프라인 코드를 작성하여, 실제 가동하며 각 검색 수단 별 결과를 비교합니다.
   위 과제 수행을 위한 스켈레톤 코드는 다음 저장소에 있습니다.

https://github.com/quant-jason/Rag-session

https://github.com/quant-jason/Rag-session
본 저장소를 fork 하거나 다운받아 본인 개인 과제에 9(1)-RAG 폴더를 생성하여 여기에 코
드를 넣은 후 작업하시면 됩니다. (다만, 깃 관리를 위해 gitignore 등에 주의해주세요.)
명세
폴더 구조

[9회차] RAG 과제 1

Rag-session/
├── app/
│ ├── streamlit_app.py # Streamlit UI (수정 불필요)
│ └── llm.py # [TODO] Solar LLM 답변 생성
│
├── data/
│ ├── download.py # HuggingFace 데이터 다운로드 (완성됨)
│ ├── raw/ # corpus.jsonl, qa.jsonl (다운로드 후 생성)
│ └── processed/ # embeddings.npy, embedding_ids.json (임베딩 후
생성)
│
├── ingest/
│ ├── embedding.py # [TODO] 임베딩 계산 (embed_passages,
embed_query)
│ ├── elastic/
│ │ └── ingest.py # [TODO] Elasticsearch BM25 인덱스 적재
│ ├── pinecone/
│ │ └── ingest.py # [TODO] Pinecone 벡터 적재
│ └── hybrid/
│ └── ingest.py # [TODO] Elasticsearch Hybrid 인덱스 적재
│
├── retrievers/
│ ├── elastic/
│ │ └── retriever.py # [TODO] BM25 검색
│ ├── pinecone/
│ │ └── retriever.py # [TODO] Vector 검색
│ └── hybrid/
│ └── retriever.py # [TODO] Hybrid (RRF) 검색
│
├── .env # API 키 설정 (gitignore 대상)
├── .env.example # .env 템플릿
└── requirements.txt # 패키지 의존성
구현해야 할 함수 (총 9개 - 필요하다면 추가로 더 구현하거나 덜 구현해도 좋음)
Step 1. 임베딩
파일 함수 설명
ingest/embedding.py

embed_passages(texts,
ids)

텍스트 리스트를 배치로 임베딩하여 (N, 4096) numpy 배열 반환 및 저장

[9회차] RAG 과제 2

파일 함수 설명
ingest/embedding.py embed_query(query) 단일 쿼리를 임베딩하
여 list[float] 반환

Passage 모델: solar-embedding-1-large-passage
Query 모델: solar-embedding-1-large-query
벡터 차원: 4096
Step 2. DB 적재
파일 함수 설명

ingest/elastic/ingest.py ingest()

corpus.jsonl을
Elasticsearch BM25
인덱스( wiki-bm25 )에
적재

ingest/pinecone/ingest.py ingest()

임베딩 벡터를
Pinecone 인덱스에
upsert

ingest/hybrid/ingest.py ingest()

corpus + 임베딩을
Elasticsearch Hybrid
인덱스( wiki-hybrid )
에 적재

Step 3. 검색 (Retriever)
파일 함수 설명
retrievers/elastic/retriever.py search(query, top_k) BM25 텍스트 매칭 검색
retrievers/pinecone/retriever.py search(query, top_k) 벡터 코사인 유사도 검색
retrievers/hybrid/retriever.py

search(query, top_k,
candidate_size)

RRF(Reciprocal Rank
Fusion) 하이브리드 검색
반환 형식: list[dict] - 각 dict는 {"id", "text", "score", "method"} 키를 포함
Step 4. LLM 답변 생성
파일 함수 설명
app/llm.py

generate(question,
context)

Solar LLM으로 답변 생성. context가 None이면
No RAG, 있으면 RAG 프롬프트 사용

API: OpenAI 호환 ( https://api.upstage.ai/v1/solar )
temperature=0, max_tokens=1024

[9회차] RAG 과제 3

제출 방법
완성된 코드파일을 9(1)-RAG 폴더 안에 위치시키고, 아래와 같이 실행 결과를 캡처하여 인
증하시면 됩니다.

채점 기준

[9회차] RAG 과제 4

1. 코드를 올바르게 구현하여 정상적으로 작동하였는가?
2. 작동 화면을 적절히 제출하였는가?
3. 멋져요!
   (이건 제출 기준 외이니 멋져요! 를 받고 싶으신 분들만 하시면 됩니다. )
   임베딩 벡터 검색 방법 (코사인 유사도 / 내적 / L2 Norm 등) 을 다양하게 바꿔가며 결
   과가 어떻게 바뀌는지 작성하여 Report.md로 폴더 내에 제출. 또한 Report 내에 키워드 검
   색과 벡터 검색의 장단점을 간단히 적어 제출.

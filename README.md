# music-agent

基于 LLM 的音乐问答 Agent（学习项目）

## 这是什么

用户用自然语言提问，Agent 自主调用工具查询音乐库后回答。

## 当前进度

- [x] 项目骨架（uv + FastAPI 分层结构）
- [x] 模型流式调用验证
- [ ] 数据接入（MySQL 只读查询）
- [ ] 工具层与 Agent 循环
- [ ] 服务化与 SSE 流式接口
- [ ] RAG 语义检索

## 技术栈

Python 3.12 · uv · OpenAI 兼容协议 · （待补充：FastAPI / MySQL / ChromaDB）

## 怎么跑

    uv sync
    cp .env.example .env   # 填入你的 API Key
    uv run python scripts/hello_llm.py

## 说明

模型接入使用 OpenAI 兼容协议，可替换为任意兼容服务商。

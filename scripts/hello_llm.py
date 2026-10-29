import os
import asyncio

from openai import AsyncOpenAI
from dotenv import load_dotenv
from openai.types.chat import ChatCompletionMessageParam

load_dotenv()

def read_env() -> tuple[str, str, str]:
    print(">>> 进了 read_env")
    base_url = os.getenv("LLM_BASE_URL")
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")

    if base_url is None:
        raise RuntimeError("base_url 是空的")
    if api_key is None:
        raise RuntimeError("api_key 是空的")
    if model is None:
        raise RuntimeError("model 是空的")
    return base_url, api_key, model

async def main():
    print(">>> 进了 main")
    base_url, api_key, model = read_env()

    # 创建客户端
    client = AsyncOpenAI(base_url=base_url, api_key=api_key)

    # 消息
    messages: list[ChatCompletionMessageParam] = [
        {"role": "user", "content": "用一句话介绍自己"}
    ]
    # 发起请求
    stream = await client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            print(delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
import json

from dotenv import load_dotenv
from mem0 import Memory

load_dotenv()

config = {
    "version": "v.1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "provider": "openai",
            "api_key": "",
            "model": "text-embedding-3-small",
        },
    },
    "llm": {"provider": "openai", "config": {"api_key": "", "model": "gpt-4.1"}},
    "vector_store": {
        "provider": "qdrant",
        "config": {"host": "localhost", "port": 6333},
    },
}

mem_client = Memory.from_config(config)

while True:
    user_query = input("> ")

    search_memory = mem_client.search(query=user_query)

    memories = [
        f"ID: {mem.get('id')}\nMemory: {mem.get('memory')}"
        for mem in search_memory.get("results")
    ]

    SYSTEM_PROMPT = f"""
    Here is the context about the user:
    _{json.dumps(search_memory)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": user_query}]
    )

    ai_response = response.choices[0].message.content

    print("AI: ", ai_response)

    mem_client.add(
        user_id="thakurrohan",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query},
            {"role": "ai", "content": ai_response},
        ],
    )

    print("Memory has been added!")


def main():
    print("Hello from mem-agent!")


if __name__ == "__main__":
    main()

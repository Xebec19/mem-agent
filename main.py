from mem0 import Memory

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


def main():
    print("Hello from mem-agent!")


if __name__ == "__main__":
    main()

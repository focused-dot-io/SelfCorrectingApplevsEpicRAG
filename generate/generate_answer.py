from generate.chat import ask_chat


async def generate_answer(state: dict) -> dict:
    docs = state["documents"]
    question = state["question"]

    answer = await ask_chat(docs, question)

    return {
        **state,
        "answer": answer
    }

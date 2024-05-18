from query_transformer.question_rewriter import question_rewriter


def query_transformer(state: dict) -> dict:
    question = state["question"]
    rephrased_question = question_rewriter(question)
    print(rephrased_question)
    return {
        **state,
        "question": rephrased_question
    }

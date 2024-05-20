from query_transformers.question_for_internet.question_rewriter import internet_question_rewriter


def internet_question_transformer(state: dict) -> dict:
    question = state["question"]
    rephrased_question = internet_question_rewriter(question)
    print(f"Rephrasing the question for the internet: {rephrased_question}\n")
    return {
        **state,
        "question": rephrased_question
    }

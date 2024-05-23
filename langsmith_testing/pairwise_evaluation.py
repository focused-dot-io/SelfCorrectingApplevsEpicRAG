from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langsmith.evaluation import evaluate_comparative
from langsmith.schemas import Run, Example

load_dotenv()

chat_35_set = "Test-b0cd9d38"
chat_4o_set = "Test-c2481751"
prompt = hub.pull("langchain-ai/pairwise-evaluation-2")


def evaluate_pairwise(runs: list[Run], example: Example):
    scores = {}

    # Create the model to run your evaluator
    model = ChatOpenAI(model_name="gpt-4")

    runnable = prompt | model
    response = runnable.invoke({
        "question": example.inputs["question"],
        "answer_a": runs[0].outputs["answer"] if runs[0].outputs is not None else "N/A",
        "answer_b": runs[1].outputs["answer"] if runs[1].outputs is not None else "N/A",
    })
    score = response["Preference"]
    if score == 1:
        scores[runs[0].id] = 1
        scores[runs[1].id] = 0
    elif score == 2:
        scores[runs[0].id] = 0
        scores[runs[1].id] = 1
    else:
        scores[runs[0].id] = 0
        scores[runs[1].id] = 0
    return {"key": "ranked_preference", "scores": scores}


evaluate_comparative(
    # Replace the following array with the names or IDs of your experiments
    [chat_35_set, chat_4o_set],
    evaluators=[evaluate_pairwise],
)

import asyncio

from dotenv import load_dotenv
from langsmith import evaluate
from langsmith.evaluation import LangChainStringEvaluator
from generate.generate_answer import generate_answer

load_dotenv()


def predict(inputs: dict) -> dict:
    loop = asyncio.new_event_loop()
    result = loop.run_until_complete(generate_answer(inputs))
    loop.close()
    return result


def prepare_data(run, example):
    if run.outputs is not None:
        return {
            "prediction": run.outputs['answer'],
            "reference": example.outputs['answer'],
            "input": example.inputs['question'],
        }
    else:
        return {
            "prediction": "",
            "reference": "",
            "input": "",
        }


data_set = "ds-sweaty-trailer-72"
qa_evaluator = LangChainStringEvaluator("cot_qa", prepare_data=prepare_data)

correctness_evaluator = LangChainStringEvaluator(
    "labeled_score_string",
    config={
        "criteria": "How accurate is this prediction compared to the reference on a scale of 1-10?",
        "normalize_by": 10
    },
    prepare_data=prepare_data,
)

test_results = evaluate(
    predict,
    data=data_set,
    evaluators=[qa_evaluator, correctness_evaluator],
    experiment_prefix="Test",
    max_concurrency=1
)

print(test_results)

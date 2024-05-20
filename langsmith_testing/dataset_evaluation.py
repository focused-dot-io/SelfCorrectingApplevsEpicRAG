import asyncio
from typing import Sequence
from langsmith import evaluate
from langsmith.evaluation import LangChainStringEvaluator
from langsmith.schemas import Example, Run

from app.run_workflow import apple_v_epic_workflow

data_set = "ds-impressionable-sheet-48"
qa_evaluator = LangChainStringEvaluator("cot_qa")


def predict(inputs: dict) -> dict:
    loop = asyncio.new_event_loop()
    result = loop.run_until_complete(apple_v_epic_workflow(inputs['question']))
    loop.close()
    return result


def format_evaluator_inputs(run: Run, example: Example):
    return {
        "input": example.inputs["inputs"],
        "prediction": next(iter(run.outputs.values())),
        "reference": example.outputs["expected"],
    }


correctness_evaluator = LangChainStringEvaluator(
    "labeled_score_string",
    config={"criteria": "correctness", "normalize_by": 10},
    prepare_data=format_evaluator_inputs,
)


test_results = evaluate(
    predict,
    data=data_set,
    evaluators=Sequence[correctness_evaluator],
    experiment_prefix="Test",
    max_concurrency=3
)

print(test_results)


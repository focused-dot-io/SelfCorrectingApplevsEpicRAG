

def decide_to_generate(state: dict) -> str:
    num_original_docs = state["num_original_docs"]
    filtered_docs = state["documents"]

    print(f'percent of relevant docs {len(filtered_docs) / num_original_docs}')

    if len(filtered_docs)/num_original_docs >= .5:
        return "generate"
    else:
        return "transform_query"

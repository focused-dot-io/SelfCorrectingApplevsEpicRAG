import asyncio

from graph.build_graph import app_workflow, graph_nodes


async def apple_v_epic_workflow(question_asked: str) -> dict:
    node = ""
    answer = ""
    async for event in app_workflow.astream_events({"question": question_asked}, version="v1"):
        kind = event["event"]
        step_name = event["name"]
        node = step_name if step_name in graph_nodes else node

        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content and node == "generate_answer":
                print(content, end="")
        elif kind == "on_chain_end" and step_name == "generate_answer":
            answer = event["data"]["output"]
            sources = event["data"]["output"]["sources"]
            print("\n\nSOURCES:")
            for source in sources:
                print(source.metadata["source"])

    return answer


def main(question_asked: str):
    loop = asyncio.new_event_loop()
    loop.run_until_complete(apple_v_epic_workflow(question_asked))
    loop.close()


if __name__ == "__main__":
    print("\t**********************************************")
    print("\t***            Apple v Epic Q&A            ***")
    print("\t**********************************************")
    print("\nAsk a question regarding the Apple vs. Epic lawsuit:")
    question = input()

    while question.lower() != "q":
        main(question)
        print("\nDo you want to ask another question? Enter q to quit.")
        question = input()

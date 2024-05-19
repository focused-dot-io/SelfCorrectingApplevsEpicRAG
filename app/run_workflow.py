import asyncio
from graph.build_graph import app_workflow, graph_nodes

question = {"question": "Who won the apple v epic lawsuit?"}


async def apple_v_epic_workflow(inputs: dict) -> dict:
    node = ""
    async for event in app_workflow.astream_events(inputs, version="v1"):
        kind = event["event"]
        step_name = event["name"]
        node = step_name if step_name in graph_nodes else node

        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content and node == "generate_answer":
                print(content, end="")
        elif kind == "on_chain_end" and step_name == "generate_answer":
            sources = event["data"]["output"]["sources"]
            print("\n\nSOURCES:")
            for source in sources:
                print(source.metadata["source"])


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(apple_v_epic_workflow(question))
    loop.close()


main()

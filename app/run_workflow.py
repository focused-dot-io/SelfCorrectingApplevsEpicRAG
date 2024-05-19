import asyncio
from graph.build_graph import app_workflow


question = {"question": "Whats is the apple v epic lawsuit about?"}


async def apple_v_epic_workflow(inputs: dict) -> dict:
    async for event in app_workflow.astream_events(inputs, version="v1"):
        kind = event["event"]
        print(event)
        if kind == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                print(content, end="")


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(apple_v_epic_workflow(question))
    loop.close()


main()

from pprint import pprint
from graph.build_graph import app_workflow


inputs = {"question": "Whats apple doing?"}
for output in app_workflow.stream(inputs):
    for key, value in output.items():
        # Node
        pprint(f"Node '{key}':")
        # Optional: print full state at each node
        pprint(value, indent=2, width=80, depth=None)

# Final generation
# pprint(value["generation"])

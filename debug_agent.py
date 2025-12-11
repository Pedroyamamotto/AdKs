import sys
import os

# Add the workspace to sys.path so we can import my_agent
sys.path.append(os.getcwd())

try:
    from my_agent.agent import root_agent
    print("Successfully imported root_agent")
    print(f"Tools: {root_agent.tools}")
    for i, tool in enumerate(root_agent.tools):
        print(f"Tool {i}: {tool} (Type: {type(tool)})")
except Exception as e:
    print(f"Error importing agent: {e}")
    import traceback
    traceback.print_exc()

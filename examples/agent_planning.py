from agents import load_tool, CodeAgent, JsonAgent, HfApiEngine
from agents.default_tools import PythonInterpreterTool

from dotenv import load_dotenv

load_dotenv()

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", cache=False)

from agents.search import DuckDuckGoSearchTool

search_tool = DuckDuckGoSearchTool()

llm_engine = HfApiEngine("Qwen/Qwen2.5-72B-Instruct")

agent = CodeAgent(tools=[search_tool], llm_engine=llm_engine, planning_interval=3)

# Run it!
print("Let's run the Code agent:")

result = agent.run(
    "How long would a cheetah at full speed take to run the length of Pont Alexandre III?",
)

print("RESULT:", result)


code_tool = PythonInterpreterTool()

agent = JsonAgent(tools=[search_tool, code_tool], llm_engine=llm_engine, planning_interval=3)

print("====================")
print("====================")
print("Now let's run the JSON agent:")
result = agent.run(
    "How long would a cheetah at full speed take to run the length of Pont Alexandre III?",
)

print("RESULT:", result)

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from smolagents import ToolCallingAgent, LiteLLMModel
from smolagents import TaskStep, ActionStep
from smolagents.mcp_client import MCPClient
import openai

#Load key from env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set.")
openai.api_key = OPENAI_API_KEY

#Connet to CG MCP
print("🔌 Connecting to CoinGecko MCP...")
client = MCPClient({
    "url": "https://mcp.api.coingecko.com/sse",
    "transport": "sse"
})
tools = client.get_tools()

#Initialize Agent
model = LiteLLMModel(model_id="gpt-4o-mini")
agent = ToolCallingAgent(
    tools=tools,
    model=model,
)

#Ask agent to get current price for hardcoded prediction
fetch_prices_prompt = """
Using the CoinGecko tools, please fetch the current USD prices for:
- Bitcoin (BTC)
- Solana (SOL)
- Ethereum (ETH)

Return them in this format:
{"btc": BTC_PRICE, "sol": SOL_PRICE, "eth": ETH_PRICE}
"""

agent.memory.steps.append(TaskStep(task=fetch_prices_prompt, task_images=[]))
step_number = len(agent.memory.steps)

while True:
    step = ActionStep(step_number=step_number, observations_images=[], timing={})
    result = agent.step(step)
    agent.memory.steps.append(step)
    step_number += 1
    if result.output:
        break

#Parse
try:
    prices = result.output if isinstance(result.output, dict) else json.loads(result.output)
    btc_price = float(prices["btc"])
    sol_price = float(prices["sol"])
    eth_price = float(prices["eth"])
except Exception as e:
    raise RuntimeError(f"Failed to parse price data: {e}")

#Compute target price
btc_target = round(btc_price * 1.03, 2)
sol_target = round(sol_price * 1.05, 2)
eth_target = round(eth_price * 1.03, 2)


#Using prompt to generate the prediction (3 with random, 3 with hardcoded)
final_prompt = f"""
You are a crypto analyst assistant. 
Use CoinGecko data and tools to generate three speculative prediction questions: one based on 24h trends, one on 7d trends, and one on 30d trends.
Use real coin names, prices, and recent data. Be concise. Do not explain anything and return the 3 questions.
Generate another 3 questions. Please follow exactly this structure:

1. Do you think BTC will make more than ${btc_target} this week?
2. Will Solana (SOL) reclaim ${sol_target} this month?
3. Will Ethereum (ETH) recover to ${eth_target} this week?

"""

agent.memory.steps.append(TaskStep(task=final_prompt, task_images=[]))

final_answer = None
while final_answer is None or final_answer.output is None:
    step = ActionStep(step_number=step_number, observations_images=[], timing={})
    final_answer = agent.step(step)
    agent.memory.steps.append(step)
    step_number += 1

#Output
print("\nFinal Prediction Questions:\n")
print(final_answer.output)
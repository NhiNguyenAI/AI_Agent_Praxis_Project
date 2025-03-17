"""
************************************************************************
 *
 * financeAiAgentTest.py: This is a test file to test finance AI agent
 *
 * Initial Creation:
 *    Author      Nhi Nguyen
 *    Created on  2025-18-03
 *
 ************************************************************************/
"""
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools

# Load environment variables from .env file
load_dotenv()

# Create an agent with the Groq model
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=["use tables to display data."],
    debug_mode=True

)

# Test the connection and get a response
agent.print_response("Write Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA.")
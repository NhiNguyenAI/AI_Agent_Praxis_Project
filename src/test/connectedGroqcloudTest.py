"""
************************************************************************
 *
 * connectedGroqCloud.py: This is a test file to test the connection between groq and cloud
 *
 * Initial Creation:
 *    Author      Nhi Nguyen
 *    Created on  2025-17-03
 *
 ************************************************************************/
"""
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an agent with the Groq model
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

# Test the connection and get a response
agent.print_response("Write a test to test the connection between Groq and cloud.")
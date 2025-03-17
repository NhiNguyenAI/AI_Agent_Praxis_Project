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
from phi.groq import Groq
from phi.test import Test
from dotenv import load_dotenv

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)
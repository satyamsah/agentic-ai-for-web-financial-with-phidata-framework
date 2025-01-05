#Building the Financial AI Agent


#Chatbot AI agent interaction to get the details of the stock

#new information from websearc

#interact with LLM model 
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()


print("phikeyVariable: ", os.getenv("PHI_API_KEY"))
print("grokkeyVariable: ", os.getenv("GROQ_API_KEY"))

#websearch agent
web_search_agent=Agent(
    name = "Satyam's Web Search Agent",
    role = " Search web for latest info",
    model = Groq(id="llama-3.2-1b-preview", api_key=os.getenv("GROQ_API_KEY")),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

#finance agent
finance_agent =  Agent(
    name="Satyam's Finance Agent Calling",
    role="Get Finanace fdata",
    model = Groq(id="llama-3.2-1b-preview", api_key=os.getenv("GROQ_API_KEY")),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_model_agent = Agent(
    team = [web_search_agent, finance_agent],
    model = Groq(id="llama-3.2-1b-preview"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_model_agent.print_response("summarize analyst recommendation for ORCL in a tabular format with buy/sell/hold", stream=True)
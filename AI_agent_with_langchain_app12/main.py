import sqlite3
import uuid
from datetime import datetime
import gradio as gr
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_ollama import ChatOllama
from langgraph.checkpoint.sqlite import SqliteSaver

load_dotenv()


@tool
def get_date() -> str:
    """Return today's date."""
    return datetime.now().strftime("%Y-%m-%d")


search_tool = TavilySearchResults()

conn = sqlite3.connect(
    "chatbot_memory.db",
    check_same_thread=False,
)

checkpoint = SqliteSaver(conn)

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
)

system_prompt = """
You are a helpful AI assistant.

Rules:
- Answer every question clearly.
- Use get_date only when the user asks for today's date.
- Use Tavily Search only for current or recent information.
"""

agent = create_agent(
    model=llm,
    tools=[get_date, search_tool],
    system_prompt=system_prompt,
    checkpointer=checkpoint,
)


def chat(message, history, thread_id):
    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ]
        },
        config=config,
    )

    last_message = response["messages"][-1]

    if hasattr(last_message, "content"):
        return last_message.content

    return str(last_message)


with gr.Blocks() as demo:
    gr.Markdown("# 🤖 AI Assistant")

    thread_id = gr.State(str(uuid.uuid4()))

    gr.ChatInterface(
        fn=chat,
        additional_inputs=[thread_id],
    )

demo.launch()
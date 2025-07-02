from mcp.server.fastmcp import FastMCP
import openai
import os

mcp = FastMCP("codelabs-assistant")

@mcp.tool()
async def answer_question(question: str) -> str:
    """Answers a question using the GPT model."""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    mcp.run(transport="stdio")

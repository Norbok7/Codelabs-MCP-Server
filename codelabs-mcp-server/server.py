import os
import asyncio
import openai
from fastmcp import FastMCP

# Initialize the FastMCP server with a descriptive name
mcp = FastMCP(name="Codelabs Learning Assistant")

# Set the OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

openai.api_key = api_key

# Define the instructional prompt
INSTRUCTION_PROMPT = """
Here’s a **streamlined** version of your original prompt, keeping all core functionality intact with drastically fewer words:

---

**Simplified Custom GPT Prompt**:

> Act as an expert–novice pair-programming partner and web dev mentor.
>
> * **Prompt Handling**: If input is vague, auto-rewrite it as a refined, context-rich prompt. Show “Refined Prompt” and “Revision Notes.”
> * **Guidance-Only Mode** (default): Don't give final answers—use Socratic hints, ask questions, scaffold thinking.
> * **Toggle**: “Give me full answers” disables guidance mode. “Back to guidance-only mode” re-enables it. Acknowledge mode changes.
> * **Learner Inference**: Detect skill level implicitly from language and errors—don’t ask directly.
> * **Answer Format**: Always respond in two parts:
>
>   1. Bullet-point summary
>   2. Deep dive with nuance
> * **Code Examples**: Include runnable Ruby on Rails snippets (model, controller, route), following official conventions.
> * **Frontend Link**: If relevant, hint how Rails ties to Angular.
> * **Learning Links**:
>
>   * CodeLabs: [codelabsdash.com](https://www.codelabsdash.com/coach/schedule)
>   * GitHub: [GitHub Classroom](https://classroom.github.com/classrooms/136737890-2025-code-labs-back-end)
> * **Sources**: Cite 3–5 links (Rails Guides, MDN, papers) per answer.
> * **Follow-Up**: Always end with a forward-looking question.
> * **Workflow**: Adopt driver/navigator pairing. Encourage testing, TDD, and self-checks.
> * **Boundaries**: Stay in web dev scope. Refuse disallowed topics but offer learning-safe alternatives.

"""

LESSON_DIR = "lessons"

def extract_relevant_lessons(question: str, max_snippets: int = 3) -> str:
    """
    Scans lesson files for content relevant to the question.
    Returns a concatenated string of relevant excerpts.
    """
    snippets = []
    question_lower = question.lower()

    for filename in os.listdir(LESSON_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(LESSON_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                    if question_lower in content.lower():
                        snippets.append(f"From {filename}:\n{content[:500]}...\n")
                        if len(snippets) >= max_snippets:
                            break
            except Exception as e:
                continue  # Skip files that can't be read

    return "\n".join(snippets)

@mcp.tool(name="answer_question", description="Answer student questions with guidance-focused responses.")
async def answer_question(question: str) -> str:
    """Processes a student's question and returns a structured, guidance-focused answer."""
    lesson_snippets = extract_relevant_lessons(question)
    prompt = INSTRUCTION_PROMPT
    if lesson_snippets:
        prompt += f"\n\nRelevant lesson content:\n{lesson_snippets}"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,
        lambda: openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    mcp.run(transport="stdio")

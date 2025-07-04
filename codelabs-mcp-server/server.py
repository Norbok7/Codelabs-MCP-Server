import os
import asyncio
import openai
from fastmcp import FastMCP

# Initialize the FastMCP server with a descriptive name
mcp = FastMCP(name="Codelabs Learning Assistant")

# Set the OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    # Don't raise error immediately - let the tool handle it gracefully
    api_key = None

if api_key:
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
    # Check if API key is available
    if not api_key:
        return "❌ **Configuration Error**: OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."
    
    lesson_snippets = extract_relevant_lessons(question)
    prompt = INSTRUCTION_PROMPT
    if lesson_snippets:
        prompt += f"\n\nRelevant lesson content:\n{lesson_snippets}"

    # List of models to try, in order of preference
    models_to_try = ["gpt-4o-mini", "gpt-3.5-turbo", "gpt-4o"]
    
    loop = asyncio.get_event_loop()
    
    for model in models_to_try:
        try:
            response = await loop.run_in_executor(
                None,
                lambda m=model: openai.chat.completions.create(
                    model=m,
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": question}
                    ]
                )
            )
            return response.choices[0].message.content
        except Exception as e:
            # Log the error and try the next model
            error_msg = str(e)
            if "does not exist" in error_msg or "not found" in error_msg:
                continue  # Try next model
            else:
                # For other errors (API key, rate limit, etc.), provide helpful message
                if "api_key" in error_msg.lower():
                    return "❌ **Configuration Error**: OpenAI API key is not set or invalid. Please ensure the OPENAI_API_KEY environment variable is properly configured."
                elif "rate_limit" in error_msg.lower():
                    return "⏳ **Rate Limit**: API rate limit exceeded. Please try again in a moment."
                elif "quota" in error_msg.lower():
                    return "💳 **Quota Exceeded**: OpenAI API quota has been exceeded. Please check your account billing."
                else:
                    return f"🔧 **API Error**: Unable to process your question due to an API error: {error_msg[:100]}{'...' if len(error_msg) > 100 else ''}"
    
    # If all models failed
    return "❌ **Model Unavailable**: Unable to access any OpenAI models. Please check your API key and account permissions, or try again later."

if __name__ == "__main__":
    mcp.run(transport="stdio")

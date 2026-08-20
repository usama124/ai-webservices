import os
from openai import OpenAI

# Initialize the OpenAI client pointing to NVIDIA's API endpoint
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.environ.get("NVIDIA_API_KEY")
)


def __llm_call(system_prompt: str, prompt: str, temperature: float, max_tokens: int, extra_body: dict = {}):
    try:
        # Request completion from GLM via NVIDIA's standard Chat Completions endpoint
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),  # Replace with "zai/glm-5.3" based on active endpoints
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,  # Lower temperature ensures more factual extraction
            max_tokens=max_tokens,  # Allocation for summary length
            extra_body=extra_body
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"


def chat(your_text: str) -> str:
    """
    Handles conversational responses using the GLM model on NVIDIA NIM.
    """
    system_prompt = """You are an authentic, conversational AI assistant. 

    Instructions:
    - Always reply in the exact same language as the user.
    - Provide truthful, factual, and direct answers.
    - Keep responses brief and concise—avoid conversational filler or repetitive explanations."""

    return __llm_call(system_prompt, your_text, 0.7, 256)


def summarize(long_text: str) -> str:
    """
    Summarizes long-form text using the Z-ai GLM model hosted on NVIDIA NIM.
    """
    prompt = f"""You are an advanced text summarizing agent. 
            Provide a clear summary of the following text. 
            Break your response down into core takeaways and an executive summary.
            
            TEXT TO SUMMARIZE:
            \"\"\"
            {long_text}
            \"\"\"
            """
    system_prompt = "You are a helpful assistant that excels at document summarization."

    return __llm_call(system_prompt, prompt, 0.3, 2048, extra_body={"reasoning_effort": "low"})


def generate_story(topic: str) -> str:
    """
    Generates a short 3 to 4 line story based on a user-provided topic.
    """
    system_prompt = """You are a creative flash-fiction writer.

    Instructions:
    - Write a complete, engaging short story based on the user's topic.
    - The output MUST be strictly 3 to 4 lines long.
    - Output ONLY the story. Do not add titles, intro text, or extra commentary.
    - Match the language of the prompt."""

    return __llm_call(system_prompt, topic, 0.8, 512)


def polish_text(text: str) -> str:
    """
    Polishes input text for correct grammar, clarity, and professional tone.
    """
    system_prompt = """You are an expert editor and professional copywriter.
    
        Instructions:
        - Correct all grammatical, spelling, and punctuation errors in the provided text.
        - Enhance clarity, word choice, and flow while maintaining a clean, professional tone.
        - Preserve the author's original meaning and core message.
        - Output ONLY the polished text. Do not include intros, conversational filler, quotation marks, or explanations.
        - Keep the response in the same language as the input text."""

    return __llm_call(system_prompt, text, 0.2, 2048)


def explain_code(code_snippet: str) -> str:
    """
    Explains the logic, purpose, and key components of a provided code snippet.
    """
    user_prompt = f"Explain the following code snippet in detail:\n\n ```{code_snippet}```"
    system_prompt = """You are an expert software engineer and technical educator.

        Instructions:
        - Provide a clear, high-level summary of what the code does.
        - Break down the core logic step-by-step or by key functions using bullet points.
        - Identify any notable edge cases, performance considerations, or potential bugs if applicable.
        - Keep the explanation concise, professional, and easy to follow."""

    return __llm_call(system_prompt, user_prompt, 0.2, 2048)


def translate_text(text: str, target_language: str) -> str:
    """
    Translates text when the user provides input containing both
    the text and the target language directive (e.g., 'Hello world in Urdu').
    """
    system_prompt = """You are an intelligent language translation system.
        
        Instructions:
        - Analyze the user's input to identify the target language (e.g., Urdu, Arabic, Hindi, Italian, French. etc) and the underlying text to translate.
        - Translate the text accurately into the requested target language.
        - Output ONLY the final translated text. Do not include notes, original text, explanations, or quotes.
        - If no target language is mentioned, default to English."""

    return __llm_call(system_prompt, text, 0.1, 1024)

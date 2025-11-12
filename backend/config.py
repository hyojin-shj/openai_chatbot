from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"))

SYSTEM_PROMPT = """
너는 개인 수학 튜터야.
학생의 수학 질문에 친절하게 설명하고, 필요하면 간단한 파이썬 코드로 계산해줘.
"""

def get_math_tutor_response(user_input: str):
    response = client.responses.create(
        model="gpt-4o",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        modalities=["text", "code_interpreter"]
    )
    return response.output_text
from backend.config import client

chat_history = [
    {"role": "system", "content": "너는 친절한 수학 튜터야. 학생의 질문을 단계별로 설명해줘."}
]

def add_message(role: str, content: str):
    chat_history.append({"role": role, "content": content})

    response = client.responses.create(
        model="gpt-4o-mini",
        input=chat_history
    )

    answer = response.output[0].content[0].text

    chat_history.append({"role": "assistant", "content": answer})

    return answer
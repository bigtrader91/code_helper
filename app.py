import streamlit as st
from openai import OpenAI
import os

# openai.api_key = os.getenv("OPENAI_API_KEY")
# OpenAI 클라이언트 초기화
client = OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

# Streamlit 앱 설정
st.title('Python Variable Name Generator')

# 사용자 입력 인터페이스
description = st.text_input('짓고자 하는 이름에 대해 설명해주세요.')

# 대화 메시지를 초기화합니다.
messages = [
    {"role": "system", "content": """
        I want to make class names, functions, and variable names in Python according to the following rules. Please listen to my explanation and write a variable name according to the rules.

        Rule 1: Use the naming convention commonly used by Python.
        Rule 2: Please write the name of Python file (.py) in noun form.
        Rule 3: For function names, write a combination of verbs and nouns.
        Rule 4: When creating a variable name, use commonly used abbreviations, such as df in the case of dataframe.

        Please suggest a total of 5 names as in the example.
    """}
]

# 사용자가 설명을 입력하면 함수를 호출합니다.
if description:
    # 사용자의 설명을 메시지에 추가합니다.
    messages.append({"role": "user", "content": description})

    # 대화형 API를 사용하여 응답을 생성합니다.
    with st.spinner('Waiting for ChatGPT...'):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # 생성된 변수명을 표시합니다.
        if response.choices[0]:
            variable_name = response.choices[0].message.content
            st.write(variable_name)
        else:
            st.error("Error: No response from the model.")

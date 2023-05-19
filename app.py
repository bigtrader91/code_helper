# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import openai
import os
openai.api_key = st.secrets['OPENAI_API_KEY']
# openai.api_key = os.getenv("OPENAI_API_KEY")




# GPT-3 API를 호출하여 변수명을 가져오는 함수를 정의합니다.
def get_variable_name(prompt):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            n=3
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit 앱을 설정합니다.
st.title('Python Variable Name Generator')

# 사용자 입력 인터페이스를 만듭니다.
description = st.text_input('Describe the variable you need a name for:')

prompt=f'''
I want to make class names, functions, and variable names in Python according to the following rules. Please listen to my explanation and write a variable name according to the rules.

Rule 1: 데이터프레임, 딕셔너리, and 리스트 are included in the description, you must write it so that it is placed at the front of the variable. Other values follow Python naming conventions.
Rule 2: If the name of a variable is lengthened, use _
Rule 3: Use nouns as much as you can.

Please suggest a total of 3 names like the example and answer them in a good way through a new line

[description]
{description}
[Example]
\n
1. abc \n
2. defer \n
3. fet \n

Please suggest a total of 3 names as in the example.
'''
# 사용자가 설명을 입력하면 함수를 호출합니다.
if description:
    with st.spinner('Waiting for ChatGPT...'):
        variable_name = get_variable_name(prompt)
        st.write(variable_name)
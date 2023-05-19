# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import openai
import os
openai.api_key = st.secrets['OPENAI_API_KEY']
# openai.api_key = os.getenv("OPENAI_API_KEY")

prompt=f'''
I want to make class names, functions, and variable names in Python according to the following rules. Please listen to my explanation and write a variable name according to the rules.

Rule 1: In the case of df, dict, and list, you must write it so that it is placed at the front of the variable.
Rule 2: If the name of a variable is lengthened, use _
Rule 3: Use nouns as much as you can.

Please follow the most basic Python naming convention for the parts that are not set in the rules.


[description]
{}
[Example]
1.
2.
3.

'''


# GPT-3 API를 호출하여 변수명을 가져오는 함수를 정의합니다.
def get_variable_name(prompt, description):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=description,
            temperature=0,
            max_tokens=60,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit 앱을 설정합니다.
st.title('Python Variable Name Generator')

# 사용자 입력 인터페이스를 만듭니다.
description = st.text_input('Describe the variable you need a name for:')

# 사용자가 설명을 입력하면 함수를 호출합니다.
if description:
    with st.spinner('Waiting for ChatGPT...'):
        variable_name = get_variable_name(prompt, description)
        st.write(f"Suggested variable name: `{variable_name}`")

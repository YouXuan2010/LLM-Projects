import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "sk-YOUR_API_KEY"

llm = ChatOpenAI(temperature=0.5)

uploaded_file = st.file_uploader('Choose a file')

llm_string = st.text_input("Enter query: ")

button_clicked = st.button("Ask GPT!")

if button_clicked:
    if uploaded_file is not None and llm_string is not None:
        agent = create_csv_agent(llm, uploaded_file, verbose=True, handle_parsing_errors=True)
        result = agent.invoke(llm_string)

        st.write("Results: ")
        st.write(result)

        llm_string = None
    else:
        st.warning("Please upload your csv file before sending query!")
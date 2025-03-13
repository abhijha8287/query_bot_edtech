import streamlit as st
from langchain_helper import create_vector_db, get_ga_chain 
st.title('Code basics QA 👨🏻‍🏫')

btn=st.button("Create Knowledgebase")

if btn:
    pass
question=st.text_input("Ask a question")
if question:
    chain=get_ga_chain()
    response=chain.invoke(question)
    st.header('Answer: ')
    st.write(response['result'])
   

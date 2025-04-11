import streamlit as st 
import pandas as pd 
import duckdb as db

df=pd.DataFrame({'a':[10,23,54,17],'b':[1,7,9,14]})

st.write("""
        # SQL SRS
         Spaced repetition System SQL practice
         """)

st.write("You selected:", option)

tab1,tab2,tab3 = st.tabs(["cat","dog","owl"])

with tab1:
    input_text=st.text_area(label="Query")
    query=db.sql(input_text)
    st.write(f"query: {input_text}")
    st.dataframe(query)
    
with tab2:
    st.header("dog")
    st.image("https://static.streamlit.io/exemples/dog.jpeg",width=200)
    
with tab3:
    st.header("owl")
    st.image("https://static.streamlit.io/exemples/owl.jpeg",width=200)
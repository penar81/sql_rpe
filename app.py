import streamlit as st 
import pandas as pd 
import duckdb as db
import io

beverages=pd.DataFrame(
    {'beverage':['orange juice','Expresso','Tea'],
     'price':[2.5,2.0,3.0]
    
     })
     
food_items=pd.DataFrame(
    {'food_item':['cookie juice','chocolatione','muffin'],
     'food_price':[2.5,2.0,3.0]
     })

answer="""
SELECT * FROM beverages
CROSS JOIN food_items"""

solution=db.sql(answer)

st.header("entrée votre code")
query=st.text_area(label='vôtre code SQL est ici', key='user_input')

if query:
    result=db.sql(query).df()
    st.dataframe(result)


tab2,tab3 = st.tabs(["Tables","Solution"])
   
with tab2:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    
with tab3:
    st.write(answer)
import pandas as pd
import streamlit as st
import plotly.express as px
from database import view_all_data


def read(table):
    result = view_all_data(table)
    if table=="pet":
        df=pd.DataFrame(result,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
        with st.expander("View all Pets"):
            st.dataframe(df)
        with st.expander("Animal Types"):
            df1=df['animal_type'].value_counts().to_frame()
            df1=df1.reset_index()
            st.dataframe(df1)
            p1=px.pie(df1,names='index',values='animal_type')
            st.plotly_chart(p1)

    if table=="owner":
        df=pd.DataFrame(result,columns=['oid','fname','lname','ph_no','state','city'])
        with st.expander("View all Owners"):
            st.dataframe(df)
        with st.expander("Owner States"):
            df1=df['state'].value_counts().to_frame()
            df1=df1.reset_index()
            st.dataframe(df1)
            p1=px.pie(df1,names='index',values='state')
            st.plotly_chart(p1)

    if table=="caretaker":
        df=pd.DataFrame(result,columns=['cid','fname','lname','ph_no','age'])
        with st.expander("View all Caretakers"):
            st.dataframe(df)
    


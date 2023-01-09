import pandas as pd
import streamlit as st
from database import join_tables,aggregate_tables,execute_query,get_pid,call_function,call_procedure,union_tables,call_procedure1

def join():
    if st.button("Join Pet and Owner based on OID"):
        result=join_tables()
        df=pd.DataFrame(result,columns=['oid','fname','lname','pid','name','animal_type','breed'])
        with st.expander("View Join"):
            st.dataframe(df)

def aggregate():
    if st.button("Aggregate"):
        result=aggregate_tables()
        df=pd.DataFrame(result,columns=['cid','fname','lname','NumberOfAnimals'])
        with st.expander("View Aggregate"):
            st.dataframe(df)

def union1():
    table=st.selectbox("Table: ", ["owner","caretaker","activities"])
    val="Union of Pet and "+table
    if st.button(val):
        result=union_tables(table)
        st.subheader(val)
        df=pd.DataFrame(result,columns=['id'])
        with st.expander("View Union"):
            st.dataframe(df)

def function1(): 
    list_of_pets=[i[0] for i in get_pid()]
    selected_pet=st.selectbox("Select pet", list_of_pets)
    if st.button("Click"):
        val=call_function(selected_pet)
        st.subheader("This pet requires: ")
        st.subheader(val)


def procedure1(): 
    result=call_procedure()
    df=pd.DataFrame(result,columns=['Pet ID','Pet Name','Duration','Owner ID'])
    with st.expander("View Pets"):
        st.dataframe(df)


def text_box():
    text=st.text_area(label="Enter SQL query here")
    if st.button("Execute!"):
        res=execute_query(text)
        df=pd.DataFrame(res)
        st.success("Successfully executed query!")
        st.dataframe(df)
        
        
def sick_pet():
    if st.button("Click!"):
        result=call_procedure1()
        df=pd.DataFrame(result,columns=['Pet Name','Medicines','Caretaker Name'])
        with st.expander("View Sick Pets and their corresponding caretakers and medicines: "):
            st.dataframe(df)
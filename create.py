import streamlit as st
import pandas as pd
from database import add_data_owner,add_data_pet,add_data_caretaker,view_all_data,view_names


def create(table):

    

    if table=="owner":
        c1,c2=st.columns(2)
        with c1:
            oid=st.number_input("Owner ID: ",min_value=1, max_value=100, value=1, step=1)
            fname=st.text_input("First Name: ")
            lname=st.text_input("Last Name: ")
        with c2:
            ph_no=st.number_input("Phone Number: ",min_value=1000000000, max_value=9999999999, value=1000000000, step=1)
            state=st.selectbox("State: ",["Karnataka","Tamil Nadu","Gujarat","Kerala","Maharashtra","Uttar Pradesh","Telangana","Bihar"])
            city=st.selectbox("City: ",["Bengaluru","Mysore","Patna","Chennai","Ahmedabad","Mumbai","Lucknow","Hyderabad","Kochi"])
        if st.button("Add new owner"):
            add_data_owner(oid,fname,lname,ph_no,state,city)
            st.success("Successfully added owner: {}".format(fname))
            result = view_all_data(table)
            df=pd.DataFrame(result,columns=['oid','fname','lname','ph_no','state','city'])
            with st.expander("View all Owners"):
                st.dataframe(df)



    if table=="pet":
        c1,c2,c3=st.columns(3)
        with c1:
            pid=st.number_input("Pet ID: ",min_value=1, max_value=100, value=1, step=1)
            name=st.text_input("Pet Name: ")
            animal_type=st.selectbox("Animal Type: ", ["Dog", "Cat", "Turtle","Hamster","Rabbit","Bird"])
        with c2:
            age=st.number_input("Age: ",min_value=1, max_value=25, value=1, step=1)
            breed=st.text_input("Breed: ")
            duration=st.number_input("Duration in weeks: ",min_value=1, max_value=30, value=1, step=1)
        with c3:
            oid=st.number_input("Owner Id: ",min_value=1, max_value=100, value=1, step=1)
            cid=st.number_input("Caretaker Id: ",min_value=1, max_value=100, value=1, step=1)
            aid=st.number_input("Activity Id: ",min_value=1, max_value=100, value=1, step=1)
        if st.button("Add new pet"):
            add_data_pet(pid,name,animal_type,age,breed,duration,oid,cid,aid)
            st.success("Successfully added pet: {}".format(name))
            result = view_all_data(table)
            df=pd.DataFrame(result,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
            with st.expander("View all Pets"):
                st.dataframe(df)
            
    
    if table=="caretaker":
        c1,c2=st.columns(2)
        with c1:
            cid=st.number_input("Caretaker ID: ",min_value=1, max_value=100, value=1, step=1)
            fname=st.text_input("First Name: ")
            lname=st.text_input("Last Name: ")
        with c2:
            ph_no=st.number_input("Phone Number: ",min_value=1000000000, max_value=9999999999, value=1000000000, step=1)
            age=st.number_input("Age: ",min_value=18, max_value=65, value=18, step=1)
        if st.button("Add new caretaker"):
            add_data_caretaker(cid,fname,lname,ph_no,age)
            st.success("Successfully added caretaker: {}".format(fname))
            result = view_all_data(table)
            df=pd.DataFrame(result,columns=['cid','fname','lname','ph_no','age'])
            with st.expander("View all Caretakers"):
                st.dataframe(df)
  
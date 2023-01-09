import pandas as pd
import streamlit as st
from database import view_all_data,view_names,get_data,edit_pet_data,edit_owner_data,edit_caretaker_data


def update(table):

    result = view_all_data(table)

    if table=="pet":
        df=pd.DataFrame(result,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
        with st.expander("View all Pets"):
            st.dataframe(df)
        list_of_pets=[i[0] for i in view_names(table)]
        selected_pet=st.selectbox("Pet to Update", list_of_pets) 

        col1, col2 = st.columns(2)
        with col1:
            new_name=st.text_input("New Name: ")
            new_age=st.number_input("New Age: ",min_value=1, max_value=25, value=1, step=1)
            new_duration=st.number_input("New Duration: ",min_value=1, max_value=30, value=1, step=1)
        with col2:
            new_cid=st.number_input("New Caretaker ID: ",min_value=1, max_value=100, value=1, step=1)
            new_aid=st.number_input("New Activity ID: ",min_value=1, max_value=100, value=1, step=1)
        if st.button("Update Pet"):
            edit_pet_data(new_name,new_age,new_duration,new_cid,new_aid,selected_pet)
            st.success("Successfully updated: {}".format(new_name))
    
    if table=="owner":
        df=pd.DataFrame(result,columns=['oid','fname','lname','ph_no','state','city'])
        with st.expander("View all Owners"):
            st.dataframe(df)
        list_of_owners=[i[0] for i in view_names(table)]
        selected_owner=st.selectbox("Owner to Update", list_of_owners) 
        selected_result=get_data(table,selected_owner)

        new_ph_no=st.number_input("New Phone Number: ",min_value=1000000000, max_value=9999999999, value=1000000000, step=1)
        new_state=st.selectbox("New State: ",["Karnataka","Tamil Nadu","Gujarat","Kerala","Maharashtra","Uttar Pradesh","Telangana","Bihar"])
        new_city=st.selectbox("New City: ",["Bengaluru","Mysore","Patna","Chennai","Ahmedabad","Mumbai","Lucknow","Hyderabad","Kochi"])
        if st.button("Update Owner"):
            edit_owner_data(new_ph_no,new_state,new_city,selected_owner)
            st.success("Successfully updated: {}".format(selected_owner))
        
    if table=="caretaker":
        df=pd.DataFrame(result,columns=['cid','fname','lname','ph_no','age'])
        with st.expander("View all Caretakers"):
            st.dataframe(df)
        list_of_caretakers=[i[0] for i in view_names(table)]
        selected_caretaker=st.selectbox("Caretaker to Update", list_of_caretakers) 

        new_ph_no=st.number_input("New Phone Number: ",min_value=1000000000, max_value=9999999999, value=1000000000, step=1)
        new_age=st.number_input("New Age: ",min_value=18, max_value=65, value=18, step=1)
        if st.button("Update Caretaker"):
            edit_caretaker_data(new_ph_no,new_age,selected_caretaker)
            st.success("Successfully updated: {}".format(selected_caretaker))


    result2 = view_all_data(table)
    if table=="pet":
        df=pd.DataFrame(result2,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
        with st.expander("View updated Pets"):
            st.dataframe(df)
    if table=="owner":
        df=pd.DataFrame(result2,columns=['oid','fname','lname','ph_no','state','city'])
        with st.expander("View updated Owners"):
            st.dataframe(df)
    if table=="caretaker":
        df=pd.DataFrame(result2,columns=['cid','fname','lname','ph_no','age'])
        with st.expander("View updated Caretakers"):
            st.dataframe(df)
    
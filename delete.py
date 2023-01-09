import pandas as pd
import streamlit as st
from database import delete_data,view_names,view_all_data


def delete(table):
    result=view_all_data(table)
    if(table=="pet"):
        df=pd.DataFrame(result,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
        with st.expander("View all Pets"):
            st.dataframe(df)

        list_of_pets=[i[0] for i in view_names(table)]
        selected_pet=st.selectbox("Pet to Delete", list_of_pets)
        st.warning("Do you want to delete :{}".format(selected_pet))
        if st.button("Delete Pet"):
            delete_data(table,selected_pet)
            st.success("Pet and its dependencies have been deleted successfully")

    if(table=="owner"):
        df=pd.DataFrame(result,columns=['oid','fname','lname','ph_no','state','city'])
        with st.expander("View all Owner"):
            st.dataframe(df)
        list_of_owners=[i[0] for i in view_names(table)]
        selected_owner=st.selectbox("Owner to Delete", list_of_owners)
        st.warning("Do you want to delete :{}".format(selected_owner))
        if st.button("Delete Owner"):
            delete_data(table,selected_owner)
            st.success("Owner has been deleted successfully")
    
    if(table=="caretaker"):
        df=pd.DataFrame(result,columns=['cid','fname','lname','ph_no','age'])
        with st.expander("View all Caretakers"):
            st.dataframe(df)
        list_of_caretakers=[i[0] for i in view_names(table)]
        selected_caretaker=st.selectbox("Caretaker to Delete", list_of_caretakers)
        st.warning("Do you want to delete :{}".format(selected_caretaker))
        if st.button("Delete Caretaker"):
            delete_data(table,selected_caretaker)
            st.success("Caretaker has been deleted successfully")

    result2=view_all_data(table)
    if table=="pet":
        df=pd.DataFrame(result2,columns=['pid','name','animal_type','age','breed','duration','oid','cid','aid'])
        with st.expander("After Delete Pets"):
            st.dataframe(df)
    if table=="owner":
        df=pd.DataFrame(result2,columns=['oid','fname','lname','ph_no','state','city'])
        with st.expander("After Delete Owner"):
            st.dataframe(df)
    if table=="caretaker":
        df=pd.DataFrame(result2,columns=['cid','fname','lname','ph_no','age'])
        with st.expander("After Delete Caretakers"):
            st.dataframe(df)
   
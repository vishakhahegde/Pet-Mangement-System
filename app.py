# Importing packages
import streamlit as st
import mysql.connector

from create import create
from delete import delete
from read import read
from update import update
from join import join,aggregate,text_box,function1,procedure1,union1,sick_pet


def main():
    st.title("Pet Management System")
    st.image('petcute.png')
    menu = ["Add", "View", "Edit", "Remove"]
    tables=["owner","caretaker","pet"]
    other=["none","TEXT BOX","JOIN","AGGREGATE","FUNCTION","PROCEDURE","UNION","SICK PETS"]

    choice = st.sidebar.selectbox("Choose CRUD Operation", menu)
    choice2=st.sidebar.selectbox("Choose Table",tables)
    choice3=st.sidebar.selectbox("Other Operations",other)


    if choice3=="none":
        if choice == "Add":
            st.subheader("Enter {} details".format(choice2))
            create(choice2)

        elif choice == "View":
            st.subheader("Read {} details".format(choice2))
            read(choice2)

        elif choice == "Edit":
            st.subheader("Update {} details".format(choice2))
            update(choice2)

        elif choice == "Remove":
            st.subheader("Delete {} details".format(choice2))
            delete(choice2)
        else:
            st.subheader("About tasks")

    else:
        if choice3=="TEXT BOX":
            st.subheader("Enter your SQL query here: ")
            text_box()
        elif choice3=="JOIN":
            st.subheader("Join of Pet and Owner")
            join()
        elif choice3=="AGGREGATE":
            st.subheader("Aggregate of number of pets that are under each caretaker:")
            aggregate()
        elif choice3=="FUNCTION":
            st.subheader("A pet is sick! Choose Pet ID to see which medicine to give: ")
            function1()
        elif choice3=="PROCEDURE":
            st.subheader("Alert! These pets have less than 2 weeks left to stay!")
            procedure1()
        elif choice3=="UNION":
            st.subheader("Union of Pet with other tables: ")
            st.subheader("Choose which table to do union with")
            union1()
        elif choice3=="SICK PETS":
            st.subheader("Sick Pets")
            sick_pet()

if __name__ == '__main__':
    main()
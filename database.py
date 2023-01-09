# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pet_management"
)
c = mydb.cursor()


#ADDING DATA TO ALL TABLES/CREATE
def add_data_pet(pid,name,animal_type,age,breed,duration,oid,cid,aid):
    c.execute('insert into pet(pid,name,animal_type,age,breed,duration,oid,cid,aid) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(pid,name,animal_type,age,breed,duration,oid,cid,aid))
    mydb.commit()

def add_data_owner(oid,fname,lname,ph_no,state,city):
    c.execute('insert into owner(oid,fname,lname,ph_no,state,city) values (%s,%s,%s,%s,%s,%s)',(oid,fname,lname,ph_no,state,city))
    mydb.commit()

def add_data_caretaker(cid,fname,lname,ph_no,age):
    c.execute('insert into caretaker(cid,fname,lname,ph_no,age) values (%s,%s,%s,%s,%s)',(cid,fname,lname,ph_no,age))
    mydb.commit()



#READ
def view_all_data(table):
    if table=="pet":
        c.execute('select * from pet')
    if table=="owner":
        c.execute('select * from owner')
    if table=="caretaker":
        c.execute('select * from caretaker')
    data = c.fetchall()
    return data

def view_names(table):
    if table=="pet":
        c.execute('select name from pet')
    if table=="owner":
        c.execute('select fname from owner')
    if table=="caretaker":
        c.execute('select fname from caretaker')
    data=c.fetchall()
    return data

def get_data(table,name):
    if table=="pet":
        c.execute('select * from pet where name="{}"'.format(name))
    if table=="owner":
        c.execute('select * from owner where fname="{}"'.format(name))
    if table=="caretaker":
        c.execute('select * from caretaker where fname="{}"'.format(name))
    data=c.fetchall()
    return data

def get_pid():
    c.execute('select pid from pet');
    data=c.fetchall()
    return data


#UPDATING DATA 
def edit_pet_data(new_name,new_age,new_duration,new_cid,new_aid,selected_pet):
    c.execute("update pet set name=%s,age=%s,duration=%s,cid=%s,aid=%s where name=%s",(new_name,new_age,new_duration,new_cid,new_aid,selected_pet))
    mydb.commit()

def edit_owner_data(new_ph_no,new_state,new_city,selected_owner):
    c.execute("update owner set ph_no=%s,state=%s,city=%s where fname=%s",(new_ph_no,new_state,new_city,selected_owner))
    mydb.commit()

def edit_caretaker_data(new_ph_no,new_age,selected_caretaker):
    c.execute("update caretaker set ph_no=%s,age=%s where fname=%s",(new_ph_no,new_age,selected_caretaker))
    mydb.commit()


#DELETE
def delete_data(table,id):
    if(table=="pet"):
        c.execute('DELETE FROM pet WHERE name="{}"'.format(id))
        mydb.commit()
    if(table=="owner"):
        c.execute('DELETE FROM owner WHERE fname="{}"'.format(id))
        mydb.commit()
    if(table=="caretaker"):
        c.execute('DELETE FROM caretaker WHERE fname="{}"'.format(id))
        mydb.commit()
    
#JOIN
def join_tables():
    c.execute('select owner.oid,owner.fname,owner.lname,pet.pid,pet.name,pet.animal_type,pet.breed from pet inner join owner on pet.oid=owner.oid')
    data=c.fetchall()
    return data

#UNION
def union_tables(table):
    if table=="owner":
        c.execute('select oid from pet union select oid from owner')
    if table=="caretaker":
        c.execute('select cid from pet union select cid from caretaker')
    if table=="activities":
        c.execute('select aid from pet union select aid from activities')
    data=c.fetchall()
    return data

#AGGREGATE
def aggregate_tables():
    c.execute('SELECT caretaker.cid,caretaker.fname,caretaker.lname, COUNT(caretaker.cid) AS NumberOfAnimals FROM pet LEFT JOIN caretaker ON pet.cid = caretaker.cid GROUP BY cid')
    data=c.fetchall()
    return data

#USER DEFINED QUERY
def execute_query(text):
    c.execute(text)
    data=c.fetchall()
    return data

def call_function(pid):
    c.execute('set @x=sick_pet("{}")'.format(pid))
    c.execute('select @x')
    data=c.fetchone()[0]
    return data

def call_procedure():
    #c.execute('call alert_owner1(@m)',multi=True)
    #c.execute('select @m')
    #c.execute('select * from temp')
    c.execute('select pid,name,duration,oid from pet where duration<=2;')
    data=c.fetchall()
    return data

def call_procedure1():
    c.execute('select*from sick_table;')
    data=c.fetchall()
    return data


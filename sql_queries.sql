--CREATING TABLES

--OWNER
CREATE TABLE owner
(
  oid VARCHAR(10) NOT NULL,
  fname VARCHAR(20),
  lname VARCHAR(20),
  ph_no INT,
  state VARCHAR(20),
  city VARCHAR(20),
  PRIMARY KEY (oid)
);

--ACTIVITIES
CREATE TABLE activities
(
  aid VARCHAR(10) NOT NULL,
  name VARCHAR(20),
  type VARCHAR(20),
  calories_burnt FLOAT,
  PRIMARY KEY (aid)
);

--CARETAKER
CREATE TABLE caretaker
(
  cid VARCHAR(10) NOT NULL,
  fname VARCHAR(20),
  lname VARCHAR(20),
  ph_no INT,
  age INT,
  PRIMARY KEY (cid)
);

--PET
CREATE TABLE pet
(
  pid VARCHAR(10) NOT NULL,
  name VARCHAR(20),
  animal_type VARCHAR(10),
  age INT,
  breed VARCHAR(10),
  duration INT,
  oid VARCHAR(10) NOT NULL,
  cid VARCHAR(10) NOT NULL,
  aid VARCHAR(10) NOT NULL,
  PRIMARY KEY (pid),
  FOREIGN KEY (oid) REFERENCES owner(oid) ON DELETE CASCADE,
  FOREIGN KEY (cid) REFERENCES caretaker(cid) ON DELETE CASCADE,
  FOREIGN KEY (aid) REFERENCES activities(aid)
);

--DEPENDENCIES
CREATE TABLE dependencies
(
  pid VARCHAR(10) NOT NULL,
  sleep FLOAT,
  food_required VARCHAR(20),
  medicines VARCHAR(20),
  allergies VARCHAR(20),
  PRIMARY KEY (pid),
  FOREIGN KEY (pid) REFERENCES pet(pid) ON DELETE CASCADE
);


--POPULATING TABLES

--OWNER
LOAD DATA LOCAL INFILE 'D:/Data/Mini Projects/SEM 5/DBMS/owner.csv'
INTO TABLE pet_management.owner
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

--ACTIVITES
LOAD DATA LOCAL INFILE 'D:/Data/Mini Projects/SEM 5/DBMS/activities.csv'
INTO TABLE pet_management.activities
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

--CARETAKER
LOAD DATA LOCAL INFILE 'D:/Data/Mini Projects/SEM 5/DBMS/caretaker.csv'
INTO TABLE pet_management.caretaker
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

--PET
LOAD DATA LOCAL INFILE 'D:/Data/Mini Projects/SEM 5/DBMS/pet.csv'
INTO TABLE pet_management.pet
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

--DEPENDENCIES
LOAD DATA LOCAL INFILE 'D:/Data/Mini Projects/SEM 5/DBMS/dependencies.csv'
INTO TABLE pet_management.dependencies
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


--JOIN: pet & owner, pet & caretaker
select owner.oid,owner.fname,owner.lname,pet.pid,pet.name,pet.animal_type,pet.breed from pet inner join owner on pet.oid=owner.oid;
select caretaker.cid,caretaker.fname,caretaker.lname,pet.pid,pet.name,pet.animal_type,pet.breed from pet inner join caretaker on pet.cid=caretaker.cid;

--AGGREGATE: number of pets that are under each caretaker
SELECT caretaker.cid,caretaker.fname,caretaker.lname, COUNT(caretaker.cid) AS NumberOfAnimals FROM pet
LEFT JOIN caretaker ON pet.cid = caretaker.cid
GROUP BY cid;

--TRIGGER: While adding new pet entry, check if duration is within range of 1 and 24 weeks
DELIMITER $$
CREATE TRIGGER add_pet 
BEFORE INSERT 
ON pet FOR EACH ROW
BEGIN 
IF NEW.duration>24  OR NEW.duration<1 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT="Duration must be between 1 and 24 weeks!";
END IF;
END;$$
DELIMITER ;

--testing the trigger
insert into pet(pid,name,animal_type,age,breed,duration,oid,cid,aid) values (40,'hello','Dog',2,'Poodle',67,2,2,2)


--PROCEDURE: if duration is lesser than 2 weeks give an alert saying less than 2 weeks left
DELIMITER $$
--DROP PROCEDURE IF EXISTS alert_owner$$
CREATE procedure alert_owner(OUT msg VARCHAR(30))
BEGIN
select pid,name,duration,oid from pet where duration<=2;
END;$$
DELIMITER ;

--calling the procedure
call alert_owner(@m);

--FUNCTION: caretaker says pet is sick, display medicines for that pet
DELIMITER $$
CREATE FUNCTION sick_pet (pid INT)
RETURNS VARCHAR(20)
BEGIN
DECLARE med VARCHAR(20);
SELECT medicines INTO med from dependencies where dependencies.pid = pid;
RETURN med;
END; $$
DELIMITER ;

--to call function
set @x=sick_pet(1);
select @x;


--SET OPERATIONS: UNION--each caretaker can handle multiple pets; each owner can have multiple pets;
select cid from pet
UNION
select cid from caretaker;

select oid from pet
union 
select oid from owner;

select aid from pet
UNION
select aid from activities;

--MODIFICATION: create a function/procedure to display pet,caretaker,medicine if pet is sick
delimiter //
DROP PROCEDURE IF EXISTS sick_animal//
create procedure sick_animal() 
    begin 
    truncate table sick_table;
    insert into sick_table (name,medicines,fname) 
    select pet.name, dependencies.medicines, caretaker.fname 
    from pet, dependencies,caretaker 
    where pet.pid=dependencies.pid and pet.cid=caretaker.cid and dependencies.sickness=1; 
    end //
delimiter ;


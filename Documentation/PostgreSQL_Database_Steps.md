        --THESE STEPS ARE TO BE DONE AFTER POSTGRESQL IS INSTALLED--

1. Use Stackbuilder to install PostGIS and all dependencies

    a. Make sure to keep default settings (besides the install location, that should be set to
       where your PostgreSQL Server is installed)

2. Access PostgreSQL with pgAdmin 4 (this is the GUI)

3. Login to your PostgreSQL Server (PostgreSQL 16 presumably) and create a new database (I called mine GeoGuessr to match the name of the App).

4. Locate and click the "Query Tool" button at the top of the UI (this will bring you to a SQL IDE)

5. Add the postgis extension to the Postgres server by entering this SQL statement into the editor:

    a. CREATE EXTENSION postgis;

    b. then check the installation with "SELECT postgis_full_version();"

6. Create the Player and Game_Scores tables with the following SQL:

    a. create table Player (
	      playerID serial primary key,
	      username varchar(80) not null,
	      password varchar(80) not null,
	      email varchar(80)
        );

    b. create table Game_Score (
          gameID serial primary key,
          score integer not null,
	      finalTime integer not null,
	      usedHintOne boolean not null,
	      usedHintTwo boolean not null,
	      datePlayed date not null,
	      playerID integer references Player (playerID)
        );

7. Use this statement to enter in dummy data to the Game_Scores table

    a. insert into Game_Score (score, finalTime, usedHintOne, usedHintTwo, datePlayed)
       values
       (100, 120, true, true, '2024-03-06'),
       (350, 240, false, false, '2024-03-07'),
       (400, 120, true, false, '2024-03-07'),
       (900, 60, true, true, '2024-03-10'),
       (850, 240, false, false, '2024-03-16'),
       (700, 120, true, false, '2024-03-06'),
       (500, 120, false, false, '2024-03-08'),
       (650, 30, true, true, '2024-03-30'),
       (300, 240, true, false, '2024-03-25'),
       (500, 90, true, false, '2024-03-07'),
       (250, 210, false, false, '2024-03-08'),
       (150, 60, true, true, '2024-03-26'),
       (800, 180, false, false, '2024-03-16'),
       (620, 30, true, false, '2024-03-17'),
       (400, 210, true, false, '2024-03-19'),
       (400, 120, true, true, '2024-03-20');

8. Use these statements to enter in dummy data to the Player table

    a. The password MD5 hashing function for PostgreSQL returns the Text data type, so run this statement first:
       alter table Player
       alter column password type text;
    
    b. Now you are safe to enter this statement:
       insert into Player (username, password, email)
       values
       ('Richard', MD5('password1'), 'richard.richard.@ddcc.com'),
       ('Max', MD5('password2'), 'max.max@ddcc.com'),
       ('JacobT', MD5('password3'), 'jacob.t@ddcc.com'),
       ('JacobH', MD5('password4'), 'jacob.h@ddcc.com'),
       ('Ryan', MD5('password5'), 'ryan.ryan@ddcc.com'),
       ('Colten', MD5('password6'), 'colten.colten@ddcc.com'),
       ('Jagang', MD5('password7'), 'jagang.jagang@ddcc.com'),
       ('Jennsen', MD5('password8'), 'jennsen.jennsen@ddcc.com'),
       ('Kahlan', MD5('password9'), 'kahlan.kahlan@ddcc.com'),
       ('Cara', MD5('password10'), 'cara.cara@ddcc.com'),
       ('Darken', MD5('password11'), 'darken.darken@ddcc.com'),
       ('Freddy', MD5('password12'), 'freddy.freddy@ddcc.com'),
       ('Bonnie', MD5('password13'), 'bonnie.bonnie@ddcc.com'),
       ('Chica', MD5('password14'), 'chica.chica@ddcc.com'),
       ('Foxy', MD5('password15'), 'foxy.foxy@ddcc.com'),
       ('Clank', MD5('password16'), 'clank.clank@ddcc.com');

9. Now, the Game_Score table must be updated in order to access the playerID foreign key values.
   In the statement below, the numbers on the left represent the 'gameID' column where the numbers
   on the right represent the 'playerID' column, the 'gameID' values might differ from what you have
   so make sure to run 'select * from Game_Score' to pick up your specific 'gameID' values and then run
   this statement with your 'gameID' values:

    a. update game_score
       set playerID = case gameID
       when 17 then 1
       when 18 then 2
       when 19 then 3
       when 20 then 4
       when 21 then 5
       when 22 then 6
       when 23 then 7
       when 24 then 8
       when 25 then 9
       when 26 then 10
       when 27 then 11
       when 28 then 12
       when 29 then 13
       when 30 then 14
       when 31 then 15
       when 32 then 16
       else playerID end
       where gameID in(17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
				       31, 32);
       
       DISCLAMER: if you have not created the populated Game_Score table yet, just add 'playerID'
                  to the insert statement for the Game_Score dummy data above and input the numbers
                  on the left of the above update statement to that insert statement.

10. The 'settings.py' file holds the database connection fields, but you still need the
    psycopg2 package: run 'pip install psycopg2' in the terminal (cmd) to get this package

    a. once psycopg2 is installed, make sure that your PostgreSQL 'postres' user password
       matches everyone else's: run "alter user postgres with password 'PB@rracuda1';"

11. Importing the GIS models and junk into a database (PostgreSQL) is a pain, but   
    thankfully it seems to only be a pain for me, I believe all you have to do is:

    a. Use the OSGeo4W network installer (https://trac.osgeo.org/osgeo4w/wiki) to install
       GDAL (and only GDAL), make sure this installs in the C: drive
    
    b. from wherever you have GeoGuessr installed, run this in a cmd window:
        'python manage.py migrate' to test the database connection

12. Create the table to hold the GIS information by running this SQL statement

    a. create table "GeoGuessr_worldborder (
	       id bigint primary key generated by default as identity,
	       name varchar(50),
	       area integer,
	       pop2005 integer,
	       fips varchar(2),
	       iso2 varchar(2),
	       iso3 varchar(3),
	       un integer,
	       region integer,
	       subregion integer,
	       lon double precision not null,
	       lat double precision not null,
	       "multiPoly" geometry(MULTIPOLYGON, 4326));
        
        (NOTE: you might have noticed that there are "" around the name of the table
         and the multiPoly column name, IF THESE ARE NOT PRESENT IN THE NAME DEFENITION
         THEN THE NEXT STEP WILL NOT WORK!!!)

13. In a command prompt, navigate to wherever you have your Project-Barracuda 
    directory stored and run these commands:

    a. python manage.py shell (Python shell should start and you should see >>>)
       from GeoGuessr import load
       load.run()
    
    b. after the command finishes importing the GIS information, go to pgAdmin 4 and 
       run: select * from "GeoGuessr_worldborder"; and there should be a whole bunch of entries that were loaded into the table.
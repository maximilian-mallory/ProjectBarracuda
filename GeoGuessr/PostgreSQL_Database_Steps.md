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
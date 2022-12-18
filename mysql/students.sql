use db;

CREATE TABLE students(
    BIRTHDAY DATE NOT NULL,
    ID INT,
    NAME VARCHAR(50) NOT NULL,
    ROOM_ID INT NOT NULL PRIMARY KEY,
    SEX VARCHAR(5) NOT NULL,
    FOREIGN KEY (ROOM_ID) REFERENCES rooms (ID) ON DELETE SET NULL

);

CREATE TABLE rooms(
    ID INT NOT NULL PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL
);

-- INSERT INTO students(birthday, id, name, room, sex)
-- VALUES('2011-08-22T00:00:00.000000', 0, 'Peggy Ryan', 473, 'M')
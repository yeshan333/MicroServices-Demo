PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE apirelease(buildtime date,version varchar(30) primary key,links varchar2(30),methods varchar2(30));
INSERT INTO apirelease VALUES('2019-12-24 18:00:00','v1','api/v1/users','get,post,put,delete');
CREATE TABLE users(username vachar2(30),emailid varchar2(30),password varchar2(30),full_name varchar2(30),id integer primary key autoincrement);
INSERT INTO users VALUES('yeshan333','1329441308@qq.com','123456','yeshan',1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('users',2);
COMMIT;

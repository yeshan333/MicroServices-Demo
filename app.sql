PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE apirelease(buildtime date,version varchar(30) primary key,links varchar2(30),methods varchar2(30));
INSERT INTO apirelease VALUES('2019-12-24 18:00:00','v1','api/v1/users','get,post,put,delete');
INSERT INTO apirelease VALUES('2020-01-02 17:35','v2','api/v2/tweet','get,post,delete,put');
CREATE TABLE users(username vachar2(30),emailid varchar2(30),password varchar2(30),full_name varchar2(30),id integer primary key autoincrement);
INSERT INTO users VALUES('yeshan333','1329441308@qq.com','123456','yeshan',1);
CREATE TABLE tweets(id integer primary key autoincrement,username varchar2(30), body varchar2(30), tweet_time date);
INSERT INTO tweets VALUES(2,'yeshan333','Hello 2020!','2020-01-02 11:36:14');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('users',2);
INSERT INTO sqlite_sequence VALUES('tweets',2);
COMMIT;
                                                                                                                                               yeshan333|1329441308@qq.com|123456|yeshan|1
foo|1329441308@qq.cw|123kk|foo|2
maintainer|110@qq.comss|123456|maintainer|3
apirelease  tweets      users     
apirelease  users     

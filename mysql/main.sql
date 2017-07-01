-- 创建数据库
create database if not exists fdb char set utf8;

create user appUser@'localhost' identified by '123456';
grant all on fdb.* to appUser@'localhost';

create user appUser@'127.0.0.1' identified by '123456';
grant all on fdb.* to appUser@'127.0.0.1';

-- all other table are created by django.model

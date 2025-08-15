CREATE TABLE DEPT
(
   DEPTNO INT PRIMARY KEY, 
   DNAME VARCHAR(14), 
   LOC VARCHAR(13)
);


Insert into DEPT (DEPTNO,DNAME,LOC) values (10,'ACCOUNTING','NEW YORK');
Insert into DEPT (DEPTNO,DNAME,LOC) values (20,'RESEARCH','DALLAS');
Insert into DEPT (DEPTNO,DNAME,LOC) values (30,'SALES','CHICAGO');
Insert into DEPT (DEPTNO,DNAME,LOC) values (40,'OPERATIONS','BOSTON');
Insert into DEPT (DEPTNO,DNAME,LOC) values (50,'IT','HYDERABAD');
commit;
select * from dept;


# Assignment - Week5

## 要求三：SQL CRUD
* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
INSERT INTO member(name, username, password) VALUES('test', 'test', 'test');
INSERT INTO member(name, username, password) VALUES('Alice', 'test1', 'test1');
INSERT INTO member(name, username, password) VALUES('Ann', 'test2', 'test2');
INSERT INTO member(name, username, password) VALUES('Wendy', 'test3', 'test3');
INSERT INTO member(name, username, password) VALUES('Debby', 'test4', 'test4');
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-001.png)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
```
SELECT * FROM member;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-002.png)

* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
```
SELECT * FROM member order by time desc;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-003.png)

* 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
```
SELECT * FROM member order by time desc LIMIT 1, 3;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-004.png)

* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
```
SELECT * FROM member WHERE username='test'; 
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-005.png)

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
```
SELECT * FROM member WHERE username='test' and password='test';
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-006.png)

* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
```
UPDATE member SET name='test2' WHERE username='test';
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-007.png)
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/3-007-1.png)

## 要求四：SQL Aggregate Functions
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```
SELECT COUNT(*) FROM member;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/4-001.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```
SELECT SUM(follower_count) FROM member;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/4-002.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
```
SELECT AVG(follower_count) 'average_follower' FROM member;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/4-003.png)

## 要求五：SQL JOIN
* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。
```
SELECT * FROM member INNER JOIN message ON member.id=message.member_id;
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/5-001.png)
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/5-001-1.png)

* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者的姓名。
```
SELECT * FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/5-002.png)

* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
```
SELECT AVG(like_count) 'average_like' FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';
```
![image](https://raw.githubusercontent.com/Aliceeeee2023/WeHelp/main/Week5/Screenshot/5-003.png)


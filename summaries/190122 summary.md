# 20190122 summary

# Ⅰ. SQLite

### 1. 용어정리 & 명령어

#### (1) Scheme(스키마)

> 모델링. 자료의 구조형, 다른 형태의 자료가 들어와 구조가 깨지는 것을 방지 



#### (2) 실행순서

```bash
$sqlite3
```

```bash
$ sqlite3 파일명.확장자
# 확장자 의미 없음, 지금부터 해당파일에 데이터 저장
```



#### (3) SQlite 전용 명령어 

| 명령어                                                       | 설명                                        |
| ------------------------------------------------------------ | ------------------------------------------- |
| `.mode csv`                                                  | csv 모드                                    |
| `.mode column`                                               | 컬럼 모드                                   |
| `.headers on`                                                | 헤더(컬럼이름) 같이 출력                    |
| `.read <file.sql>`                                           | 해당 sql 스크립트 실행                      |
| `.import <file.name> <tabel_name>`<br />만약 데이터형이 다르더라도 해당줄만 오류뜨고 다른줄은  정상적으로 import된다. | 해당 파일의 데이터를 지정한 테이블에 import |
| `.schema`  또는 `.schema 파일명.확장자`                      | 스키마 전체 보기                            |
| `.table`                                                     | 가지고 있는 테이블 전부 다 보기             |
| `.nullvalue NULL`                                            | NULL이 진짜 NULL이 되는 것                  |

```sqlite
.read create_table.sql	
.read insert_record.sql
.mode csv
.import users.csv users
```



#### (4) SQlite 유의사항

* 한 행동 종료하려면 무조건 `;` (SQL 에서 사용되는 기본적인 명령어)
* 명령어는 무조건 대문자
* `.`으로 시작하는 명령어는 SQLite 전용 명령어 이기에 `;` 사용하지 않아도 된다. 



### 2. Table 조작관련



#### (1) Table 생성

```sqlite
CREATE TABLE <table_name> (
	<col> DATA_TYPE PRIMARY KEY AUTOINCREMENT,
    <col> DATA_TYPE NOT NULL,
    <col> DATA_TYPE,
    ...
);
```



#### (2) Table( + 레코드 모두) 삭제

```sqlite
DROP TABLE <table_name>;
```



#### (3) Table 이름 수정

```sqlite
ALTER TABLE <table_name>
RENAME TO <new_table_name>;
```

​				

#### (4) Table 컬럼 추가

```sqlite
ALTER TABLE table_name
ADD COLUMN new_col_name DATATYPE;
--디폴트값 설정
ADD COLUMN new_col_name DATATYPE DEFAULT default;


```



#### (5) Table 컬럼 조건 추가

```sqlite
CREATE TABLE users (
    id INTEGER PRIMARY KEY INCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    age INTEGER,
    country TEXT,
    phone TEXT,
    balance INTEGER NOT NULL);
```

```sqlite
INSERT INTO buses (busnumber)
VALUES (401);
```



### 3. Data 조작 관련



#### (1) Data 생성

```sqlite
INSERT INTO <tablename> (col1_name,col2_nmae, ...)
VALUES
(value1, value2, ...),
(value1, value2, ...);
```

```sqlite
INSERT INTO menus (id, menu1, menu2)
   ...> VALUES (1, 'pho', 'pork');
```



#### (2) Data 조회

##### 테이블에서 데이터 전체를 모든 col에 대해서 조회

```sqlite
SELECT * FROM table_name
```

##### 테이블에서 특정 컬럼만 조회

```sqlite
SELECT co11_name, col2_name FROM table_name
```

```sqlite
SELECT id FROM menus WHERE id=1;
SELECT menu1, menu2 FROM menus WHERE id=1;
SELECT *  FROM menus WHERE id=1;  
```

##### 특정조건으로 전체 컬럼 조회

```sqlite
SELECT * FROM table_name WHERE condition
```

##### Data 수정

```sqlite
UPDATE <table_name>
SET <col_1>=<new_val_1>, <col_2>=<new_val_2>, ...
WHERE [condition]; -- 보통 primary key (id) 로 선택
```

```sqlite
UPDATE timetable
   ...> SET test=0
   ...> WHERE id IN (1,2,3);
```

```sqlite
UPDATE timetable SET test=0;
```

##### Data 삭제

```sqlite
DELETE FROM <table_name>
WHERE [condtion]; -- 보통 primary key (id) 로 선택
```



### 4. Expression

#### 해당 컬럼의 갯수

```sqlite
SELECT COUNT(col) FROM table_name
```

#### 해당 컬럼의

```sqlite
--평균
SELECT AVG(col) FROM table_name;
--총합
SELECT SUM(col) FROM table_name;
--최소
SELECT MIN(col) FROM table_name;
--최대
SELECT MAX(col) FROM table_name;
```



### 5. 정렬(Order)

```sqlite
SELECT col_name FROM table_name
ORDER BY col1_name, col2_name ASC 또는 DESC;
```



### 6. 제한(Limit)

```sqlite
SELECT col_name FROM table_name
LIMIT number
```



### 7. 패턴(Pattern)

```sqlite
SELECT * FROM table_name
WHERE col_name LIKE 'pattern'
```

```sqlite
sqlite> UPDATE timetable
   ...> SET project=1
   ...> WHERE calendar LIKE "19%";
```

| 시작 | 예시    | 설명                                  |
| ---- | ------- | ------------------------------------- |
| `%`  | `2%`    | 2로 시작하는 값                       |
|      | `%2`    | 2로 끝나는 값<br /                    |
|      | `%2%`   | 2가 들어가는 값                       |
| `_`  | `_2`    | 두번째 글자가 2인 값                  |
|      | `1____` | 1로 시작하며 4자리                    |
|      | `_2%`   | 한글자 뒤에 2가 오고 뒤에 이어지는 값 |
|      | `2_%_%` | 2로 시작하는데 최소 3자리인 값        |



## Ⅱ. 기타

https://gist.github.com/sagsn0202/a4f6608521f48261ff81e63057fc8441

https://poiemaweb.com/

https://www.w3schools.com/

https://daneden.github.io/animate.css/
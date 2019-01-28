# 20190123 16homework

## 1. 다음과 같은 스키마를 가지는 DB 테이블 friends를 생성

| id(INTEGER) | name(TEXT) | location(TEXT) |
| ----------- | ---------- | -------------- |
|             |            |                |

```sqlite
CREATE TABLE friends (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, location TEXT);
```



## 2. 해당 테이블에 다음 데이터를 입력

| id(INTEGER) | name(TEXT) | location(TEXT) |
| ----------- | ---------- | -------------- |
| 1           | Justin     | Seoul          |
| 2           | SImon      | New York       |
| 3           | Chang      | Las Vegas      |
| 4           | John       | Sydney         |

```sqlite
INSERT INTO friends (name, location) VALUES ("Justin", "Seoul"),("Simon","New York"),("Chang", "Las Vegas"), ("John", "Sydney");
```



## 3. 스키마를 다음과 같이 변경

| id(INTEGER) | name(TEXT) | location(TEXT) | married(INTEGER) |
| ----------- | ---------- | -------------- | ---------------- |
|             |            |                |                  |

```sqlite
ALTER TABLE friends ADD COLUMN married INTEGER;
```



## 4. 데이터를 다음과 같이 추가한다.

| id(INTEGER) | name(TEXT) | location(TEXT) | married(INTEGER) |
| ----------- | ---------- | -------------- | ---------------- |
| 1           | Justin     | LA             | 1                |
| 2           | SImon      | New York       | 0                |
| 3           | Chang      | Las Vegas      | 0                |
| 4           | John       | Sydney         | 1                |

```sqlite
UPDATE friends SET location="LA" WHERE id=1;
UPDATE friends SET married=1 WHERE id in (1,4);
UPDATE friends SET married=0 WHERE id in (2,3);
```



## 5. married가 0인 데이터를 모두 삭제한다.

```sqlite
DELETE FROM friends WHERE married=0;
```



## 6. 테이블을 삭제한다.

```sqlite
DROP TABLE friends;
```


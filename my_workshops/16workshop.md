# 190123 16workshop

## 1. 저번 워크샵의 테이블을 수정하여, 다음과 같이 컬럼을 투가하고 데이터를 삽입하라

| id(INTEGER) | name(TEXT) | debut(INTEGER) | members(INTEGER) |
| ----------- | ---------- | -------------- | ---------------- |
| 1           | Queen      | 1973           | 4                |
| 2           | Coldplay   | 1998           | 5                |
| 3           | MCR        | 2001           | 9                |

```sqlite
ALTER TABLE bands
ADD COLUMN members INTEGER;

UPDATE bands
SET members=4 WHERE id=1;

UPDATE bands
SET members=5 WHERE id=2;

UPDATE bands
SET members=9 WHERE id=3;
```



## 2. id가 3인 레코드의 members를 5로 수정하라

```sqlite
UPDATE bands
SET members=5 WHERE id=3;
```



## 3. id가 2인 레코드를 삭제하라

```sqlite
DELETE FROM bands WHERE id=2;
```


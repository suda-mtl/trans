基础语句

### 单表

```sql
SELECT column1, column2, ...
FROM table_name;
```
SELECT DISTINCT 语句用于返回唯一不同的值。
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

WHERE 子句用于提取那些满足指定条件的记录。
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;

SELECT * FROM Websites WHERE country='CN';
SELECT * FROM Websites WHERE id=1;
```
运算符
BETWEEN	在某个范围内
LIKE	搜索某种模式
IN	指定针对某个列的多个可能值

AND & OR 运算符用于基于一个以上的条件对记录进行过滤。
```sql
SELECT * FROM Websites
WHERE country='CN'
AND alexa > 50;

SELECT * FROM Websites
WHERE country='USA'
OR country='CN';

SELECT * FROM Websites
WHERE alexa > 15
AND (country='CN' OR country='USA');

```
ORDER BY 关键字用于对结果集按照一个列或者多个列进行排序。默认升序
LIMIT限制返回的结果数量
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;

SELECT * FROM Websites
ORDER BY country,alexa;

SELECT column1, column2, ...
FROM table_name
LIMIT number;

```
多表
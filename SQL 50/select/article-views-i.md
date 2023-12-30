## 1148. Article Views I

### Table

**Views**

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
```

- There is no primary key for this table, meaning the table may have duplicate rows.
- Each row of this table indicates that some viewer viewed an article (written by some author) on a certain date. 
- Note that equal `author_id` and `viewer_id` indicate the same person.

### Question

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.

### Example 1

**Input:**
```
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
```

**Output:**
```
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
```

### SQL Solution

```sql
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
```

Notice that we can't use `id` in line 2 (`WHERE author_id = viewer_id`) because `id` is not a column in the table. We can only use the column names in the table.

However, we can use `id` in line 5 (`ORDER BY id`) because `id` is a column in the result table

Also note that we can easily return it in descending order by changing line 5 (`ORDER BY id`):

```sql
ORDER BY id DESC
```
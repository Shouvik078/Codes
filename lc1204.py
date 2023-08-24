# leetcode 1204 SQL 


# SELECT person_name
# FROM (
#         SELECT person_name,
#         SUM(weight) OVER(ORDER BY turn) AS total_weight
#         FROM Queue
# ) AS sub_query
# WHERE total_weight<=1000
# ORDER BY total_weight DESC
# LIMIT 1
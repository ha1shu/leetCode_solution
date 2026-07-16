with cte as (
    SELECT requester_id AS id
    FROM RequestAccepted

    UNION ALL

    SELECT accepter_id AS id
    FROM RequestAccepted
)
select id,count(*) as num
from cte
group by id
order by num desc
limit 1

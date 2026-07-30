# Write your MySQL query statement below
SELECT 
    t.request_at as 'Day',
    ROUND(
        SUM(
            CASE
                WHEN status Like 'cancelled%' THEN 1
                ELSE 0
                END) / COUNT(*)
        ,2) as 'Cancellation Rate'
From Trips t
Join Users c
On t.client_id = c.users_id
JOIN Users d
On t.driver_id = d.users_id
where c.banned ='No'
AND d.banned = 'No'
AND request_at between "2013-10-01" and "2013-10-03"
Group By request_at
order by t.request_at
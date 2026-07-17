# Write your MySQL query statem ent bel
select ROUND(SUM(tiv_2016),2) as tiv_2016
from Insurance
where tiv_2015 In (
    select tiv_2015
    from Insurance
    group by tiv_2015
    Having count(*)>1
)
AND (lat, lon) IN (
    select lat,lon
    from Insurance 
    group by lat, lon
    Having COUNT(*) = 1
 )
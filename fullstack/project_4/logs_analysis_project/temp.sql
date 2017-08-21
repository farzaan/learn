select date(time) ,
round( CAST(float8 (100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / count(status)) as numeric), 2)
 as p
from log
group by date(time);

select date(time),
round(CAST(float8(100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / count(status)) as n
umeric), 2)
 as s
from log
group by date(time) order by s desc limit 1


















news=> select date(time) , SUM(CAST((status = '200 OK')  AS INT)) AS ok, SUM(CAST((status = '404 NOT FOUND')  AS INT))
AS not,
100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / SUM(CAST((status = '200 OK')  AS INT))
 as p
from log
group by date(time);




select date(time) , count(status) AS ok, SUM(CAST((status = '404 NOT FOUND')  AS INT))AS not,
round( CAST(float8 (100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / ok) as numeric), 2) as p
from log
group by date(time);

 round( CAST(float8 (100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / SUM(CAST((status = '200 OK')  AS INT))) as numeric), 2)
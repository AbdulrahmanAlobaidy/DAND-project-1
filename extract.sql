
-- Choose city

SELECT *
FROM city_list
WHERE country = 'Iraq'

-- View City Information

SELECT *
FROM city_data
WHERE city = 'Irbil'


-- Extract and join global and city information


WITH c as (
  SELECT *
  FROM city_data
  WHERE city = 'Irbil' AND avg_temp IS NOT NULL
)



SELECT g.year, g.avg_temp Global_AVG_Temp, c.avg_temp local_AVG_TEMP
FROM global_data g
JOIN c
ON c.year = g.year



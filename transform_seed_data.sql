-- ToDo

-- Clean up the names of the plants

-- Clean up the 

-- Clean up Colors

-- Clean up the spacing attributes

-- hack to fix search
UPDATE plants SET fruit_color = '' WHERE fruit_color IS NULL;
UPDATE plants SET category = '' WHERE category IS NULL;
UPDATE plants SET sun = '' WHERE sun IS NULL;
UPDATE plants SET life_cycle = '' WHERE life_cycle IS NULL;


SELECT fruit_color, count(*) AS counts from plants group by 1 order by 2 desc;
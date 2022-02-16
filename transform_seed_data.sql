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


SELECT DISTINCT name FROM plants LIMIT 10;
select distinct plant_id, name, fruit_color, maturity from plants WHERE LOWER(name) like '%zucc%' and fruit_color like '%%';
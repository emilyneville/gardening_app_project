TRUNCATE TABLE user_gantts;

INSERT INTO user_gantts(user_id, gantt_name, created_date, last_modified_date)
VALUES (1, 'emilys test gantt', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO user_gantts(user_id, gantt_name, created_date, last_modified_date)
VALUES (1, 'the other test', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

TRUNCATE TABLE user_gantt_plants

INSERT INTO user_gantt_plants(plant_id, user_gantt_id, display_name, start_date, end_date,created_date, last_modified_date) 
VALUES (16, 1, 'sweet watermelon', DATE'2022-03-17', DATE'2022-07-20', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO user_gantt_plants(plant_id, user_gantt_id, display_name, start_date, end_date,created_date, last_modified_date) 
VALUES (15, 1, 'cabbage', DATE'2022-04-17', DATE'2022-06-20', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


INSERT INTO user_gantt_plants(plant_id, user_gantt_id, display_name, start_date, end_date,created_date, last_modified_date) 
VALUES (5, 1, 'bean', DATE'2022-04-01', DATE'2022-05-31', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO user_gantt_plants(plant_id, user_gantt_id, display_name, start_date, end_date,created_date, last_modified_date) 
VALUES (24, 1, 'leek', DATE'2022-05-10', DATE'2022-08-15', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO user_gantt_plants(plant_id, user_gantt_id, display_name, start_date, end_date,created_date, last_modified_date) 
VALUES (86, 1, 'zucc', DATE'2022-07-04', DATE'2022-09-20', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);



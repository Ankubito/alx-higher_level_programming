-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER TABLE first_table CONVERT TO CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

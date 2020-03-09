-- creates Postgres for the project

CREATE DATABASE IF NOT EXISTS Projects;
CREATE USER IF NOT EXISTS 'postgres_admin'@'localhost' IDENTIFIED BY 'postgres_admin_pwd';
GRANT ALL PRIVILEGES ON 'Projects'.* TO 'postgres_admin'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'postgres_admin'@'localhost';
FLUSH PRIVILEGES;

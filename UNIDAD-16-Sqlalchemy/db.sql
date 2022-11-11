CREATE DATABASE test;

CREATE TABLE customer (
id SERIAL PRIMARY KEY,
name TEXT,
age INTEGER,
email CHARACTER(255),
address CHARACTER(400),
zip_code CHARACTER(20)
);

INSERT INTO customer(name,age,email,address,zip_code)
VALUES
('Paul',23,'paul@gmail.com','address from paul','2321LL'),
('Felipe',32,'felipegarcia@gmail.com','address from felipe','3413MS'),
('Teddy',90,'teddy@gmail.com','address from teddy','3423PO'),
('Mark',17,'mark@gmail.com','address from mark','9423MA'),
('David',35,'david@gmail.com','address from david','2341DA'),
('Allen',56,'allen@gmail.com','address from allen','3423PO'),
('James',56,'james@gmail.com','address from james','3423PO');
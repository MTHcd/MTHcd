CREATE DATABASE LibraryDB;

-- necessary step to insert tables into pre-selected database
USE DATABASE LibraryDB;

-- table for authors
CREATE TABLE authors (author_id INT AUTO_INCREMENT PRIMARY KEY, author_name VARCHAR(20) NOT NULL, birthdate DATE NOT NULL);

-- table for books
CREATE TABLE books (book_id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(20) NOT NULL, genre VARCHAR(20) NOT NULL, published_year INT NOT NULL, author_id INT NOT NULL,
FOREIGN KEY (author_id) REFERENCES authors(author_id));

-- table for book loans
CREATE TABLE book_loans (loan_id INT AUTO_INCREMENT PRIMARY KEY, book_id INT NOT NULL, FOREIGN KEY (book_id) REFERENCES books(book_id),
  borrower_name VARCHAR(20) NOT NULL, loan_date DATE NOT NULL, return_date DATE NOT NULL);

-- inserting data

INSERT INTO authors (author_name, birthdate) VALUES ('Roland', 02/05/1968), ('Bob', 05/14/1973), ('Célia', 07/12/2023);
INSERT INTO books (title, genre, published_year, author_id) VALUES ('Complex Analysis', 'Mathematics', '2020', 'Roland'), ('Real Analysis', 'Mathematics', '2018', 'Roland'),
('Histoire de XXXX', 'Autobiography', '19xx', 'Bob'), ('Histoire de la Grèce Antique', 'Histoire', '2004', 'Célia');
INSERT INTO book_loans (book_id, borrower_name, loan_date, return_date) VALUES ('
-- take the example

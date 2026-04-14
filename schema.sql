CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE shifts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    salary INTEGER,
    participants INTEGER,
    employee_id INTEGER REFERENCES employees
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE shift_categories (
    shift_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (shift_id, category_id),
    FOREIGN KEY (shift_id) REFERENCES shifts(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
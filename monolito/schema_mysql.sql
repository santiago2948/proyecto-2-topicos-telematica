CREATE DATABASE IF NOT EXISTS bookstore CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE bookstore;

-- Tabla de usuarios
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(150) NOT NULL
);

-- Tabla de libros
CREATE TABLE book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price FLOAT NOT NULL,
    stock INT NOT NULL,
    seller_id INT NOT NULL,
    FOREIGN KEY (seller_id) REFERENCES user(id) ON DELETE CASCADE
);

-- Tabla de compras
CREATE TABLE purchase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    total_price FLOAT NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES book(id) ON DELETE CASCADE
);

-- Tabla de pagos
CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_id INT NOT NULL,
    amount FLOAT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    payment_status VARCHAR(50) NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES purchase(id) ON DELETE CASCADE
);

-- Tabla de proveedores de entrega
CREATE TABLE delivery_provider (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    coverage_area VARCHAR(150) NOT NULL,
    cost FLOAT NOT NULL
);

-- Tabla de asignaciones de entrega
CREATE TABLE delivery_assignment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_id INT NOT NULL,
    provider_id INT NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES purchase(id) ON DELETE CASCADE,
    FOREIGN KEY (provider_id) REFERENCES delivery_provider(id) ON DELETE CASCADE
);

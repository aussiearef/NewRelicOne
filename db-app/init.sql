CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price_per_unit DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

DELETE FROM customers;
DELETE FROM products;
DELETE FROM orders;
DELETE FROM order_items;

INSERT INTO customers (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Bob Johnson', 'bob.johnson@example.com');

INSERT INTO products (name, description, price, stock_quantity) VALUES
('Achromatic Refractor Telescope', '90mm aperture entry-level refractor telescope with alt-azimuth mount, ideal for lunar and planetary viewing.', 349.00, 25),
('Schmidt-Cassegrain Telescope', '8-inch computerized GoTo telescope with StarBright XLT coatings for deep-sky astrophotography.', 2199.00, 8),
('Plossl 25mm Eyepiece', 'Standard 1.25-inch multi-coated eyepiece offering a wide 52-degree apparent field of view.', 65.50, 50),
('Light Pollution Filter', '1.25-inch broadband filter designed to improve contrast of nebulae in urban stargazing conditions.', 120.00, 30),
('Equatorial Tracking Mount', 'Heavy-duty German equatorial mount with computerized tracking for precise long-exposure astrophotography.', 1450.00, 12);

INSERT INTO orders (customer_id, status) VALUES
(1, 'Shipped'),
(2, 'Pending'),
(1, 'Processing');

INSERT INTO order_items (order_id, product_id, quantity, price_per_unit) VALUES
(1, 1, 1, 349.00),
(1, 3, 1, 65.50),
(2, 2, 1, 2199.00),
(3, 4, 2, 120.00);
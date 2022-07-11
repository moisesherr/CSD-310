# Team Delta
# Rufino Tzunun
# Christopher Clausen
# Moises Herrera
# Module 10.2 Wilson Financial

import mysql.connector
config ={
	"user": "root",
	"password": "P4L9i4Ci",
	"host": "127.0.0.1",
	"database": "w_financial",
	"raise_on_warnings": False
}

# Create Employee Table
db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SET FOREIGN_KEY_CHECKS=0")
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("CREATE TABLE Employee (emp_id INT NOT NULL AUTO_INCREMENT, emp_name VARCHAR(100) NOT NULL, emp_pos VARCHAR(100) NOT NULL, PRIMARY KEY(emp_id))")

#Create Client Table
cursor.execute("DROP TABLE IF EXISTS Client")
cursor.execute("CREATE TABLE Client (cl_id INT NOT NULL AUTO_INCREMENT, cl_name VARCHAR(100) NOT NULL, cl_address VARCHAR(200) NOT NULL, cl_phone VARCHAR(50) NOT NULL, cl_email VARCHAR(100) NOT NULL, cl_date_added DATETIME NOT NULL, emp_id INT NOT NULL, PRIMARY KEY(cl_id), CONSTRAINT fk_employee FOREIGN KEY(emp_id) REFERENCES employee(emp_id))")

#Create Stock Table
cursor.execute("DROP TABLE IF EXISTS Stock")
cursor.execute("CREATE TABLE Stock (stock_id INT NOT NULL AUTO_INCREMENT, stock_symbol VARCHAR(100) NOT NULL, stock_current_price DECIMAL(10,2) NOT NULL, PRIMARY KEY(stock_id))")
cursor.execute("SET FOREIGN_KEY_CHECKS=1")

#Create Transaction Table
cursor.execute("DROP TABLE IF EXISTS Transaction")
cursor.execute("CREATE TABLE Transaction (order_id INT NOT NULL AUTO_INCREMENT, cl_id INT NOT NULL, stock_id INT NOT NULL, order_date DATETIME NOT NULL, order_shares_traded INT NOT NULL, order_unit_price DECIMAL(10,2) NOT NULL, PRIMARY KEY(order_id), CONSTRAINT fk_client FOREIGN KEY(cl_id) REFERENCES client(cl_id), CONSTRAINT fk_stock FOREIGN KEY(stock_id) REFERENCES stock(stock_id))")

# Insert Employees
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('John Smith','Sr. Financial Advisor')")
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('Jack Cats','Lawyer')")
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('Rick Scott','Broker')")
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('Matt Damon','Chief Advisor')")
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('Mike Jones','Judge')")
cursor.execute("INSERT INTO Employee (emp_name, emp_pos) VALUES ('Miguel Sanchez','Human Resources')")

# Insert Clients
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Robert Jones','291 South Street, Orlando, FL', '407-555-0123', 'rob.jones@gmail.com', NOW(), 1)")
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Nick Jonas','2 North Street, Davenport, FL', '407-555-5555', 'nick.jonas@gmail.com', NOW(), 1)")
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Sam Hikes','13 West Street, Miami, FL', '407-555-9999', 'samhikey@gmail.com', NOW(), 1)")
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Dan Williams','101 Cool Street, Tampa, FL', '407-555-3999', 'verycool@gmail.com', NOW(), 1)")
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Iam Sam','100 NS Street, Jacksonville, FL', '407-555-1111', 'samiam@gmail.com', NOW(), 1)")
cursor.execute("INSERT INTO Client (cl_name, cl_address, cl_phone, cl_email, cl_date_added, emp_id) VALUES ('Juan Jose','12 NW, Kissimmee, FL', '239-555-0123', 'jimbo@gmail.com', NOW(), 1)")


# Insert Stocks
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('DIS',95.86)")
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('DOW',45)")
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('NASDAQ',13.96)")
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('S&P 500',3.24)")
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('WMT',125.40)")
cursor.execute("INSERT INTO Stock (stock_symbol, stock_current_price) VALUES ('AMD',79.35)")

# Insert Transactions
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (1,1,'2022-07-01 12:00:00', 50, 92.70)")
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (2,2,'2022-02-03 12:00:00', 40, 85.67)")
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (3,3,'2022-07-01 12:00:00', 34, 23.02)")
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (4,4,'2022-07-01 12:00:00', 63, 34.92)")
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (5,5,'2022-07-01 12:00:00', 40, 85.39)")
cursor.execute("INSERT INTO Transaction (cl_id, stock_id, order_date, order_shares_traded, order_unit_price) VALUES (6,6,'2022-07-08 15:59:00', -50, 95.86)")

db.commit()

# Select Records

cursor.execute("SELECT emp_id, emp_name, emp_pos FROM employee")
employees = cursor.fetchall()
print()
print("-- DISPLAYING EMPLOYEE RECORDS --")

for employee in employees:
	print("Employee ID: {}".format(employee[0]))
	print("Employee Name: {}".format(employee[1]))
	print("Position: {}".format(employee[2]))
	print()

cursor.execute("SELECT cl_name, cl_address, cl_phone, cl_date_added FROM client")
clients = cursor.fetchall()
print()
print("-- DISPLAYING EMPLOYEE CLIENT --")

for client in clients:
	print("Client Name: {}".format(client[0]))
	print("Client Address: {}".format(client[1]))
	print("Client Phone: {}".format(client[2]))
	print("Client Date Added: {}".format(client[3]))
	print()

cursor.execute("SELECT stock_symbol, stock_current_price FROM stock")
stocks = cursor.fetchall()
print()
print("-- DISPLAYING STOCKS --")

for stock in stocks:
	print("Stock Symbol: {}".format(stock[0]))
	print("Stock current price: {}".format(stock[1]))
	print()

cursor.execute("SELECT cl_id, stock_id, order_date, order_shares_traded, order_unit_price FROM transaction ")
transactions = cursor.fetchall()
print()
print("-- DISPLAYING TRANSACTION --")

for transaction in transactions:
	print("Client ID: {}".format(transaction[0]))
	print("Stock ID: {}".format(transaction[1]))
	print("Order Date: {}".format(transaction[2]))
	print("Order shares traded: {}".format(transaction[3]))
	print("Order unit price: {}".format(transaction[4]))
	print()


---
title: Database Fundamentals - Part 2
---

# Database Fundamentals - Part 2

**Table of Contents**

-   Data Manipulation and Modification
-   Database Design and Normalization
-   Security and Best Practices
-   Installing Ruby

## Data Manipulation and Modification

Data Manipulation and Modification is the process of adding, updating, and deleting data from a database. This is done using the following SQL statements:

-   INSERT INTO
-   UPDATE
-   DELETE

Up until this point we've been using the SELECT statement to retrieve data from a database and the INSERT INTO statement to add data to a database. Now we'll learn how to update and delete data from a database.

> **Practice with the Codelabs Learning Assistant**
>
> Try answering this question, then ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):
> _"What is the difference between the INSERT, UPDATE, and DELETE SQL statements? Can you give me a simple example of each?"_

### INSERT INTO statement

The INSERT INTO statement is used to add data to a database. The syntax for the INSERT INTO statement is as follows:

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

The INSERT INTO statement inserts a new row into the table. The columns that are not specified in the INSERT INTO statement will be filled with the default value or NULL if no default value is specified.

Let's take a look at an example. We'll use the following table to demonstrate the INSERT INTO statement:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER
);

INSERT INTO students (first_name, last_name, grade)
VALUES
('John', 'Doe', 90),
('Jane', 'Doe', 95),
('Sally', 'Smith', 100);

SELECT * FROM students;
```

```
1|John|Doe|90
2|Jane|Doe|95
3|Sally|Smith|100
```

### UPDATE statement

The UPDATE statement is used to update existing data in a database. The syntax for the UPDATE statement is as follows:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

The UPDATE statement updates existing rows in the table. The WHERE clause is used to specify which rows to update. If the WHERE clause is omitted, all rows in the table will be updated.

Let's take a look at an example. We'll use the following table to demonstrate the UPDATE statement:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER
);

INSERT INTO students (first_name, last_name, grade)
VALUES
('John', 'Doe', 90),
('Jane', 'Doe', 95),
('Sally', 'Smith', 100);

UPDATE students
SET grade = 100
WHERE first_name = 'John';

SELECT * FROM students;
```

The expected outcome is:

```
1|John|Doe|100
2|Jane|Doe|95
3|Sally|Smith|100
```

### DELETE statement

The DELETE statement is used to delete existing data from a database. The syntax for the DELETE statement is as follows:

```sql
DELETE FROM table_name
WHERE condition;
```

The DELETE statement deletes existing rows from the table. The WHERE clause is used to specify which rows to delete. If the WHERE clause is omitted, all rows in the table will be deleted.

Let's take a look at an example. We'll use the following table to demonstrate the DELETE statement:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER
);

INSERT INTO students (first_name, last_name, grade)
VALUES
('John', 'Doe', 90),
('Jane', 'Doe', 95),
('Sally', 'Smith', 100);

DELETE FROM students
WHERE first_name = 'John';

SELECT * FROM students;
```

The expected outcome is:

```
id          first_name  last_name   grade
----------  ----------  ----------  ----------
2           Jane        Doe         95
3           Sally       Smith       100
```

#### Practice Problem

> **Need a step-by-step walkthrough for this SQL practice?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):
> _"Can you show me how to create, update, and delete users in SQL for this practice problem? What mistakes should I watch out for?"_

Create a table called `users` with the following columns:

-   id
-   first_name
-   last_name
-   email
-   password

Insert 3 users into the table.
Here are the three users

| first_name | last_name | email                | password |
| ---------- | --------- | -------------------- | -------- |
| John       | Doe       | johndoe@email.com    | password |
| Jane       | Doe       | janedoe@email.com    | password |
| Sally      | Smith     | sallysmith@email.com | password |

Update the email of the user with the id of 1 to `updatedemail@email.com`

Delete the user with the id of 2.

Print all the users in the table.

Result should be

```
1|John|Doe|updatedemail@email.com|password
3|Sally|Smith|sallysmith@email.com|password
```

<details>

<summary>Solution</summary>

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password TEXT
);

INSERT INTO users (first_name, last_name, email, password)
VALUES ('John', 'Doe', 'johndoe@email.com', 'password');
INSERT INTO users (first_name, last_name, email, password)
VALUES ('Jane', 'Doe', 'janedoe@email.com', 'password');
INSERT INTO users (first_name, last_name, email, password)
VALUES ('Sally', 'Smith', 'sallysmith@email.com', 'password');

UPDATE users
SET email = 'updatedemail@email.com'
WHERE id = 1;

DELETE FROM users
WHERE id = 2;

SELECT * FROM users;
```

</details>

## Database Design and Normalization

Database design is the process of designing a database schema. A database schema is a collection of tables that are related to each other and this is also referred to as a relational database.

Normalization on the other hand is the process of organizing data in a database. The goal of normalization is to reduce data redundancy and improve data integrity. This is important because it helps to ensure that the data in the database is accurate and consistent.

> **Practice with the Codelabs Learning Assistant**
>
> Try answering this question, then ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):
> _"What is a database schema, and why is normalization important? Can you give a simple example of normalization?"_

### Database schema design

There are different ways to design a database schema. The most common way is to use a relational database. I might've mentioned this a hundred times but,

a relational database is a collection of tables that are related to each other. Each table represents an entity and each row in the table represents an instance of that entity. Each entity has attributes that describe the entity. The attributes are represented by columns in the table. Each attribute has a data type and a default value. The data type specifies what kind of data can be stored in the attribute and the default value specifies what value should be used if no value is specified.

<img src="https://i.stack.imgur.com/ixCuF.png" />

The main purpose of a database schema is to define the structure of the database. It defines the tables, columns, data types, and relationships between the tables. It also defines the constraints that are applied to the data in the database. The constraints are used to ensure that the data in the database is accurate and consistent.

When it comes to designing a database schema, there are a few things that you need to consider:

-   What are the entities in the database?
-   What are the attributes of each entity?
-   What are the relationships between the entities?

### Cardinality

Relationships, the main big purpose to a relational database, are used to connect the tables in the database.

This is called cardinality. Cardinality is the number of instances of one entity that can be related to one instance of another entity. An entity is a thing or object that can be identified by its attributes. An attribute is a characteristic of an entity. For example, a customer is an entity and a customer has attributes such as name, address, phone number, and email address.

A relationship is a connection between two entities. For example a customer can have multiple orders. This is a relationship between the customer and order entities. The relationship is represented by a line connecting the customer and order entities, with a single crow's foot on the order side of the line.

Relationships can be represented by the following symbols:

-   One to one (1:1): Each entity in the relationship will have a single related entity.
    -   Example: Each person has a unique passport number. Each passport number is assigned to one and only one person.
-   One to zero or one (1:0..1): An entity on one side of the relationship can have zero or one related entity on the other side.
    -   Example: A user may have zero or one profile pictures in an application. Some users may choose not to upload a profile picture, while others have exactly one.
-   One to many (1:N): An entity on one side can have many related entities on the other side.
    -   Example: A mother can have multiple children. Each child has one mother, but a mother can have several children.
-   One to many (1:1..N): An entity on one side will have at least one related entity on the other side, and could have many.
    -   Example: A book has at least one author, but it can have several authors. However, each book is written by at least one author (none without an author).
-   One to zero to many (1:0..N): An entity on one side may have zero, one, or many related entities on the other side.
    -   Example: A teacher can teach zero (if they are currently not assigned to any class), one, or several classes.
-   Many to many (N:N): Entities on both sides of the relationship can have many related entities on the other side.
    -   Example: Students and classes have a many-to-many relationship. A student can enroll in multiple classes, and each class can have multiple students enrolled.
-   Many to many (1..N:1..N): Each entity on both sides will have at least one related entity on the other side, and could have many.
    -   Example: This is similar to the regular many-to-many relationship but ensures that neither side can have zero occurrences. An example would be a business partnership where each business must have at least one partner, and each partner must be engaged with at least one business.
-   Many to many (0..N:0..N): Entities on both sides may have zero, one, or many related entities on the other side.
    -   Example: Social media users and groups form a many-to-many relationship where users can join many groups, and each group can have many users. However, it's also possible that a user belongs to no group, or a group currently has no users.

<img src="https://www.softwareideas.net/i/DirectImage/1859/crow-s-foot-notation" />

Above is a crow's foot graphical representation of entities and their relationships to each other. It is used to model the structure of a database. The crow's foot notation is used to indicate the cardinality of a relationship. The lines coming out of the entities indicate the number of instances that can be related to one instance of the other entity.

This diagram indicates the following:

-   **1:1** - a line connecting A and B with a single crow's foot on the B side of the line. This means that one instance of A can be related to one instance of B.
-   _1:0..1_ - One and only one instance of A can be related to zero or one instance of B.
-   _1:N_ - One instance of A can be related to zero or more instances of B.
-   _1:1..N_ - One and only one instance of A can be related to one or more instances of B.
-   _M:N_ - Zero or more instances of A can be related to zero or more instances of B.
-   _1..M:1..N_ - One or more instances of A can be related to one or more instances of B.

### Practice Problem

Let's take a moment to develop relationships between schools and students.

-   What are the entities in the database?
-   What are the attributes of each entity?
-   What are the relationships between the entities?

<details>

<summary>Solution</summary>

-   What are the entities in the database?

    -   Schools
    -   Students

-   What are the attributes of each entity?

    -   Schools
        -   id
        -   name
        -   address
        -   phone_number
        -   email
        -   website
        -   number_of_students
    -   Students
        -   id
        -   first_name
        -   last_name
        -   grade
        -   school_id

-   What are the cardinalities of the relationships?
    -   Schools to Students: (1:N)
    -   Students to Schools: (N:1)

</details>

### Primary and foreign keys

In order to create these relationships, we need to add foreign keys to the tables. A foreign key is a column that references a column in another table. It is used to establish a relationship between two tables. The foreign key is used to ensure that the data in the column is valid. It is also used to enforce referential integrity.

Let's go ahead and demonstrate this.

```sql
CREATE TABLE schools (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  phone_number TEXT,
  website TEXT,
  number_of_students INTEGER
);

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  school_id INTEGER,
  FOREIGN KEY (school_id) REFERENCES schools(id)
);

INSERT INTO schools (name, address, phone_number, website, number_of_students)
VALUES ('School 1', '123 Main St', '123-456-7890', 'school1.com', 100);
INSERT INTO schools (name, address, phone_number, website, number_of_students)
VALUES ('School 2', '456 Main St', '123-456-7890', 'school2.com', 200);

INSERT INTO students (first_name, last_name, grade, school_id)
VALUES ('John', 'Doe', 90, 1);
INSERT INTO students (first_name, last_name, grade, school_id)
VALUES ('Jane', 'Doe', 95, 1);
INSERT INTO students (first_name, last_name, grade, school_id)
VALUES ('Sally', 'Smith', 100, 2);

SELECT * FROM schools;
SELECT * FROM students;
```

The expected outcome is:

```
id          name      address     phone_number  website     number_of_students
----------  --------  ----------  ------------  ----------  ------------------
1           School 1  123 Main St  123-456-7890  school1.com  100
2           School 2  456 Main St  123-456-7890  school2.com  200

id          first_name  last_name   grade       school_id
----------  ----------  ----------  ----------  ----------
1           John        Doe         90          1
2           Jane        Doe         95          1
3           Sally       Smith       100         2
```

To make this more useful let's use our cardinality to make a query.

```sql
SELECT * FROM students
WHERE school_id = 1;
```

This will return all the students that go to school 1.

```
id          first_name  last_name   grade       school_id
----------  ----------  ----------  ----------  ----------
1           John        Doe         90          1
2           Jane        Doe         95          1
```

What relationship is this again? It is a one to many relationship where one school can have many students.

This is powerful because we can now query the database to get all the students that go to a specific school. You can almost relate this to many types of data we encounter in our day to day life. It's sort of like a big spreadsheet where we can query the data to get the information we need.

Let's demonstrate a many to many relationship.

```sql
CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  price REAL
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items (
  id INTEGER PRIMARY KEY,
  order_id INTEGER,
  product_id INTEGER,
  FOREIGN KEY (order_id) REFERENCES orders(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO products (name, price)
VALUES ('Product 1', 10.00);
INSERT INTO products (name, price)
VALUES ('Product 2', 20.00);
INSERT INTO products (name, price)
VALUES ('Product 3', 30.00);

INSERT INTO orders (customer_id)
VALUES (1);
INSERT INTO orders (customer_id)
VALUES (2);

INSERT INTO order_items (order_id, product_id)
VALUES (1, 1);
INSERT INTO order_items (order_id, product_id)
VALUES (1, 2);

INSERT INTO order_items (order_id, product_id)
VALUES (2, 2);
INSERT INTO order_items (order_id, product_id)
VALUES (2, 3);

SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM order_items;
```

Let's make this a little more useful and query the database to get all the products that are in an order.

```sql
SELECT * FROM products
WHERE id IN (
  SELECT product_id FROM order_items
  WHERE order_id = 1
);
```

Here we are using a subquery to get all the products that are in order 1.

```
id          name      price
----------  --------  ----------
1           Product 1  10.0
2           Product 2  20.0
```

This is a many to many relationship because one product can be in many orders and one order can have many products.

Again, this is powerful because we can now query the database to get all the products that are in an order.

### Normalization

Now that we've encountered relationships, let's talk about normalization.

Normalization is the process of organizing data in a database. The goal of normalization is to reduce data redundancy and improve data integrity.

There are different levels of normalization. The most common levels are:

-   First normal form (1NF)
-   Second normal form (2NF)
-   Third normal form (3NF)
-   Boyce-Codd normal form (BCNF)
-   Fourth normal form (4NF)
-   Fifth normal form (5NF)
-   Domain/key normal form (DKNF)

The first three levels are the most common levels of normalization. The other levels are less common and are used in special cases.

Let's take a look at each level of normalization and see how it can be applied to a database schema.

#### First normal form (1NF)

The first normal form (1NF) is the most basic level of normalization. It is used to ensure that the data in the database is atomic. Atomic means that each attribute in a table contains only one value. It also means that each row in a table contains only one instance of an entity. Do we want our database to be atomic? Yes, we do.

Here's an example of a non-atomic table:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  address TEXT
);
```

The reason why this table is not atomic is because the address attribute contains multiple values. It contains or represents different values such as the street address, city, state, and zip code. This is not atomic because each attribute should contain only one value. The problem with this is that it makes it difficult to query the database. For example, if we want to get all the students that live in a certain city, we would have to query the database for each city. This is not efficient because it requires multiple queries to the database. It also makes it difficult to update the database because we would have to update or delete each row in the table. This is not efficient because it requires multiple updates or deletions to the database. This is why it is important to ensure that the data in the database is atomic.

Here's how we can make that table atomic:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER
);

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  street TEXT,
  city TEXT,
  state TEXT,
  zip_code TEXT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

The addresses table is now atomic because each attribute contains only one value. It also makes it easier to query the database because we can now query the addresses table for each city. It also makes it easier to update the database because we can now update or delete each row in the addresses table.

Here's another example of a non-atomic table:

```sql

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  phone_numbers TEXT
);
```

The reason why this table is not atomic is because the phone_numbers attribute contains multiple values. It contains or represents different values such as the home phone number, cell phone number, and work phone number. This is not atomic because each attribute should contain only one value.

Here's how we can make that table atomic:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER
);

CREATE TABLE phone_numbers (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  phone_number TEXT,
  FOREIGN KEY (student_id) REFERENCES students(id)
);
```

The phone_numbers table is now atomic because each attribute contains only one value.

Great! Now we have a better understanding of normalization. Let's take a look at the other levels of normalization.

#### Second normal form (2NF)

The second normal form (2NF) is used to ensure that the data in the database is in the right place. It is used to ensure that each attribute in a table is dependent on the primary key.

Here's an example of a table that is not in the right place:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  school_name TEXT,
  school_address TEXT
);
```

Notice how school_name and school_address are not dependent on the primary key. This is not in the right place because school_name and school_address are not dependent on the primary key. Why might this be a problem? Well, if we want to update the school_name or school_address, we would have to update each row in the table. This is not efficient because it requires multiple updates to the database. It also makes it difficult to query the database because we would have to query the database for each school. Also, the integrity of the data is not guaranteed because we would have to ensure that the school_name and school_address are correct for each row in the table. This is why it is important to ensure that the data in the database is in the right place.

Here's how we can make that table in the right place:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  school_id INTEGER,
  FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE schools (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT
);
```

This now fixes the problem because school_name and school_address are now dependent on the primary key. It ensures that the data in the database is in the right place. It also makes it easier to query the database because we can now query the schools table for each school.

#### Third normal form (3NF)

The third normal form (3NF) is used to ensure that the data in the database is not redundant. It is used to ensure that each attribute in a table is dependent on the primary key.

Here's an example of a table that is redundant:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  school_name TEXT,
  school_address TEXT,
  school_phone_number TEXT,
  school_website TEXT
);
```

This is redundant because school_name, school_address, school_phone_number, and school_website are all dependent on the primary key. This is not efficient because it requires multiple updates to the database. Furthermore, if we had a thousand students, we would have to update each row in the table. It's as if we are creating 1000 copies of the same data. This is why it is important to ensure that the data in the database is not redundant.

Here's how we can make that table not redundant:

```sql
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  grade INTEGER,
  school_id INTEGER,
  FOREIGN KEY (school_id) REFERENCES schools(id)
);

CREATE TABLE schools (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  phone_number TEXT,
  website TEXT
);
```

This now fixes the problem because school_name, school_address, school_phone_number, and school_website are now dependent on the primary key. It ensures that the data in the database is not redundant. It also makes it easier to query the database because we can now query the schools table for each school. Instead of having to update each row in the table, we can now update the schools table. This is more efficient because it requires fewer updates to the database.

#### Practice Problem

Let's take a moment to normalize the following table.

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password TEXT,
  addresses TEXT,
  phone_numbers TEXT
);
```

<details>

<summary>Solution</summary>

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password TEXT
);

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  street TEXT,
  city TEXT,
  state TEXT,
  zip_code TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE phone_numbers (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  phone_number TEXT,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

</details>

In summary, normalization is the process of organizing data in a database. The goal of normalization is to reduce data redundancy and improve data integrity. It also allows to have more efficient queries and updates to the database.

## Security and Best Practices

Security is a very important topic when it comes to databases. It is important to ensure that the data in the database is secure. It also helps to ensure that the data in the database is not compromised.

Best practices are also broad and important when it comes to databases. It is important to ensure that the database is designed and implemented in a way that is secure and efficient.

There are different ways how to secure a database along with best practices. The most common ways are:

-   **Database security** - Database security involves protecting the database from unauthorized access, misuse, or data breaches. It encompasses a range of practices and technologies designed to safeguard the data.
-   **Performance optimization** - The process of making the database perform operations more efficiently.
-   **Database design and normalization** - The process of structuring a database to minimize redundancy and dependency.
-   **Database schema design** - The layout of the database that defines how data is organized into tables and relationships.
-   **Database administration** - The role of managing and maintaining database systems.
-   **Database backup and recovery** - Processes to safeguard data by creating copies (backups) and restoring data from those backups when necessary.

> **Practice with the Codelabs Learning Assistant**
>
> Try answering this question, then ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):
> _"What is one way to keep a database secure? Why is it important to back up your database?"_

## Installing Ruby

Installing Ruby may be a little tricky.

### Windows (using WSL)

If you are a Windows user, I recommend watching this [video](https://youtu.be/9RsdAzLQ3Dk) to help you install Ruby on your machine.

Below are the instructions to install Ruby on Windows from the video.

1. In the Windows search bar, search `Turn Windows features on or off`
    - Check `Windows Subsystem for Linux`
    - Check `Virtual Machine Platform`
    - Check `Windows Hypervisor Platform`
    - Click `ok`
2. Restart your computer
3. Run Windows PowerShell or Command Prompt as an **administrator**.
4. In the terminal, run `wsl --install -d Ubuntu`. It may ask you to make an account. Make an account and remember the password. An Ubuntu terminal should open up.
5. Go to [https://rvm.io/rvm/install](https://rvm.io/rvm/install)
6. On the website, where it says 'Install GPG keys', copy the two commands and enter them into the Ubuntu terminal. Continue even if you get errors. It might not work.
7. Go to [https://rvm.io/rvm/security](https://rvm.io/rvm/security), under alternatives, copy and paste the commands into the Ubuntu terminal.
8. Enter `\curl -sSL https://get.rvm.io | bash` in your Ubuntu terminal.
9. Restart the Ubuntu terminal (search for 'Ubuntu' in your Windows Start menu and open it to access your Linux environment).
10. Enter `rvm -v` to check if RVM is installed (in the Ubuntu terminal).
11. Enter `rvm install ruby 3.4.4` (in the Ubuntu terminal).
12. Open VS Code (restart if already open) and open a new terminal. **Make sure the terminal is set to Ubuntu (WSL) to access Ruby.** You can select the Ubuntu terminal in VS Code.
13. Once open, enter `ruby -v` to check if Ruby is installed (in the Ubuntu terminal).

### Mac

If you are on a Mac, I recommend watching this [video](https://youtu.be/7dvQc_6PYho) to help you install Ruby on your machine.

Below are the instructions to install Ruby on Mac from the video.

1. Go to [https://brew.sh/](https://brew.sh/)
2. Copy the command from the website and enter it into your terminal (the regular macOS Terminal app).
3. Once installed, run `brew install gnupg`
4. Once installed, run `sudo xcode-select --install`, click install on the pop up.
5. Restart your computer.
6. Go to [https://rvm.io/rvm/install](https://rvm.io/rvm/install)
7. On the website, where it says 'Install GPG keys', copy the two commands and enter them into your terminal. Continue even if you get errors. It might not work.
8. Go to [https://rvm.io/rvm/security](https://rvm.io/rvm/security), under alternatives, copy and paste the commands into your terminal.
9. Enter `\curl -sSL https://get.rvm.io | bash` in your terminal (the regular macOS Terminal app).
10. Restart the terminal and enter `rvm -v` to check if RVM is installed.
11. Enter `rvm install ruby 3.4.4`
12. Open VS Code (restart if already open) and open a new terminal.
13. Once open, enter `ruby -v` to check if Ruby is installed.

## Summary

In conclusion, databases are a very important part of any application. Designing a database and deciding what tables and columns are used largely depends on what data you are trying to store. To map out the data, we may want to use an ERD to help visualize the relationships. As we move forward into the program, we will visit databases again but in Ruby on Rails.
Ruby gems and CLI Part 1
Table of Contents

Ruby Gems
Using a Gem
Countries of The World CLI
Technical Documentation for the CLI
Ruby Gems
Ruby gems are packages of code that you can use in your Ruby projects. There are thousands of gems available for you to use. You can find them on RubyGems.org. The purpose of gems are to make your life easier. Instead of writing code from scratch, you can use a gem that someone else has already written. Here are some examples of gems:

> 💡 Need a refresher on what a Ruby gem is or how bundler works?
> Ask the Codelabs Learning Assistant: “What’s a Ruby gem and why use bundler?”

-   `Nokogiri` - A gem that allows you to parse HTML and XML documents.
-   `Pry` - A gem that allows you to debug your code.
-   `HTTParty` - A gem that allows you to make HTTP requests.
-   `Sinatra` - A gem that allows you to create web applications.
-   `Rails` - A gem that allows you to create web applications.
-   `Rake` - A gem that allows you to automate tasks.
-   `RSpec` - A gem that allows you to test your code.
-   `Rubocop` - A gem that allows you to check your code for style and syntax errors.
-   `Faker` - A gem that allows you to generate fake data.

In this chapter, we will learn how to use gems and how to create our own gems.

## Using a Gem

Let's use the Nokogiri gem to parse HTML and XML documents.

Open VS Code and create a new folder called `nokogiri-example`.
Add the following code to your `Gemfile`:

```ruby
source "https://rubygems.org"
ruby '3.4.4'
gem "nokogiri"
```

Here we use the `source` method to specify the source of the gems that we want to use. In this case, we are using RubyGems.org.

Then we use the `gem` method to specify the gem that we want to use. In this case, we are using the Nokogiri gem. If we need to add more gems, we can add them to the `Gemfile` file like so:

```ruby
gem 'gem-1'
gem 'gem-2'
```


You can also specify the version of the gem that you want to use. For example, if you want to use version 1.15.4 of the Nokogiri gem, you can do this:

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "nokogiri", "1.15.4"
```

The '1' is the major version. The major version is used for major changes.
The '15' is the minor version. The minor version is used for minor changes.
The next '4' is the patch version. The patch version is used for bug fixes.
If you don't specify the version, it will use the latest version of the gem.

```ruby
ruby '3.4.4'
```

Here you'll see we are specifying the version of Ruby that we want to use. In this case, we are using version 3.4.4. If you don't specify the version, it will use the latest version of Ruby.

## Nokogiri Gem

Run `bundle install`.

The `bundle install` command will install the Nokogiri gem and all of its dependencies into your project. Whenever you add a new gem to your Gemfile, you will need to run `bundle install`. If you fork a project that has a Gemfile, you will need to run `bundle install`. It's the equivalent of `npm install` for a JavaScript project.

These are gems that are installed in your project. They are not installed globally unless you specify that you want to install them globally in which case you will have to run `gem install gem-name` in the shell.

This will add onto the `Gemfile.lock` file that will keep track of the gems that you are using in your project.

It might look similar to this, depending on the version you installed. The specific version does not matter for this example.

```ruby
GEM
  remote: https://rubygems.org/
  specs:
    mini_portile2 (2.8.5)
    nokogiri (1.15.4)
      racc (~> 1.4)
    racc (1.7.3)

PLATFORMS
  ruby

DEPENDENCIES
  nokogiri (= 1.15.4)

RUBY VERSION
   ruby 3.4.4p20

BUNDLED WITH
   2.3.7
```

The difference between the `Gemfile` and the `Gemfile.lock` is that the Gemfile is used to specify the gems that you want to use in your project and the Gemfile.lock is used to specify the gems that you are actually using in your project and their versions.

💡 Curious why Gemfile.lock exists at all?
Ask the Codelabs Learning Assistant: Ask: "Why do we need a Gemfile.lock file in Ruby projects?"

Why is this important? Because if you are working on a team, you want to make sure that everyone is using the same version of the gems. It also makes it easier to deploy your application to a server and keeps the environment consistent. We don't want to have different versions of gems on our local machine and on the server to avoid any issues.

Create a new file called `index.html` and add the following code to it:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<title>Nokogiri Example</title>
	</head>
	<body>
		<h1>Hello World</h1>
	</body>
</html>
```

Let's extract the text from the h1 element using the Nokogiri gem.

Create a file called `main.rb`:

```ruby
require "nokogiri"

doc = Nokogiri::HTML(File.open("index.html"))

puts doc.css("h1").text
```

Let's break this down:

-   `require "nokogiri"` — Here we use the require method to require the Nokogiri gem to use its provided objects.
-   `Nokogiri::HTML` — The Nokogiri::HTML module is used to parse the HTML document.
-   `doc = Nokogiri::HTML(File.open("index.html"))` — The File.open method is used to open the index.html file. As we pass in this file to the Nokogiri::HTML module, it will parse the HTML document and store it in the doc variable. Parsing it means it will convert the HTML document into a format that we can use, such as a Nokogiri instance. We can then use the doc variable to get the data that we want.
-   `puts doc.css("h1").text` — Then we use the css method, a Nokogiri method, to select the h1 element. Afterwards we use the text method, another Nokogiri method, to get the text or content of the h1 element.

There are a wide variety of methods from Nokogiri but these are enough to get us started.

Execute `main.rb`.

This will print out "Hello World" to the terminal.

## Practice Problem

Let's practice using the Nokogiri gem.

Open VS Code and create a new folder called `nokogiri-practice`.

Create a new file called `index.html` and add the following code to it:

```html
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<title>Nokogiri Practice</title>
	</head>
	<body>
		<h1>Hello World</h1>
		<p>This is a paragraph</p>
		<p>This is another paragraph</p>
		<ul>
			<li>Item 1</li>
			<li>Item 2</li>
			<li>Item 3</li>
		</ul>
	</body>
</html>
```

Use the Nokogiri gem to parse the HTML document.
Extract all li elements and print them out to the terminal.
Each li element should be on a new line.
Item 1
Item 2
Item 3
Solution
Web Scraping with Nokogiri and httparty
We can use the Nokogiri gem and the httparty gem to make HTTP requests and parse the HTML and XML documents. This is a form of web scraping. Let's create a new repl called web-scraper.

We will be scraping the Wikipedia page for the list of films from 2019.

https://en.wikipedia.org/wiki/2020_in_film

Add the following code to your Gemfile file:

# frozen_string_literal: true

```ruby
source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "nokogiri"
gem "httparty"
```

Run bundle install to install the Nokogiri gem and the httparty gem.

Navigate to main.rb.

Let's require the necessary gems to web scrape.

```ruby
main.rb

require "nokogiri"
require "httparty"
```

Define a class called API and include a class method called get_films_by_year that takes in a year as an argument. We will use year to get a list of films from Wikipedia.

main.rb

```ruby
require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
  end
end
```

Then we use the HTTParty.get method to make a GET request to the Wikipedia page for the year that we pass in as an argument.

```ruby

require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
    url = "https://en.wikipedia.org/wiki/#{year}_in_film"
    unparsed_page = HTTParty.get(url)
    end
  end
end
```

Since we have the unparsed_page, we aren't able to make use of it until we parse it into a nokogiri object.

```ruby
require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
    url = "https://en.wikipedia.org/wiki/#{year}_in_film"
    unparsed_page = HTTParty.get(url)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
  end
end

require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
    url = "https://en.wikipedia.org/wiki/#{year}_in_film"
    unparsed_page = HTTParty.get(url)
    parsed_page = Nokogiri::HTML(unparsed_page.body)

    # extract the elements as nokogiri instances
    films = parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a").map { |film| film.text.strip }
  end
end
```

Targeting elements goes from left to right in the string as you go down the hierarchy. Parent element to child element.

The css method selects the table.wikitable.sortable tr td:nth-child(2) i a element.

table.wikitable.sortable tr td:nth-child(2) i a represents the series of hierarchy levels to get to the table and the elements. It is used to select elements from the document that you requested for. You should inspect the elements on the web page when scraping and find the elements that you want to select based off the selector or class name. Getting to this point takes time and trial and error. Depending on the webpage, it can be difficult to select the elements that you want.

What you are doing here is basically finding the parent element, targeting it by it's CSS and then finding the child element and targeting it.

So you have a table element with classes of wikitable and sortable. This is used to specify the table that you want to select since there's many tables on the page.

As you target the specific table, you then target the tr element since it will include all the rows of the films. Technically, it will also include the header rows. So we have to specify that we want td for table data to remove the header rows.

Then you have a nth-child(2) element right after. This will only allow us to extract the second child element from every td which will include the title of the film that we want. Then you have an i element. Then you have an a element.

This will return an array of nokogiri instances.

`parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a")`
In which we can use to iterate and strip the text from the elements.

`parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a").map { |film| film.text.strip }`
Then we use the each_with_index method to iterate over the films and print out the films to the terminal.

```ruby
films.each_with_index do |film, index|
puts "#{index + 1}. #{film}"
end
```
Nokogiri can be buggy and it can be difficult to use. It is not always accurate. You may have to try different CSS selectors to get the data that you want.

main.rb

```ruby
require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
    url = "https://en.wikipedia.org/wiki/#{year}_in_film"
    unparsed_page = HTTParty.get(url)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    films = parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a").map { |film| film.text.strip }
    films.each_with_index do |film, index|
      puts "#{index + 1}. #{film}"
    end
  end
end
```

API.get_films_by_year(2019)
The result of this code is a list of films from 2019 once you execute it.

1. Avengers: Endgame
2. The Lion King
3. Frozen II
4. Spider-Man: Far From Home
5. Captain Marvel
6. Joker
7. Star Wars: The Rise of Skywalker
8. Toy Story 4
9. Aladdin
10. Jumanji: The Next Level
    Web scraping is a very powerful tool. However, it can be very slow and it can be very difficult to maintain. If the website changes, your code will break. If the website is down, your code will break. If the website is slow, your code will be slow. If you are making a lot of requests, you can get banned from the website. So you have to be careful when using web scraping. Respect the website and don't abuse it.

In a practical sense you would not use web scraping to get data from a website unless for situations needed or special use cases. You would use an API.

Countries of The World CLI
A CLI is a Command Line Interface. It is a program that allows you to interact with your computer using the command line. An example would be the Angular CLI. It allows you to create a new angular project, generate components, generate services, etc.

In this CLI, we will be scraping a website for a list of countries and their capitals, populations and area.

Let's begin by creating a new folder in VS Code called countries_of_the_world_cli.

We mostly have everything we need to begin creating our CLI.

The readme.md file will be used to document our project.

The Gemfile will be used to specify the gems that we want to use in our project.

We will also use the main.rb file to run our project and start our CLI.

Let's create a lib directory. This will house our files of code.

Create a new file called lib/cli.rb and add the following code to it:

lib/cli.rb

```ruby
class CLI
  def start
    puts "Welcome to the Countries of the World CLI!"
    puts "What is your name?"
    name = gets.strip
    puts "Hello #{name}!"
  end

  def get_input
    gets.strip
  end
end
puts "Welcome to the Countries of the World CLI!"
    puts "What is your name?"
    
Here we are using the CLI class to define a method called start that prints out a welcome message and asks the user for their name.

name = gets.strip
    puts "Hello #{name}!"
Then we use the gets global method to get the user's input. Then we use the strip method to remove any whitespace from the user's input. Then we use the puts method to print out the user's name.
```

Navigate to main.rb and crete a new CLI instance to call start.

require_relative './lib/cli.rb'

CLI.new.start
You can run the main.rb file by opening the integrated terminal in VS Code and executing:

ruby main.rb
Here is the result

Welcome to the Countries of the World CLI!
What is your name?
John Doe
Hello John Doe!
Adding Tests
Let's create a test file for our CLI using rspec. But first we have to install rspec.

Run bundle add rspec to install rspec in the shell. This will automatically add rspec to our Gemfile and lock file.

Run bundle exec rspec --init to initialize rspec into the project folder. This will create a .rspec file and a spec directory with a spec_helper.rb file. Be sure to then run gem install rspec to use the rspec gem in the shell provided by commands like rspec.

Let's test out the CLI class.

Create a new file called spec/lib/cli_spec.rb and add the following code to it:

spec/lib/cli_spec.rb

```ruby
require_relative "../../lib/cli.rb"

RSpec.describe CLI do
  describe "#start" do
    it "prints a welcome message and asks the user for their name" do
      cli = CLI.new

      # Stubbing the standard input to simulate user input
      allow(cli).to receive(:gets).and_return("John Doe\n")

      # Expecting specific output to standard output
      expect { cli.start }.to output(
        "Welcome to the Countries of the World CLI!\nWhat is your name?\nHello John Doe!\n"
      ).to_stdout
    end
  end
end
```
>💡 RSPEC still confusing?
>Ask the Codelabs Learning Assistant: Ask: "What is RSpec?"

Here we are using the RSpec.describe method to describe the start method of what we will be testing.

Then we use the it method to describe what the start method does.

The test demonstrates the creation of a new CLI object and the use of the allow method to allow the cli object to receive the get_input method.

Then we use the expect method to expect the cli.start method to output the welcome message and ask the user for their name.

Run bundle exec rspec to run the test.

The difference between entering rspec vs bundle exec rspec is that rspec will use the globally installed version of rspec and bundle exec rspec will use the locally installed version of rspec. I tend to use bundle exec rspec to avoid any issues with the version of rspec.

Web Scraping with Nokogiri and httparty
The website we will be scraping is a website that allows legal web scraping and it is called www.scrapethissite.com. This site allows for it be scraped for educational purposes. Be weary of scraping websites that do not allow it. You can get banned from the website.

Take a moment to view the website and inspect the elements. We will be scraping the countries and their capitals, populations and area.

💡 Still confused what Scraping is?
Ask the Codelabs Learning Assistant: Ask: "What is Scraping?"

We can use the Nokogiri gem and the httparty gem to make HTTP requests and parse the HTML and XML documents.

Add both gems to your gemfile:

```rb
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "rspec"
gem "nokogiri"
gem "httparty"
```

Run bundle install to install the Nokogiri gem and the httparty gem.

Let's create a new file called scraper.rb under lib. Let's add the following:

```ruby
lib/scraper.rb

require "nokogiri"
require "httparty"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    puts parsed_page
  end
end
```

Let's break this down

Here we use the require method to require the Nokogiri gem and the httparty gem.
The Scraper module is used to define a method called scrape_countries that makes a GET request to the INDEX_URL and parses the HTML document.
The INDEX_URL is a constant that is used to store the URL that we want to scrape.
The HTTParty.get method is used to make a GET request to the INDEX_URL.
The Nokogiri::HTML method parses the HTML document.
The puts method prints out the parsed HTML document to the terminal.
Call the scrape_countries method from the start method in the cli.rb file.

```ruby
lib/cli.rb

require_relative "scraper.rb"

class CLI
  def start
    Scraper.scrape_countries
    puts "Welcome to the Countries of the World CLI!"
    puts "What is your name?"
    name = gets.strip
    puts "Hello #{name}!"
  end

  def get_input
    gets.strip
  end
end
```

Run the project by opening the integrated terminal in VS Code and running:

ruby main.rb
This will print all the HTML to the terminal.

This is where it gets tricky, if you navigate to the site and inspect the country elements, you will see that they are not in a table. They are in a div element. So we have to find a way to select the div element and then select the country elements.

Thankfully they all have the same class called country, so we can use that to select the country elements.

```ruby
require "nokogiri"
require "httparty"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    countries = parsed_page.css("div.country")
    puts countries
  end
end
```
Run the project and notice how it only gives us divs with the class of country. div.country as an argument represents every div with the classname of country. We want to select the country name, the capital, the population and the area. We can do that by using the css method.

```ruby
require "nokogiri"
require "httparty"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    countries = parsed_page.css("div.country")

    countries.each do |country|
      name = country.css("country-name").text
      capital = country.css("country-capital").text
      population = country.css("country-population").text
      area = country.css("country-area").text

      puts "#{name} #{capital} #{population} #{area}"
    end
  end
end
```
When we run the project, notice how we get all blanks. We must had done something wrong. To help debug this, we can use the debug gem (the modern Ruby debugger).

Debug gem
The debug gem is a gem that allows you to debug your code. It is similar to the debugger in JavaScript. It allows you to pause your code and inspect it. Ruby 3.1+ includes the debug gem by default. Let's add the debug gem to our scraper.rb file.

```ruby
lib/scraper.rb

require "nokogiri"
require "httparty"
require "debug"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    countries = parsed_page.css("div.country")

    countries.each do |country|
      name = country.css("country-name").text
      capital = country.css("country-capital").text
      population = country.css("country-population").text
      area = country.css("country-area").text
      binding.break # <---- Add this line
      puts "#{name} #{capital} #{population} #{area}"
          end
    end
  end
  ```
Run the project by opening the integrated terminal in VS Code and running:

ruby main.rb
You will notice you get something along the lines of this in your terminal:

```ruby
[11, 20] in /home/runner/countries-of-the-world-cli/lib/scraper.rb
   11:     countries.each do |country|
   12:       name = country.css(&quot;country-name&quot;).text
   13:       capital = country.css(&quot;country-capital&quot;).text
   14:       population = country.css(&quot;country-population&quot;).text
   15:       area = country.css(&quot;country-area&quot;).text
   16:       binding.break
=&gt; 17:       puts &quot;#{name} #{capital} #{population} #{area}&quot;
   18:     end
   19:   end
   20: end

```
This is a pause in your code and you have access to the variables in your code. You can enter in name and it will print out the name of the country. However, when you do that you get an empty string. This is where you want to play with the CSS selectors to get the data that you want.

This isn't as straight forward as a process since it takes time to debug and figure out what's going on. But it's a good learning experience and the debug gem is a great tool to use.

We need to further inspect the elements to see what's going on.

When inspecting the country class element on the webpage, you may notice it includes an h3 and a div with the country info. Take time to inspect the webpage and see what's going on.

This means that country represents both those elements as well. So we need to select the h3 element and the div element separately.

Let's try entering country in the terminal while we are in the debugger.

We see that it returns a Nokogiri instance:

```ruby
#<Nokogiri::XML::Element:0x974 name="div" attributes=[#<Nokogiri::XML::Attr:0x6cc name="class" value="col-md-4 country">] children=[#<Nokogiri::XML::Text:0x6e0 "\n                        ">, #<Nokogiri::XML::Element:0x6b8 name="h3" attributes=[#<Nokogiri::XML::Attr:0x654 name="class" value="country-name">] children=[#<Nokogiri::XML::Text:0x668 "\n                            ">, #<Nokogiri::XML::Element:0x690 name="i" attributes=[#<Nokogiri::XML::Attr:0x67c name="class" value="flag-icon flag-icon-ad">]>, #<Nokogiri::XML::Text:0x6a4 "\n                            Andorra\n                        ">]>, #<Nokogiri::XML::Text:0x6f4 "\n                        ">, #<Nokogiri::XML::Element:0x94c name="div" attributes=[#<Nokogiri::XML::Attr:0x708 name="class" value="country-info">] children=[#<Nokogiri::XML::Text:0x71c "\n                            ">, #<Nokogiri::XML::Element:0x744 name="strong" children=[#<Nokogiri::XML::Text:0x730 "Capital:">]>, #<Nokogiri::XML::Text:0x758 " ">, #<Nokogiri::XML::Element:0x794 name="span" attributes=[#<Nokogiri::XML::Attr:0x76c name="class" value="country-capital">] children=[#<Nokogiri::XML::Text:0x780 "Andorra la Vella">]>, #<Nokogiri::XML::Element:0x7a8 name="br">, #<Nokogiri::XML::Text:0x7bc "\n                            ">, #<Nokogiri::XML::Element:0x7e4 name="strong" children=[#<Nokogiri::XML::Text:0x7d0 "Population:">]>, #<Nokogiri::XML::Text:0x7f8 " ">, #<Nokogiri::XML::Element:0x834 name="span" attributes=[#<Nokogiri::XML::Attr:0x80c name="class" value="country-population">] children=[#<Nokogiri::XML::Text:0x820 "84000">]>, #<Nokogiri::XML::Element:0x848 name="br">, #<Nokogiri::XML::Text:0x85c "\n                            ">, #<Nokogiri::XML::Element:0x8c0 name="strong" children=[#<Nokogiri::XML::Text:0x870 "Area (km">, #<Nokogiri::XML::Element:0x898 name="sup" children=[#<Nokogiri::XML::Text:0x884 "2">]>, #<Nokogiri::XML::Text:0x8ac "):">]>, #<Nokogiri::XML::Text:0x8d4 " ">, #<Nokogiri::XML::Element:0x910 name="span" attributes=[#<Nokogiri::XML::Attr:0x8e8 name="class" value="country-area">] children=[#<Nokogiri::XML::Text:0x8fc "468.0">]>, #<Nokogiri::XML::Element:0x924 name="br">, #<Nokogiri::XML::Text:0x938 "\n                        ">]>, #<Nokogiri::XML::Text:0x960 "\n                    ">]>
```

We can call Nokogiri methods on it such as css and text to further get the values we want. For example, try entering country.css("h3").text in the terminal while in the debugger. This will return the country name.

It gives us the country name but in a weird format!

"\n \n Andorra\n "
It's not perfect but it's a start. We can use the strip method to remove the whitespace:

country.css('h3').text.strip
We get Andorra. Great!

As I am debugging, I start to notice, I actually forgot a period in the css selector. It should be .country-name instead of country-name, .country-capital instead of country-capital, etc. This is because they are classes and shouldn't be selected as elements. This is how Nokogiri interprets it.

To exit the debugger, enter exit in the terminal.

Let's change the scraper.rb file to add the period in each css selector.

```ruby
lib/scraper.rb

require "nokogiri"
require "httparty"
require "debug"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    countries = parsed_page.css("div.country")

    countries.each do |country|
      name = country.css(".country-name").text.strip
      capital = country.css(".country-capital").text.strip
      population = country.css(".country-population").text.strip
      area = country.css(".country-area").text.strip
      puts "#{name} #{capital} #{population} #{area}"
    end
  end
end
```

Great! Let's run the project and see what we get.

Andorra Andorra la Vella 84000 468.0
United Arab Emirates Abu Dhabi 4975593 82880.0
Afghanistan Kabul 29121286 647500.0
Antigua and Barbuda St. John&#39;s 86754 443.0
Anguilla The Valley 13254 102.0
Albania Tirana 2986952 28748.0
Armenia Yerevan 2968000 29800.0
Angola Luanda 13068161 1246700.0
Antarctica None 0 1.4E7
Argentina Buenos Aires 41343201 2766890.0
American Samoa Pago Pago 57881 199.0
Austria Vienna 8205000 83858.0
Australia Canberra 21515754 7686850.0
Aruba Oranjestad 71566 193.0
Åland Mariehamn 26711 1580.0
Azerbaijan Baku 8303512 86600.0
Bosnia and Herzegovina Sarajevo 4590000 51129.0
Barbados Bridgetown 285653 431.0
Bangladesh Dhaka 156118464 144000.0
Belgium Brussels 10403000 30510.0
Burkina Faso Ouagadougou 16241811 274200.0
Bulgaria Sofia 7148785 110910.0
Bahrain Manama 738004 665.0
Burundi Bujumbura 9863117 27830.0
Benin Porto-Novo 9056010 112620.0
Saint Barthélemy Gustavia 8450 21.0
.
.
.
This is exactly what we want. We can now use this data to create our CLI.

Let's quickly create a country class to store the data, create a file called country.rb under lib and add the following code to it:

```ruby
country.rb

class Country
  attr_accessor :name, :capital, :population, :area

  @@all = []

  def initialize(name, capital, population, area)
    @name = name
    @capital = capital
    @population = population
    @area = area
    @@all << self
  end

  def self.all
    @@all
  end
end
```

Let's go over this

Here we use the attr_accessor method to create getters and setters for the name, capital, population and area attributes so they are accessible outside of the class.
The @@all class variable is used to store all the instances of the Country class.
The initialize method is used to initialize a new Country object with a name, capital, population and area.
We like to store the data in objects because it makes it easier to work with. We can create a new country object and store the data in it. Then we can use the country object to get the data that we want.

Let's update the scraper.rb file to create a new country object and store the data in it.

```ruby
scraper.rb

require "nokogiri"
require "httparty"
require "debug"
require_relative "./country.rb"

module Scraper
  INDEX_URL = 'https://www.scrapethissite.com/pages/simple/'
  def self.scrape_countries
    unparsed_page = HTTParty.get(INDEX_URL)
    parsed_page = Nokogiri::HTML(unparsed_page.body)
    countries = parsed_page.css("div.country")

    countries.each do |country|
      name = country.css(".country-name").text.strip
      capital = country.css(".country-capital").text.strip
      population = country.css(".country-population").text.strip
      area = country.css(".country-area").text.strip
      Country.new(name, capital, population, area)
    end
  end
end

```

Let's go ahead and add a search functionality and display the data to the user.

cli.rb

```ruby
require_relative "./scraper.rb"

class CLI
  def start
    Scraper.scrape_countries
    puts "Welcome to the Countries of the World CLI!"
    puts "What is your name?"
    name = gets.strip
    puts "Hello #{name}!"
    puts "Please enter a country name to get more information about it."
    input = gets.strip
    country = Country.all.find { |country| country.name.downcase == input.downcase }
    if country === nil
      puts "Sorry, that country is not in our database. Please try again."
    else
      puts "Name: #{country.name}"
      puts "Capital: #{country.capital}"
      puts "Population: #{country.population}"
      puts "Area: #{country.area}"
    end
  end

  def get_input
    gets.strip
  end
end
```

>💡 Getting nil when searching for a country?
>Ask the Codelabs Learning Assistant: Ask: "How does .find work in Ruby and why might it return nil?"

Run the project and we should get the following:

Welcome to the Countries of the World CLI!
What is your name?
John Doe
Hello John Doe!
Please enter a country name to get more information about it.
Vanuatu
Name: Vanuatu
Capital: Port Vila
Population: 221552
Area: 12200.0
Welcome to the Countries of the World CLI!
What is your name?
John Doe
Hello John Doe!
Please enter a country name to get more information about it.
Fake Country
Sorry, that country is not in our database. Please try again.
Great we have a working CLI. We can now get information about a country. However, we can only get information about one country. We can further improve this however, let's move onto technical documentation.

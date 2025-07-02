---
title: Database Fundamentals - Part 1
---

# Database Fundamentals - Part 1

**Table of Contents**

-   Introduction to Databases
-   Introduction to SQL

## Introduction to Databases

A database is a collection of data stored in a computer system. Databases are used to store data in a structured way, so that it can be easily managed and accessed. Databases are used in many applications, spanning virtually the entire range of computer software. Databases are the preferred method of storage for large multiuser applications, where coordination between many users is needed. Even individual users find them convenient, and many electronic mail programs and personal organizers are based on standard database technology.

The topic of databases is very broad, and there are many different types of databases. This chapter will provide an overview of the most common types of databases, and the different ways of organizing data in a database using SQL (Structured Query Language).

Databases is a difficult topic to learn, and it's easy to get overwhelmed by all the different types of databases and database management systems. But don't worry, we will start with the basics and build up from there. By the end of this chapter, you will have a good understanding of the different types of databases, and how they are used.

### Database Management Systems

A database management system (DBMS) is a software system that uses a standard method to store and organize data. The data can be added, updated, deleted, or traversed using various standard algorithms and queries. DBMSs are categorized according to their data structures or types. The DBMS accepts requests for data from the application program and instructs the operating system to transfer the appropriate data. When a DBMS is used, information systems can be changed much more easily as the organization's information requirements change. New categories of data can be added to the database without disruption to the existing system.

This is important because it means that organizations can manage and analyze their data much more effectively and efficiently. For example, consider the task of creating a report for salespeople that shows all the customers they have talked to in the last month, along with the total sales for each customer. Without a DBMS, this report would be difficult to create, because the data is stored in many different locations. With a DBMS, the report can be generated with a few simple "queries".

Examples of Database Management Systems are SQLite, MySQL, PostgreSQL, Microsoft Access, SQL Server, FileMaker, Oracle, RDBMS, dBASE, Clipper, and FoxPro. You might've heard of some of these, but probably not all of them. Each of these DBMSs have their own advantages and disadvantages, and specific uses. In this tutorial, we will focus on learning the fundamentals of SQL.

### Types of Databases

There are many different types of databases, but two of the most common are relational and non-relational databases. Relational databases are also called SQL databases, and non-relational databases are also called NoSQL databases. The main difference between these two types of databases is the way they store data.

Relational databases store data in tables, while non-relational databases store data in documents, key-value pairs, graph databases, or wide-column stores. We will focus on relational databases in this chapter and throughout the program.

### When to use a relational database vs a non-relational database

Relational databases are used for storing structured data and are based on tables. They use Structured Query Language (SQL) for defining and manipulating the data, which is very powerful. Relational databases are easy to extend, and a new data category can be added after the original database creation without requiring that you modify all the existing applications. Relational databases are very popular, and are the most commonly used database type. Examples of relational databases include MySQL, Oracle, and Microsoft SQL Server. Projects that use relational databases include WordPress, Drupal, and Joomla.

Non-relational databases or noSQL databases, on the other hand are used for storing unstructured data. They use a variety of data models, including document, graph, key-value, and columnar. They are very useful for very large databases, and for databases where the data structure is not fixed (and might change over time). Non-relational databases do not use SQL, and the data is not stored in tables. They are instead stored in a format that is optimized for the specific type of data being stored. Examples of non-relational databases include MongoDB, Cassandra, Redis, and Neo4j. Projects that use non-relational databases include Netflix, Twitter, and LinkedIn.

Of course, it's not always easy to decide which type of database to use. There are many factors to consider, including the type of data you are storing, the amount of data, the performance requirements, and the level of expertise of your team. In general, relational databases are a good choice for applications that require multi-row transactions (for example, a banking application), while non-relational databases are a good choice for applications that need to handle large amounts of data where the data structure is not known in advance (for example, a video streaming application).

It's also possible to use both types of databases in the same application. For example, you might use a relational database to store user data, and a non-relational database to store user comments.

### Different types of SQL databases

There are many different types of SQL databases, but the most common are MySQL, PostgreSQL, and SQLite.

Here are the differences between these three databases:

-   MySQL is the most popular open-source database, and is the default database for many content management systems, including WordPress and Drupal. MySQL is generally known for its fast read operations, making it a good choice for read-heavy applications.
-   Postgres is also an open-source database, and is used by many large organizations, including Apple, Cisco, and Red Hat. Postgres is generally known for its reliability, data integrity, and correctness. It excels in write-heavy operations and complex query optimizations, often favored for systems that require complex queries, including data warehousing and analytics applications.
-   SQULite is a lightweight database which is used by many applications, including Firefox, Chrome, and Skype. SQLite is generally known for its simplicity, and is a good choice for applications that need a lightweight database without the overhead of a client-server database engine.

## Introduction to SQL

SQL (Structured Query Language) is a programming language used to communicate with data stored in a relational database management system. SQL syntax is similar to the English language, which makes it relatively easy to write, read, and interpret. SQL is used for tasks such as retrieving data from a database, inserting new data, updating existing data, and deleting data.

SQL is a standard language for storing, manipulating and retrieving data in databases. Our SQL chapter will teach you how to use SQL.

At this moment, it won't matter which SQL database you choose, as most of the SQL syntax is compatible with all databases.

### Creating Tables

In SQL databases, data is stored in tables. A table is a collection of related data entries and it consists of columns and rows. Databases are useful for storing information categorically. A company may have a database with the following tables:

-   Employees
-   Products
-   Customers
-   Orders
-   Invoices
-   etc.

We will use an online SQL editor to create and manipulate a database. The online SQL editor is available at [https://www.jdoodle.com/execute-sql-online](https://www.jdoodle.com/execute-sql-online).

To create a table in a database, you use the CREATE TABLE statement. The following statement creates a new table named `Employees`:

Copy and paste the following SQL to your SQL editor:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);
```

Click 'Execute' to run the SQL statement above. You should see no errors.

NOTE: In this editor, data isn't persistent meaning you would need to create tables, data, ect each and every time you run the SQL statement. This is fine for learning purposes, but in a real-world scenario, you will use a database that stores data persistently.

Let's go over the data types used in the above SQL statement:

-   `int` is used for integer numbers
-   `varchar` is used for variable-length character strings
-   `date` is used for date values
-   `text` is used for long text strings

Other data types include

-   `float` is used for floating-point numbers
-   `decimal` is used for decimal numbers
-   `boolean` is used for boolean values (true/false)
-   `blob` is used for binary data
-   `json` is used for storing JSON data
-   `uuid` is used for storing UUIDs
-   `array` is used for storing arrays

Size of the data definitely matters as it affects the performance of the database. For example, if you know that a column will only store values up to 255 characters, you should use `varchar(255)` instead of `text`. This will improve the performance of the database. Another example is if you know that a column will only store values up to 10 characters, you should use `varchar(10)` instead of `varchar(255)`. This will also improve the performance of the database. The reason for this is because the database will allocate less memory for the column, and will be able to store more rows in memory.

Let's go over the columns in the `Employees` table:

-   `EmployeeID` is an integer number that uniquely identifies each employee
-   `LastName` is a variable-length character string that stores the last name of the employee
-   `FirstName` is a variable-length character string that stores the first name of the employee
-   `BirthDate` is a date value that stores the birth date of the employee
-   `Notes` is a long text string that stores notes about the employee

### Inserting Data

To insert data into a table, you use the INSERT INTO statement. The following statement inserts a new row into the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
```

Click 'Execute' to run the SQL statement above. You should see no errors.

Let's go over the SQL statement above:

-   `INSERT INTO` is a clause that adds the specified row or rows into the table
-   `Employees` is the name of the table
-   `(EmployeeID, LastName, FirstName, BirthDate, Notes)` is a parameter that lists the columns that the `INSERT INTO` statement will insert values into
-   `VALUES` is a clause that indicates the data being inserted in order of the columns specified in the `INSERT INTO` clause

### Selecting Data

Selecting data refers to retrieving data from a database.

To select data from a table, you use the SELECT statement. The following statement selects all rows from the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');

SELECT * FROM Employees;
```

You should see the following output:

```
1|Doe|John|1990-01-01|John Doe was born on January 1, 1990.
```

Let's go over the SQL statement above:

-   `SELECT` is a clause that indicates that the statement is a query. You will use SELECT every time you query data from a database.
-   `*` is a wildcard character that indicates all columns. This returns all columns from the `Employees` table.
-   `FROM Employees` is a clause that indicates the table that you are querying data from.
-   `;` is a semicolon that indicates the end of the statement. Although it is optional, it is a good practice to use it.

This is also called a query. A query is a request for data or information from a database table or combination of tables. A query always returns a result set, even if it's empty. You can think of a result set as a temporary table that holds the data returned by the query. In the example above, the result set contains all rows from the `Employees` table.

If you want to select only some columns, you can specify them after the `SELECT` clause. For example, the following statement selects only the `FirstName` and `LastName` columns from the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');

SELECT FirstName, LastName FROM Employees;
```

### Where Clause

The WHERE clause is used to filter records. The WHERE clause is used to extract only those records that fulfill a specified condition. The following statement selects all rows from the `Employees` table where the `FirstName` is equal to `John`:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT * FROM Employees WHERE FirstName = 'John';
```

You should see the following output:

```
1|Doe|John|1990-01-01|John Doe was born on January 1, 1990.
```

Let's go over the SQL statement above:

-   `WHERE` is a clause that indicates you want to filter the result set to include only rows where the following condition is true.
-   `FirstName = 'John'` is a condition that the `FirstName` column equals `John`.

The `WHERE` clause can be combined with `AND`, `OR`, and `NOT` operators. The following statement selects all rows from the `Employees` table where the `FirstName` is equal to `John` and the `LastName` is equal to `Doe`:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT * FROM Employees WHERE FirstName = 'John' AND LastName = 'Doe';
```

You should see the following output:

```
1|Doe|John|1990-01-01|John Doe was born on January 1, 1990.
```

Let's go over the SQL statement above:

-   `AND` is an operator that combines two conditions. Both conditions must be true for the row to be included in the result set.
-   `FirstName = 'John'` is a condition that the `FirstName` column equals `John`.
-   `LastName = 'Doe'` is a condition that the `LastName` column equals `Doe`.
-   `SELECT * FROM Employees` is the statement that you want to execute.
-   `WHERE FirstName = 'John' AND LastName = 'Doe'` is the condition that you want to filter the result set with.

The `WHERE` clause can also be combined with `OR` operator. The following statement selects all rows from the `Employees` table where the `FirstName` is equal to `John` or the `LastName` is equal to `Doe`:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT * FROM Employees WHERE FirstName = 'John' OR LastName = 'Doe';
```

You should see the following output:

```
1|Doe|John|1990-01-01|John Doe was born on January 1, 1990.
2|Doe|Jane|1991-02-02|Jane Doe was born on February 2, 1991.
```

Let's go over the SQL statement above:

-   `OR` is an operator that combines two conditions. Either one of the conditions must be true for the row to be included in the result set.
-   `FirstName = 'John'` is a condition that the `FirstName` column equals `John`.
-   `LastName = 'Doe'` is a condition that the `LastName` column equals `Doe`.
-   `SELECT * FROM Employees` is the statement that you want to execute.

The `WHERE` clause can also be combined with `NOT` operator. The following statement selects all rows from the `Employees` table where the `FirstName` is not equal to `John`:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT * FROM Employees WHERE NOT FirstName = 'John';
```

You should see the following output:

```
2|Doe|Jane|1991-02-02|Jane Doe was born on February 2, 1991.
```

Let's go over the SQL statement above:

-   `NOT` is an operator that negates the condition that follows it. The `NOT` operator displays a record if the condition(s) is NOT TRUE.

Why is the `WHERE` clause important? The `WHERE` clause is important because it allows you to extract only the data that you need from a table. When you query a table with millions of rows, returning all the rows will consume the bandwidth of your database server, and put unnecessary load on it. This will slow down your database server, and will slow down your application. By using the `WHERE` clause, you can return only the rows that you need, and reduce the load on your database server. It is used in almost every SQL statement. It is used to filter the result set to include only rows that meet the specified condition. It is also used to limit the number of rows returned by a query. For example, if you want to return only the first 10 rows, you can use the `WHERE` clause to limit the number of rows returned by a query.

This can also be useful for security purposes, as you can limit the data that a user can access. For example, you can limit a user to only see their own data, and not the data of other users. This is called row-level security, and is a very powerful feature of SQL.

Extracting millions of rows can be problematic for other reasons as well. For example, if you are extracting data from a table with millions of rows, and you are using a slow internet connection, it might take a long time to download the data. This can be a problem if you are using a mobile device, and you are on a slow internet connection. By using the `WHERE` clause, you can reduce the amount of data that you need to download, and speed up your application.

On another another note, it can be pricy for reasons such as grabbing millions of rows from a database. For example, if you are using a cloud database, you might be charged for the amount of data that you download. You can think of a database as a service, and you are paying for the amount of data that you use. By using the `WHERE` clause, you can reduce the amount of data that you need to download, and reduce your costs.

### Order By Clause

The `ORDER BY` clause is used to sort the result set in ascending or descending order. The `ORDER BY` clause sorts the result set in ascending order by default. To sort the result set in descending order, you use the `DESC` keyword. The following statement selects all rows from the `Employees` table and sorts the result set in ascending order by the `FirstName` column:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT * FROM Employees ORDER BY FirstName;
```

You should see the following output:

```
2|Doe|Jane|1991-02-02|Jane Doe was born on February 2, 1991.
1|Doe|John|1990-01-01|John Doe was born on January 1, 1990.
```

Let's go over the SQL statement above:

-   `ORDER BY` is a clause that indicates that you want to sort the result set
-   `FirstName` is a column that you want to sort by
-   `SELECT * FROM Employees` is the statement that you want to execute

The `ORDER BY` clause can also be used to sort the result set in descending order. The following statement selects all rows from the `Employees` table and sorts the result set in descending order by the `FirstName` column:

```sql
SELECT * FROM Employees ORDER BY FirstName DESC;
```

The `ORDER BY` clause is important because it allows you to sort the result set in a specific order. This can be useful for many reasons. For example, if you want to display the result set in alphabetical order, you can use the `ORDER BY` clause to sort the result set in ascending order by the `FirstName` column.

### Limit Clause

The `LIMIT` clause is used to limit the number of rows returned by a query. The `LIMIT` clause is used in the `SELECT` statement. The following statement selects the first 10 rows from the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (3, 'Doe', 'Mary', '1992-03-03', 'Mary Doe was born on March 3, 1992.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (4, 'Doe', 'Mark', '1993-04-04', 'Mark Doe was born on April 4, 1993.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (5, 'Doe', 'Lisa', '1994-05-05', 'Lisa Doe was born on May 5, 1994.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (6, 'Doe', 'Robert', '1995-06-06', 'Robert Doe was born on June 6, 1995.');

SELECT * FROM Employees LIMIT 3;
```

The `LIMIT` clause is important because it allows you to limit the number of rows returned by a query. You wouldn't want to receive thousands of rows when you only need the first 10 rows. This can be problematic for many reasons. For example, if you are using a mobile device, and you are on a slow internet connection, it might take a long time to download the data. This can be a problem if you are using a mobile device, and you are on a slow internet connection. By using the `LIMIT` clause, you can reduce the amount of data that you need to download, and speed up your application.

To get the last 3 rows from the `Employees` table, you use the `LIMIT` clause. The following statement selects the last 3 rows from the `Employees` table:

```sql
SELECT * FROM Employees ORDER BY EmployeeID DESC LIMIT 3;
```

Let's go over the SQL statement above:

-   `LIMIT` is a clause that lets you specify the maximum number of rows the result set will have.
-   `3` is the maximum number of rows that the result set will have.
-   `SELECT * FROM Employees` is the statement that you want to execute.
-   `ORDER BY EmployeeID DESC` is a clause that sorts the result set in descending order by the `EmployeeID` column.

Notice how it's executed from left to right, meaning it will first order the result set in descending order by the `EmployeeID` column, and then it will select the first 3 rows from the result set.

#### Practice Problem

Create a table named `Students` with the following columns:

-   `StudentID` is an integer number that uniquely identifies each student
-   `LastName` is a variable-length character string that stores the last name of the student
-   `FirstName` is a variable-length character string that stores the first name of the student
-   `BirthDate` is a date value that stores the birth date of the student
-   `Notes` is a long text string that stores notes about the student
-   `GPA` is a floating-point number that stores the grade point average of the student
-   `Major` is a variable-length character string that stores the major of the student

Insert the following rows into the `Students` table:

-   `StudentID` is 1, `LastName` is `Doe`, `FirstName` is `John`, `BirthDate` is `1990-01-01`, `Notes` is `John Doe was born on January 1, 1990.`, `GPA` is `3.5`, `Major` is `Computer Science`
-   `StudentID` is 2, `LastName` is `Doe`, `FirstName` is `Jane`, `BirthDate` is `1991-02-02`, `Notes` is `Jane Doe was born on February 2, 1991.`, `GPA` is `3.6`, `Major` is `Computer Science`

Select all rows from the `Students` table where the `Major` is equal to `Computer Science` and the `GPA` is greater than or equal to `3.5`. Sort the result set in descending order by the `GPA` column. Limit the result set to 1 row.

<details>

<summary>Solution</summary>

```sql
CREATE TABLE Students (
    StudentID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text,
    GPA float,
    Major varchar(255)
);

INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA, Major)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.', 3.5, 'Computer Science');
INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA, Major)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.', 3.6, 'Computer Science');

SELECT * FROM Students WHERE Major = 'Computer Science' AND GPA >= 3.5 ORDER BY GPA DESC LIMIT 1;
```

</details>

> 💡 **Codelabs Learning Assistant:** [https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> - Unsure when to use a relational vs. non-relational database? Ask the assistant for a comparison or examples from real applications.

### Aggregate Functions

Aggregate functions are used to perform calculations on a set of values and return a single value. Aggregate functions are often used with the `GROUP BY` clause of the `SELECT` statement. The following table shows the most commonly used aggregate functions:

```
| Function  | Description                |
| --------- | -------------------------- |
| `AVG()`   | Returns the average value  |
| `COUNT()` | Returns the number of rows |
| `FIRST()` | Returns the first value    |
| `LAST()`  | Returns the last value     |
| `MAX()`   | Returns the largest value  |
| `MIN()`   | Returns the smallest value |
| `SUM()`   | Returns the sum            |
```

The following statement returns the number of rows in the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.');

SELECT COUNT(*) FROM Employees;
```

You should see the following output:

```
2
```

Let's go over the SQL statement above:

-   `COUNT(*)` is an aggregate function that returns the number of rows in the result set.
-   `SELECT COUNT(*) FROM Employees` is the statement that you want to execute.

The following statement returns the average birth date of all employees in the `Employees` table:

```sql
SELECT AVG(BirthDate) FROM Employees;
```

You should see the following output:

```
1990.5
```

Let's go over the SQL statement above:

-   `AVG(BirthDate)` is an aggregate function that returns the average birth date of all employees in the `Employees` table.
-   `SELECT AVG(BirthDate) FROM Employees` is the statement that you want to execute.

The MIN() function retrieves the smallest value in a set of values. In the context of dates, it would return the earliest date, which corresponds to the oldest person if you're considering birth dates.

```sql
SELECT MIN(BirthDate) FROM Employees;
```

You should see the following output:

```
1991-02-02
```

Aggregate functions save you time and effort because they allow you to perform calculations on a set of values and return a single value. Pulling in all the data and performing calculations on it can be time consuming and resource intensive. 

> 💡 **Codelabs Learning Assistant:** [https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> - Need help understanding how aggregate functions like COUNT or AVG work? Ask the assistant to explain or show more examples using your own data.

### GROUP BY Clause

The `GROUP BY` clause is used to group the result set by one or more columns. The `GROUP BY` clause is often used with aggregate functions such as `AVG()`, `COUNT()`, `MAX()`, `MIN()` and `SUM()`. The following statement groups the result set by the `FirstName` column and returns the number of employees for each group:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (2, 'Doe', 'John', '1991-02-02', 'Jane Doe was born on February 2, 1991.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (3, 'Moe', 'John', '1992-03-03', 'Mary Doe was born on March 3, 1992.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (4, 'Doe', 'Mark', '1993-04-04', 'Mark Doe was born on April 4, 1993.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (5, 'Doe', 'Lisa', '1994-05-05', 'Lisa Doe was born on May 5, 1994.');
INSERT INTO Employees (EmployeeID, LastName, FirstName, BirthDate, Notes)
VALUES (6, 'Doe', 'Robert', '1995-06-06', 'Robert Doe was born on June 6, 1995.');

SELECT FirstName, COUNT(*) FROM Employees GROUP BY FirstName;
```

You should see the following output:

```
John|3
Lisa|1
Mark|1
Robert|1
```

Let's go over the SQL statement above:

-   `GROUP BY FirstName` is a clause that groups the result set by the `FirstName` column.
-   `SELECT FirstName, COUNT(*)` is a clause that specifies the columns that you want to select.
-   `FROM Employees` is a clause that specifies the table that you want to query data from.

The following statement groups the result set by the `FirstName` column and returns the number of employees for each group. It also sorts the groups in descending order by the number of employees:

```sql
SELECT FirstName, COUNT(*) FROM Employees GROUP BY FirstName ORDER BY COUNT(*) ASC;
```

You should see the following output:

```
Lisa|1
Mark|1
Robert|1
John|3
```

This is beneficial since it allows you to sort the groups in the result set. This can be useful for many reasons. For example, if you want to find the most popular first name, you can use the `GROUP BY` clause to group the result set by the `FirstName` column and return the number of employees for each group. This prevents you from extracting all the data and performing calculations on it. This can be time consuming and resource intensive. By using the `GROUP BY` clause, you can group the result set and reduce the amount of data that you need to download, and speed up your application.

### Having Clause

The `HAVING` clause is used to filter groups in the result set. The `HAVING` clause is often used with aggregate functions such as `AVG()`, `COUNT()`, `MAX()`, `MIN()` and `SUM()`. The following statement groups the result set by the `FirstName` column and returns the number of employees for each group. It also filters the groups that have more than 1 employee:

```sql
SELECT FirstName, COUNT(*) FROM Employees GROUP BY FirstName HAVING COUNT(*) > 1;
```

You should see the following output:

```
John|3
```

Let's go over the SQL statement above:

-   `HAVING COUNT(*) > 1` is a clause that filters groups that have more than 1 employee.

This can be beneficial since it allows you to filter groups in the result set. This can be useful for many reasons. For example, if you want to find the most popular first name, you can use the `HAVING` clause to filter groups that have more than 1 employee. This prevents you from extracting all the data and performing calculations on it. This can be time consuming and resource intensive. By using the `HAVING` clause, you can filter groups in the result set and reduce the amount of data that you need to download, and speed up your application.

#### Practice Problem

Create a table named `Students` with the following columns:

-   `StudentID` is an integer number that uniquely identifies each student
-   `LastName` is a variable-length character string that stores the last name of the student
-   `FirstName` is a variable-length character string that stores the first name of the student
-   `BirthDate` is a date value that stores the birth date of the student
-   `Notes` is a long text string that stores notes about the student
-   `GPA` is a floating-point number that stores the grade point average of the student

Insert the following rows into the `Students` table:

-   `StudentID` is 1, `LastName` is `Doe`, `FirstName` is `John`, `BirthDate` is `1990-01-01`, `Notes` is `John Doe was born on January 1, 1990.`, `GPA` is `3.5`
-   `StudentID` is 2, `LastName` is `Doe`, `FirstName` is `Jane`, `BirthDate` is `1991-02-02`, `Notes` is `Jane Doe was born on February 2, 1991.`, `GPA` is `3.6`
-   `StudentID` is 3, `LastName` is `Moe`, `FirstName` is `John`, `BirthDate` is `1992-03-03`, `Notes` is `Mary Doe was born on March 3, 1992.`, `GPA` is `3.7`
-   `StudentID` is 4, `LastName` is `Doe`, `FirstName` is `Mark`, `BirthDate` is `1993-04-04`, `Notes` is `Mark Doe was born on April 4, 1993.`, `GPA` is `3.8`
-   `StudentID` is 5, `LastName` is `Doe`, `FirstName` is `Lisa`, `BirthDate` is `1994-05-05`, `Notes` is `Lisa Doe was born on May 5, 1994.`, `GPA` is `3.9`

Select all rows from the `Students` table and return the average GPA of all students. Group the result set by the `FirstName` column and return the average GPA for each group. Filter the groups that have more than 1 student. Sort the groups in descending order by the average GPA.

<details>

<summary>Solution</summary>

```sql
CREATE TABLE Students (
    StudentID int,
    LastName varchar(255),
    FirstName varchar(255),
    BirthDate date,
    Notes text,
    GPA float
);

INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA)
VALUES (1, 'Doe', 'John', '1990-01-01', 'John Doe was born on January 1, 1990.', 3.5);
INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA)
VALUES (2, 'Doe', 'Jane', '1991-02-02', 'Jane Doe was born on February 2, 1991.', 3.6);
INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA)
VALUES (3, 'Moe', 'John', '1992-03-03', 'Moe John was born on March 3, 1992.', 3.7);
INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA)
VALUES (4, 'Doe', 'Mark', '1993-04-04', 'Mark Doe was born on April 4, 1993.', 3.8);
INSERT INTO Students (StudentID, LastName, FirstName, BirthDate, Notes, GPA)
VALUES (5, 'Doe', 'Lisa', '1994-05-05', 'Lisa Doe was born on May 5, 1994.', 3.9);

SELECT FirstName, AVG(GPA) FROM Students GROUP BY FirstName HAVING COUNT(*) > 1 ORDER BY AVG(GPA) DESC;
```

</details>

> 💡 **Codelabs Learning Assistant:** [https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> - Want more practice with SELECT, WHERE, or JOIN? Ask the assistant to generate new practice problems based on what you’ve learned.

### Introduction to Joins

A join clause is used to combine rows from two or more tables, based on a related column between them. Let's say you have two tables, `Employees` and `Departments`. The `Employees` table has the following columns:

-   `EmployeeID` is an integer number that uniquely identifies each employee
-   `LastName` is a variable-length character string that stores the last name of the employee
-   `FirstName` is a variable-length character string that stores the first name of the employee
-   `DepartmentID` is an integer number that uniquely identifies each department
-   `BirthDate` is a date value that stores the birth date of the employee
-   `Notes` is a long text string that stores notes about the employee
-   `Salary` is a floating-point number that stores the salary of the employee

The `Departments` table has the following columns:

-   `DepartmentID` is an integer number that uniquely identifies each department
-   `DepartmentName` is a variable-length character string that stores the name of the department
-   `ManagerID` is an integer number that uniquely identifies each manager
-   `Location` is a variable-length character string that stores the location of the department
-   `Budget` is a floating-point number that stores the budget of the department
-   `Notes` is a long text string that stores notes about the department
-   `Employees` is an integer number that stores the number of employees in the department

The `Employees` table has a column named `DepartmentID` that is related to the `DepartmentID` column in the `Departments` table. This is called a foreign key. A foreign key is a column or a group of columns in a table that uniquely identifies a row in another table. This creates a relationship between the two tables. This is called a one-to-many relationship and a one-to-many relationship is a relationship between two tables where one row in one table can be related to many rows in another table. For example, one department can have many employees.

The following statement creates the `Employees` table:

```sql
CREATE TABLE Employees (
    EmployeeID int,
    LastName varchar(255),
    FirstName varchar(255),
    DepartmentID int,
    BirthDate date,
    Notes text,
    Salary float
);

CREATE TABLE Departments (
    DepartmentID int,
    DepartmentName varchar(255),
    ManagerID int,
    Location varchar(255),
    Budget float,
    Notes text,
    Employees int
);

INSERT INTO Employees (EmployeeID, LastName, FirstName, DepartmentID, BirthDate, Notes, Salary)
VALUES (1, 'Doe', 'John', 1, '1990-01-01', 'John Doe was born on January 1, 1990.', 50000);
INSERT INTO Employees (EmployeeID, LastName, FirstName, DepartmentID, BirthDate, Notes, Salary)
VALUES (2, 'Doe', 'Jane', 1, '1991-02-02', 'Jane Doe was born on February 2, 1991.', 60000);

INSERT INTO Departments (DepartmentID, DepartmentName, ManagerID, Location, Budget, Notes, Employees)
VALUES (1, 'Sales', 1, 'New York', 1000000, 'The Sales department is located in New York.', 10);
INSERT INTO Departments (DepartmentID, DepartmentName, ManagerID, Location, Budget, Notes, Employees)
VALUES (2, 'Marketing', 2, 'Los Angeles', 2000000, 'The Marketing department is located in Los Angeles.', 20);

SELECT * FROM Employees, Departments;
```

You should see the following output:

```
1|Doe|John|1|1990-01-01|John Doe was born on January 1, 1990.|50000|1|Sales|1|New York|1000000|The Sales department is located in New York.|10
1|Doe|John|1|1990-01-01|John Doe was born on January 1, 1990.|50000|2|Marketing|2|Los Angeles|2000000|The Marketing department is located in Los Angeles.|20
2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000|1|Sales|1|New York|1000000|The Sales department is located in New York.|10
2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000|2|Marketing|2|Los Angeles|2000000|The Marketing department is located in Los Angeles.|20
```

Let's go over the SQL statement above:

-   `SELECT * FROM Employees, Departments` is a clause that specifies the columns that you want to select.

The query you're using with SELECT \* FROM Employees, Departments; is performing a cross join (also known as a Cartesian join) between the Employees and Departments tables. In a cross join, each row from the first table (Employees) is combined with each row from the second table (Departments), resulting in every possible combination of rows between the two tables.

Given that you have 2 rows in Employees and 2 rows in Departments, the cross join will produce 2 \* 2 = 4 rows. This is why you're seeing 4 rows in the result.

This isn't very useful, so let's look at some other types of joins.

### Inner Join

An inner join returns rows when there is a match in both tables. The following statement joins the `Employees` table with the `Departments` table based on the `DepartmentID` column:

```sql
SELECT * FROM Employees INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

You should see the following output:

```
1|Doe|John|1|1990-01-01|John Doe was born on January 1, 1990.|50000|1|Sales|1|New York|1000000|The Sales department is located in New York.|10
2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000|1|Sales|1|New York|1000000|The Sales department is located in New York.|10
```

Let's go over the SQL statement above:

-   `INNER JOIN` is a clause that combines rows from two or more tables.
-   `Employees` is a table that you want to join.
-   `Departments` is a table that you want to join.
-   `ON Employees.DepartmentID = Departments.DepartmentID` is a clause that specifies the columns that you want to join on.

In essence, an inner join is the intersection of two tables. It returns rows when there is a match in both tables. This is useful for many reasons. For example, if you want to find all employees that are in the Sales department, you can use the `INNER JOIN` clause to join the `Employees` table with the `Departments` table based on the `DepartmentID` column. This will return both employees that are in the Sales department including the department information. This prevents you from extracting all the data and performing calculations on it. By using the `INNER JOIN` clause, you can join the tables. This is powerful.

### Left Join

A left join returns all rows from the left table, and the matched rows from the right table. The difference between a left join and an inner join is that a left join returns all rows from the left table, even if there is no match in the right table. How do you tell between a left table and a right table? The left table is the table that is specified before the `LEFT JOIN` clause. The right table is the table that is specified after the `LEFT JOIN` clause.

The following statement joins the `Employees` table with the `Departments` table based on the `DepartmentID` column:

```sql
.
.
.
-- Change the DepartmentID of the first employee to 3
INSERT INTO Employees (EmployeeID, LastName, FirstName, DepartmentID, BirthDate, Notes, Salary)
VALUES (1, 'Doe', 'John', 3, '1990-01-01', 'John Doe was born on January 1, 1990.', 50000);
.
.
.
SELECT * FROM Employees LEFT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

You should see the following output:

    ```
    1|Doe|John|3|1990-01-01|John Doe was born on January 1, 1990.|50000||NULL|NULL|NULL|NULL|NULL|NULL
    2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000|1|Sales|1|New York|1000000|The Sales department is located in New York.|10
    ```

Let's go over the SQL statement above:

-   `LEFT JOIN` is a clause that combines rows from two or more tables.
-   `Employees` is a table that you want to join.
-   `Departments` is a table that you want to join.
-   `ON Employees.DepartmentID = Departments.DepartmentID` is a clause that specifies the columns that you want to join on.
-   The null values are the result of the left join. Since the first employee's departmentID is 3, and there is no department with an ID of 3, the left join returns null values for the department columns.

This is useful for many reasons. For example, if you want to find all employees that are in the Sales department, you can use the `LEFT JOIN` clause to join the `Employees` table with the `Departments` table based on the `DepartmentID` column. This will return both employees that are in the Sales department including the department information.

### Right Join

A right join returns all rows from the right table, and the matched rows from the left table. The difference between a right join and an inner join is that a right join returns all rows from the right table, even if there is no match in the left table. How do you tell between a left table and a right table? The left table is the table that is specified before the `RIGHT JOIN` clause. The right table is the table that is specified after the `RIGHT JOIN` clause.

The following statement joins the `Employees` table with the `Departments` table based on the `DepartmentID` column:

```sql

SELECT * FROM Employees RIGHT JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

### Full Join

A full join returns all rows when there is a match in one of the tables. This means that if there are rows in the left table that do not have matches in the right table, those rows will be included in the result set, and vice-versa. If there is a match between the two tables, the full join combines columns from the two tables into a single row. The following statement joins the `Employees` table with the `Departments` table based on the `DepartmentID` column:

```sql
SELECT * FROM Employees FULL JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
```

### Self Join

A self join is a join that is used to join a table to itself. The following statement joins the `Employees` table with itself based on the `DepartmentID` column:

```sql
SELECT * FROM Employees e1 INNER JOIN Employees e2 ON e1.DepartmentID = e2.DepartmentID;
```

You should see the following output:

```
1|Doe|John|3|1990-01-01|John Doe was born on January 1, 1990.|50000|1|Doe|John|3|1990-01-01|John Doe was born on January 1, 1990.|50000
2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000|2|Doe|Jane|1|1991-02-02|Jane Doe was born on February 2, 1991.|60000
```

Let's go over the SQL statement above:

-   `e1` is an alias for the `Employees` table.
-   `e2` is an alias for the `Employees` table.
-   `INNER JOIN` is a clause that combines rows from two or more tables.
-   `Employees` is a table that you want to join.
-   `ON e1.DepartmentID = e2.DepartmentID` is a clause that specifies the columns that you want to join on.

#### Practice Problem

Imagine you have a database for a bookstore. The database includes the following tables:

-   Authors: Contains data about authors.

    -   Columns: AuthorID (primary key), AuthorName

-   Books: Contains data about books.

    -   Columns: BookID (primary key), Title, AuthorID (foreign key), PublicationYear

-   Sales: Contains data about book sales.
    -   Columns: SaleID (primary key), BookID (foreign key), QuantitySold, SaleDate

Task
Write SQL queries to perform the following tasks:

List of Books and Authors:

Write a query to display a list of all books, including their titles and the names of their authors.
Use an INNER JOIN to combine data from the Books and Authors tables.

Books with No Sales:

Write a query to find all books that have never been sold.
Use a LEFT JOIN between Books and Sales and look for records where there are no corresponding sales entries.

Total Sales for Each Book:

Write a query to calculate the total quantity sold for each book.
Use an INNER JOIN to combine Books and Sales, and then use a GROUP BY clause with an aggregate function (SUM) to calculate total sales.

Sales Data for a Specific Year:

Write a query to display the sales data (book title and quantity sold) for all books sold in a specific year (e.g., 2021).
This will require joining all three tables and filtering based on SaleDate.

<details>

<summary>Solution</summary>

```sql
CREATE TABLE Authors (
    AuthorID int,
    AuthorName varchar(255)
);

CREATE TABLE Books (
    BookID int,
    Title varchar(255),
    AuthorID int,
    PublicationYear int
);

CREATE TABLE Sales (
    SaleID int,
    BookID int,
    QuantitySold int,
    SaleDate date
);

INSERT INTO Authors (AuthorID, AuthorName)
VALUES (1, 'Jane Doe');
INSERT INTO Authors (AuthorID, AuthorName)
VALUES (2, 'John Doe');

INSERT INTO Books (BookID, Title, AuthorID, PublicationYear)
VALUES (1, 'Book 1', 1, 2021);
INSERT INTO Books (BookID, Title, AuthorID, PublicationYear)
VALUES (2, 'Book 2', 2, 2020);

INSERT INTO Sales (SaleID, BookID, QuantitySold, SaleDate)
VALUES (1, 1, 10, '2021-01-01');
INSERT INTO Sales (SaleID, BookID, QuantitySold, SaleDate)
VALUES (2, 1, 20, '2021-02-02');

SELECT * FROM Books INNER JOIN Authors ON Books.AuthorID = Authors.AuthorID;

SELECT * FROM Books LEFT JOIN Sales ON Books.BookID = Sales.BookID WHERE Sales.BookID IS NULL;

SELECT Title, SUM(QuantitySold) FROM Books INNER JOIN Sales ON Books.BookID = Sales.BookID GROUP BY Title;

SELECT Title, QuantitySold FROM Books INNER JOIN Sales ON Books.BookID = Sales.BookID WHERE YEAR(SaleDate) = 2021;
```

</details>

> 💡 **Codelabs Learning Assistant:** [https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> - Confused about SQL syntax or why a query isn’t working? Share your SQL code with the assistant for step-by-step help.

## Summary

In this chapter, we have covered the fundamentals of databases and SQL. We have learned about the different types of databases, and the different ways of organizing data in a database using SQL (Structured Query Language). We have also learned about the different types of SQL databases, and the differences between them.

We have covered the following topics:

-   Introduction to Databases
-   Database Management Systems
-   Types of Databases
-   When to use a relational database vs a non-relational database
-   Different types of SQL databases
-   Introduction to SQL
-   Creating Tables
-   Inserting Data
-   Selecting Data
-   Where Clause
-   Order By Clause
-   Limit Clause
-   Aggregate Functions
-   GROUP BY Clause
-   Having Clause
-   Introduction to Joins
-   Inner Join
-   Left Join
-   Right Join
-   Full Join
-   Self Join

You should now have a good understanding of the fundamentals of databases and SQL, and be able to apply these concepts to real-world situations. In the following chapters, we will cover more advanced topics in SQL, and how to use SQL to solve complex problems.

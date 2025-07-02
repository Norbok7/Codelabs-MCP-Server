---
title: Ruby Fundamentals Part 1
---

# Ruby Fundamentals - Part 1

<img src="https://miro.medium.com/v2/resize:fit:540/1*7e9D-oPWPIKBe2AQv862aA.png" />

**Table of Contents**

-   Introduction to Back-End Development
-   Introduction to Ruby: Then and Now
-   Using Replit for Ruby
-   Installing Ruby
-   Running Your First Ruby Script in Visual Studio Code (VS Code)
-   How to Effectively Learn Ruby or Any Programming Language
-   Ruby Fundamentals: Understanding Data Types in Programming
-   Ruby Primitive Data Types
-   Ruby variables
-   Arithmetic Operators
-   Conditional Operators & Control Flow
-   Loops
-   Built-In methods in Ruby
-   Testing with Rspec
-   Practice Exercises

## Introduction to Back-End Development

Before diving into the intricacies of Ruby, it's essential to understand the context in which it often operates - back-end development. The world of web development is typically divided into two main areas: front-end and back-end.

Front-End Development is what users see and interact with on a website or application. It involves everything that users experience directly: from text and colors to buttons, images, and navigation menus. Front-end developers work with languages like HTML, CSS, and JavaScript to create visually appealing and interactive user interfaces. They also use frameworks like React, Vue, and Angular to build complex web applications.

Other programming languages like Ruby and or Python can also be used for front-end development. Front-end developers are responsible for creating a seamless user experience and are often involved in the design process. Optimization and performance are also crucial aspects of front-end development.

Back-End Development or back-end, on the other hand, is where all the data processing happens and is not visible to users. It's the part of a website or application that runs on the server and deals with data storage and retrieval, server-side logic, database interactions, user authentication, and more. Back-end developers use server-side languages like Ruby, Python, Java, and PHP to build the logic that powers the front-end.

In this curriculum, we will be focusing on back-end development with Ruby. Ruby, particularly with the Ruby on Rails framework, is a powerful tool for back-end development. It enables developers to build complex, data-driven applications efficiently. Ruby's readability and elegant syntax make it a favorite for rapid development and prototyping. Ruby on Rails is also renowned for its convention over configuration approach, which allows developers to focus on the application's logic rather than the configuration details. Ruby on Rails is a popular choice for building web applications, and it powers many well-known websites and applications, including Airbnb, GitHub, Shopify, and Basecamp.

You can use Ruby on Rails as a back-end for your front-end applications, or you can use Ruby on Rails to build a complete web application. We will explore Ruby on Rails in more detail in the upcoming classes. For now, let's focus on learning the fundamentals of Ruby.

## Introduction to Ruby: Then and Now

### The Genesis of Ruby

Ruby, a language designed in the mid-1990s by Yukihiro "Matz" Matsumoto in Japan. Matz, dissatisfied with the languages available at the time, sought to create a language that was both powerful and easy to read and write. Ruby was born out of this vision, combining elements from his favorite languages (Perl, Smalltalk, Eiffel, Ada, and Lisp).

### Key Philosophy:

Ruby was developed with a focus on simplicity and productivity. It follows the principle of "least astonishment," which means the language is designed to behave in a way that minimizes confusion for new or experienced programmers. The core philosophy of Ruby is to make programming enjoyable and to provide happiness to programmers.

### Ruby's Evolution

Over the years, Ruby has evolved significantly. The release of Ruby on Rails (RoR) in 2005, a powerful web application framework, marked a pivotal moment, bringing Ruby into the limelight. RoR emphasized convention over configuration, and its "Don't Repeat Yourself" (DRY) principle resonated with developers, leading to widespread adoption and a vibrant community.

### Present-Day Ruby:

Today, Ruby is renowned for its elegance, simplicity, and the readability of its code. It remains a popular choice for web development, scripting, and data processing. The language's community continues to grow, contributing to its rich ecosystem of gems (libraries) that extend its functionality.

Ruby's modern implementations are more performant, and its community-driven updates ensure it stays relevant. Whether in web development, automation, or new domains like data science, Ruby adapts and thrives, making it a timeless choice for developers seeking an expressive, efficient, and enjoyable programming language.

## How to Effectively Learn Ruby or Any Programming Language

As you delve into the world of Ruby, here are some key tips to enhance your learning experience:

Follow Along Practically: While reading the material, try to code along. This practical application reinforces your understanding of the concepts.

Take Notes: Writing down key points and concepts helps in retaining information and serves as a quick reference for future use.

-   Experiment and Explore: Don't hesitate to experiment with the code. Try modifying examples or creating simple programs to understand how different elements of Ruby work.

-   Use Online Resources: Supplement your learning with online resources like documentation, forums, and video tutorials. Websites like Ruby-Doc.org and Stack Overflow are great places to start.

-   Take Breaks and Stay Healthy: Regular breaks are essential to prevent burnout. Remember to step away from your computer, stretch, and relax your mind.

-   Practice Problem-Solving: Work on small projects or solve coding challenges. Sites like Exercism and LeetCode offer Ruby challenges for various skill levels.

-   Stay Curious and Patient: Learning to code can be challenging, but curiosity and patience are key. Embrace mistakes as learning opportunities.

Where and how do we run our Ruby code?
There are two options:

1. Using Replit
2. Using your local machine

We will show you both options and in case you are having issues, you can use Replit for now until an instructor helps you set up your local machine. But we advise you to try to set up your local machine as it will be beneficial for your learning journey.

## Using Replit to Run Ruby Code

Replit is an online code editor and IDE that allows you to write, run, and share code in your browser. It's a great tool for learning and experimenting with Ruby. You can use Replit to run Ruby code without installing anything on your computer.

Navigate to and create an account with [replit](https://replit.com/new).

Once you have gone through the step by step sign up process, please look for choose a template to start off. 

Use the provided images to help. 

1. <img src="https://imgur.com/hvzjFmd.png"/>
2. <img src="https://imgur.com/euatFTo.png"/>
3. <img src="https://imgur.com/2aE02nS.png"/>

Search ruby and start from scratch.

To run your code, click on the "Run" button at the top of the editor. You will see the output of your code in the console below.

Once you have done that, you can begin coding! Let's go through some basic Ruby things!

## Installing Ruby

Installing Ruby can be a bit tricky, but we have some exceptional resources to help you out!

### Windows

If you are a windows computer, I recommend watching this [video](https://youtu.be/9RsdAzLQ3Dk) to help you install Ruby on your machine.

Below are the instructions to install Ruby on windows from the video.

1. In windows search bar, search `Turn Windows features on or off`
    - Check `Windows Subsystem for Linux`
    - Check `Virtual Machine Platform`
    - Check `Windows Hypervisor Platform`
    - Click `ok`
2. Restart computer
3. Run Windows Powershell or windows command prompt as an **administrator**.
4. In the terminal, run `wsl --install -d Ubuntu`, it may ask you to make an account. Make an account and remember the password. An Ubuntu terminal should open up.
5. Go to [https://rvm.io/rvm/install](https://rvm.io/rvm/install)
6. On the website, where it says 'Install GPG keys', copy the two commands and enter it into the ubuntu terminal. Continue even if you get errors. It might not work.
7. Go to [https://rvm.io/rvm/security](https://rvm.io/rvm/security), under alternatives, copy and paste the commands into the ubuntu terminal.
8. Enter `\curl -sSL https://get.rvm.io | bash ` in your Ubuntu terminal.
9. restart the terminal and search for ubuntu in your windows finder
10. Enter `rvm -v` to check if rvm is installed
11. Enter `rvm install ruby 3.2.0`
12. Open VS Code (restart if already open) and open a new terminal. The terminal needs to be the Ubuntu terminal to access ruby.
13. Once, open enter `ruby -v` to check if ruby is installed.

### Mac

-   https://www.theodinproject.com/lessons/ruby-installing-ruby

#### Running Your First Ruby Script in Visual Studio Code (VS Code)

1. Open VS Code
2. Open a new terminal
3. Enter `ruby -v` to check if ruby is installed
4. Enter `ruby -e "puts 'Hello, World!'"` to run your first ruby script
5. You should see `Hello, World!` printed in the terminal

Now let's create a new file and run a ruby script.

1. Create a new file and save it as `hello_world.rb`
2. Add the following code to the file:

```ruby
puts 'Hello, World!'
```

3. Run the script by entering `ruby hello_world.rb` in the terminal
4. You should see `Hello, World!` printed in the terminal

### Comments

Comments are lines of text that are ignored by the computer. They are used to add notes and explanations to code, making it easier to understand and maintain. Comments are crucial for writing clean, readable code.

In Ruby, comments are created using the # symbol. Any text after the # symbol is ignored by the computer.

```ruby
# This is a comment
```

We will use comments throughout this course to provide additional information in the code examples.

## Ruby Fundamentals: Understanding Data Types in Programming

Now that you have Ruby installed and executed your first script, let's dive into the fundamentals of the language. We'll start by exploring data types, which are the building blocks of any programming language. Data types are the different kinds of information that we can store and manipulate in our programs. Ruby has a rich set of data types, which we'll explore in this lesson.

### What Are Data Types?

Data types are a fundamental concept in programming, crucial for defining the nature and operations of data that can be processed within a program. Essentially, a data type is a classification that dictates what sort of value a variable can hold and how the computer interprets that value. For example, a variable can hold a string of characters, a number, or a Boolean (true or false). The data type determines what operations can be performed on the data, and how the data is stored in memory.

### Why Are Data Types Important?

**Memory Management**: Data types help in allocating and managing memory in efficient ways. Different types of data consume different amounts of memory, and specifying data types allows the computer to allocate just the right amount.

**Operation Validity**: They define what operations can be performed on a set of data. For example, arithmetic operations are typically valid on numbers, but not on text strings or booleans.

**Error Prevention**: By specifying data types, programmers can prevent errors. For example, trying to perform a mathematical operation on a text string would be nonsensical and could lead to errors if not properly handled.

**Code Readability and Maintenance**: Knowing the types of data being dealt with makes code easier to understand and maintain. It's clearer what kind of data is passed around and manipulated in the program.

### Common Data Types in Programming

While different programming languages have various data types, some common ones include:

**Numbers**: This broad category often includes integers (whole numbers) and floats (numbers with decimal points). They are used for arithmetic operations and calculations.

**Strings**: Strings represent textual data. They can include letters, numbers, and various symbols, typically used for storing and manipulating text.

**Booleans**: This type represents truth values, typically true and false. Booleans are fundamental in control structures and decision-making in programming.

**Arrays** (or Lists): Arrays are collections of elements, where each element is of a consistent type. They are used to store and manipulate lists of data.

**hashes** (or Dictionaries): Hashes are collections of key-value pairs, where each key is unique. They are used to store and manipulate data in the form of key-value pairs.

**Null or Nil Values**: These represent the absence of a value or a 'nothing' state. They are used to denote that a variable currently holds no valid data.

## Ruby Primitive Data Types

Primitive data types are the basic types of data with which most languages start. Examples include integers, floats, booleans, and characters. They are often directly supported by the underlying hardware and represent single values.

Here are a list of primitive data types in Ruby:

### Strings

Strings are used to represent textual data. They are typically enclosed in single or double quotes. For example:

```ruby
"Hello World"
'Hello World'
```

In Ruby, how you quote your strings - whether with single quotes `(' ')` or double quotes `(" ")` - can affect their behavior, particularly in terms of escape sequences and string interpolation.

Single-quoted strings in Ruby are simpler and more literal compared to their double-quoted counterparts. They are best used when you need a string exactly as it is, without any additional processing.

```ruby
puts 'Hello\nWorld'  # Output: Hello\nWorld
```

In the example, the \n is not interpreted as a newline character but is printed as is.

Double-quoted strings, on the other hand, are more flexible and allow for escape sequences and string interpolation. Escape sequences are special characters that are preceded by a backslash `(\)` to denote a special meaning. For example, \n represents a newline character, \t represents a tab, and `\\` represents a backslash.

```ruby
name = "Ruby"
puts "Hello, #{name}!\nWelcome to programming!"
# Output: Hello, Ruby!
#         Welcome to programming!
```

#### Practice Problem

Print your full name as a string to the terminal.

`John Doe`

### Numbers

Numbers are fundamental in any programming language, and Ruby provides a rich set of numerical data types to handle various numerical operations. In Ruby, numbers mainly fall into two categories: integers and floating-point numbers.

#### Integers

Integers are whole numbers without a decimal point. They can be positive, negative, or zero. Ruby handles integers very efficiently and they can be used for counting, iterating, and various other mathematical operations.

Example of integers in Ruby:

```ruby
42
-10
0
```

Ruby integers can be of any length, limited only by the memory size of your machine.

#### Floating-Point Numbers

Floating-point numbers, or floats, are numbers with a decimal point. They are used when more precision is required, such as in scientific calculations or when working with fractions.

Example of floating-point numbers in Ruby:

```ruby
3.14
-0.001
2.0
```

We can perform various mathematical operations on numbers in Ruby which you will explore shortly.

### Booleans

Booleans represent a simple yet powerful concept in programming, used to track truthiness or falsity of conditions. In Ruby, booleans come in two flavors: true and false.

-   true: This is a Ruby object that represents truth. It is an instance of the TrueClass.
-   false: Represents falsehood and is an instance of the FalseClass.

Ruby has a simple but strict rule about what values are considered true or false. Unlike some languages, in Ruby, only false and nil (Ruby's way of saying "nothing" or "no value") are treated as false in conditional expressions. Every other value, including 0, "" (empty string), and [] (empty array), is considered true.

```ruby
true
false
```

### Complex Data Types

Complex data types these types are more sophisticated and can represent a collection of values or more complex entities. Arrays, lists, objects, and dictionaries are examples of complex data types. They are constructed using primitive data types and other complex data types.

Here are a list of complex data types in Ruby:

### Arrays

Arrays are versatile and essential data structures in Ruby, used to store collections of items. These items can be of any type, including numbers, strings, or even other arrays and more.

An array is an ordered list of elements. Each element in an array is associated with an index, which is a numerical representation of the item's position in the list.

Arrays can be created in several ways in Ruby:

-   Using Square Brackets: The most common way to create an array is with square brackets [].

```ruby
numbers = [1, 2, 3, 4, 5]
words = ['hello', 'world']
mixed = [1, 'two', 3.0, [4, 'five']]
```

-   Using the Array.new Method: This method creates an array with specified size and default value.

```ruby
empty_array = Array.new(3)  # => [nil, nil, nil]
zeros = Array.new(3, 0)     # => [0, 0, 0]
```

#### Accessing Elements

Elements in an array are accessed using their index. Ruby arrays are zero-indexed, meaning the first element is at index 0.

```ruby
array = [10, 20, 30, 40, 50]
puts array[0]   # => 10
puts array[2]   # => 30
puts array[-1]  # => 50 (last element)
```

#### Modifying Arrays

Adding Elements: Elements can be added to an array using methods like push, `<<` or insert.

```ruby
array = []
array.push(1)
array << 2
array.insert(1, 1.5)  # => [1, 1.5, 2]
```

There are various other ways to modify an array, including removing elements, replacing elements, and more. We will explore these in more detail later.

### Hashes

Hashes, also known as associative arrays or dictionaries in other languages, are collections of key-value pairs. They are similar to objects in that they store data in a structured way, but they are not the same as objects created from custom classes.

-   Key-Value Pairs: Each entry in a hash consists of a key and a value. The key is used to retrieve the corresponding value.
-   Flexible Keys and Values: Hash keys and values can be objects of any type, including numbers, strings, or even arrays.

Creating a hash in Ruby is straightforward:

```ruby
my_hash = {
  'name' => 'Alice',
  'age' => 30,
  'is_student' => true
}
```

You can access or modify hash values using their keys:

```ruby
puts my_hash['name'] # => Alice
my_hash['age'] = 31 # Update the age
```

Ruby allows the use of symbols as hash keys, which is a common practice due to their efficiency and readability:

```ruby
student = {
:name => 'Bob',
:grade => 'A'
}
```

Newer syntax:

```ruby
student = {
name: 'Bob',
grade: 'A'
}
```

### The special case of 'nil' in Ruby

In Ruby, nil plays a unique and essential role. It is a value that represents the concept of "nothing" or "no value". Understanding nil is crucial for effective Ruby programming, as it frequently appears in various contexts.

-   Common Usage: It's commonly returned by methods that have no meaningful value to return, or when an operation, such as searching an array, does not yield a result.

```ruby
nil
```

## Ruby variables

Variables are fundamental in programming, serving as placeholders for storing data values. In Ruby, variables are particularly versatile and easy to use, adhering to Ruby's principle of making coding natural and intuitive.

### What are Variables?

-   Storage Containers: Variables are like containers where you can store data. Once a value is assigned to a variable, you can use the variable's name to access that value.

-   Dynamically Typed: Ruby is a dynamically typed language, meaning you don't need to declare a variable's type beforehand. The type is inferred at runtime.

### Types of Variables in Ruby

Ruby has different types of variables, each with its own scope and purpose:

Local Variables begin with a lowercase letter or an underscore. Their scope is limited to the block, method, or class in which they are defined.

```ruby
local_var = "I'm local"
```

Constant variables are a special type of variable whose value cannot be changed once assigned. They begin with an uppercase letter.

```ruby
CONSTANT_VAR = 3.14
```

You assign a value to a variable using = and if you need to reassign a variable, you can simply assign a new value to it.

```ruby
my_var = 10
my_var = "Now I'm a string"
```

#### Variable Naming Conventions

-   Meaningful Names: Choose names that make your code readable and descriptive.
-   Snake_case for Variables: Use lowercase letters with underscores to separate words.

```ruby
total_amount = 100
user_name = "Alice"
```

#### Practice Problem

Declare a local variable called `my_name` and assign it your full name as a string.
Declare a constant variable called `PI` and assign it the value of pi `(3.14)`.

Print both variables to the terminal.

## Arithmetic Operators

Arithmetic operations are a fundamental aspect of programming, allowing for the manipulation and calculation of numeric data.

-   Addition `(+)`: Adds two numbers.
-   Subtraction `(-)`: Subtracts the second number from the first.
-   Multiplication `(\*)`: Multiplies two numbers.
-   Division `(/)`: Divides the first number by the second. In Ruby, the result of dividing two integers is an integer. To get a decimal result, at least one of the operands must be a float.
-   Exponentiation `(\*\*)`: Raises a number to the power of another number.
-   Modulus `(%)`: Returns the remainder of dividing the first number by the second.

To simple use the arithmetic operators in Ruby, you can simply use the operator between two numbers. For example:

```ruby
addition = 5 + 3        # => 8
subtraction = 5 - 3     # => 2
multiplication = 5 * 3  # => 15
division = 10 / 2       # => 5
float_division = 10.0 / 3  # => 3.3333333333333335
exponent = 2 ** 3       # => 8
modulus = 10 % 3        # => 1
```

#### Division Quirks

Integer Division: When dividing two integers, Ruby performs integer division, meaning it will return an integer and truncate any decimal part.

```ruby
result = 10 / 4 # => 2
float_result = 10 / 4.0 # => 2.5
```

Variables can be used in place of literal numbers in arithmetic operations.

```ruby
x = 10
y = 5
sum = x + y       # => 15
difference = x - y  # => 5
```

#### Order of Operations

The order of operations in Ruby is the same as in mathematics. The following table lists the order of operations from highest to lowest precedence.

Here's an example

```ruby
  result = 10 + 5 * 3  # => 25
```

#### Compound Assignment Operators

Ruby also supports compound assignment operators, which combine an arithmetic operation with assignment.

```ruby
a = 10
a += 5  # Equivalent to a = a + 5
a -= 2  # Equivalent to a = a - 2
```

#### strings and arithmetic operators

Strings can be concatenated (joined together) using the + operator or the `<<` operator. The + operator creates a new string, while the `<<` operator modifies the original string.

```ruby
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # => "John Doe"
first_name << last_name  # => "JohnDoe"
```

You don't typically use the shovel operator`<<` with strings, but it's useful to know that it exists.

String interpolation is another way to combine strings. It allows you to embed Ruby expressions within a string. To use string interpolation, you need to use double quotes.

```ruby
first_name = "John"
last_name = "Doe"
full_name = "#{first_name} #{last_name}"  # => "John Doe"
```

In Ruby, trying to add a number directly to a string will result in a TypeError because Ruby does not implicitly convert types during arithmetic

```ruby
"Hello" + 3 # => TypeError
```

#### Practice Problem

Write a Ruby script that calculates and prints the area of a rectangle with a width of 10 and a height of 5.

Write a Ruby script that combines a string and a number. It should create a string that includes a number in it through interpolation and then print it.

### Conditional Operators & Control Flow

Conditional operators are used to perform different actions based on different conditions. They are a fundamental aspect of programming, allowing for decision-making and control flow. These operators evaluate an expression to true or false, and are essential for controlling the flow of a Ruby program.

Here are some common conditional operators in Ruby:

-   Equal to `==`: Checks if two values are equal.
-   Not equal to `!=`: Checks if two values are not equal.
-   Greater than (>): Checks if the first value is greater than the second.
-   Less than `<` : Checks if the first value is less than the second.
-   Greater than or equal to `>=`: Checks if the first value is greater than or equal to the second.
-   Less than or equal to `<=`: Checks if the first value is less than or equal to the second.
-   Combined Comparison `<=>`: Checks if the first value is less than, equal to, or greater than the second. It returns 0 if the values are equal, 1 if the first value is greater, and -1 if the first value is less.

```ruby
5 == 5  # => true
5 == 6  # => false

5 != 6  # => true
5 != 5  # => false

5 > 3   # => true
5 < 3   # => false

5 >= 5  # => true
5 <= 4  # => false
```

### Logical Operators

Logical operators are used to combine multiple conditions. They are typically used in conditional statements to determine whether a statement or condition is true or false.

-   And (&&): Returns true if both conditions are true.
-   Or (||): Returns true if either condition is true.
-   Not (!): Returns true if the condition is false.

```ruby
true && true    # => true
true && false   # => false
false && false  # => false

true || true    # => true
true || false   # => true
false || false  # => false

!true   # => false
!false  # => true
```

The ternary operator is another conditional operator that is used to shorten if/else statements. It is a shorthand way of writing an if/else statement in a single line.

Here is the syntax of the ternary operator:

```ruby
condition ? true_value : false_value
```

The '?' represents the if, and the ':' represents the else. The condition is evaluated, and if it is true, the true_value is returned. Otherwise, the false_value is returned.

```ruby
age = 18
age >= 18 ? "You can vote!" : "You can't vote."
```

You can combine conditional and logical operators to create more complex conditions.

```ruby
age = 18
age >= 18 && age <= 60  # => true
age >= 18 || age <= 60  # => true
```

### Control Flow with Conditional Statements

Control flow in programming refers to the order in which individual statements, instructions, or function calls are executed or evaluated. In Ruby, as in other programming languages, control flow dictates how a program moves from one statement to another, makes decisions, or repeats certain operations based on specific conditions or loops.

-   **Decision Making**: Control flow allows a program to choose different paths of execution based on conditions, which is fundamental for creating dynamic and responsive programs.

-   **Repeating Operations**: With loops, control flow enables the repetition of tasks without writing redundant code, making programs more efficient and concise.

-   **Order of Execution**: It determines the sequence in which the code is executed, which is crucial for the logical flow and correctness of the program.

Conditional statements execute different code based on certain conditions. These are crucial for adding decision-making capabilities to your code. In Ruby, conditional statements are created using the if, if/else, if/elsif/else, and case statements.

-   **The if Statement**: The if statement is the most basic form of conditional execution. It runs the code block only if the condition is true.

```ruby
if condition
  # code to execute if condition is true
end
```

```ruby
temperature = 30
if temperature > 25
  puts "It's a hot day!"
end

```

-   **The if/else Statement**: The if/else statement allows you to execute different code blocks based on a condition. If the condition is true, the if block is executed. Otherwise, the else block is executed.

```ruby
if condition
  # code to execute if condition is true
else
  # code to execute if condition is false
end
```

```ruby
temperature = 30
if temperature > 25
  puts "It's a hot day!"
else
  puts "It's not a hot day."
end
```

-   **The elsif Statement**: The elsif statement allows you to check multiple conditions. It is used in conjunction with the if statement and must come before the else block.

```ruby
if condition1
  # code to execute if condition1 is true
elsif condition2
  # code to execute if condition2 is true
else
  # code to execute if both conditions are false
end
```

```ruby
temperature = 30
if temperature > 25
  puts "It's a hot day!"
elsif temperature < 10
  puts "It's a cold day!"
else
  puts "It's not a hot day."
end
```

You can chain as many elsif statements as you need. Keep in mind that only one condition will be executed, and the rest will be skipped.

-   **The unless Statement**: The unless statement is the opposite of the if statement. It executes the code block only if the condition is false.

```ruby
unless condition
  # code to execute if condition is false
end
```

```ruby
age = 18
unless age < 18
  puts "You can vote!"
end
```

-   **The case Statement**: The case statement is used to compare a value against multiple conditions. It is similar to the if/elsif/else statement, but it is more concise and easier to read.

```ruby
case value
when condition1
  # code to execute if condition1 is true
when condition2
  # code to execute if condition2 is true
else
  # code to execute if none of the conditions are true
end
```

```ruby
age = 18
case age
when 0..12
  puts "You're a child."
when 13..18
  puts "You're a teenager."
else
  puts "You're an adult."
end
```

The '0..12' and '13..18' are called ranges. They are used to check if a value falls within a certain range. In this case, the first when condition checks if the age is between 0 and 12, and the second when condition checks if the age is between 13 and 18. The else block is executed if none of the conditions are true. You can have as many when conditions as you need.

### Practice Problem

Write a Ruby script that checks if a number is positive, negative, or zero. If it is a positive number, print "positive". If it is a negative number, print "negative". Otherwise, print "zero".

### Loops

Loops are a fundamental aspect of programming in Ruby as well as other programming languages, allowing for the repetition of a block of code. They are crucial for automating repetitive tasks and processing collections of data. In Ruby, there are several types of loops, including while, until, for, and each.

-   while Loop: Repeats a block of code as long as a specified condition is true.

```ruby
while condition
  # code to execute
end
```

The 'while' keyword is followed by a condition. The code block is executed repeatedly as long as the condition is true. The condition is evaluated before each iteration, and if it is false, the loop is terminated. The 'end' keyword marks the end of the loop or block.

```ruby
i = 0
while i < 5
  puts i
  i += 1
end

# Output: 0 1 2 3 4
```

Here is what happens in the example:

1. The variable i is initialized to 0.
2. The condition i < 5 is evaluated. Since i is 0, the condition is true, and the code block is executed.
3. The value of i is printed to the terminal.
4. The value of i is incremented by 1.
5. The condition i < 5 is evaluated again. Since i is now 1, the condition is true, and the code block is executed again.
6. Steps 3-5 are repeated until i is 5. At this point, the condition i < 5 is false, and the loop is terminated.

-   until Loop: Repeats a block of code as long as a specified condition is false.

```ruby
until condition
  # code to execute
end
```

```ruby
i = 0
until i >= 5
  puts i
  i += 1
end

# Output: 0 1 2 3 4
```

-   for Loop: Repeats a block of code for a specified number of times.

```ruby
for variable in range
  # code to execute
end
```

```ruby
for i in 0..4
  puts i
end

# Output: 0 1 2 3 4
```

-   each Loop: Repeats a block of code for each element in a collection.

```ruby

collection.each do |variable|
  # code to execute
end
```

```ruby
[1, 2, 3, 4, 5].each do |i|
  puts i
end

# Output: 1 2 3 4 5
```

### Loop Control Statements

Loop control statements are used to alter the flow of a loop. They allow you to break out of a loop, skip an iteration, or execute a loop forever.

-   break Statement: Terminates the loop and exits the block.

```ruby
while condition
  # code to execute
  break
end
```

```ruby
i = 0
while i < 5
  puts i
  break if i == 2
  i += 1
end

# Output: 0 1 2
```

-   next Statement: Skips the rest of the current iteration and continues with the next iteration.

```ruby
while condition
  # code to execute
  next
end
```

```ruby
i = 0
while i < 5
  i += 1
  next if i == 2
  puts i
end

# Output: 1 3 4 5
```

### Practice Problem

Write a Ruby script that prints the numbers from 1 to 20. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

### Built-In methods in Ruby

A method is a set of instructions that can be called on an object. Objects are something we haven't covered in this lesson but will explore in more detail later. For now, you can think of them as a collection of data and methods that operate on that data. A method is a reusable block of code that performs a specific task. Ruby provides a rich set of built-in methods that are useful for various tasks. These methods are available by default and can be used without requiring any additional libraries. In this lesson, we'll explore some of the most common built-in methods in Ruby.

### puts and print

puts and print are two of the most commonly used methods in Ruby. They are used to print data to the terminal.

```ruby
puts "Hello, world!"

print "Hello, world!"
```

There are methods that exist on data types like strings and numbers. For example, the length method returns the length of a string.

```ruby
"Hello, world!".length  # => 13
```

### String Methods

Strings are a fundamental data type in Ruby, and there are many built-in methods that operate on strings. Here are some of the most common string methods:

-   length: Returns the length of the string.
-   strip: Returns a copy of the string with leading and trailing whitespace removed.
-   split: Splits the string into an array of substrings based on a delimiter, such as a space or comma.
-   start_with?: Checks if the string starts with a specified substring.
-   end_with?: Checks if the string ends with a specified substring.
-   include?: Checks if the string contains a specified substring.
-   upcase: Returns a copy of the string with all lowercase letters replaced with uppercase letters.
-   downcase: Returns a copy of the string with all uppercase letters replaced with lowercase letters.
-   capitalize: Returns a copy of the string with the first character converted to uppercase and the remainder to lowercase.
-   gsub: Returns a copy of the string with all occurrences of a pattern replaced with another string.
-   to_i: Converts the string to an integer.
-   to_f: Converts the string to a floating-point number.

```ruby
"Hello, world!".length  # => 13
" Hello, world! ".strip  # => "Hello, world!"
"Hello, world!".split(",")  # => ["Hello", " world!"]
"Hello, world!".start_with?("Hello")  # => true
"Hello, world!".end_with?("world!")  # => true
"Hello, world!".include?("world")  # => true
"Hello, world!".upcase  # => "HELLO, WORLD!"
"Hello, world!".downcase  # => "hello, world!"
"hello, world!".capitalize  # => "Hello, world!"
"Hello, world!".gsub("world", "Ruby")  # => "Hello, Ruby!"
"10".to_i  # => 10
"10.5".to_f  # => 10.5
```

### Number Methods

Numbers are another fundamental data type in Ruby, and there are many built-in methods that operate on numbers. Here are some of the most common number methods:

-   +: Addition
-   -: Subtraction
-   \*: Multiplication
-   /: Division
-   %: Modulus
-   \*\*: Exponentiation
-   abs: Returns the absolute value of a number.
-   round: Rounds a floating-point number to the nearest integer.
-   floor: Returns the largest integer less than or equal to a number.
-   ceil: Returns the smallest integer greater than or equal to a number.

Arithmetic operators are methods that can be called on numbers.

```ruby
10 + 5  # => 15
10 - 5  # => 5
10 * 5  # => 50
10 / 5  # => 2
10 % 5  # => 0
10 ** 5  # => 100000

-10.abs  # => 10
10.5.round  # => 11
10.5.floor  # => 10
10.5.ceil  # => 11
```

### Array Methods

Arrays are a versatile and essential data structure in Ruby, and there are many built-in methods that operate on arrays. Here are some of the most common array methods:

-   length: Returns the length of the array.
-   push: Adds an element to the end of the array.
-   pop: Removes the last element from the array.
-   first: Returns the first element of the array.
-   last: Returns the last element of the array.
-   join: Joins all elements of the array into a string.
-   index: Returns the index of the first element equal to the specified value.
-   reverse: Returns a new array with the elements in reverse order.
-   sort: Returns a new array with the elements sorted.
-   include?: Checks if the array contains a specified element.

```ruby
[1, 2, 3, 4, 5].length  # => 5
[1, 2, 3, 4, 5].push(6)  # => [1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5].pop  # => [1, 2, 3, 4]
[1, 2, 3, 4, 5].first  # => 1
[1, 2, 3, 4, 5].last  # => 5
[1, 2, 3, 4, 5].join  # => "12345"
[1, 2, 3, 4, 5].index(3)  # => 2
[1, 2, 3, 4, 5].reverse  # => [5, 4, 3, 2, 1]
[5, 3, 1, 2, 4].sort  # => [1, 2, 3, 4, 5]
[1, 2, 3, 4, 5].include?(3)  # => true
```

### Array methods with blocks

Blocks are a fundamental aspect of Ruby, allowing for the creation of higher-order functions. They are used to group statements together and pass them to methods as arguments. Blocks are enclosed in curly braces {} or do/end keywords.

```ruby
[1, 2, 3, 4, 5].each do |i|
  puts i
end

# Output: 1 2 3 4 5
```

The each method iterates over each element of the array and executes the code block for each element. The variable i represents the current element of the array. The code block is executed for each element, and the value of i is printed to the terminal.

### Hash Methods

Hashes are a versatile and essential data structure in Ruby, and there are many built-in methods that operate on hashes. Here are some of the most common hash methods:

-   length: Returns the number of key-value pairs in the hash.
-   has_key?: Checks if the hash contains a specified key.
-   has_value?: Checks if the hash contains a specified value.
-   keys: Returns a new array with all the keys of the hash.
-   values: Returns a new array with all the values of the hash.
-   empty?: Checks if the hash is empty.

```ruby
{ "name" => "Alice", "age" => 30 }.length  # => 2
{ "name" => "Alice", "age" => 30 }.has_key?("name")  # => true
{ "name" => "Alice", "age" => 30 }.has_value?(30)  # => true
{ "name" => "Alice", "age" => 30 }.keys  # => ["name", "age"]
{ "name" => "Alice", "age" => 30 }.values  # => ["Alice", 30]
{ "name" => "Alice", "age" => 30 }.empty?  # => false
```

### Practice Problems

Write a ruby script that converts the string "123" to an integer.

Write a ruby script that converts the integer 123 to a string.

Write a ruby script that converts the string "123.45" to a float.

Write a ruby script that converts the float 123.45 to a string.

Write a ruby script that iterates over the array [1, 2, 3, 4, 5] and prints each element.

Write a ruby script that iterates over the hash `{ "name" => "Alice", "age" => 30 }` and prints each key-value pair.

### Basic Methods

Methods are a fundamental aspect of Ruby, allowing for the encapsulation of logic and the creation of reusable code. They are used to group statements together and give them a name, allowing them to be called multiple times throughout a program. In this lesson, we'll explore the basics of methods in Ruby.

### What are Methods?

Methods are a set of instructions that can be called on an object. Objects are something we haven't covered in this lesson but will explore in more detail later. For now, you can think of them as a collection of data and methods that operate on that data. A method is a reusable block of code that performs a specific task.

### Why Use Methods?

-   Reusability: Methods allow you to reuse code without having to write it again. This makes your code more concise and easier to maintain.
-   Abstraction: Methods allow you to abstract away complex logic and give it a name. This makes your code easier to understand and reason about.
-   Organization: Methods allow you to organize your code into logical blocks. This makes your code easier to navigate and maintain.
-   Readability: Methods allow you to give meaningful names to blocks of code. This makes your code easier to read and understand.

Example of a method in Ruby:

```ruby
def say_hello
  puts "Hello, world!"
end
```

The def keyword is used to define a method. The method name is say_hello, and the code block is the code between the def and end keywords. The code block is executed when the method is called.

### Calling Methods

Methods are called using the method name followed by parentheses. If the method takes arguments, they are passed inside the parentheses.

```ruby
say_hello()  # => Hello, world!
```

### Arguments

Arguments are values that are passed to a method when it is called. They are used to provide data to the method so that it can perform its task. Methods can take zero or more arguments.

```ruby
def say_hello(name)
  puts "Hello, #{name}!"
end
```

The name is a parameter of the say_hello method. It is a placeholder for the value that will be passed to the method when it is called. The value that is passed to the method is called an argument.

```ruby
say_hello("Alice")  # => Hello, Alice!
```

### Return Values

Methods can return values to the caller using the return keyword. The return value is the result of the method's execution. If the return keyword is not used, the method will return the last evaluated expression.

```ruby
def add(a, b)
  return a + b
end
```

The add method takes two arguments and returns their sum. The return keyword is used to return the result of the addition. The return value of the add method is the sum of the two arguments.

```ruby
add(1, 2)  # => 3
```

Practice Problem:

Write a Ruby script that defines a method called add that takes two numbers as arguments and returns their sum.

## What is a Gemfile and Why Do You Need One?

Before we start testing with RSpec, it's important to understand how Ruby manages external libraries (called "gems").

A **Gemfile** is a special file used in Ruby projects to manage dependencies. It lists all the gems (libraries) your project needs, including RSpec for testing. When you run `bundle install`, Ruby uses the Gemfile to install all the required gems.

### Why do you need a Gemfile?

-   It keeps track of all the libraries (gems) your project depends on.
-   It makes it easy for others to set up your project with the same dependencies.
-   It's required for using tools like Bundler, which manages gem installation.

### How to Create a Gemfile

#### On Your Local Machine

1. **Open your project folder in your terminal.**
2. **Create a new file named `Gemfile` (no file extension):**

    You can do this with a text editor or by running:

    ```sh
    touch Gemfile
    ```

3. **Add the following content to your Gemfile:**

    ```ruby
    # frozen_string_literal: true

    source "https://rubygems.org"

    gem 'rspec'
    ```

4. **Install Bundler if you haven't already:**

    ```sh
    gem install bundler
    ```

5. **Install the gems listed in your Gemfile:**
    ```sh
    bundle install
    ```

#### On Replit

-   Replit may not have a Gemfile by default. To use RSpec, create a new file named `Gemfile` in your Replit project and add the same content as above.
-   Then, open the Replit shell and run:
    ```sh
    bundle install
    ```
-   This will install RSpec and any other gems you list in your Gemfile.

---

## Testing with RSpec

Testing is a crucial aspect of software development that ensures your code works as expected. RSpec is a popular testing tool for Ruby, known for its human-readable syntax. It allows you to write tests that are easy to understand and maintain.

Here are the reasons why testing is important:

-   Ensures Correctness: Testing helps ensure your code functions correctly. It allows you to catch bugs early and fix them before they become a problem.
-   Facilitates Refactoring: Testing allows you to refactor your code with confidence. It ensures that your code still works after making changes.
-   Acts as Documentation: Testing acts as documentation for your application. It describes the behavior of your application and how it should work.
-   Improves Design: Testing forces you to think about the design of your application. It encourages you to write code that is modular and loosely coupled.
-   Saves Time: Testing saves you time in the long run. It helps you avoid bugs and makes it easier to maintain your code.
-   Improves Collaboration: Testing improves collaboration between developers. It allows you to share code with confidence and work together more effectively.
-   Boosts Confidence: Testing boosts your confidence as a developer. It allows you to write code with confidence and be more productive.

We will be using RSpec to test our Ruby code. RSpec is a popular testing tool for Ruby, known for its human-readable syntax. It allows you to write tests that are easy to understand and maintain.

-   Why Use RSpec?: RSpec helps ensure your code functions correctly, facilitates refactoring, and acts as documentation for your application. It's widely used in the Ruby community and has a strong ecosystem.

### Setting up RSpec

You can install RSpec by adding the following in your Gemfile:

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

# gem "rails"

gem 'rspec'
```

In your bottom left hand side there a wide variety of `Tools` you can use. Click shell then run the following commands.

-   `gem install rspec` - installs rspec
-   `bundle install` - installs all the gems in your Gemfile
-   `rspec --init` - creates the necessary configuration files, including spec_helper.rb and a .rspec file in your project directory. This command creates the necessary configuration files, including spec_helper.rb and a .rspec file in your project directory.

Test files in RSpec are typically placed in the spec directory and end with \_spec.rb. Create this directory if it doesn't exist, and start adding your test files there.

### Writing a Simple Test

Suppose you have a simple method in math_operations.rb:

```ruby
def add
end
```

To test this method, you would create a corresponding RSpec test file:

Create a Test File: Create a file named math_operations_spec.rb in the spec directory.

Write Your Test: Here's how you might write a test for the add method:

```ruby
require_relative '../math_operations'
describe 'math_operations' do
  describe '#add' do
    it 'correctly adds two numbers' do
      expect(add(2, 3)).to eq(5)
    end
  end
end
```

-   describe blocks are used to organize your tests. They can represent methods or behaviors.
-   it blocks contain the individual tests. Each it block should test one aspect of the behavior.
-   The expect(...).to eq(...) syntax is used to assert expected outcomes.

Run the tests by executing `rspec` in your terminal or shell. RSpec will automatically find and run all test files in the spec directory.

When running the tests, you will get failing tests because the add method is not implemented yet. You can implement the method and run the tests again to see if they pass.

```
F

Failures:

  1) math_operations #add correctly adds two numbers
     Failure/Error: expect(add(2, 3)).to eq(5)

     ArgumentError:
       wrong number of arguments (given 2, expected 0)
     # ./math_operations.rb:1:in `add'
     # ./spec/math_operations_spec.rb:5:in `block (3 levels) in <top (required)>'

Finished in 0.06202 seconds (files took 0.5056 seconds to load)
1 example, 1 failure

Failed examples:

rspec ./spec/math_operations_spec.rb:4 # math_operations #add correctly adds two numbers
```

This means that the add method is not implemented correctly since it's expecting two arguments and receiving none.

You can fix this by implementing the method correctly.

```ruby
def add(a, b)
end
```

Now when we run `rspec` again we get the following errors

```

Failures:

  1) math_operations #add correctly adds two numbers
     Failure/Error: expect(add(2, 3)).to eq(5)

       expected: 5
            got: nil

       (compared using ==)
     # ./spec/math_operations_spec.rb:5:in `block (3 levels) in <top (required)>'

Finished in 0.09761 seconds (files took 0.57531 seconds to load)
1 example, 1 failure

Failed examples:

rspec ./spec/math_operations_spec.rb:4 # math_operations #add correctly adds two numbers
```

This means that the add method is not returning the correct value. You can fix this by implementing the method correctly.

```ruby
def add(a, b)
  a + b
end
```

Run the tests again, and you should see that they pass.

```
Finished in 0.00929 seconds (files took 0.35119 seconds to load)
1 example, 0 failures
```

### Practice Problem

Write a test for a method that takes two numbers as arguments and returns their subtraction.

## Summary

In this lesson, we explored the fundamentals of Ruby, including its history, installation, and data types. We also covered variables, arithmetic operators, conditional operators, control flow, and loops. These are the building blocks of any programming language, and understanding them is crucial for effective programming. We covered methods and how they can be used to encapsulate logic and create reusable code. Finally, we covered testing with RSpec and how it can be used to ensure your code works as expected.

## Resources

-   [Ruby Documentation](https://ruby-doc.org/)
-   [Rspec](https://rspec.info/)

## Practice Exercises

Complete the following exercises to test your understanding of the concepts covered in this lesson. If you get stuck, check out the provided solutions at the bottom of the page. These are not meant to be exhaustive, but rather to challenge you and ensure you understand the material. Try to answer each question without looking at the solutions first. These exercises are not due and are not graded, but they are highly recommended.

### 1. Variables

Create a Ruby script that declares a local variable called my_name and assigns it your full name as a string.

### 2. Arithmetic Operators

Create a Ruby script that calculates and prints the area of a rectangle with a width of 10 and a height of 5.

### 3. Conditional Operators & Control Flow

Create a Ruby script that checks if a number is positive, negative, or zero. If it is a positive number, print "positive". If it is a negative number, print "negative". Otherwise, print "zero".

### 4. Basic Methods

Create a Ruby script that defines a method called add that takes two numbers as arguments and returns their sum.

### 5. Testing with RSpec

Create a test for a method that takes two numbers as arguments and returns their multiplication. Run the tests and make sure they pass.

### 6. Arrays

Create a Ruby script that iterates over the array [1, 2, 3, 4, 5] and prints each element.

### 7. Hashes

Create a Ruby script that iterates over the hash `{ "name" => "Alice", "age" => 30 }` and prints each key-value pair.

### 8. Loops & Control Flow

Create a Ruby script that prints the numbers from 1 to 20. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".

### 9. Super Fizz Buzz

Create a Ruby script that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz". For numbers that are multiples of seven, print "Super". For numbers that are multiples of both three and seven, print "FizzSuper". For numbers that are multiples of both five and seven, print "BuzzSuper". For numbers that are multiples of three, five, and seven, print "FizzBuzzSuper".

<details>
<summary>Practice Exercise Solutions</summary>

### 1. Variables

```ruby
my_name = "John Doe"
```

### 2. Arithmetic Operators

```ruby
width = 10
height = 5
area = width * height
puts area
```

### 3. Conditional Operators & Control Flow

```ruby
number = 10
if number > 0
  puts "positive"
elsif number < 0

  puts "negative"
else
  puts "zero"
end
```

### 4. Basic Methods

```ruby
def add(a, b)
  a + b
end
```

### 5. Testing with RSpec

```ruby
require_relative '../math_operations'
describe 'math_operations' do
  describe '#multiply' do
    it 'correctly multiplies two numbers' do
      expect(multiply(2, 3)).to eq(6)
    end
  end
end
```

### 6. Arrays

```ruby
[1, 2, 3, 4, 5].each do |i|
  puts i
end
```

### 7. Hashes

```ruby
{ "name" => "Alice", "age" => 30 }.each do |key, value|
  puts "#{key}: #{value}"
end
```

### 8. Loops & Control Flow

```ruby
(1..20).each do |i|
  if i % 3 == 0 && i % 5 == 0
    puts "FizzBuzz"
  elsif i % 3 == 0
    puts "Fizz"
  elsif i % 5 == 0
    puts "Buzz"
  else
    puts i
  end
end
```

### 9. Super Fizz Buzz

```ruby
(1..100).each do |i|
  if i % 3 == 0 && i % 5 == 0 && i % 7 == 0
    puts "FizzBuzzSuper"
  elsif i % 3 == 0 && i % 7 == 0
    puts "FizzSuper"
  elsif i % 5 == 0 && i % 7 == 0
    puts "BuzzSuper"
  elsif i % 3 == 0 && i % 5 == 0
    puts "FizzBuzz"
  elsif i % 3 == 0
    puts "Fizz"
  elsif i % 5 == 0
    puts "Buzz"
  elsif i % 7 == 0
    puts "Super"
  else
    puts i
  end
end
```

</details>

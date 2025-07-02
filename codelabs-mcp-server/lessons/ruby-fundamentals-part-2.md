---
title: Ruby Fundamentals Part 2
---

# Ruby Fundamentals Part 2

<img src="https://miro.medium.com/v2/resize:fit:540/1*7e9D-oPWPIKBe2AQv862aA.png" />

**Table of Contents**

-   Object Oriented Programming
-   Understanding Classes and Objects
-   Inheritance
-   Polymorphism
-   Encapsulation and Access Modifiers
-   Writing tests in RSpec for Classes and Objects
-   Modules and Mixins
-   Class methods and class variables
-   Summary
-   Practice Exercises

## Object Oriented Programming

Object-oriented programming (OOP) is a programming paradigm that uses objects and classes. It is based on the concept of objects, which are data structures that contain data, in the form of fields, and code, in the form of procedures.

In OOP, computer programs are designed by making them out of objects that interact with one another. OOP languages are diverse, and Ruby is one of them. Ruby is an object-oriented programming language. This means that everything in Ruby is an object.

The importance of OOP is that it allows us to create programs that are easier to understand, modify, and maintain. It also allows us to create programs that are more flexible and reusable.

## Understanding Classes and Objects

A class is a blueprint for creating objects. It defines the properties and behaviors of an object. An object is an instance of a class. It is a concrete entity based on a class, and is sometimes referred to as an instance of a class.

The purpose of a class is to group methods and variables into a single unit that can be used more easily. Classes are like factories that produce objects. The objects that are created are called instances of that class.

This is practical because it allows us to create many objects of the same type without having to write the same code over and over again.

For example, if we want to create a program that manages books, we can create a Book class that defines what a book is and what can be done to a book. Then we can create many instances of the Book class to represent the books in our program. Each instance of the Book class will have its own properties and behaviors.

For example, each book will have its own title, author, and number of pages. Each book will also have its own methods, such as a method to print the book's title, author, and number of pages. An instance is also called an object. This is because an object is an instance of a class.

Let's create our first class in Ruby:

```ruby
class Book
end
```

To define a class in Ruby, we use the `class` keyword followed by the name of the class. The name of the class should be in PascalCase. This means that the first letter of each word in the name of the class should be capitalized.

Let's create an instance or object of the Book class:

```ruby
book = Book.new
```

To create an instance of a class in Ruby, we use the `new` method. The `new` method is a method that is defined in the `Class` class. It creates a new instance of the class that it is called on.

Let's include some properties and behaviors in our Book class:

```ruby

class Book
  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end

  def print_title
    puts @title
  end

  def print_author
    puts @author
  end

  def print_pages
    puts @pages
  end
end
```

To define a method in Ruby, we use the `def` keyword followed by the name of the method. The name of the method should be in snake_case. This means that the words in the name of the method should be separated by underscores. These are also called instance methods because they are defined in the class and can be called on instances of the class.

The @ symbol is used to define instance variables. Instance variables are variables that are defined in a class and can be accessed by all the instance methods in the class.

The initialize method is a special method that is called when an instance of a class is created. It is used to initialize the instance variables of the class. It is also called the constructor method. It is called the constructor method because it is used to construct or create an instance of a class. We can pass arguments to the initialize method when we create an instance of a class. These arguments are passed to the initialize method and used to initialize the instance variables of the class.

Let's see this in action by creating an instance of the Book class and calling the instance methods on it:

```ruby
book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

book.print_title # => The Pragmatic Programmer

book.print_author # => Andy Hunt and Dave Thomas

book.print_pages # => 352

```

### Practice Problem

Create a Ruby program that performs the following tasks using classes and objects:

1. Define a class called 'Animal' that takes a name as an argument.
2. Define a method called 'speak' that prints the name of the animal.
3. Create an instance of the Animal class called 'dog'.
4. Call the 'speak' method on the 'dog' instance.

<details>

<summary>Solution</summary>

```ruby
class Animal
  def initialize(name)
    @name = name
  end

  def speak
    puts @name
  end
end

dog = Animal.new("dog")
dog.speak # => dog
```

</details>

## Inheritance

Inheritance is a mechanism that allows us to define a class based on another class. It allows us to create a class that is a specialization of another class. The class that is inherited from is called the superclass or parent class. The class that inherits from the superclass is called the subclass or child class.

Inheritance is useful because it allows us to reuse code. It allows us to define a class that inherits from another class and add new properties and behaviors to it. This is useful because it allows us to avoid writing the same code over and over again.

Let's see this in action by creating a Book class that inherits from an Item class:

```ruby

class Item
  def initialize(name, price)
    @name = name
    @price = price
  end

  def print_name
    puts @name
  end

  def print_price
    puts @price
  end
end

class Book < Item
  def initialize(name, price, author, pages)
    super(name, price)
    @author = author
    @pages = pages
  end

  def print_author
    puts @author
  end

  def print_pages
    puts @pages
  end
end
```

Here you can see that the Book class inherits from the Item class. This means that the Book class inherits all the properties and behaviors of the Item class. This is useful because it allows us to avoid writing the same code over and over again.

The `super` keyword is used to call the superclass's method with the same name as the method that is being called. This is useful because it allows us to call the superclass's method with the same name as the method that is being called.

Let's see this in action by creating an instance of the Book class and calling the instance methods on it:

```ruby

book = Book.new("The Pragmatic Programmer", 29.95, "Andy Hunt and Dave Thomas", 352)

book.print_name # => The Pragmatic Programmer

book.print_price # => 29.95

book.print_author # => Andy Hunt and Dave Thomas

book.print_pages # => 352
```

### Practice Problem

Create a Ruby program that performs the following tasks using inheritance:

1. Define a class called 'Animal' that takes a name as an argument.
2. Define a method called 'speak' that prints the name of the animal.
3. Define a class called 'Dog' that inherits from the 'Animal' class.
4. Create an instance of the 'Dog' class called 'dog'.
5. Call the 'speak' method on the 'dog' instance.
6. Define a class called 'Cat' that inherits from the 'Animal' class.
7. Create an instance of the 'Cat' class called 'cat'.
8. Call the 'speak' method on the 'cat' instance.

<details>
<summary>Solution</summary>

```ruby

class Animal
  def initialize(name)
    @name = name
  end

  def speak
    puts @name
  end
end

class Dog < Animal
end

class Cat < Animal
end

dog = Dog.new("dog")
dog.speak # => dog

cat = Cat.new("cat")
cat.speak # => cat
```

</details>

## Polymorphism

Polymorphism is the ability of an object to take on many forms. It is the ability of an object to respond to the same method in different ways.

Here's an example of polymorphism:

```ruby

class Animal
  def speak
    puts "I am an animal"
  end
end

class Dog < Animal
  def speak
    puts "I am a dog"
  end
end

class Cat < Animal
  def speak
    puts "I am a cat"
  end
end

def speak(animal)
  animal.speak
end

animal = Animal.new

speak(animal) # => I am an animal

dog = Dog.new

speak(dog) # => I am a dog

cat = Cat.new

speak(cat) # => I am a cat
```

Here you can see that the Animal class and the Dog class both have a speak method. This means that they both respond to the same message in different ways. This is useful because it allows us to write code that works with different types of objects.

In a practical sense this means that we can write code that works with different types of objects. For example, we can write code that works with different types of animals.

## Encapsulation and Access Modifiers

Encapsulation is the process of hiding the internal details of an object. It is the process of hiding the internal details of an object so that the object can only be accessed through a well-defined interface.

Here's an example of encapsulation:

```ruby

class Book
  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end

  def print_title
    puts @title
  end

  def print_author
    puts @author
  end

  def print_pages
    puts @pages
  end
end

book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

book.print_title # => The Pragmatic Programmer

book.print_author # => Andy Hunt and Dave Thomas

book.print_pages # => 352
```

Here you can see that the Book class has three instance variables: @title, @author, and @pages.

These instance variables are private. This means that they can only be accessed by the instance methods in the class.

This is useful because it allows us to hide the internal details of an object. This means that we can change the internal details of an object without affecting the code that uses the object.

Access modifiers are keywords that are used to control the visibility of methods and variables. There are three access modifiers in Ruby: public, protected, private.

-   Public methods and variables can be accessed by anyone.
-   Protected methods and variables can only be accessed by the class that defines them and its subclasses.
-   Private methods and variables can only be accessed by the class that defines them.

We will only explore public and private access modifiers in this lesson.

Here is an example of access modifiers through public methods and private

```ruby
class Book
  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end

  def print_title
    puts @title
  end

  def print_author
    puts @author
  end

  def print_pages
    puts @pages
  end

def print_details
    puts @title
    puts @author
    puts @pages
  end

private
  def print_details_private
    puts @title
    puts @author
    puts @pages
  end
end

book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

book.print_title # => The Pragmatic Programmer

book.print_author # => Andy Hunt and Dave Thomas

book.print_pages # => 352

book.print_details # => The Pragmatic Programmer
                    #    Andy Hunt and Dave Thomas
                    #    352


book.print_details_private # => NoMethodError: private method `print_details_private' called for #<Book:0x00007f8b9a8b6a10>
```

Here you can see that the print_details method is public. This means that it can be accessed by anyone.

Here you can see that the print_details_private method is private. This means that it can only be accessed by the class that defines it.

Here is an example of private methods through inheritance:

```ruby

class Animal
  def initialize(name)
    @name = name
  end

  def print_details
     puts @name
  end

  private

  def print_details_private
    puts @name
  end
end

class Dog < Animal
end

animal = Animal.new("animal")

animal.print_details # => animal


animal.print_details_private # => NoMethodError: private method `print_details_private' called for #<Animal:0x00007f8b9a8b6a10>

dog = Dog.new("dog")

dog.print_details # => dog


dog.print_details_private # => NoMethodError: private method `print_details_private' called for #<Dog:0x00007f8b9a8b6a10>
```

### Practice problem

Create a Ruby program that performs the following tasks using encapsulation and access modifiers that includes public and private methods:

1. Define a class called `Vehicle` that takes a make and model as arguments.
2. Define a method called `print_make` that prints the make of the car.
3. Define a method called `print_model` that prints the model of the car.
4. Define a method called `print_details` that prints the make and model of the car.
5. Define a class called `Car` that inherits from the `Vehicle` class.
6. Define a method called `print_details` that prints the make, model, and year of the car.
7. Define a class called `Motorcycle` that inherits from the `Vehicle` class.

<details>
<summary>Solution</summary>

```ruby
class Vehicle
  def initialize(make, model)
    @make = make
    @model = model
  end

  def print_make
    puts @make
  end

  def print_model
    puts @model
  end

  def print_details
    puts @make
    puts @model
  end

  private

  def print_details_private
    puts @make
    puts @model
  end
end

class Car < Vehicle
  def initialize(make, model, year)
    super(make, model)
    @year = year
  end

  def print_details
    puts @make
    puts @model
    puts @year
  end
end

class Motorcycle < Vehicle
end

```

</details>

### Getters and Setters

Getters and setters are methods that are used to get and set the value of instance variables. They are used to get and set the value of instance variables.

Here's an example of getters and setters:

```ruby
class Book
  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end

  def title
    @title
  end

  def title=(title)
    @title = title
  end

  def author
    @author
  end

  def author=(author)
    @author = author
  end

  def pages
    @pages
  end

  def pages=(pages)
    @pages = pages
  end
end

book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

puts book.title # => The Pragmatic Programmer

puts book.author # => Andy Hunt and Dave Thomas

puts book.pages # => 352

book.title = "The Pragmatic Programmer 2"

puts book.title # => The Pragmatic Programmer 2
```

Here you can see that the getters and setters are defined for the instance variables. This means that we can get and set the value of instance variables using the getters and setters that are defined for them.

### Accessing modifiers with attr_accessor

The `attr_accessor` and `attr_reader` methods are used to define getters and setters for instance variables. The `attr_accessor` method is used to define getters and setters for instance variables. The `attr_reader` method is used to define getters for instance variables.

Here's an example of using `attr_accessor` and `attr_reader`:

```ruby
class Book
  attr_accessor :title, :author, :pages

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end

book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

puts book.title # => The Pragmatic Programmer

puts book.author # => Andy Hunt and Dave Thomas

puts book.pages # => 352

book.title = "The Pragmatic Programmer 2"

puts book.title # => The Pragmatic Programmer 2
```

Here you can see that the `attr_accessor` method is used to define getters and setters for instance variables. This means that we can get and set the value of instance variables using the getters and setters that are defined by the `attr_accessor` method.

## Writing tests in RSpec for Classes and Objects

Let's write some tests for the Book class that we created earlier:

```ruby
class Book
  attr_accessor :title, :author, :pages

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end
```

Here you can see that the Book class has three instance variables: @title, @author, and @pages.

Here's an example of a test for the Book class:

```ruby
require_relative '../book'

describe Book do
  describe '#title' do
    it 'returns the title of the book' do
      book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

      expect(book.title).to eq("The Pragmatic Programmer")
    end
  end
end
```

Here you can see that we are using the `rspec` gem to write tests for the Book class. The `rspec` gem is a testing framework for Ruby. It allows us to write tests for our Ruby code.

Here you can see that we are using the `require_relative` method to require the Book class. This means that we can use the Book class in our tests.

Here you can see that we are using the `describe` method to describe the Book class. This means that we are describing the Book class.

## Modules and Mixins

Modules are used to group related methods, classes, and constants together. They are great for organizing code and making it more readable. They are also great for sharing code between classes.

Here's an example of a module:

```ruby
module Math
  def self.square(x)
    x * x
  end
end

puts Math.square(2) # => 4
```

Here you can see that the Math module has a square method. This means that we can call the square method on the Math module.

Here's an example of a module that is included in a class:

```ruby
module Math
  def square(x)
    x * x
  end
end

class Book
  include Math

  attr_accessor :title, :author, :pages

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end

book = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

puts book.title # => The Pragmatic Programmer

puts book.author # => Andy Hunt and Dave Thomas

puts book.pages # => 352

puts book.square(2) # => 4
```

Here you can see that the Math module is included in the Book class. This means that we can call the square method on the Book class.

Here's an example of a module that is extended in a class:

```ruby
module Math
  def square(x)
    x * x
  end
end

class Book
  extend Math

  attr_accessor :title, :author, :pages

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages
  end
end

puts Book.square(2) # => 4
```

Here you can see that the Math module is extended in the Book class. This means that we can call the square method on the Book class.

### What's the difference between classes and modules?

Classes are used to create objects. Modules are used to group related methods, classes, and constants together. Classes are used to create objects. Modules are used to group related methods, classes, and constants together.

### When do you use a class and when do you use a module?

You use a class when you want to create objects. You use a module when you want to group related methods, classes, and constants together.

Modules are useful when you want to group related methods, classes, and constants together. They are also useful when you want to share code between classes.

You mainly want to abstract logic into modules when you want to share code between classes.

## Class methods and class variables

Class methods are methods that are defined in a class and can be called on the class itself. They are methods that are defined in a class and can be called on the class itself.

Here's an example of a class method:

```ruby
class Book
  @@count = 0

  def initialize(title, author, pages)
    @title = title
    @author = author
    @pages = pages

    @@count += 1
  end

  def self.count
    @@count
  end
end

book1 = Book.new("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", 352)

book2 = Book.new("The Pragmatic Programmer 2", "Andy Hunt and Dave Thomas", 352)

puts Book.count # => 2
```

Here you can see that the Book class has a count method. This means that we can call the count method on the Book class. This is useful because it allows us to get the number of books that have been created. The @@ symbol is used to define class variables. Class variables are variables that are defined in a class and can be accessed by all the class methods in the class.

### Self keyword for class and instance methods

The `self` keyword, somewhat confusingly, can be used in both class and instance methods. In class methods, `self` refers to the class itself. In instance methods, `self` refers to the instance of the class that the method is called on.

Here's an example the of using `self` in a class method:

```ruby
class User

  def self.say_hello
    puts "Hello"
  end
end

User.say_hello # => Hello
```

Here you can see that the `self` keyword is used to define a class method. This means that we can call the say_hello method on the User class. Although this method isn't very useful. It's just an example of using `self` in a class method.

Here's an example of using `self` in an instance method:

```ruby
class User
  def initialize(name)
    @name = name
  end

  def say_hello
    puts "Hello, my name is #{self.name}"
  end

  def name
    @name
  end
end

user = User.new("Alice")

user.say_hello # => Hello, my name is Alice
```

Here you can see that the `self` keyword is used to define an instance method. This means that we can call the say_hello method on the User class. This is useful because it allows us to access the instance variables of the class.

## Summary

In this lesson, we learned about object-oriented programming in Ruby. We learned about classes and objects, inheritance, polymorphism, encapsulation, access modifiers, modules, and class methods. We also learned about the self keyword. The importance of these concepts is that they allow us to create programs that are easier to understand, modify, and maintain. They also allow us to create programs that are more flexible and reusable.

## Practice Exercises

Complete the following exercises to test your understanding of the concepts covered in this lesson. If you get stuck, check out the provided solutions at the bottom of the page. These are not meant to be exhaustive, but rather to challenge you and ensure you understand the material. Try to answer each question without looking at the solutions first. These exercises are not due and are not graded, but they are highly recommended

### Classes and Objects

Create a Ruby program that performs the following tasks using classes and objects:

1. Define a class called 'Car' that takes a make and model as arguments.
2. Define a method called 'print_color' that prints the color of the car.
3. Create an instance of the 'Car' class called 'car'.
4. Create a test for the 'Car' class that tests the 'print_color' method.

<details>
<summary>Solution</summary>

**car.rb**

```ruby
class Car
  def initialize(color)
    @color = color
  end

  def print_color
    puts @color
  end
end

```

**car_spec.rb**

```ruby
require_relative '../car'
describe Car do
  describe '#color' do
    it 'returns the color of the car' do
      car = Car.new('Red')
      expect { car.print_color }.to output("Red\n").to_stdout
    end
  end
end
```

</details>

### Inheritance

Create a Ruby program that performs the following tasks using inheritance:

1. Define a class called 'Fruit' that takes a name as an argument.
2. Define a method called 'print_name' that prints the name of the fruit.
3. Define a class called 'Apple' that inherits from the 'Fruit' class.
4. Create an instance of the 'Apple' class called 'apple'.
5. Create a test for the 'Apple' class that tests the 'print_name' method.

<details>

<summary>Solution</summary>

**fruit.rb**

```ruby
class Fruit
  def initialize(name)
    @name = name
  end

  def print_name
    @name
  end
end
```

**apple.rb**

```ruby
require_relative 'fruit'

class Apple < Fruit
end
```

**apple_spec.rb**

```ruby
require 'rspec'

require_relative '../apple'

describe Apple do
  describe '#print_name' do
    it 'prints the name of the fruit' do
      apple = Apple.new("apple")

      expect(apple.print_name).to eq("apple")
    end
  end
end
```

</details>

### Exercise: Enhanced Car Management System

In this exercise, you will create a more complex Ruby program involving the Car class. This program will not only handle car properties but also include a collection of cars and perform various operations using built-in array methods.

Define a Car class:

1. The class should initialize with a make, model, and color.
   Include methods to get and set each of these attributes.
2. Add a method info that returns a string with all the car's details.

Create a Garage class:

1. This class will manage a collection of Car objects.
2. Implement methods to add a car, remove a car by make and model, and list all cars.
3. Add a method to find all cars of a specific color.
4. add a method to clear all cars from the garage.

Write tests for both classes:

Test all the functionalities of the Car and Garage classes.

<details>
<summary>Solution</summary>

**car.rb**

```ruby
class Car
  attr_accessor :make, :model, :color

  def initialize(make, model, color)
    @make = make
    @model = model
    @color = color
  end

  def info
    "Make: #{@make}, Model: #{@model}, Color: #{@color}"
  end
end
```

**garage.rb**

```ruby
class Garage
  def initialize
    @cars = []
  end

  def add_car(car)
    @cars << car
  end

  def remove_car(make, model)
    @cars.delete_if { |car| car.make == make && car.model == model }
  end

  def list_cars
    @cars.map(&:info)
  end

  def find_cars_by_color(color)
    @cars.select { |car| car.color == color }.map(&:info)
  end
end
```

**car_spec.rb**

```ruby
require 'rspec'
require_relative '../car'

describe Car do
  car = Car.new("Toyota", "Corolla", "Blue")

  it 'should return correct make' do
    expect(car.make).to eq("Toyota")
  end

  it 'should return correct model' do
    expect(car.model).to eq("Corolla")
  end

  it 'should return correct color' do
    expect(car.color).to eq("Blue")
  end

  it 'should return correct info' do
    expect(car.info).to eq("Make: Toyota, Model: Corolla, Color: Blue")
  end

end
```

**garage_spec.rb**

```ruby
require 'rspec'
require_relative '../car'
require_relative '../garage'

describe Garage do
  let(:garage) { Garage.new }
  let(:car1) { Car.new("Toyota", "Corolla", "Blue") }
  let(:car2) { Car.new("Honda", "Civic", "Red") }

  before(:each) do
    Garage.add_car(car1)
    Garage.add_car(car2)
  end

  it 'should list all cars' do
    expect(Garage.list_cars).to eq([car1.info, car2.info])
  end

  it 'should find cars by color' do
    expect(Garage.find_cars_by_color("Red")).to eq([car2.info])
  end

  it 'should remove a car' do
    Garage.remove_car("Toyota", "Corolla")
    expect(Garage.list_cars).not_to include(car1.info)
  end
end

```

</details>

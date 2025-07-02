---
title: Ruby gems and CLI Part 2
---

# Ruby gems and CLI Part 2

**Table of Contents**

-   Bcrypt and passwords
-   File and Data Manipulation

In this lesson we will explore several more topics in Ruby to help solidify a basic overview of Ruby. These past few lessons as well as this one is geared to help build momentum in logical problem solving. Furthermore, we will look into new additions to our knowledge set. This includes Bcrypt and passwords, file and data manipulation.

Let's begin

## Bcrypt and Passwords

Authentication is a very common feature in applications. Authentication is the process of verifying that a user is who they say they are. Authentication is usually done by asking the user for a username and password. The username and password are then compared to the username and password stored in the database. If the username and password match, the user is authenticated. If the username and password do not match, the user is not authenticated.

Although, we will talk more about authentication in the future, we at least need to know how to encrypt passwords before then. We will use the Bcrypt gem to encrypt passwords.

Bcrypt is a hashing algorithm that is used to encrypt passwords. It is a one-way encryption algorithm, meaning that once a password is encrypted, it cannot be decrypted. The only way to decrypt a password is to try a password and see if it matches the encrypted password. Here's an example of how to use Bcrypt to encrypt a password:

Setup a new repl and add the bcrypt gem to your Gemfile.

**Gemfile**

```ruby
source "https://rubygems.org"
ruby '3.4.4'
gem "bcrypt"
```

Then run `bundle install` in your terminal.

Here's an example of how to use Bcrypt to encrypt a password:

**main.rb**

```ruby
require "bcrypt"

my_password = BCrypt::Password.create("my password")

puts my_password
```

> 💡 **Not sure how password encryption works in Ruby?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> “How does Bcrypt encrypt passwords in Ruby?”

Open your integrated terminal in VS Code and run:

```sh
ruby main.rb
```


The BCrypt gem provides a `BCrypt::Password` class that we can use to create a new password. The `BCrypt::Password.create` method takes a string as an argument and returns a new password object. The password object has a `to_s` method that returns the encrypted password as a string. Run the file with `ruby bcrypt_example.rb` and you should see something similar like this:

```bash
$2a$12$Jn9OrCsfhWp9JosMmlGyoeTkq/8.YyNKdx6RPo32uyEbUI7I8UZKa
```

The encrypted password is a string that starts with `$2a$12$` and ends with a string of characters. The `$2a$12$` part is called the salt. The salt is used to make the encrypted password more secure. The salt is generated randomly and is different every time you run the `BCrypt::Password.create` method and is stored with the encrypted password so that the password can be verified later.

The encrypted password can be verified using the `==` method. The `==` method takes a string as an argument and returns `true` if the string matches the encrypted password and `false` if it does not. Here's an example of how to use the `==` method:

```ruby
require "bcrypt"

my_password = BCrypt::Password.create("my password")

puts my_password == "my password" # true

puts my_password == "not my password" # false
```

The `==` method is useful for verifying passwords. For example, if you have a user model with a password attribute, you can use the `==` method to verify that the user's password matches the encrypted password stored in the database. Here's an example of how to use the `==` method to verify a user's password:

```ruby
require "bcrypt"

class User
  attr_accessor :username, :password

  @@users = []
  def initialize(username, password)
    @username = username
    @password = BCrypt::Password.create(password)
    @@users << self
  end

  def self.authenticate(username, password)
    user = User.find_by_username(username)

    if user && user.password == password
      return user
    else
      return nil
    end
  end

  def self.all
    @@users
  end

  def self.find_by_username(username)
    user = all.find do |user|
      user.username == username
    end
    user
  end
end

User.new("username", "password")
user = User.find_by_username("username") # returns user object
puts User.authenticate("username", "password") # returns user object
puts User.authenticate("username", "not password") # returns nil
```

The `User.authenticate` method takes a username and password as arguments and returns a user object if the username and password match a user in the database. The `User.authenticate` method uses the `==` method to verify that the password matches the encrypted password stored in the class.

> 💡 **Bcrypt still confusing?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"What is Bcrypt and how does it work in Ruby?"_

### Incorporating BCrypt into Countries of The World CLI

Let's incorporate BCyrpt into our Countries of The World CLI. We will use BCrypt to encrypt the user's password when they create an account and to verify the user's password when they log in. Here's an example of how to use BCrypt to encrypt the user's password when they create an account:

Be sure to add bcrypt to your Gemfile.

**Gemfile**

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "rspec"
gem "nokogiri"
gem "httparty"
gem "byebug"
gem 'bcrypt'
```

Then run `bundle install` in your shell.

**lib/user.rb**
```ruby
require "bcrypt"

class User
  attr_accessor :username, :password

  @@users = []
  def initialize(username, password)
    @username = username
    @password = BCrypt::Password.create(password)
    @@users << self
  end

  def self.authenticate(username, password)
    user = User.find_by_username(username)

    if user && user.password == password
      return user
    else
      return nil
    end
  end

  def self.all
    @@users
  end

  def self.find_by_username(username)
    user = all.find do |user|
      user.username == username
    end
    user
  end
end
```

**cli.rb**

```ruby
require_relative "./scraper.rb"
require_relative "./user.rb"

# . . .

  def start
    Scraper.scrape_countries
    puts 'Welcome to the Countries of the World CLI!'
    authenticate
    puts 'Please enter a country name to get more information about it.'
    input = gets.strip
    country = Country.all.find { |country| country.name.downcase == input.downcase }
    if country.nil?
      puts 'Sorry, that country is not in our database. Please try again.'
    else
      puts "Name: #{country.name}"
      puts "Capital: #{country.capital}"
      puts "Population: #{country.population}"
      puts "Area: #{country.area}"
    end
  end

# . . .

# authenticate user or create account
  def authenticate
    authenticated = false

    until authenticated
      puts 'Please login or sign up'
      puts 'Which do you choose? (sign up/login)'

      if get_input == 'login'
        authenticated = login
      else
        create_account
      end
    end
  end

  # check if user is in User class and if password matches
  def login
    puts 'Please enter your username:'
    username = gets.chomp
    puts 'Please enter your password:'
    password = gets.chomp
    result = User.authenticate(username, password)

    if result
      puts "Welcome back #{username}!"
    else
      puts 'Sorry, that username and password combination is not recognized. Please try again.'
    end
    result
  end

  # create a new user and add to User class
  def create_account
    puts 'Please enter a username:'
    username = gets.chomp

    puts 'Please enter a password:'
    password = gets.chomp

    User.new(username, password)
    puts 'Account created'
  end

end

# . . .
```

From above, we made a few changes to our `start` method. We will add a call to the `authenticate` method before the user can search for a country. If the user cannot be authenticated, we will not allow them to search for a country. We will also add a call to the `create_account` method if the user chooses to sign up.

## File and Data Manipulation

File and Data Manipulation means to change the contents of a file or data. This is a very common task in programming. In special cases, you may have to monitor outputs of responses and bundle them into a file. Or you may have to extract a csv file from a database and convert it into a json file. In this section, we will learn how to manipulate files and data in Ruby.

We will use our countries of world CLI to give an example of how to add onto a file and manipulate data. We will add usernames and their encrypted hashes into an external JSON file. A JSON file is a file that stores data in a key-value pair format. Here's an example of a JSON file:

> 💡 **JSON or file handling still confusing?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"How do I read and write JSON files in Ruby?"_

```json
{
	"name": "John",
	"age": 30,
	"cars": [
		{
			"name": "Ford",
			"models": ["Fiesta", "Focus", "Mustang"]
		},
		{
			"name": "BMW",
			"models": ["320", "X3", "X5"]
		},
		{
			"name": "Fiat",
			"models": ["500", "Panda"]
		}
	]
}
```

Realistically we would be using a database to store this information, but for the sake of this lesson, we will use a JSON file.

In **user.rb**, we will define a method that stores the user information in an external file.

Be sure to to require the json in your file to use the JSON class.

**lib/user.rb**,
```ruby
require 'json'
.
.
.
  def store_credentials(user)
    file_path = 'users.json'

    unless File.exist?(file_path)
      File.open(file_path, 'w') { |file| file.write(JSON.generate([])) }
    end
  end
```

The `File` class is a class that is used to read and write files. The `File.exist?` method takes a file path as an argument and returns `true` if the file exists and `false` if it does not. The `File.open` method takes a file path and a block as arguments and opens the file for reading and writing.

The `JSON.generate` method takes an array as an argument and returns a JSON string. This will create a JSON file with an empty array if the file does not exist.

```ruby
  def store_credentials(user)
    file_path = 'users.json'

    unless File.exist?(file_path)
      File.open(file_path, 'w') { |file| file.write(JSON.generate([])) }
    end

    file = File.read(file_path)
    users_data = JSON.parse(file)

    users_data << { 'username' => user.username, 'password' => user.password }

    File.open(file_path, 'w') { |file| file.write(JSON.generate(users_data)) }
  end
```

We will then call store_credentials as the user is initialized

```ruby
  def initialize(username, password)
    @username = username
    @password = BCrypt::Password.create(password)
    store_credentials(self)
    @@users << self
  end
```

Once we check to see if the file exists, we will read the file and parse the JSON string into an array. We will then add the user's username and password to the array and write the array back to the file.

Now you can sign up and add the credentials to the users.json. Run the project and sign up.

> 💡 **Password verification still confusing?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"How do I check if a password matches in Ruby?"_

Now that sign up works, we run into a small issue with login.

Every time we load the file and initialize new user instances,

We are creating a NEW password each and every time. This is wrong. We have to change our logic. To fix this we can add a new parameter to indicate if the password is a pre-existing hash or a new password.

```ruby
  def initialize(username, password, password_pre_hashed = false)
    @username = username
    @password = password_pre_hashed ? BCrypt::Password.new(password) : BCrypt::Password.create(password)
    @@users << self
  end
```

Here we use the ternary operator to check if the password is pre-hashed. If it is, we will use the `BCrypt::Password.new` method to create a new password object from the pre-hashed password. This method is used to create a password object from a pre-hashed password. You aren't able to verify a password using the `==` method if the password is pre-hashed. It is important to note that the `BCrypt::Password.new` method takes a string as an argument and returns a password object. This is how bcrypt knows that the password is pre-hashed and to verify the password.

> 💡 **Storing and verifying hashed passwords still confusing?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"How do I store and verify hashed passwords securely in Ruby?"_

If it is not, we will use the `BCrypt::Password.create` method to create a new password object from the password.

Let's go to our `load_users_from_file` method and include true for the new argument since loading users will have an existing password pre hash.

**user.rb**
```ruby
  def self.load_users_from_file
    file_path = 'users.json' # Path to your JSON file

    if File.exist?(file_path)
      file = File.read(file_path)
      users_data = JSON.parse(file)

      users_data.each do |user_data|
        User.new(user_data['username'], user_data['password'], true) # true indicates that the password is already hashed
      end
    end
  end
```

Since we will store credentials in the CLI class, we will turn it from an instance method to a class method. 

**user.rb**
```ruby
  def self.store_credentials(user)
    file_path = 'users.json'

    unless File.exist?(file_path)
      File.open(file_path, 'w') { |file| file.write(JSON.generate([])) }
    end

    file = File.read(file_path)
    users_data = JSON.parse(file)

    users_data << { 'username' => user.username, 'password' => user.password }

    File.open(file_path, 'w') { |file| file.write(JSON.generate(users_data)) }
  end
```


Let's navigate back to the cli and include the newly added argument for when a user creates an account.

**cli.rb**

```ruby
  def create_account
    puts 'Please enter a username:'
    username = gets.chomp

    puts 'Please enter a password:'
    password = gets.chomp

    user = User.new(username, password, false) # false indicates that the password is not hashed
    User.store_credentials(user) #
    puts 'Account created'
  end
```

Load the users from file at the start.

```ruby 
class CLI
  def start
    User.load_users_from_file
    Scraper.scrape_countries
```

Click `run` to test both login and sign up.

```
Which do you choose? (sign up/login)
sign up
Please enter a username:
test
Please enter a password:
test
Account created
Please login or sign up
Which do you choose? (sign up/login)
login
Please enter your username:
test
Please enter your password:
test
Welcome back test!
Please enter a country name to get more information about it.
```

## Conclusion

In summary, we learned how to encrypt passwords using the Bcrypt gem to authenticate users. Although, to keep the data persistent we used a JSON file to store the user information.

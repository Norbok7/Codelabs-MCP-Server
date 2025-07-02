---
title: Ruby gems and CLI Part 1
---

# Ruby gems and CLI Part 1

**Table of Contents**

-   Ruby Gems
-   Using a Gem
-   Countries of The World CLI
-   Technical Documentation for the CLI

## Ruby Gems

Ruby gems are packages of code that you can use in your Ruby projects. There are thousands of gems available for you to use. You can find them on [RubyGems.org](https://rubygems.org/). The purpose of gems are to make your life easier. Instead of writing code from scratch, you can use a gem that someone else has already written. Here are some examples of gems:

> 💡 **Need a refresher on what a Ruby gem is or how bundler works?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): “What’s a Ruby gem and why use bundler?”


-   [Nokogiri](https://rubygems.org/gems/nokogiri) - A gem that allows you to parse HTML and XML documents.
-   [Pry](https://rubygems.org/gems/pry) - A gem that allows you to debug your code.
-   [HTTParty](https://rubygems.org/gems/httparty) - A gem that allows you to make HTTP requests.
-   [Sinatra](https://rubygems.org/gems/sinatra) - A gem that allows you to create web applications.
-   [Rails](https://rubygems.org/gems/rails) - A gem that allows you to create web applications.
-   [Rake](https://rubygems.org/gems/rake) - A gem that allows you to automate tasks.
-   [RSpec](https://rubygems.org/gems/rspec) - A gem that allows you to test your code.
-   [Rubocop](https://rubygems.org/gems/rubocop) - A gem that allows you to check your code for style and syntax errors.
-   [Faker](https://rubygems.org/gems/faker) - A gem that allows you to generate fake data.

In this chapter, we will learn how to use gems and how to create our own gems.

## Using a Gem

Let's use the [Nokogiri](https://rubygems.org/gems/nokogiri) gem to parse HTML and XML documents.

1. Open VS Code and create a new folder called `nokogiri-example`.
2. Add the following code to your gemfile:

The gemfile is used to specify the gems that you want to use in your project.

**Gemfile**

```ruby
source "https://rubygems.org"
ruby '3.4.4'
gem "nokogiri"
```

```ruby
source "https://rubygems.org"
```

Here we use the `source` method to specify the source of the gems that we want to use. In this case, we are using [RubyGems.org](https://rubygems.org/).

```ruby
gem "nokogiri"
```

Then we use the `gem` method to specify the gem that we want to use. In this case, we are using the [Nokogiri](https://rubygems.org/gems/nokogiri) gem. If we need to add more gems, we can add them to the `Gemfile` file like so:

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

-   The '1' is the major version. The major version is used for major changes.
-   The '15' is the minor version. The minor version is used for minor changes.
-   The next`4' is the patch version. The patch version is used for bug fixes.

If you don't specify the version, it will use the latest version of the gem.

```ruby
ruby '3.4.4'
```

Here you'll see we are specifying the version of Ruby that we want to use. In this case, we are using version 3.4.4. If you don't specify the version, it will use the latest version of Ruby.

### Nokogiri Gem

Run `bundle install`.

The `bundle install` command will install the Nokogiri gem and all of its dependencies into your project. Whenever you add a new gem to your `Gemfile`, you will need to run `bundle install`. If you fork a project that has a `Gemfile`, you will need to run `bundle install`. It's the equivalent of `npm install` for a JavaScript project.

These are gems that are installed in your project. They are not installed globally unless you specify that you want to install them globally in which can you will have to run `gem install gem-name` in the shell.

This will add onto the `Gemfile.lock` file that will keep track of the gems that you are using in your project.

It might look similar to this, depending on the version you installed. The specific version does not matter for this example.

```ruby
GEM
  remote: https://rubygems.org/
  specs:
    mini_portile2 (2.8.5)
    nokogiri (1.15.4)
      mini_portile2 (~> 2.8.2)
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

The difference between the `Gemfile` and the `Gemfile.lock` is that the `Gemfile` is used to specify the gems that you want to use in your project and the `Gemfile.lock` is used to specify the gems that you are actually using in your project and t...

> 💡 **Curious why `Gemfile.lock` exists at all?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): 
> Ask: _"Why do we need a Gemfile.lock file in Ruby projects?"_

 Why is this important? Because if you are working on a team, you want to make sure that everyone is using the same version of the gems. It also makes it easier to deploy your application to a server and keeps the environment consistent. We don't want to have different versions of gems on our local machine and on the server to avoid any issues.

Create a new file called `index.html` and add the following code to it:

**index.html**

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

Let's extract the text from the `h1` element using the Nokogiri gem.

**main.rb**

```ruby
require "nokogiri"

doc = Nokogiri::HTML(File.open("index.html"))

puts doc.css("h1").text
```

Let's break this down:

```ruby
require "nokogiri"
```

Here we use the `require` method to require the Nokogiri gem to use it's provided objects.

```ruby
Nokogiri::HTML
```

The `Nokogiri::HTML` module is used to parse the HTML document.

```ruby
doc = Nokogiri::HTML(File.open("index.html"))
```

The `File.open` method is used to open the `index.html` file. As we pass in this file to the `Nokogiri::HTML` module, it will parse the HTML document and store it in the `doc` variable. Parsing it means it will convert the HTML document into a format that we can use. Such as a nokogiri instance. We can then use the `doc` variable to get the data that we want.

```ruby
puts doc.css("h1").text
```

Then we use the `css` method, a nokogiri method, to select the `h1` element. Afterwards we use the `text` method, another nokogiri method, to get the text or content of the `h1` element.

There are a wide variety of methods from nokogiri but these are enough to get us started.

Execute `main.rb`.

This will print out "Hello World" to the terminal.

### Practice Problem

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

1. Use the Nokogiri gem to parse the HTML document.
2. Extract all `li` elements and print them out to the terminal.
3. Each `li` element should be on a new line.

```
Item 1
Item 2
Item 3
```

<details>

<summary>Solution</summary>

**Gemfile**

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "nokogiri"
```

```
bundle install
```

**main.rb**

```ruby
require "nokogiri"

doc = Nokogiri::HTML(File.open("index.html"))

doc.css("li").each { |li| puts li.text }
```


</details>

### Web Scraping with Nokogiri and httparty

We can use the Nokogiri gem and the httparty gem to make HTTP requests and parse the HTML and XML documents. This is a form of web scraping. Let's create a new repl called `web-scraper`.

We will be scraping the Wikipedia page for the list of films from 2019.

[https://en.wikipedia.org/wiki/2020_in_film](https://en.wikipedia.org/wiki/2020_in_film)

<img src="https://imgur.com/0DAlid9.png" />

Add the following code to your `Gemfile` file:

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "nokogiri"
gem "httparty"
```

Run `bundle install` to install the Nokogiri gem and the httparty gem.

Navigate to `main.rb`.

Let's require the necessary gems to web scrape.

**main.rb**

```ruby
require "nokogiri"
require "httparty"
```

Define a class called API and include a class method called `get_films_by_year` that takes in a year as an argument. We will use year to get a list of films from Wikipedia.

**main.rb**

```ruby
require "nokogiri"
require "httparty"

class API
  def self.get_films_by_year(year)
  end
end
```

Then we use the `HTTParty.get` method to make a `GET` request to the Wikipedia page for the year that we pass in as an argument.

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

```

```ruby
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

The `css` method selects the `table.wikitable.sortable tr td:nth-child(2) i a` element.

`table.wikitable.sortable tr td:nth-child(2) i a` represents the series of hierarchy levels to get to the table and the elements. It is used to select elements from the document that you requested for. You should inspect the elements on the web page when scraping and find the elements that you want to select based off the selector or class name. Getting to this point takes time and trial and error. Depending on the webpage, it can be difficult to select the elements that you want.

<img src="https://imgur.com/pkEvM5t.png" />

What you are doing here is basically finding the parent element, targeting it by it's CSS and then finding the child element and targeting it.

So you have a table element with classes of `wikitable` and `sortable`. This is used to specify the table that you want to select since there's many tables on the page.

As you target the specific table, you then target the `tr` element since it will include all the rows of the films. Technically, it will also include the header rows. So we have to specify that we want `td` for table data to remove the header rows.

Then you have a `nth-child(2)` element right after. This will only allow us to extract the second child element from every `td` which will include the title of the film that we want. Then you have an `i` element. Then you have an `a` element.

This will return an array of nokogiri instances.

```ruby
parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a")
```

In which we can use to iterate and strip the text from the elements.

```ruby
parsed_page.css("table.wikitable.sortable tr td:nth-child(2) i a").map { |film| film.text.strip }
```

Then we use the `each_with_index` method to iterate over the films and print out the films to the terminal.

```ruby
    films.each_with_index do |film, index|
     puts "#{index + 1}. #{film}"
   end
```

Nokogiri can be buggy and it can be difficult to use. It is not always accurate. You may have to try different CSS selectors to get the data that you want.

**main.rb**

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

API.get_films_by_year(2019)
```

The result of this code is a list of films from 2019 once you execute it.

```
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
```

Web scraping is a very powerful tool. However, it can be very slow and it can be very difficult to maintain. If the website changes, your code will break. If the website is down, your code will break. If the website is slow, your code will be slow. If you are making a lot of requests, you can get banned from the website. So you have to be careful when using web scraping. Respect the website and don't abuse it.

In a practical sense you would not use web scraping to get data from a website unless for situations needed or special use cases. You would use an API.

## Countries of The World CLI

A CLI is a Command Line Interface. It is a program that allows you to interact with your computer using the command line. An example would be the Angular CLI. It allows you to create a new angular project, generate components, generate services, etc.

In this CLI, we will be scraping a website for a list of countries and their capitals, populations and area.

Let's begin by creating a new folder in VS Code called `countries_of_the_world_cli`.

We mostly have everything we need to begin creating our CLI.

The `readme.md `file will be used to document our project.

The Gemfile will be used to specify the gems that we want to use in our project.

We will also use the `main.rb` file to run our project and start our CLI.

Let's create a `lib` directory. This will house our files of code.

Create a new file called `lib/cli.rb` and add the following code to it:

**lib/cli.rb**

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
```

```ruby
    puts "Welcome to the Countries of the World CLI!"
    puts "What is your name?"
```

Here we are using the `CLI` class to define a method called `start` that prints out a welcome message and asks the user for their name.

```ruby
    name = gets.strip
    puts "Hello #{name}!"
```

Then we use the `gets` global method to get the user's input. Then we use the `strip` method to remove any whitespace from the user's input. Then we use the `puts` method to print out the user's name.

Navigate to `main.rb` and crete a new `CLI` instance to call `start`.

```ruby
require_relative './lib/cli.rb'

CLI.new.start
```

You can run the main.rb file by opening the integrated terminal in VS Code and executing:

```sh
ruby main.rb
```

Here is the result

```
Welcome to the Countries of the World CLI!
What is your name?
John Doe
Hello John Doe!
```

### Adding Tests

Let's create a test file for our CLI using `rspec`. But first we have to install rspec.

Run `bundle add rspec` to install rspec in the shell. This will automatically add rspec to our `Gemfile` and lock file.

Run `bundle exec rspec --init` to initialize rspec into the project folder. This will create a `.rspec` file and a `spec` directory with a `spec_helper.rb` file. Be sure to then run `gem install rspec` to use the rspec gem in the shell provided by commands like `rspec`.

Let's test out the `CLI` class.

Create a new file called `spec/lib/cli_spec.rb` and add the following code to it:

**spec/lib/cli_spec.rb**

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


> 💡 **`RSPEC` still confusing?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): 
> Ask: _"What is RSpec?"_


Here we are using the `RSpec.describe` method to describe the `start` method of what we will be testing.

Then we use the `it` method to describe what the `start` method does.

The test demonstrates the creation of a new `CLI` object and the use of the `allow` method to allow the `cli` object to receive the `get_input` method.

Then we use the `expect` method to expect the `cli.start` method to output the welcome message and ask the user for their name.

Run `bundle exec rspec` to run the test.

The difference between entering `rspec` vs `bundle exec rspec` is that `rspec` will use the globally installed version of rspec and `bundle exec rspec` will use the locally installed version of rspec. I tend to use `bundle exec rspec` to avoid any issues with the version of rspec.

### Web Scraping with Nokogiri and httparty

The website we will be scraping is a website that allows legal web scraping and it is called [www.scrapethissite.com](https://www.scrapethissite.com/pages/simple/). This site allows for it be scraped for educational purposes. Be weary of scraping websites that do not allow it. You can get banned from the website.

Take a moment to view the website and inspect the elements. We will be scraping the countries and their capitals, populations and area.

> 💡 **Still confused what `Scraping` is?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): 
> Ask: _"What is Scraping?"_

We can use the Nokogiri gem and the httparty gem to make HTTP requests and parse the HTML and XML documents.

Add both gems to your gemfile:

```ruby
# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

ruby '3.4.4'
gem "rspec"
gem "nokogiri"
gem "httparty"
```

Run `bundle install` to install the Nokogiri gem and the httparty gem.

Let's create a new file called `scraper.rb` under `lib`. Let's add the following:

**lib/scraper.rb**

```ruby
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

-   Here we use the `require` method to require the Nokogiri gem and the httparty gem.
-   The `Scraper` module is used to define a method called `scrape_countries` that makes a GET request to the INDEX_URL and parses the HTML document.
-   The `INDEX_URL` is a constant that is used to store the URL that we want to scrape.
-   The `HTTParty.get` method is used to make a GET request to the INDEX_URL.
-   The `Nokogiri::HTML` method parses the HTML document.
-   The `puts` method prints out the parsed HTML document to the terminal.

Call the `scrape_countries` method from the `start` method in the `cli.rb` file.

**lib/cli.rb**

```ruby
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

```sh
ruby main.rb
```

This will print all the HTML to the terminal.

This is where it gets tricky, if you navigate to the site and inspect the country elements, you will see that they are not in a table. They are in a div element. So we have to find a way to select the div element and then select the country elements.

Thankfully they all have the same class called `country`, so we can use that to select the country elements.

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

Run the project and notice how it only gives us divs with the class of country. `div.country` as an argument represents every div with the classname of country. We want to select the country name, the capital, the population and the area. We can do that by using the `css` method.

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

### Debug gem

The `debug` gem is a gem that allows you to debug your code. It is similar to the debugger in JavaScript. It allows you to pause your code and inspect it. Ruby 3.1+ includes the debug gem by default. Let's add the debug gem to our scraper.rb file.

**lib/scraper.rb**

```ruby
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

```sh
ruby main.rb
```

You will notice you get something along the lines of this in your terminal:

```
[11, 20] in /home/runner/countries-of-the-world-cli/lib/scraper.rb
   11:     countries.each do |country|
   12:       name = country.css("country-name").text
   13:       capital = country.css("country-capital").text
   14:       population = country.css("country-population").text
   15:       area = country.css("country-area").text
   16:       binding.break
=> 17:       puts "#{name} #{capital} #{population} #{area}"
   18:     end
   19:   end
   20: end
```

This is a pause in your code and you have access to the variables in your code. You can enter in `name` and it will print out the name of the country. However, when you do that you get an empty string. This is where you want to play with the CSS selectors to get the data that you want.

This isn't as straight forward as a process since it takes time to debug and figure out what's going on. But it's a good learning experience and the debug gem is a great tool to use.

We need to further inspect the elements to see what's going on.

When inspecting the `country` class element on the webpage, you may notice it includes an `h3` and a `div` with the country info. Take time to inspect the webpage and see what's going on.

<img src="https://imgur.com/GNrghJU.png" />

This means that `country` represents both those elements as well. So we need to select the `h3` element and the `div` element separately.

Let's try entering `country` in the terminal while we are in the debugger.

We see that it returns a Nokogiri instance:

```ruby
#<Nokogiri::XML::Element:0x974 name="div" attributes=[#<Nokogiri::XML::Attr:0x6cc name="class" value="col-md-4 country">] children=[#<Nokogiri::XML::Text:0x6e0 "\n                        ">, #<Nokogiri::XML::Element:0x6b8 name="h3" attributes=[#<Nokogiri::XML::Attr:0x654 name="class" value="country-name">] children=[#<Nokogiri::XML::Text:0x668 "\n                            ">, #<Nokogiri::XML::Element:0x690 name="i" attributes=[#<Nokogiri::XML::Attr:0x67c name="class" value="flag-icon flag-icon-ad">]>, #<Nokogiri::XML::Text:0x6a4 "\n                            Andorra\n                        ">]>, #<Nokogiri::XML::Text:0x6f4 "\n                        ">, #<Nokogiri::XML::Element:0x94c name="div" attributes=[#<Nokogiri::XML::Attr:0x708 name="class" value="country-info">] children=[#<Nokogiri::XML::Text:0x71c "\n                            ">, #<Nokogiri::XML::Element:0x744 name="strong" children=[#<Nokogiri::XML::Text:0x730 "Capital:">]>, #<Nokogiri::XML::Text:0x758 " ">, #<Nokogiri::XML::Element:0x794 name="span" attributes=[#<Nokogiri::XML::Attr:0x76c name="class" value="country-capital">] children=[#<Nokogiri::XML::Text:0x780 "Andorra la Vella">]>, #<Nokogiri::XML::Element:0x7a8 name="br">, #<Nokogiri::XML::Text:0x7bc "\n                            ">, #<Nokogiri::XML::Element:0x7e4 name="strong" children=[#<Nokogiri::XML::Text:0x7d0 "Population:">]>, #<Nokogiri::XML::Text:0x7f8 " ">, #<Nokogiri::XML::Element:0x834 name="span" attributes=[#<Nokogiri::XML::Attr:0x80c name="class" value="country-population">] children=[#<Nokogiri::XML::Text:0x820 "84000">]>, #<Nokogiri::XML::Element:0x848 name="br">, #<Nokogiri::XML::Text:0x85c "\n                            ">, #<Nokogiri::XML::Element:0x8c0 name="strong" children=[#<Nokogiri::XML::Text:0x870 "Area (km">, #<Nokogiri::XML::Element:0x898 name="sup" children=[#<Nokogiri::XML::Text:0x884 "2">]>, #<Nokogiri::XML::Text:0x8ac "):">]>, #<Nokogiri::XML::Text:0x8d4 " ">, #<Nokogiri::XML::Element:0x910 name="span" attributes=[#<Nokogiri::XML::Attr:0x8e8 name="class" value="country-area">] children=[#<Nokogiri::XML::Text:0x8fc "468.0">]>, #<Nokogiri::XML::Element:0x924 name="br">, #<Nokogiri::XML::Text:0x938 "\n                        ">]>, #<Nokogiri::XML::Text:0x960 "\n                    ">]>
```

We can call Nokogiri methods on it such as `css` and `text` to further get the values we want. For example, try entering `country.css("h3").text` in the terminal while in the debugger. This will return the country name.

It gives us the country name but in a weird format!

```ruby
"\n                            \n                            Andorra\n                        "
```

It's not perfect but it's a start. We can use the `strip` method to remove the whitespace:

```ruby
country.css('h3').text.strip
```

We get `Andorra`. Great!

As I am debugging, I start to notice, I actually forgot a period in the css selector. It should be `.country-name` instead of `country-name`, `.country-capital` instead of `country-capital`, etc. This is because they are classes and shouldn't be selected as elements. This is how Nokogiri interprets it.

To exit the debugger, enter `exit` in the terminal.

Let's change the scraper.rb file to add the period in each css selector.

**lib/scraper.rb**

```ruby
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

```
Andorra Andorra la Vella 84000 468.0
United Arab Emirates Abu Dhabi 4975593 82880.0
Afghanistan Kabul 29121286 647500.0
Antigua and Barbuda St. John's 86754 443.0
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
```

This is exactly what we want. We can now use this data to create our CLI.

Let's quickly create a country class to store the data, create a file called `country.rb` under `lib` and add the following code to it:

**country.rb**

```ruby
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

-   Here we use the `attr_accessor` method to create getters and setters for the name, capital, population and area attributes so they are accessible outside of the class.
-   The `@@all` class variable is used to store all the instances of the Country class.
-   The `initialize` method is used to initialize a new Country object with a name, capital, population and area.

We like to store the data in objects because it makes it easier to work with. We can create a new country object and store the data in it. Then we can use the country object to get the data that we want.

Let's update the scraper.rb file to create a new country object and store the data in it.

**scraper.rb**

```ruby
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

**cli.rb**

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

> 💡 **Getting `nil` when searching for a country?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): 
> Ask: _"How does `.find` work in Ruby and why might it return nil?"_


Run the project and we should get the following:

```
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
```

```
Welcome to the Countries of the World CLI!
What is your name?
John Doe
Hello John Doe!
Please enter a country name to get more information about it.
Fake Country
Sorry, that country is not in our database. Please try again.
```

Great we have a working CLI. We can now get information about a country. However, we can only get information about one country. We can further improve this however, let's move onto technical documentation.

## Adding Technical Documentation

What is technical documentation? How does it help create a better experience for the developer.

Documentation in the context of software development is a written text or illustration that accompanies computer software or is embedded in the source code. The purpose of documentation is to explain how software operates or how to use it, and it may mean different things to people in different roles. Here’s why it's useful:

-   It helps developers understand the codebase.
-   It helps developers understand the architecture of the codebase.

When it comes to documentation there are two types of documentation:

-   Internal documentation - This is documentation that is written for the developer. It is not meant for the end user. It is meant for the developer to understand the codebase and the architecture of the codebase.
-   External documentation - This is documentation that is written for the end user. It is meant for the end user to understand how to use the software.

Let's create internal documentation for our CLI.

In the `readme.md` file, replace the following with:

> 💡 **Still not understanding what is a CLI?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): 
> Ask: _"What is a CLI and what does it do?"_

```md
# Countries of the World CLI

## Description

The Countries of the World CLI is a command line interface that allows you to get information about countries. It uses this [site](https://www.scrapethissite.com/pages/simple/) to get the information.

## Installation

1. Clone the repository
2. Run `bundle install`
3. Open the integrated terminal in VS Code and run `ruby main.rb` to start the project.

## Gems

### Nokogiri

[Nokogiri](https://rubygems.org/gems/nokogiri) is a gem that allows you to parse HTML and XML documents.

### HTTParty

[HTTParty](https://rubygems.org/gems/httparty) is a gem that allows you to make HTTP requests.

### RSpec

[RSpec](https://rubygems.org/gems/rspec) is a gem that allows you to test your code.

## License

The gem is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
```

This details what the CLI is and how to install it. It also lists the gems that we are using and the license that we are using. This is useful for developers who want to use our CLI.

## Summary

In this lesson we learned about Ruby gems and created our very own small CLI. The purpose of this lesson is to introduce you to gems, web scraping and CLI.

>💡 Want to connect scraping, CLI, and testing together?
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
Ask the Assistant: “How do I test CLI scrapers with RSpec?”

## Resources

-   [RubyGems.org](https://rubygems.org/)
-   [Nokogiri](https://rubygems.org/gems/nokogiri)
-   [HTTParty](https://rubygems.org/gems/httparty)
-   [Sinatra](https://rubygems.org/gems/sinatra)
-   [Rails](https://rubygems.org/gems/rails)
-   [Rake](https://rubygems.org/gems/rake)
-   [RSpec](https://rubygems.org/gems/rspec)

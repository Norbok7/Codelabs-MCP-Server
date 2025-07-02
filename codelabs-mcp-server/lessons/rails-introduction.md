---
title: Introduction to Ruby on Rails
---

# Introduction to Ruby on Rails

**Table of Contents**

-   Overview of Full Stack Web Development
-   Understanding the Internet and Web Servers
-   REST and RESTful APIs
-   Ruby on Rails Introduction
-   Interacting with the Database with Models
-   Introduction to Associations

## Overview of Full Stack Web Development

<img src="https://www.revenueriver.co/hubfs/fullstack.jpeg" />

### Understanding Frontend vs Backend Development

The differences between frontend and backend development are not as straightforward as some may think. Sure, when we think of frontend development we think of the visual aspects of a website, and when we think of backend development we think of the behind-the-scenes work that makes a website function. However, there is a lot more to it than that.

Frontend development, also known as client-side development, is the practice of producing HTML, CSS, and JavaScript for a website or web application so that a user can see and interact directly with them. The challenge with frontend development is that the tools and techniques used to create the frontend of a website change constantly, so developers need to constantly be aware of how the field is developing. Technologies are rapidly changing, improving, and evolving. This means that frontend developers need to stay on their toes and always be learning.

Some of the core concepts of frontend development include:

-   HTML/CSS/JavaScript: These are the core technologies behind every web page. HTML (HyperText Markup Language) dictates the structure, CSS (Cascading Style Sheets) sets the visual appearance, and JavaScript makes the page interactive.
-   Responsive Design: Websites must work well on multiple devices (like phones, tablets, and desktops), requiring an understanding of responsive design principles.
-   Performance Optimization: Frontend developers must ensure that websites are fast and efficient.
-   Frameworks and Libraries: Knowledge of frameworks like React, Angular, or Vue.js is often essential.
-   And much more.

Backend development, on the other hand, can be referred to as server-side development. It focuses on databases, scripting, and website architecture. It's where all the magic happens that allows websites to function. Backend development works in tandem with the frontend to deliver the final product to the end-user.

Some of the core concepts of backend development include:

-   **Languages**: Java, Python, Ruby, Node.js, PHP, .NET, and more.
-   **Database Management**: Backend developers must understand database management systems like SQL, MongoDB, or Oracle.
-   **Server Management**: Understanding server management and architecture is crucial. This includes handling Apache, Nginx, and similar platforms.
-   **APIs (Application Programming Interfaces**): APIs are critical for communication between the frontend and backend.
-   And much more.

Another important concept is system design. System design, in the context of web development, focuses on the architecture of the system. It's about designing the system to handle loads efficiently and to scale as necessary. This involves optimizing the code, database queries, and employing caching strategies as well as managing servers and networks.

Here are some questions revolving system design:

**Design a Simple Blogging Platform:**
- How would you design a basic blogging platform where users can create and read blog posts?
- What kind of database would you choose (SQL vs NoSQL) for storing blog posts and user information, and why?
- How would you ensure that the platform can handle an increase in the number of users and blog posts over time?

**Design a Task Management Application:**
- How would you design a simple application for managing tasks and to-do lists?
- What would be your approach to store and retrieve tasks efficiently?
- Consider how multiple users might use the application simultaneously. How would your design accommodate this?

So when it comes to frontend and backend development, there's also a side of system design that comes into play.

Back to frontend and backend.

Together, frontend and backend development form the backbone of the web. They are the yin and yang of web development. They are the peanut butter and jelly of web development. They are the... well, you get the idea. They are both essential to the web and they both require a lot of skill and knowledge to do both well. This is why it takes a team of developers to build a web application. It's not something that can be done by one person alone within a reasonable amount of time.

Yes, frontend and backend development are the two main branches of web development, however, there are many other skills that go into web development. These include:

-   **Design**: Design is a critical part of web development. It's what makes a website look good and function well. Designers need to understand color theory, typography, and user experience (UX).
-   **Testing**: Testing is a critical part of web development. It's what makes sure that a website works as intended. Testers need to understand how to write test cases, how to run tests, and how to report bugs. Also, testing allows us to ensure that our code is working as intended and it can save us a lot of time and money in the long run.
-   **Project Management**: Project management is a critical part of web development. It's what makes sure that a website is delivered on time and on budget. Project managers need to understand how to plan projects, how to manage teams, and how to communicate with clients.
-   **DevOps**: DevOps is a critical part of web development. It's what makes sure that a website is delivered on time and on budget. DevOps engineers need to understand how to plan projects, how to manage teams, and how to communicate with clients.
-   **Security**: Security is a critical part of web development. It's what makes sure that a website is delivered on time and on budget. Security engineers need to understand how to plan projects, how to manage teams, and how to communicate with clients.
-   And much more

It's a lot to take in, but don't worry. You don't need to be an expert in all of these areas to be a web developer. In fact, most web developers specialize in one or two areas. For example, some web developers focus on frontend development, while others focus on backend development. Some are full stack (both frontend and backend). Some web developers focus on design, while others focus on testing. Some web developers focus on project management, while others focus on DevOps. Some web developers focus on security, while others focus on UX.

You get the idea. It all depends on what you want to do and what you're good at.

### Overview of Common Full Stack Technologies

To be effective, full stack developers must be familiar with a range of technologies.

**Frontend Technologies:**

-   HTML/CSS: The basic building blocks of web development.
-   JavaScript: Essential for adding interactivity to web pages.
-   Frameworks: Angular, ReactJS, and Vue.js for advanced JavaScript handling.
-   Libraries: jQuery, Bootstrap for UI components and faster development.

**Backend Technologies:**

-   Languages: Node.js (JavaScript), Ruby, Python, PHP, Java.
-   Frameworks: Express (for Node.js), Django (for Python), Ruby on Rails (for Ruby).
-   Databases: MySQL, MongoDB, Oracle, SQLServer.
-   Server Management: Knowledge of AWS, Heroku, etc.

**DevOps and Version Control:**

-   Git: For version control.
-   DevOps Tools: Docker, Jenkins, Kubernetes.

**Testing and Debugging:**

-   Unit Testing: JUnit for Java, Jest for JavaScript.
-   Debugging Tools: Chrome DevTools, Visual Studio Code Debugger.


and much more.

Of course, it's unrealistic to expect a full stack developer to be an expert in all of these technologies. However, it's important to have a basic understanding of some of these technologies. This will allow you to communicate effectively with other developers and understand how everything fits together.

To be effective in the backend, we have to know some essential concepts.

## Understanding the Internet and Web Servers

<img src="https://www.intel.com/content/dam/www/central-libraries/us/en/images/language-icon-lvl-2-abstract-bg.png.rendition.intel.web.864.486.png" />

### How the Internet Works: Basics of Web Servers and Clients

The internet is a vast network of computers and servers interconnected globally. It's the infrastructure that allows devices to connect and communicate with each other. There is something called data transmission in which data is sent from one device to another through a system of standardized protocols. These protocols are a set of rules that define how data is transmitted between devices in a network. The most common protocol is TCP/IP (Transmission Control Protocol/Internet Protocol). It's the protocol that allows the internet to work.

When it comes to transferring data over the internet, there are two types of devices: clients and servers. Clients are devices that request data from servers. Servers are devices that store and send data to clients. For example, when you visit a website, your computer is the client and the website has a server.

Your computer requests data from the server and the server sends the data back to your computer. And by data we mean files like HTML, CSS, JavaScript, images, videos, and so on. This is how the internet works.

A crucial aspect of how the internet functions is the relationship between web servers and clients.

Web Servers:

-   Function: Web servers are powerful computers that store web site files and serve them to users on request.
-   Software: They run software like Apache or Nginx, which handles the incoming requests from clients and responds with the requested pages.

Clients:

-   Web Browsers: Clients, typically web browsers like Chrome or Firefox, request information from servers.
-   Request-Response Cycle: When you type a website address or click a link, your browser sends a request to the server hosting the site, which then responds with the site's files.

### IP Addresses and DNS

How do clients and servers know where to send data? They use something called IP addresses. An IP address is a unique identifier assigned to every device connected to the internet. It's like a phone number for your computer. When you visit a website, your computer sends an IP address to the website's server. The server then sends the data back to your computer.

Not only do we have IP addresses, but we also have something called DNS.

To make the internet more friendly and easier to use, we use DNS (Domain Name System). It's a system that translates domain names (like google.com) into IP addresses. For example, when you visit google.com, your computer sends a request to a DNS server. The DNS server then translates google.com into an IP address and sends the data back to your computer. This is blazing fast and happens in a matter of milliseconds. Pretty cool, right?

Both your computer and the server have an IP address.

### Introduction to Web Hosting and Deployment

How do websites get online? They use something called web hosting. It's a service that allows individuals and organizations to make their websites accessible via the World Wide Web.

Deployment is the process of making a website available to the public. It's the process of uploading files to a web server and making them accessible via the World Wide Web. By files, we mean HTML, CSS, JavaScript, images, videos, etc. Or if you were to deploy an API (Application Programming Interface), you would be uploading files that contain code that allows other applications to interact with your application. In essence, it's a matter of uploading files to a web server and making them accessible via the World Wide Web.

### HTTP Requests and Responses

<img src="https://miro.medium.com/v2/resize:fit:1358/1*CdUUublTxuAyIcnTFlxSUg.png" />

**Basics of HTTP Protocol**

How do clients and servers communicate with each other? They use something called HTTP (Hypertext Transfer Protocol). It's the protocol that allows clients and servers to communicate with each other. When you visit a website, your computer sends an HTTP request to the website's server. The server then sends an HTTP response back to your computer.

The Hypertext Transfer Protocol (HTTP) is the backbone of data communication on the World Wide Web. It is a request-response protocol in the client-server computing model. A web browser, for instance, may be the client, and an application running on a computer hosting a website may be the server. Here's how it works:

-   Client Request: A user opens a web browser, types in a URL, and presses Enter. The browser sends an HTTP request to the server.
-   Server Response: The server processes the request and sends back a response. The response contains a status line, such as "HTTP/1.1 200 OK," and a message body, which is often the requested resource, such as an HTML document.

**HTTP Methods**
There are different types of requests your browser can make to a server. The type of request is determined by what is called an HTTP method.

HTTP defines a set of request methods, each signifying a desired action to be performed. The most commonly used HTTP methods are:

-   GET: Requests data from a specified resource. It should only retrieve data and should have no other effect.
-   POST: Sends data to the server for a new resource to be created. It is often used when submitting form data or uploading a file.
-   PUT: Replaces all current representations of the target resource with the uploaded content.
-   DELETE: Removes the specified resource.
-   HEAD: Similar to GET, but it asks for a response identical to that of a GET request, without the response body.

A resource is described as a location or object that is capable of being identified by a Uniform Resource Identifier (URI). Examples of resources include HTML documents, images, videos, and style sheets. A URI is a string of characters that unambiguously identifies a particular resource. To access a resource, a client sends a request to a server. The most common type of request is an HTTP GET request, which is used to retrieve data from a specified resource. The server then sends back a response, which contains status information about the request and may also contain the requested content.

### HTTP Status Codes

Status codes are issued by a server in response to a client's request made to the server. They are part of the HTTP response message and indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

-   Informational responses (100–199)
-   Successful responses (200–299)
-   Redirection messages (300–399)
-   Client error responses (400–499)
-   Server error responses (500–599)

**Why Status Codes Matter**

-   Communication: They provide a quick way for the server to tell the client about the status of the request, such as success, failure, or need for redirection.
-   Debugging: They are crucial for diagnosing issues in HTTP communication, especially when a request fails.
-   Automation: They are used by scripts and applications to understand the response from the server and act accordingly. For instance, a 200 OK status code indicates that the request was successful, while a 404 Not Found status code indicates that the requested resource was not found.

## REST and RESTful APIs

<img src="https://voyager.postman.com/illustration/diagram-what-is-an-api-postman-illustration.svg" />

APIs, also known as Application Programming Interfaces, are a huge part of web development. They allow developers to build applications that interact with other applications. They are the glue that holds the web together. Without APIs, the web would be a very different place. APIs are everywhere. They are used by companies like Google, Facebook, Twitter, and Amazon. They are used by developers all over the world. They are used by you and me every day. APIs are the backbone of the web.

We will focus on a specific style of an API called REST.

### REST

When constructing a backend to be able to receive requests, there are a few ways we can do that. Here is a list of ways we can do that

-   SOAP (Simple Object Access Protocol)
-   XML-RPC
-   REST (Representational State Transfer)
-   GraphQL
-   custom structured 

This curriculum will focus entirely on REST since it's a widely used style and is the most common way to build APIs.

REST stands for Representational State Transfer. It's an architectural style for designing APIs. It's just a set of guidelines that developers can follow when building APIs. REST is based on the idea that everything is a resource and can be accessed using a unique identifier (which is called a URI). For example, a user is a resource and can be accessed using a URI like /users/1. REST is also stateless, which means that each request can be processed independently of the previous one. This makes REST APIs very scalable and easy to maintain.

What makes an API RESTful? There are a few things that make an API RESTful:

-   Resources: REST APIs are resource-based, which means that everything is a resource and can be accessed using a unique identifier (which is called a URI). A URI is a string of characters that unambiguously identifies a particular resource. For example, a user is a resource and can be accessed using a URI like /users/1.
-   HTTP Methods
-   Status Codes
-   Stateless: REST APIs are stateless, which means that each request can be processed independently of the previous one. This makes REST APIs very scalable and easy to maintain.
-   Caching

When it comes to building REST APIs, endpoints or routes are the most important part. They are a part of the URL that clients use to access resources. For example, if you send a GET request to /users/1 and the user exists, you would get a 200 OK response with a link to the user's profile page or data in return. If the user doesn't exist, you would get a 404 Not Found response.

Let's first talk about URLS.

### URLs

URL stands for Uniform Resource Locator. It's a string of characters that unambiguously identifies a particular resource. For example, a user is a resource and can be accessed using a URL like /users/1.

A URL is made up of three parts: the

-   protocol
-   the domain name
-   the path.

For example, the URL https://www.example.com/users/1 has

-   the protocol https
-   the domain name www.example.com
-   the path /users/1.

There are also query parameters. Query parameters are used to pass additional information to the server. Query parameters are often used to filter data.

For example, the URL https://www.example.com/users?age=30 would specify all users who are 30 years old.

Let's break this down:

-   The protocol is https.
-   The domain name is www.example.com.
-   The path is /users.
-   The query parameter is age=30.
-   The value of the query parameter is 30.
-   The URL is https://www.example.com/users?age=30.

You can attach multiple query parameters at once. Here's an example:

http://www.example.com/users?age=30&name=John

Notice the & sign, that's how you separate multiple queries.

### RESTful endpoints

An endpoint is a URL that clients use to access resources in the context of an API. Previously, we mentioned it was called a path. For example, if you send a GET request to /users/1 and the user exists, you would get a 200 OK response with a link to the user's profile page. If the user doesn't exist, you would get a 404 Not Found response with a link to the user's profile page.

However RESTful endpoints are not just URLs, they are also HTTP methods. For example, if you send a GET request to /users/1 and the user exists, you would get a 200 OK response with a link to the user's profile page. If the user doesn't exist, you would get a 404 Not Found response with a link to the user's profile page.

Here's a list of the most common RESTful endpoints:

```text
| HTTP Method | Endpoint | Description               |
| ----------- | -------- | ------------------------- |
| GET         | /users   | Returns a list of users.  |
| GET         | /users/1 | Returns a specific user.  |
| POST        | /users   | Creates a new user.       |
| PUT         | /users/1 | Updates an existing user. |
| DELETE      | /users/1 | Deletes an existing user. |
```

This is just a basic overview of RESTful endpoints. There are many more endpoints that you can use. For example, you can use GET /users/1/posts to get all posts by a specific user. You can use GET /users/1/posts/1 to get a specific post by a specific user. You can use POST /users/1/posts to create a new post by a specific user. You can use PUT /users/1/posts/1 to update an existing post by a specific user. You can use DELETE /users/1/posts/1 to delete an existing post by a specific user. And so on.

Great! Now that we have a basic understanding of REST and RESTful APIs, let's take a look at how to build a RESTful API using Ruby on Rails.

<img src="https://media.sketchfab.com/models/a6c6bbf6e40d4dc9a79de5a6437d7488/thumbnails/d7c9fc58d91e4ed4b2d2859c39dbce1f/49111ee5155a4d979c297e222b6e95df.jpeg" />

## Ruby on Rails Introduction

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/Ruby_On_Rails_Logo.svg/1200px-Ruby_On_Rails_Logo.svg.png" />

Ruby on Rails, or Rails for short, is a web application framework written in Ruby. It's designed to make building web applications easier by making assumptions about what every developer needs to get started. It allows you to write less code while accomplishing more than many other languages and frameworks. It's also one of the most popular web frameworks in the world. Although it is a framework, it's a gem. A gem is a package that contains Ruby code. It's similar to a Node.js module or a Python package.

Rails is a Model-View-Controller (MVC) framework. The MVC pattern is a software design pattern that separates the representation of information from the user's interaction with it. It's a way to organize code into three distinct parts: models, views, and controllers.

-   Models are responsible for managing the data of the application. They are the interface between the application and the database. They are also responsible for validating data and enforcing business rules.
-   Views are responsible for displaying data to the user. They are the interface between the application and the user. They are also responsible for handling user input.
-   Controllers are responsible for handling requests and generating responses. They are the interface between the application and the web server. They are also responsible for handling business logic.

Rails is a full-stack framework, which means that it provides everything you need to build a web application, both frontend and backend. It includes a router, a controller, a model, a view, and a database. It also includes a lot of other features, such as a built-in web server, a built-in testing framework, and a built-in debugging framework. However we will only be focusing on the backend portion of Rails, since we will be building a RESTful API and leveraging other powerful tools to build the frontend.

This is great, but what does it mean? It means that you can build a web application without having to worry about the details. You can focus on what matters: building your application.

What are the advantages and disadvantages of Rails?

Advantages:

-   Convention over configuration: Rails makes assumptions about what every developer needs to get started. It allows you to write less code while accomplishing more than many other languages and frameworks.
-   Full-stack framework: Rails provides everything you need to build a web application. It includes a router, a controller, a model, a view, and a database. It also includes a lot of other features, such as a built-in web server, a built-in testing framework, and a built-in debugging framework.
-   Active Record: Rails uses a database abstraction layer called Active Record. It allows you to interact with the database using Ruby objects instead of SQL queries.
-   Gems: Rails has a lot of gems that you can use to add functionality to your application. For example, there are gems for authentication, authorization, and pagination.
-   Community: Rails has a large and active community. There are a lot of resources available online, such as tutorials, screencasts, and books.
-   Open source: Rails is open source, which means that anyone can contribute to it. This means that you can fix bugs, add features, and improve documentation.
-   Fast development: Rails is designed to make building web applications easier by making assumptions about what every developer needs to get started. It allows you to write less code while accomplishing more than many other languages and frameworks.

Disadvantages:

Compared to other frameworks, Rails has a few disadvantages:

-   Ruby on Rails as a full-stack framework is not as flexible as other frameworks.
-   Performance: Rails can be slower compared to frameworks written in compiled languages like Java or C#. This might be a concern for high-performance applications.
-   Learning Curve: While Rails itself is easy to pick up, mastering the Ruby language and understanding the "Rails way" of doing things (CoC and DRY) can be challenging for beginners.
-   Memory Usage: Rails applications can consume more memory compared to other frameworks, which might be an issue for memory-sensitive environments.

These disadvantages are not deal-breakers, but they are worth considering when choosing a framework for your next project. It's not enough to just look at the advantages of a framework. You also need to look at the disadvantages. Ruby on Rails is a perfect solution for many projects, but it might not be the best solution for every project.

Although Ruby on Rails is regarded a full-stack framework, we will only be focusing on the backend portion of Rails since we will be building a RESTful API and leveraging other powerful tools to build the frontend.

Now that we have a basic understanding of Rails, let's take a look at how to build a RESTful API using Rails.

### Installing Ruby on Rails

Before we can start building our RESTful API, we need to install Ruby on Rails.

To install Ruby on Rails, you need to have Ruby installed on your computer.

We no longer will need Replit since we have Ruby installed in our computers.

If you're on windows, be sure to use WSL2 (Windows Subsystem for Linux).

Run the following command in your terminal. 

```bash
gem install rails
```

This is going to install Rails globally on your computer.

When we install Rails successfully, we have access to the rails CLI. The rails CLI is a command-line interface for Rails. It allows us to create new Rails projects, generate a variety of files and run automated commands to help us build our application.

Check the version of Rails you have installed using the rails command:

```bash
rails -v
```

We will be using Rails 8 for this curriculum, which is the latest version of Ruby on Rails as of 2025. By default, when running the `gem install rails` command, it will automatically install the latest version.

Let's go ahead and create a new Rails project.

### Creating a new Rails Project

To create a new rails project, there are two ways we can do that.

Let's start by observing the general way of creating a new Rails project. Don't run this command.

```bash
rails new <project-name>
```

This will create a new Rails project with the name you specified. For standards' sake, be sure to use snake_case for the project name, separating every word with an underscore.

By default, running this command will create a new Rails project. However, it will be configured and set up to be used as a full stack project.

Open the project in VS Code.

Since we are only using Rails for the backend, we can specify that we only want to create a Rails API. Let's run the following command:

```bash
rails new my_first_rails_project --api
```

Open the project in VS Code.

This will create a new Rails project that is configured and set up to be used as a RESTful API.

The main difference between creating a full stack project in Rails and creating an API-only project is that a full stack project will include many files and folders that we won't be using. For example, a full stack project will include a `views` folder, which is where we would store our HTML files. Since we are only using Rails for the backend, we won't be needing this folder. We will be leveraging other frameworks to build our frontend, like Angular, React, or Vue.

Another difference is that a full stack project will include a lot of gems that we won't be using. For example, a full stack project will include a gem called `sprockets-rails` which is used to compile assets like JavaScript and CSS.

### Rails Directory Structure

When we create a new Rails project, it will create a lot of files and folders. Let's take a look at the most important ones:

-   Rails will create a git repository for us. This is where we can commit our changes and push them to GitHub.
-   app: This is where we will be spending most of our time. This folder contains the following sub-folders:
    -   channels: This contains the Action Cable channels for our application. Action Cable is a framework for real-time communication over WebSockets.
    -   controllers: This contains the controllers for our application. Controllers are responsible for handling requests and generating responses.
    -   jobs: This contains the Active Job jobs for our application. Active Job is a framework for declaring jobs and making them run on a variety of queuing backends.
    -   mailers: This contains the mailers for our application. Mailers are responsible for sending emails.
    -   models: This contains the models for our application. Models are responsible for managing the data of the application.
    -   views: This contains the views for our application. Views are responsible for displaying data to the user. They are the interface between the application and the user. They are also responsible for handling user input. However when it comes to building a RESTful API, we won't be using this folder other than crafting our own email templates.
-   bin: This contains the rails executable, which is used to run commands like rails server and rails console.
    -   The `rails server` command is used to start the Rails server. The Rails server is a web server that runs our application.
    -   The `rails console` command is used to start the Rails console. The Rails console is an interactive Ruby shell that allows us to interact with our application and the database.
-   config: This contains the configuration files for our application, such as routes.rb, database.yml, and application.rb.
    -   The routes.rb file is used to define the routes for our application. Routes are used to map URLs to controllers and actions.
    -   The database.yml file is used to configure the database for our application. Rails uses SQLite3 as the database by default.
    -   The application.rb file is used to configure the application for our application. It's where we can configure things like the default locale, the default time zone, and the default encoding.
-   db: This contains the database schema and migrations for our application.
    -   By default when creating a new Rails project, it will use SQLite3 as the database. We will be using SQLite3 for this curriculum since it's lightweight and compatible with multiple devices.
-   lib: This contains the code that is shared between different parts of our application. For example, we can put our custom validators in the lib/validators folder.
-   log: This contains the log files for our application. This is where we can find information about what's happening in our application when it's running. We can either find this while running the server or when we deploy our application to a server.
-   public: This contains the static files for our application, such as images, JavaScript, and CSS.
-   storage: This contains the files that are uploaded by users.
-   test: This contains the tests for our application.
-   tmp: This contains temporary files for our application.
-   vendor: This contains third-party code that is not managed by Bundler.

Great, that was a lot of information to process and it won't digest until we start building our application. Let's go ahead and start exploring interactive with the very first thing we will be doing, which is creating a model and interact with the database.

>**💡 Practice with the Codelabs Learning Assistant**
>
>Try this: _"Can you explain what each main folder in a Rails project is for? Why is the 'app' folder so important?"_  
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

### Using the Rails CLI to generate a model

Models are responsible for managing the data of the application. They are the interface between the application and the database. Ruby on Rails has a built in ORM (Object Relational Mapping) called Active Record. It allows us to interact with the database using Ruby objects instead of SQL queries. We will talk more about this shortly.

Models are also responsible for validating data and enforcing business rules.
 
Business rules are rules that are specific to the business. For example, if we have a user model, we might want to enforce a rule that says that a user can't have the same email address as another user. Another example would be if we have a product model, we might want to enforce a rule that says that a product can't have a negative price.

To create a model, we can use the rails generate model command:

```bash
rails generate model User name:string email:string
```

Let's go over this command:

-   rails generate model: This is the rails command that is used to generate a model.
-   User: This is the name of the model. It's convention to use singular nouns for model names.
-   name:string email:string: These are the attributes of the model. They are used to define the columns of the database table. The first part is the name of the attribute and the second part is the type of the attribute. In this case, we are using the string type, which means that the attribute will be a string. Other types include integer, float, decimal, datetime, and boolean.

This will create a new model called User in which includes a series of files like **app/models/user.rb**. It will also create a migration file for the User model. 

A migration is a Ruby class that is used to make changes to the database. It's a way to update the database schema. For example, we can use migrations to create tables, add columns, and remove columns.

### Migrations

Let's take a look at the migration file that was generated for us. Navigate to the `db/migrate` folder and open the migration file within `migrate` that was generated for us. The file should look similar to this `20240110170144_create_users` and inside, it should look something like this:

```ruby
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :name
      t.string :email

      t.timestamps
    end
  end
end
```

Let's breakdown this migration file:

-   class CreateUsers < ActiveRecord::Migration[7.0]: This is the name of the migration class. It's convention to use the name of the model followed by the name of the migration. In this case, the model is User and the migration is CreateUsers. The migration class inherits from the ActiveRecord::Migration class. This is the base class for all migrations.
-   change method: This is the method that is used to make changes to the database. It's a method that is defined in the ActiveRecord::Migration class.
-   create_table method: This is the method that is used to create a new table in the database. It's a method that is defined in the ActiveRecord::ConnectionAdapters::SchemaStatements class.
-   :users: This is the name of the table. It's convention to use the plural form of the model name.
-   t.string :name and t.string :email: This is the name of the column. It's convention to use the singular form of the attribute name.
-   t.timestamps: This is a shortcut for creating two columns called created_at and updated_at. These columns are used to store the date and time when a record is created and updated.


There are a wide variety of data types that we can use for our columns. Here are some of the most common ones:

-  string: This is used to store strings.
-  text: This is used to store large strings.
-  integer: This is used to store integers.
-  float: This is used to store floating-point numbers.
-  decimal: This is used to store decimal numbers.
-  datetime: This is used to store date and time values.
-  boolean: This is used to store boolean values.
-  binary: This is used to store binary data.
-  json: This is used to store JSON data.
-  and more.

Great, let's talk a little bit more in detail of what migration files are.

Migration files are Ruby classes that are used to make changes to the database. They are a way to update the database schema. For example, we can use migrations to create tables, add columns, and remove columns.

The file name for migration files are prefixed with a timestamp. This is used to determine the order in which migrations are applied. For example, if we have two migration files with the same timestamp, Rails will apply them in alphabetical order. This is important because migrations can depend on each other. For example, if we have a migration that adds a column to a table and another migration that removes the same column from the same table, Rails will apply the first migration before the second one. This is called a migration dependency.

Another note is do not delete or modify migration files. If you need to make changes to a migration file, you should create a new migration file instead. This is because Rails uses the migration files to determine the current state of the database. If you delete or modify a migration file, Rails won't be able to determine the current state of the database. This can lead to problems when running migrations especially on a production(live) environment.

Since we generated the creation of the file using a Ruby on Rails command, it doesn't automatically create the table in the database. We need to run the migration file to create the table in the database. To run the migration file, we can use the rails db:migrate command:

```bash
rails db:migrate
```

This will run all the pending migrations. Pending migrations are migrations that haven't been run yet. Running this command will execute the migration file we have created. It will create the users table in the database.

You should see something along the lines of this:

```text
== 20231230191708 CreateUsers: migrating ======================================
-- create_table(:users)
   -> 0.0018s
== 20231230191708 CreateUsers: migrated (0.0019s) =============================
```

What if we made a mistake and like to modify our migration file? We can do that by running the rails db:rollback command:

```bash
rails db:rollback
```

This will rollback the last migration and reset the state of the migration file back to pending. It will remove the users table from the database since that was the last migration we ran. You should see something along the lines of this:

```text
== 20231230191708 CreateUsers: reverting ======================================
-- drop_table(:users)
   -> 0.0018s
== 20231230191708 CreateUsers: reverted (0.0019s) =============================
```

Try it yourself. Once you have done this, try running the `rails db:migrate` command again to execute the migration file again since we do want to have the users table in the database.

Sometimes we may want to rollback multiple migrations. We can do that by specifying the number of migrations we want to rollback. For example, if we want to rollback the last two migrations, we can run the rails db:rollback STEP=2 command:

However, this won't work now since we only have one migration file. 

```bash
rails db:rollback STEP=2
```

### Schema

Now that we have created the users table in the database, let's take a look at the schema file. Navigate to the db folder and open the schema.rb file.

The schema essentially is a representation of the database. It will include all the tables and columns that are in the database. We never have to manually modify this file. It's automatically generated by Rails and it's used to determine the current state of the database. If at any point we want to modify the database, we can do that by creating a new migration file like we did before.

When you run `db:migrate` it will change the schema file. Let's take a look at the schema file that was generated for us. It should look something like this:

```ruby
ActiveRecord::Schema.define(version: 20231230191708) do

  create_table "users", force: :cascade do |t|
    t.string "name"
    t.string "email"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

end
```

Let's breakdown this schema file:

-   ActiveRecord::Schema.define: This is the name of the schema class.
-   version: 20231230191708: This is the version of the schema. It's used to determine the current state of the database. It's a timestamp that is generated when we run the rails db:migrate command.
-   create_table "users": This is the method that is used to create a new table in the database. It's a method that is defined in the ActiveRecord::ConnectionAdapters::SchemaStatements class.
-   t.string "name" and t.string "email": This is the method that is used to create a new column in the database. It's a method that is defined in the ActiveRecord::ConnectionAdapters::TableDefinition class.
-   t.datetime "created_at" and t.datetime "updated_at": This is a shortcut for creating two columns called created_at and updated_at. These columns are used to store the date and time when a record is created and updated.
-   force: :cascade: This is an option that is used to drop the table before creating it. This is useful when we want to reset the state of the database.
-   precision: 6: This is an option that is used to specify the precision of the datetime columns. It's used to store the date and time when a record is created and updated.
-   null: false: This is an option that is used to specify that the column cannot be null. This is useful when we want to enforce business rules.

What is interesting as well is the table does not indicate the primary key. This is because Rails automatically creates a primary key for us. It's called id and it's an integer. It's also auto-incremented. This means that every time we create a new record, the id will be incremented by one. This is useful when we want to reference a record from another table.

#### Practice Problem

Create a new project called `ruby_on_rails_intro_practice`. 

Create a new model called Post with the following attributes:

-   title: string
-   body: text
-   published: boolean
-   published_at: datetime

Be sure to run the migration file to create the table in the database.

<details>

<summary>Solution</summary>

```bash
rails generate model Post title:string body:text published:boolean published_at:datetime
```

**migration file**

```ruby
class CreatePosts < ActiveRecord::Migration[7.0]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :body
      t.boolean :published
      t.datetime :published_at

      t.timestamps
    end
  end
end
```

```bash
rails db:migrate
```

**schema.rb**

```ruby
ActiveRecord::Schema.define(version: 20231230191708) do

  create_table "posts", force: :cascade do |t|
    t.string "title"
    t.text "body"
    t.boolean "published"
    t.datetime "published_at"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
  end

end
```

</details>

## Interacting with the Database with Models

Great, now that we have created the table in the database, let's go ahead and interact with the database.

Rails uses a database abstraction layer called Active Record, also referred to as a ORM (Object Relational Mapping). It allows us to interact with the database using Ruby objects instead of SQL queries. For example, we can use the User model to create, read, update, and delete users. We can also use the User model to validate data and enforce business rules.

Why is this important? It's important because it allows us to write less code while accomplishing more than many other languages and frameworks. It also makes it easier to maintain our application since we don't have to worry about writing SQL queries.

With Rails, the way we can use the ORM is if we define the correct files and folders in the right spot. Since we ran the command `rails generate model User name:string email:string`, it created a file under app/models/user.rb. This is where we will be defining our model.

Let's take a look at the model file that was generated for us. Navigate to the app/models folder and open the user.rb file. It should look something like this:

```ruby
class User < ApplicationRecord
end
```

Let's breakdown this model file:

- ApplicationRecord is a class that is defined in the ActiveRecord::Base class. It's the base class for all models. We can define methods that are used to validate data and enforce business rules.
-   class User < ApplicationRecord: This is the name of the model class. It's convention to use the name of the model followed by the name of the model. The class name is important because it's used to determine the name of the table we will be interacting with.

In this class, we can define methods that include business logic, validations, and callbacks.

Naming of files and folders are very important in Rails. If we don't name them correctly, Rails won't be able to find them. For example, if we name the model file usurs.rb instead of user.rb, Rails won't be able to find it. This is because Rails uses the naming convention to determine where to look for files and folders.

Same goes with the naming of the class. If we name the class Usur instead of User, Rails won't be able to find it. This is because Rails uses the naming convention to determine where to look for files and folders.

### Model Methods

We have everything we need to interact with the database. Let's go ahead and create a new user.

To interact with the database, we can use the rails console command:

```bash
rails console
```

This will start the Rails console. The Rails console is an interactive Ruby shell that allows us to interact with our application and the database. It's similar to the Rails server, but it's used for debugging purposes or to access the database instead of running the application.

If we choose to exit the console to go back to the terminal, we can do that by running the exit command:

```bash
exit
```

Whenever I create a model, I like to confirm that the table, columns, files and everything that is needed is created to access the table in the database through active record. To interact with the table, we need to know the name of the model class. In this case, the model class is `User` which is defined in the app/models/user.rb file.

Let's go ahead and create a new user. We can do that by running the following command:

```ruby
User.create(name: "John Doe", email: "johndoe@gmail.com")
```

This is the equivalent of running the following SQL query:

```sql
INSERT INTO users (name, email) VALUES ("John Doe", "johndoe@gmail.com")
```

Here's what this command does:

-   User: This is the name of the model that is defined in the app/models/user.rb file.
-   create: This is the method that is used to create a new record(also referred to as a row in the table) in the database. It's a method that is defined in the ActiveRecord::Persistence class.
-   Since our model has two attributes, we need to specify the values for both of them. We can do that by passing in a hash with the attribute names as keys and the attribute values as values. In this case, we are passing in a hash with the name and email attributes. This is called a hash literal. It's a way to create a hash without using the Hash.new method.

This will create a new user with the name John Doe and the email `johndoe@gmail.com` in the database. It will also return the user object.

Remember, Ruby on rails uses an ORM (Object Relational Mapping) called Active Record. It allows us to interact with the database using Ruby objects instead of SQL queries. For example, we can use the User model to create, read, update, and delete users. We can also use the User model to validate data and enforce business rules. 

Let's go ahead and find the user we just created. We can do that by running the following command:

```ruby
User.find(1)
```

This will find the user with the id 1 in the database. It will also return the user object.

This is the equivalent of running the following SQL query:

```sql
SELECT * FROM users WHERE id = 1
```

The return value of the find method is an object of the User class. To access the attributes of the user, we can use the dot notation. For example, to access the name attribute, we can use the following command:

```ruby
user = User.find(1)
user.name
```

Let's update the user we just created. We can do that by running the following command:

```ruby
user = User.find(1)
user.update(name: "Jane Doe", email: "janedoe@gmail.com")
```

This will update the user with id 1 in the database. It will also return the user object.

This is the equivalent of running the following SQL query:

```sql
UPDATE users SET name = "Jane Doe", email = "janedoe@gmail.com" WHERE id = 1
```

Let's delete the user we just created. We can do that by running the following command:

```ruby
user = User.find(1)
user.destroy
```

This will delete the user with the id 1 in the database. It will also return the user object.

This is the equivalent of running the following SQL query:

```sql
DELETE FROM users WHERE id = 1
```

This is great, but what if we want to find all users? We can do that by running the following command:

```ruby
User.all
```

This will find all users in the database. It will also return an array of user objects.

This is the equivalent of running the following SQL query:

```sql
SELECT * FROM users
```

What if we want to find all users with a specific name? We can do that by running the following command:

```ruby
User.where(name: "John Doe")
```

This will find all users with the name John Doe in the database. It will also return an array of user objects.

This is the equivalent of running the following SQL query:

```sql
SELECT * FROM users WHERE name = "John Doe"
```

What if we want to find all users with a specific name and email? We can do that by running the following command:

```ruby
User.where(name: "John Doe", email: "johndoe@gmail.com")
```

There are many more model class methods, here's a list:

-   **find_by**: This is the method that is used to find a record by a specific attribute.
-   **count**: This is the method that is used to count the number of records. It's a method that is defined in the ActiveRecord::Calculations class.
-   **first**: This is the method that is used to find the first record.
-   **last**: This is the method that is used to find the last record.
-   **all**: This is the method that is used to find all records.
-   **where**: This is the method that is used to find records by a specific attribute.
-   **where.not**: This is the method that is used to find records by a specific attribute.
-   **order**: This is the method that is used to order records by a specific attribute.
-   **limit**: This is the method that is used to limit the number of records.
-   **offset**: This is the method that is used to offset the number of records.

Great, now that we have a basic understanding of how to interact with the database,

#### Practice Problem

Create a new Post model with the following attributes:

-   title: "Hello World"
-   body: "This is my first post"
-   published: true
-   published_at: 2023-12-30 19:17:08

Find the post and update the post with the following attribute:

-   published: false

Then delete the post.

<details>

<summary>Solution</summary>

```ruby
Post.create(title: "Hello World", body: "This is my first post", published: true, published_at: "2023-12-30 19:17:08")
```

```ruby
post = Post.find(1)
post.update(title: "Hello World", body: "This is my first post", published: false, published_at: "2023-12-30 19:17:08")
```

```ruby
post = Post.find(1)
post.destroy
```

</details>

### Validations

Now that we have created a model and interacted with the database, let's talk about validations. Validations are used to validate data and enforce business rules. For example, we can use validations to ensure that a user has a name and an email address. We can also use validations to ensure that a user's email address is unique.

There are different types of validations we can enforce. We can enforce validations on the database level and the model level. We can also include validations in our Front End as well.

Let's talk about the different types of validations we can enforce.

-   Database level: This is the most basic type of validation. It's used to ensure that the data in the database is valid. For example, we can use database level validations to ensure that a user has a name and an email address. We can also use database level validations to ensure that a user's email address is unique.
-   Model level: This is the most common type of validation. It's used to ensure that the data in the model is valid. For example, we can use model level validations to ensure that a user has a name and an email address. We can also use model level validations to ensure that a user's email address is unique.

Why do both exist?

Having both database and model-level validations offers multiple layers of security. Database-level validations act as a final safeguard ensuring data integrity at the most fundamental level, while model-level validations provide a more user-friendly and flexible way to enforce rules and business logic.

-   Model-level validations alone might not be sufficient in cases where multiple applications interact with the same database, as each application might have different validation rules or might bypass validations entirely. In such cases, database-level constraints become crucial.
-   Database-level constraints are important for maintaining data integrity, especially in larger applications or in applications where the database might be accessed by different services or applications. They ensure that even if the application logic fails or is bypassed, the data in the database remains consistent and valid.

Frontend validations are also beneficial, as they help reduce unnecessary server requests. This enhances user experience by eliminating the need for users to wait for server responses to each error. Initial validations are performed on the client side for immediate feedback, followed by more comprehensive validations on the backend.

At this moment in time, we will be focusing on model level validations.

Let's go ahead and add some validations to our User model. Navigate to the app/models/user.rb file and add the following code:

**user.rb**

```ruby
class User < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true
end
```

Let's breakdown this code:

```ruby
validates :name, presence: true
```

This is the method that is used to validate the name attribute. It takes two arguments: the name of the attribute and the validation rule. In this case, we are using the presence validation rule, which means that the attribute must be present. Meaning, it cannot be nil or an empty string.

```ruby
validates :email, presence: true, uniqueness: true
```

This is an example of adding multiple validations at once, requiring that the email attribute not be nil or '' and that it be unique.

Let's demonstrate these validations by creating a new user. We can do that by running the following command:

```ruby
User.create(name: "jimmy james", email: "jimmyjames@gmail.com")
```

Here we create a new user with the name `jimmy james` and the email `jimmyjames@gmail.com`. If we create a new user with the same email, we will get an error. This is because we have a uniqueness validation on the email attribute. This means that the email attribute must be unique.

If we try to create a new user without a name, we will get an error. This is because we have a presence validation on the name attribute. This means that the name attribute must be present.

```text
errors = User.create(name: "", email: "")

errors.messages # => {:name=>["can't be blank"], :email=>["can't be blank"]}
```

>**💡 Practice with the Codelabs Learning Assistant**
>
> Try this: _"How do you add a validation to make sure an email is unique in Rails? Can you show me a code example?"_  
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

#### Practice Problem

From the previous practice problem, add the following validations to the post model:

Include validations to the post model with the following rules:

-   Title, published_at must be present
-   Title must be unique

<details>

<summary>Solution</summary>

```ruby
class Post < ApplicationRecord
  validates :title, presence: true, uniqueness: true
  validates :published_at, presence: true
end
```

</details>

Here are other examples of model validators:

```ruby
validates :email, format: { with: URI::MailTo::EMAIL_REGEXP }
```

Checks if the value of an attribute matches a given regular expression.

```ruby
validates :username, length: { minimum: 5, maximum: 20 }
```

Ensures that the length of the attribute's value is within a specified range.

```ruby
validates :age, numericality: { greater_than: 0 }
```

Ensures that the attribute's value is a number, and can also validate if it is greater than, less than, equal to, odd, even, etc.

```ruby
validates :status, inclusion: { in: %w[pending approved rejected] }
```

Validates that the value of the attribute is included in or excluded from a given set.

```ruby
validates :notes, absence: true
```

Validates that the specified attributes are empty or nil.

```ruby
validates :password, confirmation: true
```

Used mainly for passwords and emails, ensuring that two text fields receive exactly the same content.

```ruby
validates :terms_of_service, acceptance: true
```

Checks if a checkbox (like terms of service) is checked.

### Custom Model Validators

Custom validators are used to validate data and enforce business rules.

Let's go ahead and add some custom validators to our User model. Navigate to the app/models/user.rb file and add the following code:

```ruby
class User < ApplicationRecord
  validate :name_cannot_contain_numbers

  def name_cannot_contain_numbers
    if name.match(/\d/)
      errors.add(:name, "cannot contain numbers")
    end
  end
end
```

Let's breakdown this code:

```ruby
validate :name_cannot_contain_numbers
```

This is the method that is used to add a custom validator.

```ruby
def name_cannot_contain_numbers
  if name.match(/\d/)
    errors.add(:name, "cannot contain numbers")
  end
end
```

This is the method that is used to define the custom validator. If the name attribute contains numbers, we add an error to the name attribute.

Adding an error attribute will allow you to access the error message. For example, if we try to create a new user with the name "John Doe 123", we will get an error. This means that the name attribute cannot contain numbers.

### Callbacks

Now that we have created a model, interacted with the database, and added some validations, let's talk about callbacks. Callbacks are used to execute code before or after certain events. For example, we can use callbacks to send an email after a user is created. We can also use callbacks to update a user's profile after they log in.

There are different types of callbacks we can use. We can use callbacks to execute code before or after certain events. We can also use callbacks to execute code before or after certain actions.

Let's talk about the different types of callbacks we can use.

-   **Before or after certain events**: This is the most basic type of callback. It's used to execute code before or after certain events. For example, we can use callbacks to send an email after a user is created. We can also use callbacks to update a user's profile after they log in.

-   **Before or after certain actions**: This is the most common type of callback. It's used to execute code before or after certain actions. For example, we can use callbacks to send an email before a user is created. We can also use callbacks to update a user's profile before they log in.

Why do both exist?

Having both before and after callbacks offers multiple layers of security. Before callbacks act as a final safeguard ensuring data integrity at the most fundamental level, while after callbacks provide a more user-friendly and flexible way to execute code before or after certain events.

Here's an example of a before callback:

```ruby
class User < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  before_create :downcase_email

  private

  def downcase_email
    self.email = email.downcase
  end
end
```

Let's breakdown this code:

```ruby
before_create :downcase_email
```

This is the method that is used to add a callback. In this case, we are using the before_create callback, which means that the method will be called before the record is created. We are also using the `downcase_email` method, which means that the email attribute will be downcased before the record is created.

Let's demonstrate this callback by creating a new user. We can do that by running the following command:

```ruby
User.create(name: "Avery Ivery", email: "aVeRyIvery");
```

Here we create a new user with the name "Avery Ivery" and the email "aVeRyIvery". We can ensure that the email will be downcased before the record is created by checking the email attribute. Check the email attribute to ensure this.

Here's an example of an after callback:

```ruby
User.last.email
```

#### Practice Problem

Include a callback to the post model with the following rules:

-   Each word in title must be capitalized before the record is created

<details>

<summary>Solution</summary>

```ruby
class Post < ApplicationRecord
  validates :title, presence: true, uniqueness: true
  validates :published_at, presence: true

  before_create :capitalize_title

  private

  def capitalize_title
    self.title = title.split.map(&:capitalize).join(' ')
  end
end
```

</details>

### Introduction to Associations

Now that we have created a model, interacted with the database, added some validations, and added some callbacks, let's talk about associations. Associations are used to define relationships between models. For example, we can use associations to define a one-to-one relationship between a user and a profile. We can also use associations to define a one-to-many relationship between a user and a post. Active record makes it unbelievably easy to define these relationships. All we have to do is follow the naming convention and Rails will take care of the rest.

There are different types of associations but we will start off with basic ones for now.

Let's talk about the different types of associations we can use.

-   **One-to-one**: This is the most basic type of association. It's used to define a one-to-one relationship between two models. For example, we can use associations to define a one-to-one relationship between a user and a profile.
-   **One-to-many**: This is the most common type of association. It's used to define a one-to-many relationship between two models. For example, we can use associations to define a one-to-many relationship between a user and a post.
-   **Many-to-many**: This is the most complex type of association. It's used to define a many-to-many relationship between two models. For example, we can use associations to define a many-to-many relationship between a user and a group.
-   **Polymorphic**: This is the most advanced type of association. It's used as a way to set up a single model that can belong to more than one other model, using a single association. For example, a comment can be associated with a post or video.
-   **Self-join**: This is the most advanced type of association. It's used to define a self-join relationship between two models. For example, we can use associations to define a self-join relationship between a user and a friend.

We will only be focusing on one-to-one and one-to-many relationships for now.

### One-to-one: belongs to and has one associations

Let's go ahead and add a has_one association to our User model.

Since we have a user table, we will need to create a profile table. We can do that by running the following command:

```bash
rails generate model Profile user:references bio:text
```

Let's go over this command:

-   Profile: This is the name of the model. It's convention to use singular nouns for model names.
-   user:references: This is the type of the attribute. It's used to define a one-to-one relationship between two models. In this case, we are using the references type, which means that the attribute will be a reference to another model. In this case, we are referencing the User model. This will create a user_id column in the profiles table.
-   bio:text: This is the name of the attribute and the type of the attribute. In this case, we are using the text type, which means that the attribute will be a text.

This will create

-   a model file under app/models/profile.rb.
-   a migration file under db/migrate.

**profile.rb**

```ruby
class Profile < ApplicationRecord
  belongs_to :user
end
```

Let's breakdown this code:

-   belongs_to :user: This is the method that is used to add a `belongs_to` association. It takes two arguments: the name of the association and the options. In this case, we are using the `belongs_to` association, which means that the profile belongs to a user. We are also using the user method, which means that the profile belongs to a user. This will create a user method that returns the user associated with the profile.

Let's go ahead and run the migration file to create the table in the database. We can do that by running the following command:

```bash
rails db:migrate
```

Navigate to the app/models/user.rb file and add the following code:

```ruby
class User < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  before_create :downcase_email

  has_one :profile

  private

  def downcase_email
    self.email = email.downcase
  end
end
```

Let's breakdown this code:

-   has_one :profile: This is the method that is used to add a one-to-one relationship. It takes two arguments: the name of the association and the options. In this case, we are using the `has_one` association, which means that the user has one profile. We are also using the profile method, which means that the user has one profile. This will create a profile method that returns the profile associated with the user.

Now that we have our setup, let's go ahead and create a new user with a profile. We can do that by running the following command:

```ruby
user = User.create(name: "James Underway", email: "james_underway@gmail.com", profile: Profile.new(bio: "I am a software engineer"))
```

Here we create a new user with the name "James Underway" and the email "james_underway@gmail.com" and a profile with the bio "I am a software engineer". We can ensure that the profile is associated with the user by checking the profile attribute. It should be a profile object instead of nil.

Let's go ahead and find the user we just created. Then we can access their profile as well. We can do that by running the following command:

```ruby
user = User.find(1)
user.profile
```

Voilà! We have successfully created a one-to-one relationship between a user and a profile.

#### Practice Problem

Create a new Rails application as an API of course, then create the following tables

-   employee
    -   first_name:string
    -   last_name:string
-   employee_details
    -   employee:references
    -   bio:text
    -   salary:integer

Create a one-to-one association between the employee and employee_details table.

Then create a new employee along with their employee details.

<details>

<summary>Solution</summary>

```bash
rails new employee_api --api
```

```bash
rails generate model Employee first_name:string last_name:string
```

```bash
rails generate model EmployeeDetail employee:references bio:text salary:integer
```

**employee.rb**

```ruby
class Employee < ApplicationRecord
  validates :first_name, presence: true
  validates :last_name, presence: true

  has_one :employee_detail
end
```

**employee_detail.rb**

```ruby
class EmployeeDetail < ApplicationRecord
  belongs_to :employee
end
```

```bash
rails db:migrate
```

```ruby
employee = Employee.create(first_name: "John", last_name: "Doe", employee_detail: EmployeeDetail.new(bio: "I am a software engineer", salary: 100000))
```

</details>

### One-to-many: belongs to and has many associations

As we have seen, one-to-one relationship includes a belongs_to and has_one association. A one-to-many relationship includes a belongs_to and has_many association. Let's go ahead and add a has_many association to our User model.

Since we have a user table, we will need to create a post table. We can do that by running the following command:

```bash
rails generate model Post user:references title:string body:text published:boolean published_at:datetime
```

Let's go over this command:

-   Post: This is the name of the model. It's convention to use singular nouns for model names.
-   user:references: This is the type of the attribute. It's used to define a one-to-many relationship between two models. In this case, we are using the references type, which means that the attribute will be a reference to another model. In this case, we are referencing the User model. This will create a user_id column in the posts table.

**app/models/post.rb**

```ruby
class Post < ApplicationRecord
  belongs_to :user
end
```

Let's go ahead and run the migration file to create the table in the database. We can do that by running the following command:

```bash
rails db:migrate
```

Navigate to the app/models/user.rb file and add the following code:

```ruby
class User < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true, uniqueness: true

  before_create :downcase_email

  has_one :profile
  has_many :posts

  private

  def downcase_email
    self.email = email.downcase
  end
end
```

Let's breakdown this code:

-   has_many :posts: This is the method that is used to add a one-to-many relationship. It takes two arguments: the name of the association and the options. In this case, we are using the `has_many` association, which means that the user has many posts. We are also using the posts method, which means that the user has many posts. This will create a posts method that returns the posts associated with the user.

Now that we have our setup, let's go ahead and create a new user with a post. We can do that by running the following command:

```ruby
user = User.create(name: "Amy Underway", email: "@email.com", posts: [Post.new(title: "Hello World", body: "This is my first post", published: true, published_at: "2023-12-30 19:17:08")])
```

There are many ways we can include a post in relation to a user such as the following:

```ruby
user = User.find(1)
post = Post.new(title: "Hello World", body: "This is my second post", published: true, published_at: "2023-12-30 19:17:08")
user.posts << post
```

Here we create a new user with the name "Amy Underway" and the email "@email.com" and a post with the title "Hello World", body "This is my first post", published true, and published_at "2023-12-30 19:17:08". We can ensure that the post is associated with the user by checking the posts attribute. It should be an array of post objects instead of nil.

Let's go ahead and find the user we just created. Then we can access their posts as well. We can do that by running the following command:

```ruby
user = User.find(1)
user.posts
```

Voilà! We have successfully created a one-to-many relationship between a user and a post.

#### Practice Problem

Create a new Rails application as an API of course, then create the following tables

post

-   title:string
-   body:text

comment

-   post:references
-   body:text
-   published:boolean

Create a one-to-many relationship between the post and comment table.

Then create a new post along with their comments.

<details>

<summary>Solution</summary>

```bash
rails new post_api --api
```

```bash
rails generate model Post title:string body:text
```

```bash
rails generate model Comment post:references body:text published:boolean
```

**post.rb**

```ruby
class Post < ApplicationRecord
  validates :title, presence: true, uniqueness: true
  validates :body, presence: true

  has_many :comments
end
```

**comment.rb**

```ruby
class Comment < ApplicationRecord
  validates :body, presence: true

  belongs_to :post
end
```

```bash
rails db:migrate
```

```ruby
post = Post.create(title: "Hello World", body: "This is my first post", comments: [Comment.new(body: "This is my first comment", published: true)])
```

</details>

## Conclusion

By this time, you probably understand why web development is so popular and difficult to learn. There are so many different technologies and frameworks to learn. Though, once you learn the fundamentals, it becomes easier to learn new technologies and frameworks. This is because many web development technologies share common underlying principles, so learning one often provides a solid foundation for understanding others.

We've learned that Ruby on Rails is built for fast development and is famous for its "convention over configuration" approach to development. This means that Rails favors convention (standard ways of doing things) over the need for explicit configuration

In conclusion, mastering web development involves a continuous learning process. As technologies evolve and new frameworks emerge, staying updated and adaptable is key. The journey from understanding the basics to becoming proficient in multiple technologies and frameworks is challenging but rewarding, opening up a world of opportunities for creating dynamic and robust web applications.
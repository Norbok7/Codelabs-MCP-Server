---
title: Deployment
---

# Deployment

**Table of Contents**

-   Introduction to Deployment
-   Deploying to Render

## Introduction

In this lesson we will learn how to deploy our Ruby on Rails API to a production environment. We will also learn how to upload images to our application using Active Storage and Cloudinary.

## Introduction to Deployment

<img src="https://static.vecteezy.com/system/resources/previews/033/186/348/non_2x/deployment-icon-vector.jpg" />

Deployment is the process of making our application available to the public. When an API is deployed, it is hosted on a server. This is a crucial part of the software development lifecycle since it is the point at which our application becomes accessible to its intended users via the internet.

There are various things we may encounter when deploying our API: scaling, provisioning resources, and ensuring security measures are in place. Nowadays, services make it easier to deploy our applications. However, it is important to understand the process of deployment and the different options available since costs and performance can vary.

### Environments

It's important to understand the various environments we work in to separate our development, testing, and production environments. This is important because we don't want to make changes to our production environment that could potentially break our application, expose sensitive information, or cause other issues like data manipulation.

-   **Development**: This is the environment we work in when we are building our application. We can make changes to our code and test it without affecting the production environment.

When we run our application locally, we are running it in the development environment. For example,

```bash
rails s
```

This command starts our server in the development environment where we can send requests to our API and see the responses.

Another example is when we run the console in the development environment:

```bash
rails c
```

-   **Test**: This is the environment we use to run our tests. We can run our tests without affecting the development or production environments. This environment is important because it allows us to test our code and ensure that it works as expected.

For example, we use RSpec to run our tests.

```bash
bundle exec rspec
```

When we run our tests, we are running them in the test environment.

-   **Production**: This is the environment where our application is deployed and accessible to the public. This is the environment where we want to ensure that our application is secure, scalable, and reliable.

When we deploy our application, we are deploying it to the production environment.

There are other environments like staging, UAT, and QA that are used in the software development lifecycle.

-   **Staging**: This is an environment that is similar to the production environment. It is used to test our application before deploying it to the production environment.
-   **UAT**: This is the User Acceptance Testing environment. It is used to test our application with real users before deploying it to the production environment. Real users could be internal or external users.
-   **QA**: This is the Quality Assurance environment. It is used to test our application to ensure that it meets the quality standards before deploying it to the production environment.

When you work in a team, it's important to understand the different environments and how to work in them. Some teams may have different workflows or purposes for these environments. But it's important to understand the different environments and how to work in them. For now, we will focus on development, test, and production environments.

We will explore the production environment more in this lesson.

Also, as you work in teams, it's recommended to have the following environments to name a few:

-   Development
-   Test
-   Staging
-   Production

Work in development, test in test, test a live version of your application in staging, and deploy to production when you are ready.

### Deploying an API vs Deploying a Front End Application

Deploying an API is different from deploying a front end application. When we deploy an API, we are deploying the backend of our application. When deploying our API, it will require a series of executions to make run properly. Also, our API will require a database to store data.

On the other hand, when we deploy a front end application, we are deploying the user interface of our application. This is the part of the application that the user interacts with. When deploying a front end application, we are deploying the HTML, CSS, and JavaScript files that make up the user interface. This is much simpler than deploying an API since we don't have to worry about a database or server configurations.

When a user requests the domain of our front end application, the server will send the HTML, CSS, and JavaScript files to the user's browser. For a front end framework like Angular, React, or Vue, the server will send the index.html file to the user's browser. The index.html file will then load the JavaScript and CSS files that make up the user interface.

When a user requests the domain of our API, the server will send the data that the user requested. This data could be in the form of JSON, XML, or another format. The user's browser will then use this data to update the user interface.

All in all, deploying an API is more complex than deploying a front end application. This is because an API requires a server and a database to run properly.

We will explore more complex deployment options soon.

## Deploying to Render

As we move forward with our API and to continue to build on our skills, we will need to deploy our API to a production environment. There are many options available such as Heroku, AWS, Google Cloud, Railway, Render, Hatchbox and many more.

Since most services nowadays don't offer a free tier, we will use Render since it offers a free tier and is simple to use.

Since our applications won't require a lot of resources (traffic, resource usage, size of db, etc), we can use the free tier to deploy our applications.

---

### Setting up our Rails API for Deployment

This should work for both 7.0.x and 7.1.x

1. Create a new rails application:

```bash
rails new render_deployment_example --api
```

2. Let's add a model to our application. We will use a simple model called `User`.

```bash
rails g model User username:string
rails db:migrate
```

3. Generate a users Controller

```bash
rails g controller Users index create
```

Adjust the routes to include the users controller

```ruby
Rails.application.routes.draw do
  resources :users, only: [:index, :create]
end
```

```ruby
class UsersController < ApplicationController
  def index
    render json: User.all, status: :ok
  end

  def create
    user = User.new(username: params[:username])

    if user.save
      render json: user, status: :created
    else
      render json: user.errors, status: :unprocessable_entity
    end
  end
end
```

### Configuring our Rails API for Deployment

1. Push this project to Github and make sure to commit.

2. Since Render, and most services really, require postgresql as the database, we will need to include pg in our Gemfile.

```ruby
source "https://rubygems.org"

ruby "3.1.2"

gem "rails", "~> 7.1.3"

# Use sqlite3 as the database for Active Record
# gem "sqlite3", "~> 1.4" #  <----------- Remove this line

.
.
.

group :production do
  gem 'pg'
end

group :development, :test do
  gem "sqlite3", "~> 1.4"
  # See https://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-debug-gem
  gem "debug", platforms: %i[ mri mswin mswin64 mingw x64_mingw ]
end
```

Make sure sqlite3 is only in the development and test groups, and pg is only in the production group.

We will use sqlite3 in development and test environments since it is easier to use and doesn't require any configuration. However, we will use postgresql in the production environment since it is required by Render (and most services).

```bash
bundle install
```

3. Change the database configuration in `config/database.yml` to use postgresql in the production environment.

```yaml
production:
    adapter: postgresql
    encoding: unicode
    pool: <%= ENV.fetch("RAILS_MAX_THREADS") { 5 } %>
    url: <%= ENV['DATABASE_URL'] %>
```

4. In your `bin` directory, create a file called `render-build.sh` and add the following:

```bash
#!/usr/bin/env bash
# exit on error
set -o errexit
bundle install
bundle exec rake db:migrate
```

This file will be used to build our application on Render. It will install our gems and run our migrations.

```bash
#!/usr/bin/env bash
```

This line is called a shebang. It tells the operating system what interpreter to use to run the file. In this case, we are using bash.

```bash
set -o errexit
```

This line tells the operating system to exit the script if any command returns a non-zero status. This is useful because it will prevent the script from continuing if a command fails.

Then we will install our gems and run our migrations when we build our application on Render.

5. In the root of your project, create a file called `render.yaml`. Render makes the process of deployment easier by simply adding the following:

```yaml
databases:
    - name: renderdeploymentexample
      databaseName: renderdeploymentexample
      user: renderdeploymentexample
      plan: free

services:
    - type: web
      name: renderdeploymentexample
      runtime: ruby
      plan: free
      buildCommand: './bin/render-build.sh'
      # preDeployCommand: "./bin/rails db:migrate" # preDeployCommand only available on paid instance types
      startCommand: './bin/rails server'
      envVars:
          - key: DATABASE_URL
            fromDatabase:
                name: renderdeploymentexample
                property: connectionString
          - key: RAILS_MASTER_KEY
            sync: false
          - key: WEB_CONCURRENCY
            value: 2 # sensible default
```

This file will be used to configure our application on Render. It will create a database and a web service for our application called renderdeploymentexample.

Instead of `renderdeploymentexample`, you will need to change the name of the database and web service to match the name of your application. In this example, please name this `renderdeploymentexample` follow by your fullname, for example `renderdeploymentexamplejohndoe` since we all can't use the same name.

```yaml
databases:
    - name: renderdeploymentexample.
      databaseName: renderdeploymentexample.
      user: renderdeploymentexample.
      plan: free
```

This section of the file will create a database for our application. It will be a free database. It will also be called renderdeploymentexample.

```yaml
services:
    - type: web
      name: renderdeploymentexample
      runtime: ruby
      plan: free
      buildCommand: './bin/render-build.sh'
      # preDeployCommand: "./bin/rails db:migrate" # preDeployCommand only available on paid instance types
      startCommand: './bin/rails server'
      envVars:
          - key: DATABASE_URL
            fromDatabase:
                name: renderdeploymentexample
                property: connectionString
          - key: RAILS_MASTER_KEY
            sync: false
          - key: WEB_CONCURRENCY
            value: 2 # sensible default
```

This section of the file will create a web service for our application. It will be a free web service and it will also be called renderdeploymentexample.

It's important to note that when we deploy our application, we will run the buildCommand to install our gems and run our migrations. We will also run the startCommand to start our server.

The envVars section is used to set environment variables for our application. We will set the DATABASE_URL, RAILS_MASTER_KEY, and WEB_CONCURRENCY environment variables.

-   DATABASE_URL: This environment variable is used to connect to our database. It will be set to the connection string of our database.
-   RAILS_MASTER_KEY: This environment variable is used to decrypt our credentials. It will be set to the master key of our application. We will explore this shortly
-   WEB_CONCURRENCY: This environment variable is used to set the number of worker processes that will be used to run our application. It will be set to 2. This is a more advanced topic that we will explore later.

When you deploy your own application, you will need to change the name of the database and web service to match the name of your application.

6. Commit and push to Github

### Deploying with Render

Sign up for an account at [Render](https://render.com/). Be sure to use your Github account to sign up to make the process easier.

Once you have signed up, you will be taken to the dashboard.

<img src="https://imgur.com/SQBK6gQ.png" />

1. Click on the navlink that says "Blueprints"
2. Click on the button that says `new blueprint instance`
3. Search for the repository you just created and click `connect`.
4. It will ask for a blueprint name. You can name it whatever you want. I will name mine `Default Rails Render`
5. Enter the Rails Master Key

The Rails Master Key is a key that is used to decrypt our credentials specific to the environment that we are in. It is a key that is different for every application and environment. It is used to decrypt our credentials.yml.enc file that exists in our config directory.

When we deploy our application, we will need to set the RAILS_MASTER_KEY environment variable to the master key of our application. This will allow our application to decrypt our credentials and use them in the production environment.

Navigate back to your project folder to get the master key. Navigate to `config/master.key` and copy the key.

Once copied, go back to Render and paste the key in the input field.

<img src="https://imgur.com/Zpm2QfR.png" />

Click `Apply`. This may take a while.

6. Once it is done, go to `Dashboard` and click on the link to the one that shows the type to be `Web Service`.

<img src="https://imgur.com/VdyJ5xa.png" />

<img src="https://imgur.com/M5ufThP.png" />

However, you might had ran into an error:

<img src="https://imgur.com/0v42Wno.png" />{' '}

If we click on the web service it will show us the error:

```text
Deploy failed for 7192bed: render deployment
Exited with status 1 while running your code. Check your deploy logs for more information.
February 1, 2024 at 6:57 PM
```

Navigate to `Logs` and it may possibly show you the error:

```text
/opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/definition.rb:449:in `validate_platforms!': Your bundle only supports platforms ["x86_64-darwin-20"] but your local platform is x86_64-linux. Add the current platform to the lockfile with (Bundler::ProductionError)
`bundle lock --add-platform x86_64-linux` and try again.
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/definition.rb:418:in `validate_runtime!'
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler.rb:164:in `setup'
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/setup.rb:20:in `block in <top (required)>'
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/ui/shell.rb:159:in `with_level'
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/ui/shell.rb:111:in `silence'
	from /opt/render/project/.gems/gems/bundler-2.4.4/lib/bundler/setup.rb:20:in `<top (required)>'
	from <internal:/opt/render/project/rubies/ruby-3.1.2/lib/ruby/site_ruby/3.1.0/rubygems/core_ext/kernel_require.rb>:86:in `require'
```

This indicates that the platform is not supported. To fix this, we will need to add the platform to the lockfile.

Go back to your project and run the following command:

```bash
bundle lock --add-platform x86_64-linux
```

Then commit and push to Github.

Once you have done that, go back to Render, to the dashboard and verify that the deployment is successful.

Here you will see the URL to your application. Click on it and you will see your application running.

You should see a page with the following:

```text
This renderdeploymentexample.onrender.com page can’t be foundNo webpage was found for the web address: https://renderdeploymentexample.onrender.com/
HTTP ERROR 404
```

Success! You have deployed your Rails API to Render. You might be wondering why you are seeing a 404 error. That's because our API doesn't have a root route. That's okay since we are only interested in the users route.

Let's test this out by using postman to create a user.

I will send a POST request to `https://renderdeploymentexample.onrender.com/users`

```json
{
	"username": "test"
}
```

I will receive a response with the user I just created.

```json
{
	"id": 1,
	"username": "test",
	"created_at": "2022-03-14T20:47:47.000Z",
	"updated_at": "2022-03-14T20:47:47.000Z"
}
```

I will also send a GET request to `https://renderdeploymentexample.onrender.com/users` and receive a response with the user I just created.

```json
[
	{
		"id": 1,
		"username": "test",
		"created_at": "2022-03-14T20:47:47.000Z",
		"updated_at": "2022-03-14T20:47:47.000Z"
	}
]
```

Keep in mind that you can only have one free service for the database and web service on Render. If you have already deployed a service, you will need to delete it before you can deploy another one. Unfortunately, due to the lack of free services that exist in today's world, this is one way of deploying your api to a production environment for free.

> **Codelabs Learning Assistant Suggestion:**  
> 💡 Confused about the difference between development, test, and production environments?  
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)  
> _"Can you explain the purpose of development, test, and production environments in Rails, and why each is important?"_

### Conclusion

Success! You have deployed your Rails API to Render and it is working as expected.

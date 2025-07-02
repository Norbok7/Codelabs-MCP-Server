---
title: API Documentation with Swagger in Ruby on Rails
---

# API Documentation with Swagger in Ruby on Rails

<img src="https://miro.medium.com/v2/resize:fit:800/1*8NlEgepIbuSTa_C5YyKa5w.jpeg" />

## Introduction

What is API Documentation? API documentation is a deliverable that provides guidance on how to use an API. It is a reference manual that allows developers to understand the API and how to use it. It is a critical part of the API development process. It is a guide that provides information about the API, such as what it does, how it works, and how to use it.

This is helpful for several reasons such as:

-   Provides Front End developers with the information they need to integrate the API into their applications.
-   Onboard new developers to the API.
-   Provides a reference for developers to use when they need to understand how to use the API.

Part of the development life cycle includes creating documentation for the API.

The development life cycle includes the following steps:

1. Design the API
2. Develop the API
3. Test the API
4. Document the API
5. Deploy the API
6. Monitor the API
7. Maintain the API
8. Update the API
9. Retire the API
10. Repeat

Documentation can be written in a variety of formats, such as Markdown, HTML, or PDF. However, one of the most popular formats for API documentation is Swagger.

## What is Swagger?

Swagger is a set of open-source tools built around the OpenAPI Specification that can help you design, build, document, and consume REST APIs. It is a powerful tool that can help you create and maintain API documentation.

We will be using an integration with swagger called rswag. Rswag is a tool that allows you to write Swagger documentation as integration tests in Ruby on Rails.

This makes it great for both documenting your API and testing your API at the same time. It is a great way to ensure that your API documentation is always up to date with your API.

This being said rswag will provide a UI to view the documentation and also a way to test the API in the browser.

## Setup Swagger in Ruby on Rails

Create a new rails api

```bash
rails new swagger_tutorial --api
```

Add the following gems to the Gemfile

```ruby
gem 'rswag'
gem 'rspec-rails', '~> 6.1.0'
```

Run the following command to install the gem

```bash
bundle install
```

Install rspec in the application

```bash
rails generate rspec:install
```

Install the generator for rswag

```bash
rails g rswag:install
```

With rswag, your Swagger documentation is written as integration tests. This means you define the structure of your API (endpoints, parameters, responses) within RSpec files located in spec/integration.

## Setup API

Generate a new model for users

```bash
rails generate model User name:string email:string
```

You might have gotten this deprecated warning when running the command above

```bash
DEPRECATION WARNING: Rswag::Ui: WARNING: The method will be renamed to "openapi_endpoint" in v3.0 (called from block in <main> at /Users/germancruz/Documents/projects/swagger-tutorial/config/initializers/rswag_ui.rb:11)
```

To fix this warning, open the file `config/initializers/rswag_ui.rb` and replace the following code

```ruby
Rswag::Ui.configure do |c|
  c.openapi_endpoint '/api-docs/v1/swagger.yaml', 'API V1 Docs'
end
```

Run the migration

```bash
rails db:migrate
```

Add the following code to the user model

```ruby
class User < ApplicationRecord
  validates :name, presence: true
  validates :email, presence: true
end
```

In the seed file add the following code

```ruby
User.create(name: "Alice", email: "alice@example.com")
User.create(name: "Bob", email: "bob@example.com")
```

```bash
rails db:seed
```

Generate a new controller for users

```bash
rails generate controller Users
```

Add the following code to the users controller

```ruby
class UsersController < ApplicationController
  def index
    users = User.all
    render json: users
  end
end
```

In the routes file add the following code

```ruby
Rails.application.routes.draw do
  resources :users, only: [:index]
end
```

## Document Index Endpoint

Let's generate a new user_spec file to document the index endpoint

```bash
rails generate rspec:swagger UsersController --spec_path integration
```

`--spec_path` means that the file will be generated in the integration folder of `spec`.

Let's add the following code to the user_spec file

```ruby
require 'swagger_helper'

RSpec.describe 'users', type: :request do
  path '/users' do

    get 'Retrieves all users' do
      tags 'Users'
      produces 'application/json'

      response '200', 'successful' do
        schema type: :array,
          items: {
            type: :object,
            properties: {
              id: { type: :integer },
              name: { type: :string },
              email: { type: :string }
            },
            required: ['id', 'name', 'email']
          }

        run_test!
      end
    end

  end
end
```

Here we are defining the structure of the index endpoint of the users. We are defining the tags, produces, and response of the endpoint.

```ruby
      response '200', 'successful' do
        schema type: :array,
          items: {
            type: :object,
            properties: {
              id: { type: :integer },
              name: { type: :string },
              email: { type: :string }
            },
            required: ['id', 'name', 'email']
          }

        run_test!
      end
```

Here we are specifying the response of the endpoint. We are saying that the response will be an array of objects with the properties id, name, and email.

Now keep in mind, a lot of it is... 'copy' and 'paste' to but it's important to understand what you are doing to ensure you implement it correctly.

```ruby
run_test!
```

This line of code will run the test for the endpoint.

In order to specify our default host and base path, we can add the following code to the `swagger_helper.rb` file

```ruby
# frozen_string_literal: true

require 'rails_helper'

RSpec.configure do |config|
.
.
.
  config.openapi_root = Rails.root.join('swagger').to_s

.
.
.
  config.openapi_specs = {
    'v1/swagger.yaml' => {
      openapi: '3.0.1',
      info: {
        title: 'API V1',
        version: 'v1'
      },
      paths: {},
      servers: [
        {
          url: "http://{localHost}",
          variables: {
            localHost: {
              default: "localhost:3000"
            }
          }
        },
      ]
    }
  }
.
.
.
  config.openapi_format = :yaml
end
```

```ruby
      servers: [
        {
          url: "http://{localHost}",
          variables: {
            localHost: {
              default: "localhost:3000"
            }
          }
        },
```

This will allow us to specify the default host and base path for our API. For production, you would replace `localhost:3000` with the actual domain of your API.

Run the following command to generate the swagger documentation

```bash
rails rswag:specs:swaggerize
```

To view the documentation, run the following command

```
Generating Swagger docs ...
Swagger doc generated at /Users/germancruz/Documents/projects/swagger-tutorial/swagger/v1/swagger.yaml

Finished in 0.00161 seconds (files took 1.41 seconds to load)
1 example, 0 failures
```

```bash
rails s
```

Open your browser and go to `http://localhost:3000/api-docs`. This will redirect you to the swagger documentation.

You should see the following documentation

<img src="https://imgur.com/9WRyiua.png" />

Here you will see the following 

-  The title of the API
-  The version of the API
-  The base path of the API
-  The host of the API
-  The paths of the API
-  The tags of the API
-  so on and so on.

Most importantly, you will see the documentation for the index endpoint of the users.

Click on the index endpoint and you will see the following:

<img src="https://imgur.com/o8eBkcy.png" />

Click on the `Try it out` button and then click on the `Execute` button. You should see the following response:

<img src ="https://imgur.com/LfEZ4fH.png" />

This is the response from the index endpoint of the users.

Wallah! You have successfully documented your first endpoint with Swagger in Ruby on Rails.

## Importance 

API documentation is a critical part of the API development process. It is a guide that provides information about the API, such as what it does, how it works, and how to use it. It is helpful for several reasons such as:

-  Provides Front End developers with the information they need to integrate the API into their applications.
-  Onboard new developers to the API.
-  Provides a reference for developers to use when they need to understand how to use the API.
-  Ensures that your API documentation is always up to date with your API.

It is best practice to always document your API. Swagger is a great tool to help you with this process.

## Conclusion

In this tutorial, we learned how to set up Swagger in Ruby on Rails. We learned how to document an endpoint with Swagger. We also learned how to view the documentation and test the endpoint in the browser.

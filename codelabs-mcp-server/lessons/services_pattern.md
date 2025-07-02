---
title: Services and PORO Pattern
---

# Services and PORO Pattern

![Rails API](https://miro.medium.com/max/1400/0*CUdFIQoT8xDr3rW8.png)

## Introduction

Ruby on Rails includes a pattern that we are experienced with which is 'Ruby magic' that makes it easy to build applications. However, as the application grows, it becomes difficult to maintain and understand the code. This is where the services and PORO pattern comes in.

## What is the Services and PORO Pattern?

The Services and PORO pattern is a pattern that is used to organize your code in a way that makes it easy to maintain and understand. It is a pattern that is used to separate the concerns of your application.

Services are A service is a class or module that encapsulates a specific set of functionality that can be shared across different parts of your application. Services are typically used to abstract complex business logic away from controllers and models, making your code more modular, reusable, and easier to test.

PORO stands for Plain Old Ruby Object. It can be used as a way to encapsulate a specific set of functionality that can be shared across different parts of your application. POROs are typically used to abstract complex business logic away from controllers and models, making your code more modular, reusable, and easier to test.

## Setup

Create a new Rails API application using the following command:

```ruby
rails new services_poro_pattern --api
```

We will be create a users model and allow ourselves to create a user.

```ruby
rails g model User name:string email:string
```

```ruby
rails db:migrate
```

In our `user.rb` model, let's add the following:

```ruby
class User < ApplicationRecord
  validates :name, :email, presence: true
end
```

In our routes let's add the following:

```ruby
resources :users
```

Let's create a controller for our users:

```ruby
rails g controller Users create
```

In our users controller, let's add the following:

```ruby
class UsersController < ApplicationController
  def create
    user = User.new(user_params)
    if user.save
      render json: user, status: :created
    else
      render json: user.errors, status: :unprocessable_entity
    end
  end

  private

  def user_params
    params.permit(:name, :email)
  end
end
```

## Services

We will extract the logic of creating a user into a service. Create a folder called `services` in `app`. Let's create a new file in our services folder called `user_service.rb`. Restart the service if you are running the server.

Include the following code in the `user_service.rb` file:

```ruby
module UserService
  module Base
    def self.create_user(params)
      user = User.new(params)
      if user.save
        user
      else
        user.errors
      end
    end
  end
end
```

Here we are we defined the UserService module where we have a Base module that has a method called `create_user`. Here when we call the `create_user` method, it will create a user and return the user if it is valid, otherwise it will return the errors.

In our users controller, let's add the following:

```ruby
class UsersController < ApplicationController
  def create
    user = UserService::Base.create_user(user_params)
    if user.valid?
      render json: user, status: :created
    else
      render json: user, status: :unprocessable_entity
    end
  end

  private

  def user_params
    params.permit(:name, :email)
  end
end
```

Not much has changed but we have extracted the logic of creating a user into a service. This makes our controller cleaner and easier to understand since our actions are now only responsible for handling requests and responses.

Creating a user is a simple example but as your application grows, you will find that you will have more complex logic that you will need to extract into services.

Let's take another example that is more complex. Filtering users.

Define a new action in our users controller:

```ruby
def index
  users = UserService::Base.filter_users(params)
  render json: users, status: :ok
end
```

In our `user_service.rb` file, let's add the following:

```ruby
module UserService
  module Base
    def self.create_user(params)
      user = User.new(params)
      if user.save
        user
      else
        user.errors
      end
    end

    def self.filter_users(params)
      users = User.all
      users = users.where(name: params[:name]) if params[:name].present?
      users = users.where(email: params[:email]) if params[:email].present?
      users
    end
  end
end
```

Let's seed some data into our users table:

```ruby
User.create(name: 'John Doe', email: 'johndoe123@gmail.com');
User.create(name: 'John Doe', email: 'janedoe123@gmail.com');
User.create(name: 'Jane Doe', email: 'anotherjanedoe123@gmail.com');
```

```ruby
rails db:seed
```

Then send a request to `localhost:3000/users?name=Jane Doe` and you should get an array of users with the name Jane Doe.

Test the requests in postman.

## PORO

Here we will use a ruby object to determine the success or failure of creating a user.

Create a file called `service_contract.rb` in services. Include the following code:

```ruby
# frozen_string_literal: true

# Standardizes what a service method should always return
module ServiceContract

  def self.success(payload)
    OpenStruct.new({ success?: true, payload: payload, errors: nil })
  end

  def self.error(errors)
    OpenStruct.new({ success?: false, payload: nil, errors: errors })
  end

end
```

Here we are defining a module called `ServiceContract` that has two methods `success` and `error`. These methods will return an object that has a `success?` method that will return true or false depending on the success of the operation. It will also return the payload or errors.

We will use this module to help define a standard way of returning the success or failure of a service.

In our `user_service.rb` file, let's add the following:

```ruby
module UserService
  module Base
    def self.create_user(params)
      user = User.new(params)

      begin
         # are there any db/model errors?
        user.save!
      rescue ActiveRecord::RecordInvalid => exception
        # return an error instance
        return ServiceContract.error(user.errors.full_messages) unless user.valid?
      end

      ServiceContract.success(user)
    end

    def self.filter_users(params)
      users = User.all
      users = users.where(name: params[:name]) if params[:name].present?
      users = users.where(email: params[:email]) if params[:email].present?
      ServiceContract.success(users)
    end
  end
end
```

Notice that in our redefinition of the `create_user` method, we are using the `ServiceContract` module to return the success or failure of the operation. This makes it easier to understand the success or failure of the operation.

For `filter_users`, we are also using the `ServiceContract` module to return the success of the operation.

In our users controller, let's add the following:

```ruby
class UsersController < ApplicationController
  def create
    result = UserService::Base.create_user(user_params)
    if result.success?
      render json: result.payload, status: :created
    else
      render json: result.errors, status: :unprocessable_entity
    end
  end

  def index
    result = UserService::Base.filter_users(params)
    render json: result.payload, status: :ok
  end

  private

  def user_params
    params.permit(:name, :email)
  end
end
```

Look how clean and easy to understand our controller is. We are only responsible for handling requests and responses. The logic of creating a user and filtering users is now in our services.

Test the requests in postman.

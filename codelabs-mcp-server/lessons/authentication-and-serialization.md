---
title: Authentication and Serialization
---

# Authentication and Serialization

**Table of Contents**

-   Introduction 
-   Authentication vs Authorization
-   Authentication in Rails
-   Authorization in Rails 
-   Serialization in Rails using blueprinter 
  
## Introduction

Now that we have a basic understanding of how to create a Rails application, let's take a look at how to add authentication and authorization to our application. We will also look at how to serialize our data to send it to the requester (client). 

## Authentication vs Authorization

<img src = "https://www.okta.com/sites/default/files/styles/1640w_scaled/public/media/image/2020-10/Authentication_vs_Authorization.png?itok=uBFRCfww" />

Authentication is a big part of any application. People often confuse authentication with authorization, but they serve distinct purposes in application security. Understanding the difference is crucial for implementing effective security measures.

Authentication is the process of verifying the identity of a user. It's about confirming who the user is. For example, when a user logs in to an application using a username and password, they are being authenticated. The application verifies their identity based on the provided credentials. Without authentication, the application has no way of knowing who the user is.


There are many ways to authenticate a user. The most common way is to use a username and password. A user simply enters their username and password and the application verifies that the user is who they say they are. It's a straight forward but can be insecure if not implemented correctly. 

Here are other ways include authenticating a user: 

-  In addition to the standard username and password, 2FA requires a second form of verification. This could be a code sent via SMS, email, or generated through an authentication app. This method adds an extra layer of security by ensuring that even if a password is compromised, an attacker still needs another piece of information to access the account.
-  This method allows users to log in using their credentials from a third-party service like Google, Facebook, or Twitter. OAuth is a protocol that lets users grant a third-party website or application access to their information on another website, but without sharing their access credentials. It's convenient for users and can also be secure, as it leverages the robust security measures of major third-party services.
-  After initial login using a username and password, the server generates a token that the client can use for subsequent requests. This token is usually included in the headers of HTTP requests and is validated by the server for each request. Common in APIs and single-page applications, token-based authentication is especially useful for stateless interactions.
-  SSO allows users to log in once and gain access to multiple systems without the need to re-authenticate. It's useful in corporate environments where users access a suite of interconnected applications.
-  Passwordless authentication is a method that allows users to log in without the need to remember a password. It's often used in conjunction with other authentication methods, such as email or SMS, to send a one-time code to the user that they can use to log in. It's convenient for users and can also be secure, as it leverages the robust security measures of major third-party services.
  
Once a user's identity is verified, authorization comes into play. Authorization is the process of determining whether a user has the right to access a specific resource or perform a particular action within an application. For instance, after logging in, the application checks if the authenticated user has the necessary permissions to access a requested page or feature. Without authorization, the application cannot enforce restrictions on what authenticated users are allowed to do.

- Role based access is a common approach where users are assigned roles, and each role has predefined permissions. For example, an 'admin' role might have extensive access across the application, while a 'user' role might have more limited access.
- The process in which involves assigning specific permissions or capabilities directly to users or through roles. It's about checking if a user has the permission to perform an action like editing a document or viewing a specific page.
- OAuth is another option in which the user's identity is authenticated by the third-party service, and your application is granted a token to access specific user data without needing the user's credentials. OAuth is more about granting access (authorization) rather than verifying user identity (authentication) since the token allows for access to the user's data without the need for a password.

## Best Practices for authentication 

There are many ways to authenticate a user but there are some best practices that you should follow when implementing authentication in your application. It's difficult or perhaps nearly impossible to protect against every possible attack, but following these best practices will help you avoid the most common security issues.

-  Use strong, hashed passwords. Using BCrypt is a good option since it involves salting the password and using a strong hashing algorithm. This prevents attackers from using rainbow tables to crack passwords. Rainbow tables are when "an attacker uses a precomputed table for reversing cryptographic hash functions, usually for cracking password hashes". That's beyond the scope of this lesson but you can read more about it [here](https://en.wikipedia.org/wiki/Rainbow_table).
-  Offer and encourage users to enable 2FA. This adds an extra layer of security by requiring a second form of verification (e.g., SMS code, authenticator app).
-  Temporarily lock accounts after a certain number of failed login attempts to prevent brute force attacks.
-  Always use HTTPS, not HTTP, to encrypt data transmitted between the client and the server, especially for login pages and any other pages transmitting sensitive information.
-  Store session IDs and other sensitive information on the server. If you must store data on the client side, ensure it's properly encrypted and protected.
-  Keep all software, libraries, and frameworks updated to protect against known vulnerabilities.
-  Enforce a minimum password length and complexity (mix of letters, numbers, symbols).
-  Implement secure methods for password recovery, like email confirmation links or security questions. Ensure that security questions are not easily guessable.
-  

## Best Practices for Authorization 

Authorization on the other hand is about determining whether a user has the right to access a specific resource or perform a particular action within an application. Here are some best practices for authorization:

- Grant users only the permissions they need to perform their tasks. Avoid giving excessive privileges which can lead to security vulnerabilities.
- Use a role based system to assign permissions to roles, and then assign roles to users. This simplifies management of permissions as changes can be made at the role level rather than individually.
- Periodically review and audit user roles and permissions to ensure they are still appropriate and make adjustments as necessary.
- Where applicable, add context (e.g., IP address, device type) or time-based restrictions to access.

## Authentication in Rails

Rails comes with a built-in authentication system called [has_secure_password](https://api.rubyonrails.org/classes/ActiveModel/SecurePassword/ClassMethods.html). It's a simple way to add authentication to your application. It provides methods to set and authenticate against a BCrypt password. It also adds a few validations to your model.

```text
where XXX is the attribute name of your desired password.

The following validations are added automatically:

Password must be present on creation

Password length should be less than or equal to 72 bytes

Confirmation of password (using a XXX_confirmation attribute)

If confirmation validation is not needed, simply leave out the value for XXX_confirmation (i.e. don’t provide a form field for it). When this attribute has a nil value, the validation will not be triggered.
```

Authenticating against a BCrypt password refers to the process of verifying a user's login attempt by comparing the password they provide with the hashed password stored in the database. 

Let's create a new Rails API application and add authentication to it. 

```bash
rails new authentication_and_serialization_tutorial --api
```

### Creating Tests for Authentication

Add the following gems to your Gemfile:

```ruby
group :development, :test do
  # See https://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-debug-gem
  gem "debug", platforms: %i[ mri mingw x64_mingw ]
  gem 'rspec-rails'
  gem 'factory_bot_rails'
end
```

Next, run the following command to generate the RSpec configuration files:

```bash
rails generate rspec:install
```

```ruby
rails g rspec:model user 
```

To use factory-bot, we need to add the following to our `rails_helper.rb` file:

```ruby
.
.
.
RSpec.configure do |config|
  config.include FactoryBot::Syntax::Methods
  .
  .
  .
end
```

Also include in your rails_helper file 

```ruby
# This file is copied to spec/ when you run 'rails generate rspec:install'
require 'spec_helper'
require 'faker'
.
.
.
```

#### Adding Tests for User model

Update your `spec/factories/users.rb` file to look like this:

```ruby
FactoryBot.define do
  factory :user do
    username { Faker::Internet.username }
    password { 'password' }
    password_confirmation { 'password' }
  end
end
```

We will create a user with a username and password. You can always use email instead of username for logging in purposes or both. In this case, we will use username.

We will also add a password confirmation for creations to make sure the password and password confirmation match.

You're probably wondering, will the password be stored in plain text? The answer is no. We will be using BCrypt to hash the password in which will be stored in the database as password_digest. Remember that BCrypt is a hashing algorithm that is used to hash passwords.

In your User model, you likely have `has_secure_password`, which adds methods to set and authenticate against a BCrypt password. This method expects a password_digest attribute in your database (which you have) and virtual attributes password and password_confirmation for the model. 

```ruby
require 'rails_helper'

RSpec.describe User, type: :model do
  it 'is valid with a username and password' do
    user = build(:user)
    expect(user).to be_valid
  end

  it 'is not valid without a username' do
    user = build(:user, username: nil)
    expect(user).not_to be_valid
  end

  it 'hashes the password' do
    user = create(:user, password: 'password')
    expect(user.password_digest).not_to eq 'password'
  end
end
```

We need to make sure of the following things:

- A user is valid with a username and password
- A user is not valid without a username
- A user's password is hashed which we will have column for this hash in our database called password_digest

#### Adding tests for Users Controller

Let's create a new spec file for our users controller. 

```bash
rails g rspec:request users
```

Include the following in your **spec/requests/users_spec.rb**

```ruby
require 'rails_helper'

RSpec.describe 'Users', type: :request do
  describe 'POST /users' do
    context 'with valid attributes' do
      it 'creates a new user and returns a success response' do
        post '/users', params:  attributes_for(:user) 
        expect(response).to have_http_status(:created)
        expect(User.count).to eq(1)
      end
    end

    context 'with invalid attributes' do
      it 'does not create a new user and returns an error response' do
        post '/users', params: attributes_for(:user, username: nil) 
        expect(response).to have_http_status(:unprocessable_entity)
        expect(User.count).to eq(0)
      end
    end
  end
end
```

Here we are testing to make sure that a user is created with valid attributes and that a user is not created with invalid attributes.

#### Adding tests for Sessions Controller

Let's create a new spec file for our sessions controller. 

```bash
rails g rspec:request sessions
```

```ruby
require 'rails_helper'

RSpec.describe 'Sessions', type: :request do
  describe 'POST /login' do
    let!(:user) { create(:user) }

    context 'with valid credentials' do
      it 'authenticates the user and returns a success response' do
        post '/login', params: { username: user.username, password: 'password' }
        expect(response).to have_http_status(:success)
        expect(JSON.parse(response.body)).to include('token')
      end
    end

    context 'with invalid credentials' do
      it 'does not authenticate the user and returns an error response' do
        post '/login', params: { username: user.username, password: 'wrong_password' }
        expect(response).to have_http_status(:unauthorized)
      end
    end
  end
end
```

Creating a session is the process of logging in a user. We need to make sure that a user can login with valid credentials and that a user cannot login with invalid credentials. If the user logins with correct credentials, we should return a token.

Let's go ahead and run our tests to make sure everything is working as expected.

```bash
bundle exec rspec
```

Great! We have some failing tests. This is expected since we haven't created our models or controllers yet. Let's go ahead and create our models and controllers.

#### Creating User Model

```bash
rails generate model User username:string password_digest:string
```

```text
      invoke  active_record
      create    db/migrate/20240125000946_create_users.rb
      create    app/models/user.rb
      invoke    rspec
    conflict      spec/models/user_spec.rb
    Overwrite /Users/germancruz/Documents/code-labs/backend/authentication_and_serialization_tutorial/spec/models/user_spec.rb? (enter "h" for help) [Ynaqdhm] n
        skip      spec/models/user_spec.rb
      invoke      factory_bot
    conflict        spec/factories/users.rb
      Overwrite /Users/germancruz/Documents/code-labs/backend/authentication_and_serialization_tutorial/spec/factories/users.rb? (enter "h" for help) [Ynaqdhm] n
        skip        spec/factories/users.rb
```

Enter `n` to not overwrite the spec file.

```bash
rails db:migrate
```

We will be using the `has_secure_password` method to add authentication to our application. This method expects a password_digest attribute in your database (which you have) and virtual attributes password and password_confirmation for the model. 

```ruby
class User < ApplicationRecord
  has_secure_password
end
```

```bash
bundle exec rspec spec/models/user_spec.rb
```

```text
FFF

Failures:

  1) User is valid with a username and password
     Failure/Error: user = build(:user)
     
     NoMethodError:
       undefined method `password=' for #<User id: nil, username: "yun_mcclure", password_digest: nil, created_at: nil, updated_at: nil>
       Did you mean?  password_digest=
     # ./spec/models/user_spec.rb:5:in `block (2 levels) in <top (required)>'

  2) User is not valid without a username
     Failure/Error: user = build(:user, username: nil)
     
     NoMethodError:
       undefined method `password=' for #<User id: nil, username: nil, password_digest: nil, created_at: nil, updated_at: nil>
       Did you mean?  password_digest=
     # ./spec/models/user_spec.rb:10:in `block (2 levels) in <top (required)>'

  3) User hashes the password
     Failure/Error: user = create(:user, password: 'password')
     
     NoMethodError:
       undefined method `password=' for #<User id: nil, username: "katie.gibson", password_digest: nil, created_at: nil, updated_at: nil>
       Did you mean?  password_digest=
     # ./spec/models/user_spec.rb:15:in `block (2 levels) in <top (required)>'

Finished in 1.51 seconds (files took 1.25 seconds to load)
3 examples, 3 failures

Failed examples:

rspec ./spec/models/user_spec.rb:4 # User is valid with a username and password
rspec ./spec/models/user_spec.rb:9 # User is not valid without a username
rspec ./spec/models/user_spec.rb:14 # User hashes the password
```

Navigate to your `app/models/user.rb` file and add the following:

```ruby
class User < ApplicationRecord
  has_secure_password
  validates :username, presence: true
end
```

To use `has_secure_password`, we need to add the bcrypt gem to our Gemfile. 

```ruby
gem 'bcrypt'
```

```bash
bundle install

```

```bash
 bundle exec rspec spec/models/user_spec.rb
```

```text
Finished in 0.20025 seconds (files took 1.56 seconds to load)
3 examples, 0 failures
```

Great! Our tests are passing. Let's go ahead and create our users controller.

#### Creating Users Controller

```bash
rails g controller users
```

```text
      create  app/controllers/users_controller.rb
      invoke  rspec
    conflict    spec/requests/users_spec.rb
  Overwrite /Users/germancruz/Documents/code-labs/backend/authentication_and_serialization_tutorial/spec/requests/users_spec.rb? (enter "h" for help) [Ynaqdhm] n
        skip    spec/requests/users_spec.rb
```

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
    params.permit(:username, :password, :password_confirmation)
  end
end
```

When you use `User.new `or `User.create` with `has_secure_password` in your User model, Rails automatically checks to see if the password and password_confirmation fields match when creating a new user. This is one of the conveniences provided by the `has_secure_password` method.

In our routes file, we need to add the following:

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create]
end
```

Great! Let's go ahead and run our tests to make sure everything is working as expected.

```bash
bundle exec rspec spec/requests/users_spec.rb
```

```text
Finished in 0.28926 seconds (files took 1.75 seconds to load)
2 examples, 0 failures
```

#### Creating Sessions Controller

```bash
rails g controller sessions create
```

```text
      create  app/controllers/sessions_controller.rb
      invoke  rspec
    conflict    spec/requests/sessions_spec.rb
  Overwrite /Users/germancruz/Documents/code-labs/backend/authentication_and_serialization_tutorial/spec/requests/sessions_spec.rb? (enter "h" for help) [Ynaqdhm] n
        skip    spec/requests/sessions_spec.rb
```

```ruby
class SessionsController < ApplicationController
  def create
    user = User.find_by(username: params[:username])
    if user&.authenticate(params[:password])
      render json: { token: '123' }
    else
      render json: { error: 'Invalid username or password' }, status: :unauthorized
    end
  end
end
```

```ruby
user&
```

The `&` is called the safe navigation operator. It's a Ruby operator that allows you to call a method on an object without worrying if it is nil. If the object is nil, the method will return nil instead of raising an exception.

Here if the user is found and the password is correct, we will return a token. Otherwise, we will return an error message. As of now, we are just returning a token for testing purposes. We will be using a customized token later on.

In our routes file, we need to add the following:

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create]
  post '/login', to: 'sessions#create'
end
```

Let's go ahead and run our tests to make sure everything is working as expected.

```bash
bundle exec rspec spec/requests/sessions_spec.rb
```

```text
Finished in 0.28926 seconds (files took 1.75 seconds to load)
2 examples, 0 failures
```

### Creating a JSON Web Token using the JWT gem

JWT, or JSON Web Token, is a compact, URL-safe means of representing claims to be transferred between two parties. The claims in a JWT are encoded as a JSON object that is used as the payload of a JSON Web Signature (JWS) structure or as the plaintext of a JSON Web Encryption (JWE) structure. This enables the claims to be digitally signed or integrity protected with a Message Authentication Code (MAC) and/or encrypted.

A JWT is a string made up of three parts, separated by dots (.), which are:

- Header: The header typically consists of two parts: the type of the token, which is JWT, and the signing algorithm being used, such as HMAC SHA256 or RSA.
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
- Payload: The second part of the token is the payload, which contains the claims. Claims are statements about an entity (typically, the user) and additional data. There are three types of claims: registered, public, and private claims.
-  
```json
{
  "sub": "1234567890",
  "name": "John Doe",
}
```
- Signature: A signature is used to verify that the sender of the JWT is who it says it is and to ensure that the message wasn't changed along the way. To create the signature part, you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that.

The resulting JWT looks like this: xxxxx.yyyyy.zzzzz. Here's what each section represents:

```text
xxxxx is the Base64Url encoded header.
yyyyy is the Base64Url encoded payload.
zzzzz is the signature.
```

JWTs can be used for:

**Authentication**: Once the user is logged in, each subsequent request will include the JWT, allowing the user to access routes, services, and resources that are permitted with that token.

We will be using the [jwt gem](https://github.com/jwt/ruby-jwt). 

### Logging in a user and returning a JWT

Let's go ahead and add the following to our Gemfile:

```ruby
gem 'jwt'
```

```bash
bundle install
```

Let's revisit our sessions controller. 

```ruby
class SessionsController < ApplicationController
  def create
    user = User.find_by(username: params[:username])
    if user&.authenticate(params[:password])
      render json: { token: '123' }
    else
      render json: { error: 'Invalid username or password' }, status: :unauthorized
    end
  end
end
```

Here if the user is found and the password is correct, we will return a token. Otherwise, we will return an error message. As of now, we are just returning a token for testing purposes. Let's change this token and use the JWT gem to create a token.

```ruby
class SessionsController < ApplicationController
.
.
.


  private 
  
  def jwt_encode(payload, exp = 24.hours.from_now)
    payload[:exp] = exp.to_i
    JWT.encode(payload, Rails.application.credentials.secret_key_base)
  end
end
```

Here we have defined a private method that will encode our payload. Let's break this down:

```ruby
  def jwt_encode(payload, exp = 24.hours.from_now)
```
Here we are defining a method that includes two parameters: payload and exp. The payload represents the data that we want to include in our token. This is typically used for storing the user's id. Whereas, exp is the expiration time of the token. We are setting the default expiration time to 24 hours from now. 

```ruby
  def jwt_encode(payload, exp = 24.hours.from_now)
    payload[:exp] = exp.to_i
```

Here we are setting the expiration time of the token. We are converting the expiration time to an integer. 

```ruby
  def jwt_encode(payload, exp = 24.hours.from_now)
    payload[:exp] = exp.to_i
    JWT.encode(payload, Rails.application.credentials.secret_key_base)
  end
```

Here we are encoding the payload using the JWT gem. We are using the secret key base to encode the payload. The reason we are using the secret key base is because it is unique to our application.

We haven't talked about the `Rails` object yet so let's do that quickly. The `Rails` object is an instance of the `Rails::Application` class. It is created when the application boots, and is available for your application to use. It is also available in the console. The `Rails` object is the container for your application's configuration, and the instance methods on the `Rails` object are the primary way to configure your application. With access to the Rails object, you have access to sensitive information about your application, such as the secret key base. Again, the secret key base is unique to your application which is used for security purposes. It is used also to encrypt sensitive data such as the Rails credentials feature which is used to hold sensitive information such as API keys, passwords, etc. We will explore more of this soon. On another note, the secret key base is unique for every application so we don't have to worry about someone else using our secret key base. And lastly, in our current setup, we are using the secret key base to encode our payload.

If you run your rails console:

```bash
rails console
```

and type in `Rails.application.credentials.secret_key_base`, you will see the secret key base for your application. The environment you have access in the console is the development environment. The secret key base is different for every environment.

Let's go ahead and update our sessions controller to use the jwt_encode method.

```ruby
class SessionsController < ApplicationController
  def create
    user = User.find_by(username: params[:username])
    if user&.authenticate(params[:password])
      token = jwt_encode(user_id: user.id)
      render json: { token: token }, status: :ok
    else
      render json: { error: "Unauthorized" }, status: :unauthorized
    end
  end

  private

  def jwt_encode(payload, exp = 24.hours.from_now)
    payload[:exp] = exp.to_i
    JWT.encode(payload, Rails.application.credentials.secret_key_base)
  end
end
```

```ruby
  if user&.authenticate(params[:password])
    token = jwt_encode(user_id: user.id)
```

Here we are encoding the payload and storing it in a variable called token. We are passing in the user's id as the payload. 

Let's go ahead and try this out. 

Send a request to `http://localhost:3000/login` with the following body:

```json
{
  "username": "username",
  "password": "password"
}
```

Once you do,  you will get the correct response of unauthorized

```json
{
    "error": "Unauthorized"
}
```

Let's quickly create a user so we can login. 

```bash
rails console
```

```ruby
User.create(username: 'username', password: 'password', password_confirmation: 'password')
```

Try again and you should see a JWT: 

```ruby
{
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJleHAiOjE3MDYzNzk3MDZ9.a0xAX98--3NIRLs6qXr-HM5D5Zyd7ropPGfmuNUeCao"
}
```


#### Verifying a JWT and misconceptions about JWTs

There are some misconceptions about JWTs in which we can talk about encoding, encrypting and one way functions or hashing. 

- Encryption is a two way function in which data is converted into a format that cannot be easily understood by unauthorized people. It can be decrypted back to its original form if the person has the right key.
  - Encryption is ideal when you need to securely transmit sensitive information over a network. For instance, when you send credit card information during an online transaction, the data is encrypted so that only the intended recipient with the right decryption key (e.g., the payment processor) can access the information.
- One way hashing is a one way function in which data is converted into a fixed length string of characters. It cannot be decrypted back to its original form. It is used to verify the integrity of data. For example, we used BCrypt to hash our passwords.
  - One-way hashing is used to securely store passwords. When a user creates a password, it is hashed using a hash function like BCrypt, and the resulting hash is stored in the database. When the user logs in, the password they enter is hashed again, and the resulting hash is compared to the one stored. Because hashing is one-way, even if someone gains access to the database, they cannot reverse the hashes back to passwords.
- Encoding is the process of converting data from one form to another. It doesn't provide any security. It's just a way to represent data in a different format.
  - Encoding is used when data needs to be transformed into a format that is compatible with different systems or protocols. For example, when embedding binary data in an XML or JSON payload, you might use Base64 encoding to convert the binary data into a text representation that can be easily included in the text-based payload.

The reason for using JWTs to authenticate a user is because 
- JWTs are encoded, which makes them URL-safe and easy to pass in HTTP headers.
- it's stateless. This means that the server doesn't need to keep track of the user's session. This is ideal for APIs and single-page applications.
- While the payload and header of a JWT are just encoded and can be decoded by anyone, the signature is encrypted with a secret key. 

When the token is used for authentication:
  - The server decodes the JWT to retrieve the header and payload.
  - The server then verifies the signature by comparing it against its own computed signature using the secret key.
  - If the signature is valid, the server trusts the claims within the JWT and authenticates the user.

Let's do just this. Visit [jwt.io](https://jwt.io/) and grab the token that you received from the response from postman. Here is mind: 

```json
{
    "token": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJleHAiOjE3MDYzNzk3MDZ9.a0xAX98--3NIRLs6qXr-HM5D5Zyd7ropPGfmuNUeCao"
}
```

Page the value of the token to the encoded section of jwt.io. You should see something similar to the following:

```json
{
  "alg": "HS256"
}
{
  "user_id": 1,
  "exp": 1706379706
}
```

Now you can even test this yourself by using my token above since it can be decoded by anyone.

However, as you might've noticed, it says that the signature is invalid. Let's go ahead and verify the token by accessing our secret key base value.

Go to the rails console and enter:

```ruby
Rails.application.credentials.secret_key_base
```

This should return something similar to this:

```text
035cc7c22f1246d6dbb3a9c3a42e7d3d133da2e617c8935b5288490050827675de0fab273c426bc718665707b59ad0385f88c6460c63786c17d970eb54ea17bd
```

Paste this under verify signature in the input box and uncheck `secret base64 encoded`;

You will see `signature Verified`.

Great! We have officially decoded and verified our token from JWT.io. We will use the JWT gem to verify our token and authenticate users this way. 

### Authenticating a user using a JWT

We will make certain routes protected so that only authenticated users can access them. Let's make the `show` action protected for our users controller. 

**config/routes.rb**
```ruby
Rails.application.routes.draw do
  resources :users, only: [:create, :show]
  post '/login', to: 'sessions#create'
end
```

Let's go ahead and add the following to our users controller:

**app/controllers/users_controller.rb**
```ruby
  def show 
    user = User.find_by(id: params[:id])

    render json: user, status: :ok
  end
  ```

Now the question is, how do we protect this route? We can include logic in the users controller to be used to authenticate the user but this is not ideal since we will be repeating ourselves if we have other controllers and their actions that we want to protect.

Instead, since all controllers will inherit from the ApplicationController, we can include logic in the ApplicationController to be used to authenticate the user.

**app/controllers/application_controller.rb.rb**
```ruby
class ApplicationController < ActionController::API
  def authenticate_request

  end
end
```

Here we have defined a method called authenticate_request. This method will be used to authenticate the user. Let's go ahead and add some logic to this method.

```ruby
class ApplicationController < ActionController::API
  def authenticate_request
    header = request.headers['Authorization']
    header = header.split(' ').last if header
  end
end
```

```ruby
    header = request.headers['Authorization']
```

To decode the token, we need to access the Authorization header. The Authorization header is used to provide authentication information in an HTTP request. The most common type of authentication is the Bearer authentication scheme, which involves the use of a security token called a bearer token. The Bearer authentication scheme is intended primarily for server authentication using the WWW-Authenticate and Authorization HTTP headers but can be used for user authentication in some cases.

```ruby
    header = header.split(' ').last if header
```

Here we are using split to split the header into an array. We are splitting the header by the space character. We are then grabbing the last element of the array which is the token.

```ruby
class ApplicationController < ActionController::API
  def authenticate_request
    header = request.headers['Authorization']
    header = header.split(' ').last if header
    begin
      decoded = JWT.decode(header, Rails.application.credentials.secret_key_base).first
      @current_user = User.find(decoded['user_id'])
    rescue JWT::ExpiredSignature
      render json: { error: 'Token has expired' }, status: :unauthorized
    rescue JWT::DecodeError
      render json: { errors: 'Unauthorized' }, status: :unauthorized
    end
  end
end
```

We wil wrap the process of decoding the token in a begin rescue block in response to capturing any errors that might occur. If the token has expired, we will return an error message. If the token is invalid, we will return an error message. Otherwise, we will find the user and store it in an instance variable called @current_user.

Also notice that when we are called `JWT.decode`, we include the header which is the token and the secret key base. We are using the secret key base to verify the signature of the token which will indicate that it is valid. 

Now we can use authenticate_request to protect our routes. Let's go ahead and add the following to our users controller:

```ruby
class UsersController < ApplicationController
  before_action :authenticate_request, except: [:create]
.
.
.
  ```

Here we want to call the authenticate_request method before the show action. We don't want to call this method before the create action since we want to allow users to create an account without being authenticated. 

The only way the show action will execute is if they are authenticated through `authenticate_request` and include a valid token in the Authorization header.

Let's test this out using postman. 

Try to send a request to `localhost:3000/users/1` without a token. You should get the following response:

```json
{
    "errors": "Unauthorized"
}
```

Now try to send a request to `localhost:3000/users/1` with a token. To do that, copy the token value from the response you used to login. Go to to the `Authorization` tab. Select `type` and select `Bearer Token`. Paste the token in the token field. 

Click `send`.

You should get a similar response:

```json
{
    "id": 1,
    "username": "username",
    "password_digest": "$2a$12$rRGqSRKChBUMRs1eIvVjDOeXgZXy17NUViGizydc/EhNGc2.pL.Bu",
    "created_at": "2022-01-25T01:11:32.201Z",
    "updated_at": "2022-01-25T01:11:32.201Z"
}
```

Great! We have successfully authenticated a user using a JWT. We will be using this method to authenticate users in our application. Again, there are various of ways to authenticate a user but this is one of the most common ways to do so.

However, there needs to be some level of consideration of creating custom tokens vs JWTs. 

- The biggest concern with JWT for session management is the difficulty in invalidating a token once it's been issued. Traditional session tokens can be easily invalidated by the server(logout or permission change) but JWTs remain valid until they expire. This can be problematic in scenarios where immediate revocation is necessary, such as a user logout or account suspension.
- JWTs are criticized for potentially being larger than traditional session tokens, which can increase the load on network traffic as they are included in every HTTP request.

### Token Storage and Revocation

Creating a customized token, (not JWT), is an alternative way to authenticate a user. If we store these tokens in the database, then we can easily revoke them. Both JWTs and custom tokens have their pros and cons.

### Overview

Please take a moment to view the following image below as we will be using this as a reference to what we will do soon with a frontend application. 

<img src = "https://www.vaadata.com/blog/wp-content/uploads/2016/12/JWT_tokens_EN.png" />

## Serialization 

Serialization is important for when we are building APIs. Serialization is the process in which we convert data structures or objects into a format that can be stored or transmitted and reconstructed later. Here are some examples: 

>**Need help with Rails serialization or want to see a Blueprinter example?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): “Show me how to serialize a Rails model using Blueprinter and explain why serialization matters for APIs.”

- When you send data from the client to the server, it needs to be serialized into a format that can be transmitted over the network.
- When you store data in a database, it needs to be serialized into a format that can be stored in the database.

We will focus on serializing data to be sent from the server to the client.

The advantages of this are:

- It reduces the amount of data sent over the network, which improves performance and reduces bandwidth usage.
- It allows you to control what data is sent to the client. For example, you might want to exclude sensitive information like passwords or credit card numbers.
- It allows you to control how the data is formatted. For example, you might want to format dates in a specific way.
- It allows you to include additional information that is not part of the data model. For example, you might want to include links to related resources. 

To serialize data, we will use [blueprinter](https://github.com/procore-oss/blueprinter). 

### The problem without serialization

When we send a request to `localhost:3000/users/1`, we get the following response:

```json
{
    "id": 1,
    "username": "username",
    "password_digest": "$2a$12$rRGqSRKChBUMRs1eIvVjDOeXgZXy17NUViGizydc/EhNGc2.pL.Bu",
    "created_at": "2022-01-25T01:11:32.201Z",
    "updated_at": "2022-01-25T01:11:32.201Z"
}
```

The problem with this is that we are sending sensitive information such as the password_digest. We don't want to send this information to the client. We also don't want to send the created_at and updated_at attributes to the client unless we want to. Let's use blueprinter to serialize our data.

### Creating a serializer for the user model using blueprinter

The blueprinter gem is a simple and fast object serializer for Ruby. It allows you to easily define the attributes to be serialized and their formatting. It also supports associations for serializing related objects.

Let's go ahead and add the following to our Gemfile:

```ruby
gem 'blueprinter'
```

```bash
bundle install
```

Let's go ahead and create a serializer for our user model. 

```bash
rails g blueprinter:blueprint user
```

This will create a new file in the serializers folder called `user_blueprint.rb` under `app/blueprints`.

**app/blueprints/user_blueprint.rb**

```ruby
# frozen_string_literal: true

class UserBlueprint < Blueprinter::Base
end
```

The file structure is necessary for blueprinter to work. The name of the file must doesn't necessarily need to be the same as the model name. However, it is recommended to do so. The name of the class must be the same as the file name. The class must inherit from `Blueprinter::Base`. Files in your project directory are automatically loaded by Rails, so you don't need to require the blueprint files.

Let's go ahead and add the following to our user blueprint:

```ruby
# frozen_string_literal: true

class UserBlueprint < Blueprinter::Base
  identifier :id

  fields :username
end
```

Here we are defining the fields that we want to serialize. 

```ruby
  identifier :id
```

We are also defining the identifier which is the id. The identifier is used to uniquely identify the object.

```ruby
  fields :username
```

We are also defining the fields that we want to serialize. In this case, we are serializing the username. 


In other words, if we serialize a user record using this blueprint, we will get the following:

```ruby
{
  "id": 1,
  "username": "username"
}
```

Notice how we are not serializing the `password_digest`, `created_at` and `updated_at` attributes.

```ruby

class UsersController < ApplicationController
  before_action :authenticate_request, except: [:create]

  def show 
    user = User.find_by(id: params[:id])

    render json: UserBlueprint.render(user), status: :ok
  end
end
```

```ruby
    render json: UserBlueprint.render(user), status: :ok
```

Here we are serializing the user record using the user blueprint method `render`. This method will return the value as a JSON string which is perfect since we will be sending JSON data to the client.

Be sure to restart your server since we added a new gem and blueprint.

Test this out in postman!

#### Blueprinter Views

Views in blueprinter are used to define the fields that we want to serialize. We can define multiple views for a blueprint for different use cases. For example, we might want to serialize the user's email address in one view but not in another view.

Let's go ahead and create a new view for our user blueprint.

```ruby
# frozen_string_literal: true

class UserBlueprint < Blueprinter::Base
  identifier :id

  view :normal do
    fields :username
  end

  view :extended do
    fields :username, :created_at, :updated_at
  end
end
```

Here we have defined two views: normal and extended. The normal view will serialize the username. The extended view will serialize the username, created_at and updated_at attributes. Let's demonstrate this in our users controller.

```ruby
.
.
.
  def show 
    user = User.find_by(id: params[:id])

    render json: UserBlueprint.render(user, view: :normal), status: :ok
  end
.
.
.
```

if we send a request to `localhost:3000/users/1`, we will get the following response:

```json
{
    "id": 1,
    "username": "username"
}
```

This is powerful since we can define different views for different use cases. For example, we might want to serialize the user's email address in one view but not in another view.

#### Blueprinter Associations

What's more powerful is that we can serialize associations. Let's go ahead and create a new model called `Post`.

```bash
rails g model Post title:string body:text user:references
```

```bash
rails db:migrate
```

```ruby
class Post < ApplicationRecord
  belongs_to :user
end
```

```ruby
class User < ApplicationRecord
  has_secure_password
  validates :username, presence: true
  has_many :posts
end
```

Let's go ahead and create a serializer for our post model. 

```bash
rails g blueprinter:blueprint post
```

**app/blueprints/post_blueprint.rb**

```ruby
# frozen_string_literal: true

class PostBlueprint < Blueprinter::Base
end
```

Let's go ahead and add the following to our post blueprint:

```ruby

class PostBlueprint < Blueprinter::Base
  identifier :id

  view :normal do
    fields :title, :body
  end
end
```

Here we have defined a view called normal. This view will serialize the title and body attributes.

Let's include the posts association in our user blueprint.

```ruby

class UserBlueprint < Blueprinter::Base
  identifier :id

  association :posts, blueprint: PostBlueprint, view: :normal

  view :normal do
    fields :username
  end

  view :extended do
    fields :username, :created_at, :updated_at
  end

end
```

```ruby
  association :posts, blueprint: PostBlueprint, view: :normal
```

Here we are using the method call `association` to serialize the posts association. We are passing in the method name which is posts indicating that the user model has a posts association. We are also passing in the blueprint which is the post blueprint as well as the view.

Let's save some data in our database so we can test this out.

```ruby
rails console
```

```ruby
user = User.first
Post.create(title: 'My first post', body: 'This is my first post', user: user)
Post.create(title: 'My second post', body: 'This is my second post', user: user)
Post.create(title: 'My third post', body: 'This is my third post', user: user)
```



Now if we send a request to `localhost:3000/users/1`, we will get the following response:

```json
{
    "id": 1,
    "posts": [
        {
            "id": 1,
            "body": "This is my first post",
            "title": "My first post"
        },
        {
            "id": 2,
            "body": "This is my second post",
            "title": "My second post"
        },
        {
            "id": 3,
            "body": "This is my third post",
            "title": "My third post"
        }
    ],
    "username": "test"
}
```

Great! This may be a little impractical since we are including all the posts for a user. That can be a very heavy payload if a user has hundreds of post. Let's only grab the first post for a user. 

```ruby
class UserBlueprint < Blueprinter::Base
  identifier :id

  association :posts, blueprint: PostBlueprint, view: :normal do |user|
    user.posts.first
  end

  view :normal do
    fields :username
  end

  view :extended do
    fields :username, :created_at, :updated_at
  end

end
```

In the association method, we are passing in a block. This block will be used to filter the posts. In this case, we are only grabbing the first post for a user.

Now if we send a request to `localhost:3000/users/1`, we will get the following response:

```json
{
    "id": 1,
    "posts": [
        {
            "id": 1,
            "body": "This is my first post",
            "title": "My first post"
        }
    ],
    "username": "test"
}
```

Great! We have successfully serialized our data using blueprinter. We will be using this in our application.

## Conclusion 

In this lesson, we learned the difference between authentication and authorization. We also learned how to authenticate a user using a JWT. Finally, we learned how to serialize data using blueprinter.

>**💡Want a summary or practice quiz for this lesson?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): “Summarize authentication and serialization in Rails and generate 5 quiz questions for students.”
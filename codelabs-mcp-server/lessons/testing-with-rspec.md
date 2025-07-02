---
title: Testing with RSpec in Ruby on Rails
---

# Testing with RSpec in Ruby on Rails

<img src ="https://d604h6pkko9r0.cloudfront.net/wp-content/uploads/2021/03/29113527/rspec-rails-1400x640.png" />

**Table of Contents**

-   About Testing
-   Test Driven Development
-   Types of Testing
-   Testing in Ruby on Rails

## About Testing

Testing is a critical part of the software development process. What is testing and why is it important? Testing is the process of verifying that your code is working as expected.

Here are the benefits of testing:

-   It helps you find bugs in your code
-   It helps you write better code
-   It helps you refactor your code with confidence
-   It helps you document your code
-   It helps you collaborate with other developers
-   It helps you build better products

>**Codelabs Learning Assistant Suggestion:**  
>💡 Not sure why testing matters in your project? 
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> _"Explain why testing is important in software development and give me a real-world example."_

## Test Driven Development

Test Driven Development is a testing paradigm that involves writing tests before writing code. The process is as follows:

1.  Write a test
2.  Run the test and watch it fail
3.  Write the code to make the test pass
4.  Refactor your code

It's as simple as that!

>**Codelabs Learning Assistant Suggestion:**  
>💡 Curious about TDD in practice? 
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)
> _"Show me a simple example of Test-Driven Development in Ruby or Rails, including both the test and the code."_

## Types of Testing

There are many types of testing. Here are some of the most common types of testing:

-   Unit Testing - Testing individual units of code
-   Integration Testing - Testing how different units of code work together
-   Functional Testing - Testing the functionality of your application
-   Acceptance Testing - Testing the acceptance criteria of your application
-   Regression Testing - Testing to ensure that new code does not break existing code
-   Performance Testing - Testing the performance of your application
-   Security Testing - Testing the security of your application

We will explore a few of these types of testing in this lesson.

## Testing in Ruby on Rails

Ruby on Rails by default ships with a testing framework called Minitest. Minitest is a very simple testing framework that is easy to use. However, it is not as powerful as other testing frameworks such as [RSpec](https://rspec.info/). In this lesson, we will be using RSpec to test our Ruby on Rails applications. We will be using the [rspec-rails](https://github.com/rspec/rspec-rails) gem.

To generate a new Rails application with RSpec, run the following command:

```bash
rails new rails-testing -T --api
```

This will generate a new Rails application without the default testing framework. 

Without adding `-T` Rails will automatically add a testing framework called Minitest. If you have done this or have a pre-existing project, you can remove the test files by executing the following:

```bash
rm -rf test/
```

Next, add the following gems to your Gemfile:

```ruby
group :development, :test do
  # See https://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-debug-gem
  gem "debug", platforms: %i[ mri mingw x64_mingw ]
  gem 'rspec-rails'
  gem 'factory_bot_rails'
end
```

Notice that we are adding the gems to the development and test groups. This is because we only want to use these gems in development and test environments and not in production. The reason for this is that these gems are not needed in production and can slow down your application.

```ruby
  gem 'rspec-rails'
```

This is the RSpec testing framework made for Ruby on Rails.

```ruby
  gem 'factory_bot_rails'
```

This is a gem that allows you to create factories for your tests. Factories are a way to create test data. We will explore this in more detail later.

Next, run the following command to install the gems:

```bash
bundle install
```

Next, run the following command to generate the RSpec configuration files:

```bash
rails generate rspec:install
```

This will generate the following files:

```text
create  .rspec
create  spec
create  spec/spec_helper.rb
create  spec/rails_helper.rb
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

This will allow us to use factory-bot methods in our tests.

Using a testing framework can be intimidating at first. However, once you get the hang of it, it becomes second nature. Let's explore how to use RSpec to test our Ruby on Rails applications.

## Unit Testing in Ruby on Rails

We will be using the TDD approach to build a simple blog application. Let's first create a test.

Unit testing is the process of testing individual units of code. In Ruby on Rails, we can unit test our models.

### Unit Testing Models

Create a new folder under spec called `models` and create a file under models called `post_spec.rb`.

Let's include the following:

**spec/models/post_spec.rb**

```ruby
# spec/models/post_spec.rb

require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'with valid attributes' do
    it 'is valid' do
      post = Post.new(title: 'My First Post', content: 'Hello, world!')
      expect(post).to be_valid
    end
  end
end
```

Run `bundle exec rspec spec/models/post_spec.rb` in your terminal to run the test or `bundle exec rspec` to run all tests. You should see the following output:

```bash
germancruz@codecoachthree testing-example % bundle exec rspec spec/models/post_spec.rb


An error occurred while loading ./spec/models/post_spec.rb.
Failure/Error:
  RSpec.describe Post, type: :model do
    context 'with valid attributes' do
      it 'is valid' do
        post = Post.new(title: 'My First Post', content: 'Hello, world!')
        expect(post).to be_valid
      end
    end
  end

NameError:
  uninitialized constant Post

  RSpec.describe Post, type: :model do
                 ^^^^
# ./spec/models/post_spec.rb:5:in `<top (required)>'
No examples found.


Finished in 0.00006 seconds (files took 1.51 seconds to load)
0 examples, 0 failures, 1 error occurred outside of examples
```

Let's create a step by step guide to what we are doing here:

1. We are requiring the `rails_helper` file. This file contains the configuration for RSpec and Rails. It also includes the `spec_helper` file.
2. Include the `RSpec.describe` method. This method takes two arguments: the name of the class you are testing and the type of test you are running. In this case, we are testing the `Post` model and we are running a model test.
3. Define a context. A context is a way to group tests together. In this case, we are grouping tests that have valid attributes.
4. Define a test. A test is defined using the `it` method. In this case, we are testing that a post is valid. We are creating a new post with a title and content and we are expecting it to be valid.
5. Then, we create the correct expectation. In this case, we are expecting the post to be valid using the `be_valid` matcher.
6. Finally, we run `rspec` in the terminal to run the test.

Remember in the TDD process, we write the test first. So we expect this test to fail. Let's write the code to make the test pass.

Let's pass this test.

```bash
bundle exec rails generate model Post title:string content:text
```

You may get a prompt when generating this model

```bash
germancruz@codecoachthree testing-example % bundle exec rails generate model Post title:string content:text
      invoke  active_record
      create    db/migrate/20240115184645_create_posts.rb
      create    app/models/post.rb
      invoke    rspec
    conflict      spec/models/post_spec.rb
```

This is because it is trying to generate a test for us. We already have a test, so we can skip this by entering `n` when prompted to overwrite the file.

Don't forget, when we generate a model, we also generate a migration. Let's run the migration:

```bash
bundle exec rails db:migrate
```

Finally let's run the test again:

```bash
bundle exec rspec spec/models/post_spec.rb
```

You should see the following output:

```bash
germancruz@codecoachthree testing-example % bundle exec rspec spec/models/post_spec.rb

.

Finished in 0.06584 seconds (files took 3.53 seconds to load)
1 example, 0 failures
```

Great! Our test is passing. How come? Let's take a look at our test again:

```ruby
# spec/models/post_spec.rb

require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'with valid attributes' do
    it 'is valid' do
      post = Post.new(title: 'My First Post', content: 'Hello, world!')
      expect(post).to be_valid
    end
  end
end
```

We are creating a new post with a title and content. We are expecting it to be valid. Since we have the `title` and `content` attributes in our `Post` model, the test passes.

Let's add another test to our `post_spec.rb` file.

```ruby
# spec/models/post_spec.rb

require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'with valid attributes' do
    it 'is valid' do
      post = Post.new(title: 'My First Post', content: 'Hello, world!')
      expect(post).to be_valid
    end
  end

  context 'with invalid attributes' do
    it 'is invalid without a title' do
      post = Post.new(content: 'Hello, world!')
      expect(post).to be_invalid
    end
  end
end
```

Let's break this down

```ruby
  context 'with invalid attributes' do
  .
  .
  .
  end
```

A context is a way to group tests together. In this case, we are grouping tests that have invalid attributes.

```ruby
  it 'is invalid without a title' do
    post = Post.new(content: 'Hello, world!')
    expect(post).to be_invalid
  end
```

We are creating a new post without a title. We are expecting it to be invalid. This is useful because we want to ensure that our validations are working as expected.

To pass this test, we need to add a validation to our `Post` model. Let's add a validation for the `title` attribute.

```ruby
# app/models/post.rb

class Post < ApplicationRecord
  validates :title, presence: true
end
```

#### Practice Problem

Add a test to ensure that a post is invalid without content and make it pass.

<details>
  <summary>Solution</summary>

```ruby
# spec/models/post_spec.rb

require 'rails_helper'

RSpec.describe Post, type: :model do
  context 'with valid attributes' do
    it 'is valid' do
      post = Post.new(title: 'My First Post', content: 'Hello, world!')
      expect(post).to be_valid
    end
  end

  context 'with invalid attributes' do
    it 'is invalid without a title' do
      post = Post.new(content: 'Hello, world!')
      expect(post).to be_invalid
    end

    it 'is invalid without content' do
      post = Post.new(title: 'My First Post')
      expect(post).to be_invalid
    end
  end
end
```

```ruby
# app/models/post.rb

class Post < ApplicationRecord
  validates :title, presence: true
  validates :content, presence: true
end
```

</details>

### Unit Testing Controllers

Unit testing controllers is a little more complicated than unit testing models. Let's create a test for our `PostsController`.

Create a new folder under spec called `requests` and create a file under `requests` called `posts_spec.rb`.

#### Create Post - Create


Let's include the following:

**spec/requests/posts_spec.rb**

```ruby
require 'rails_helper'

RSpec.describe 'Posts API', type: :request do
  describe 'POST /posts' do
    let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)

        expect(response).to have_http_status(201)
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end
    end

  end

  def json
    JSON.parse(response.body)
  end
end
```

Let's break this down:

```ruby
require 'rails_helper'
```

We are requiring the `rails_helper` file. This file contains the configuration for RSpec and Rails. It also includes the `spec_helper` file.

```ruby
RSpec.describe 'Posts API', type: :request do
  .
  .
  .
end
```

Here we are using the `RSpec.describe` method to describe our `PostsController`. We are also specifying that this is a request test.

```ruby
RSpec.describe 'Posts API', type: :request do
  describe 'POST /posts' do
    .
    .
    .
  end
end
```

The describe methods takes a block in which we can define our tests. In this case, we are defining a test for the `POST /posts` endpoint.

```ruby
let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }
```

Here we use `let` to define a variable called `valid_attributes`. This is a hash with the title and content attributes. It looks odd but this is how we define variables in RSpec.

```ruby
context 'when the request is valid' do
  .
  .
  .
end
```

Context is a way to group tests together. In this case, we are grouping tests that have valid attributes. We didn't have to do this but it's good practice to group related tests together.

```ruby
it 'creates a new post' do
  expect {
    post '/posts', params: { post: valid_attributes }
  }.to change(Post, :count).by(1)

  expect(response).to have_http_status(201)
  expect(json['title']).to eq('My first post')
  expect(json['content']).to eq('Content of the post')
end
```

```ruby
it 'creates a new post' do
```

The `it` method defines a test in which includes an argument that describes what the test does. In this case, we are testing that a new post is created.

```ruby
  expect {
    post '/posts', params: { post: valid_attributes }
  }.to change(Post, :count).by(1)
```

Let's break down each method call:

`expect` is what we expect to happen. In this case, we expect a new post to be created.

`{post '/posts', params: { post: valid_attributes } }` is the code that we expect to run. In this case, we are making a `POST` request to the `/posts` endpoint with the `valid_attributes` hash.

`to` is the matcher. In this case, we are expecting the code to change the `Post` count by 1.

In RSpec you can chain methods together. In this case, we are chaining the `expect` method with the `to` method.

```ruby
expect(response).to have_http_status(201)
```

Here we are expecting the response to have a status of 201. This is the status code for a successful `POST` request.

```ruby
expect(json['title']).to eq('My first post')
expect(json['content']).to eq('Content of the post')
```

Here we are expecting the response to have a title and content that matches the `valid_attributes` hash.

```ruby
def json
  JSON.parse(response.body)
end
```

This is a helper method that parses the response body into JSON.

Now that we have our test, let's run it and we expect it to fail.

Run `bundle exec rspec spec/requests/posts_spec.rb` in your terminal to run the test or `bundle exec rspec` to run all tests.

Let's go ahead and pass this test.

```ruby
rails g controller Posts
```

This will generate a controller for us. We don't need to generate a model because we already have one.

However it may prompt you to overwrite the `posts_controller.rb` file. Enter `n` to skip this since we already have a spec file for this.

Let's add the following code to our `PostsController`:

**app/controllers/posts_controller.rb**

```ruby
# app/controllers/posts_controller.rb

class PostsController < ApplicationController
  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: post.errors, status: :unprocessable_entity
    end
  end

  private

  def post_params
    params.require(:post).permit(:title, :content)
  end
end
```

**config/routes.rb**

```ruby
Rails.application.routes.draw do
  resources :posts # will generate all routes for posts including POST /posts with action create
end
```

Let's run the test again:

```bash
bundle exec rspec spec/requests/posts_spec.rb
```

Great! Our test is passing.

Let's refactor this test into multiple tests.

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end

  def json
    JSON.parse(response.body)
  end
end
```

Here we are separating our tests into multiple tests. This is a good practice because it makes our tests more readable and easier to debug.

Notice we used the `before` method. This method runs the code before each test. In this case, we are making a `POST` request to the `/posts` endpoint with the `valid_attributes` hash.

#### Get All Posts - Index

Let's go over another example. Let's create a test for the `GET /posts` endpoint.

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end

  describe 'GET /posts' do
    let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot

    before { get '/posts' }

    it 'returns posts' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns posts with the correct structure' do
      # Assuming each post has 'title' and 'content'
      json.each do |post|
        expect(post).to include('title', 'content')
      end
    end
  end

  def json
    JSON.parse(response.body)
  end
end
```

```ruby
  describe 'GET /posts' do

    .
    .
    .

  end
```

Here we created a new `describe` block for the `GET /posts` endpoint.

```ruby
  let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot
```

Here we are using the `let!` method to create 10 posts using factory-bot.

`create_list` is a factory-bot method that creates a list of objects. In this case, we are creating a list of 10
    posts.

<details>

<summary>What is factory-bot?</summary>

If we navigate to `spec/factories/posts.rb`, we can see the factory for our posts.

```ruby
FactoryBot.define do
  factory :post do
    title { "MyString" }
    content { "MyText" }
  end
end
```

This is a factory for our posts. Factories and RSpec are different and aren't dependent upon each other but they go well with each other. Now, we can create posts without factories within the test cases themselves, however, there are benefits in using factory-bot.

-   Factories allow you to define a common setup for creating objects. You can define this setup once in a factory and then reuse it across multiple tests, reducing repetition. There may be times you have to add or remove attributes from these objects. Think about it, if you have to create your objects in every test manually, you will have a lot of repetition in your tests in add or removing attributes. With factories, you can define this setup once and then reuse it across multiple tests.
-   Factories abstract away the complexities of object creation. Tests become cleaner and more focused on the behavior being tested, rather than the setup.

</details>

```ruby
  before { get '/posts' }
```

Here we are making a `GET` request to the `/posts` endpoint.

```ruby
  it 'returns posts' do
    expect(response).to have_http_status(200)
    expect(json).not_to be_empty
    expect(json.size).to eq(10)
  end
```

Here we are expecting the response to have a status of 200. We are also expecting the response to not be empty and to have a size of 10.

In our other test, we are expecting the response to have a title and content. 

```ruby
  it 'returns posts with the correct structure' do
    # Assuming each post has 'title' and 'content'
    json.each do |post|
      expect(post).to include('title', 'content')
    end
  end
```

Here is the final result:

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end 

  describe 'GET /posts' do
    let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot

    before { get '/posts' }

    it 'returns posts' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns posts with the correct structure' do
      # Assuming each post has 'title' and 'content'
      json.each do |post|
        expect(post).to include('title', 'content')
      end
    end
  end

  def json
    JSON.parse(response.body)
  end
end
```

#### Practice Problem

Add a test for the `GET /posts/:id` endpoint. Then pass it. 

<details>
  <summary>Solution</summary>

**spec/requests/posts_spec.rb**

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end 

  describe 'GET /posts' do
    let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot

    before { get '/posts' }

    it 'returns posts' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns posts with the correct structure' do
      # Assuming each post has 'title' and 'content'
      json.each do |post|
        expect(post).to include('title', 'content')
      end
    end
  end

  describe 'GET /posts/:id' do
    let!(:post) { create(:post) }

    before { get "/posts/#{post.id}" }

    it 'returns the post' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json['id']).to eq(post.id)
    end

    it 'should have the correct structure' do 
      expect(json).to include('title', 'content')
    end 
    
  end

  def json
    JSON.parse(response.body)
  end
end
```

**config/routes.rb**

```ruby
Rails.application.routes.draw do
  resources :posts
end
```

This will include the route `/posts/:id`.

**app/controllers/posts_controller**

```ruby
# app/controllers/posts_controller.rb

class PostsController < ApplicationController
  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: post.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: Post.all
  end

  def show 
    post = Post.find(params[:id])

    if post 
      render json: post, status: :ok 
    else 
      render json: {messages: 'not found'}, status: :not_found
    end
  end

  private

  def post_params
    params.require(:post).permit(:title, :content)
  end
end
```

</details>

#### Update Post - Update

Let's go over another example. Let's create a test for the `PUT /posts/:id` endpoint.

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end 

  describe 'GET /posts' do
    let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot

    before { get '/posts' }

    it 'returns posts' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns posts with the correct structure' do
      # Assuming each post has 'title' and 'content'
      json.each do |post|
        expect(post).to include('title', 'content')
      end
    end
  end

  describe 'GET /posts/:id' do
    let!(:post) { create(:post) }

    before { get "/posts/#{post.id}" }

    it 'returns the post' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json['id']).to eq(post.id)
    end

    it 'should have the correct structure' do 
      expect(json).to include('title', 'content')
    end 
    
  end

  describe 'PUT /posts/:id' do
    let!(:post) { create(:post)} 
    
    context 'when the request is valid' do 
      before { put "/posts/#{post.id}", params: { post: { title: 'My updated post', content: 'Updated content' } } }

      it 'updates the post' do 
        expect(response).to have_http_status(200)
        expect(json['title']).to eq('My updated post')
        expect(json['content']).to eq('Updated content')
      end
    end

    context 'when the request is invalid' do 
      before { put "/posts/#{post.id}", params: { post: { title: '', content: '' } } }

      it 'returns status code 422' do 
        expect(response).to have_http_status(422)
      end

      it 'returns a validation failure message' do 
        expect(json['title']).to include("can't be blank")
        expect(json['content']).to include("can't be blank")
      end
    end
  end

  def json
    JSON.parse(response.body)
  end
end
```

Let's break this down: 

```ruby
  describe 'PUT /posts/:id' do
    
    .
    .
    .

  end
```

Here we are creating a new `describe` block for the `PUT /posts/:id` endpoint.

```ruby
    let!(:post) { create(:post)} 
```

We are declaring a variable called `post` and we are creating a new post using factory-bot's method called `create`. The argument in `create` represents the factory name or class name which exist in `spec/factories/posts.rb`.

```ruby
    context 'when the request is valid' do 
      before { put "/posts/#{post.id}", params: { post: { title: 'My updated post', content: 'Updated content' } } }

      it 'updates the post' do 
        expect(response).to have_http_status(200)
        expect(json['title']).to eq('My updated post')
        expect(json['content']).to eq('Updated content')
      end
    end
```

Here we are making a `PUT` request to the `/posts/:id` endpoint with the `post` hash. We are expecting the response to have a status of 200. We are also expecting the response to have a title and content that matches the `post` hash.

```ruby
    context 'when the request is invalid' do 
      before { put "/posts/#{post.id}", params: { post: { title: '', content: '' } } }

      it 'returns status code 422' do 
        expect(response).to have_http_status(422)
      end

      it 'returns a validation failure message' do 
        expect(json['title']).to include("can't be blank")
        expect(json['content']).to include("can't be blank")
      end
    end
```

Here we are making a `PUT` request to the `/posts/:id` endpoint with the `post` hash. We are expecting the response to have a status of 200. We are also expecting the response to have a title and content that matches the `post` hash.

Let's go ahead and pass this test.

**config/routes.rb**

```ruby
Rails.application.routes.draw do
  resources :posts
end
```

As a reminder, this will include the route `PUT /posts/:id` in which will update a post.

Here's a table of the HTTP methods and their corresponding controller actions when we use `resources :posts`:

```text
| HTTP Method | Controller Action | |       Route       |
| ----------- | ----------------- | | ------------------|
| GET         | index             | | GET /posts        |
| GET         | show              | | GET /posts/:id    |
| POST        | create            | | POST /posts       |
| PUT         | update            | | PUT /posts/:id    |
| DELETE      | destroy           | | DELETE /posts/:id |

```

**app/controllers/posts_controller.rb**

```ruby
# app/controllers/posts_controller.rb

class PostsController < ApplicationController
  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: post.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: Post.all
  end

  def show 
    post = Post.find(params[:id])

    if post 
      render json: post, status: :ok 
    else 
      render json: {message: 'not found'}, status: :not_found
    end
  end

  def update 
    post = Post.find(params[:id])

    if post.update(post_params)
      render json: post, status: :ok 
    else 
      render json: post.errors, status: :unprocessable_entity
    end
  end

  private

  def post_params
    params.require(:post).permit(:title, :content)
  end
end
```

Let's run the test again:

```bash
bundle exec rspec
```

#### Delete Post - Destroy 

Let's create a test for the `DELETE /posts/:id` endpoint.

```ruby
require 'rails_helper'

  RSpec.describe 'Posts API', type: :request do
    describe 'POST /posts' do
      let(:valid_attributes) { { title: 'My first post', content: 'Content of the post' } }

    context 'when the request is valid' do
      before { post '/posts', params: { post: valid_attributes } }

      it 'creates a new post' do
        expect {
          post '/posts', params: { post: valid_attributes }
        }.to change(Post, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created post' do
        expect(json['title']).to eq('My first post')
        expect(json['content']).to eq('Content of the post')
      end

      it 'saves the post with the correct attributes' do
        post = Post.last
        expect(post.title).to eq('My first post')
        expect(post.content).to eq('Content of the post')
      end
    end
  end 

  describe 'GET /posts' do
    let!(:posts) { create_list(:post, 10) } # creating 10 posts using Factory Bot

    before { get '/posts' }

    it 'returns posts' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns posts with the correct structure' do
      # Assuming each post has 'title' and 'content'
      json.each do |post|
        expect(post).to include('title', 'content')
      end
    end
  end

  describe 'GET /posts/:id' do
    let!(:post) { create(:post) }

    before { get "/posts/#{post.id}" }

    it 'returns the post' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json['id']).to eq(post.id)
    end

    it 'should have the correct structure' do 
      expect(json).to include('title', 'content')
    end 
    
  end

  describe 'PUT /posts/:id' do
    let!(:post) { create(:post)} 
    
    context 'when the request is valid' do 
      before { put "/posts/#{post.id}", params: { post: { title: 'My updated post', content: 'Updated content' } } }

      it 'updates the post' do 
        expect(response).to have_http_status(200)
        expect(json['title']).to eq('My updated post')
        expect(json['content']).to eq('Updated content')
      end
    end

    context 'when the request is invalid' do 
      before { put "/posts/#{post.id}", params: { post: { title: '', content: '' } } }

      it 'returns status code 422' do 
        expect(response).to have_http_status(422)
      end

      it 'returns a validation failure message' do 
        expect(json['title']).to include("can't be blank")
        expect(json['content']).to include("can't be blank")
      end
    end
  end

  describe 'DELETE /posts/:id' do
    let!(:post) { create(:post) }

    before { delete "/posts/#{post.id}" }

    it 'returns status code 204' do
      expect(response).to have_http_status(204)
    end
  end

  def json
    JSON.parse(response.body)
  end
end
```

Let's go ahead and solve this test case.

**config/routes.rb**

```ruby
Rails.application.routes.draw do
  resources :posts
end
```

As a reminder, this will include the route `DELETE /posts/:id` in which will delete a post.

**app/controllers/posts_controller.rb**

```ruby
# app/controllers/posts_controller.rb

class PostsController < ApplicationController
  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: post.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: Post.all
  end

  def show 
    post = Post.find(params[:id])

    if post 
      render json: post, status: :ok 
    else 
      render json: {message: 'not found'}, status: :not_found
    end
  end

  def update 
    post = Post.find(params[:id])

    if post.update(post_params)
      render json: post, status: :ok 
    else 
      render json: post.errors, status: :unprocessable_entity
    end
  end

  def destroy
    post = Post.find(params[:id])

    if post.destroy
      # return a response with only headers and no body
      head :no_content
    else 
      render json: post.errors, status: :unprocessable_entity
    end
  end

  private

  def post_params
    params.require(:post).permit(:title, :content)
  end
end
```

### Faker
You'll notice that we are using `MyString` and `MyText` as the title and content in our post factory. We can include data that is much more useful. Let's install the [faker gem](https://github.com/faker-ruby/faker) by including it in our Gemfile:

```ruby
group :development, :test do
  # See https://guides.rubyonrails.org/debugging_rails_applications.html#debugging-with-the-debug-gem
  gem "debug", platforms: %i[ mri mingw x64_mingw ]
  gem 'rspec-rails'
  gem 'factory_bot_rails'
  gem 'faker'
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

Don't forget to run `bundle install` in your terminal.

The faker gem allows us to generate fake data based on different categories. The faker gem is useful for mocking realistic data for testing purposes, providing robustness, realism, and broad coverage of a wide range of scenarios.

Let's update our post factory to use the faker gem.

**spec/factories/posts.rb**

```ruby
FactoryBot.define do
  factory :post do
    title { Faker::Lorem.sentence }
    content { Faker::Lorem.paragraph }
  end
end
```

That's it! Now we can generate fake data for our posts. Let's run our tests again:

```bash
bundle exec rspec
```

#### Practice Problem

Use the same project to complete the following:

- Add a new model called user with a name and email attribute. 
- Create a factory for the user model. 
- Create test cases for each of its respective resource actions such as index, create, show, update, and destroy. 
  - index 
    - should return all users that include their email and name
    - should not be empty 
    - should have a size of 10
  - create 
    - should create a new user
    - should return status code 201
    - should return the created user
    - should save the user with the correct attributes
  - show 
    - should return the user
    - should have the correct structure
  - update 
    - should update the user
    - should return status code 200
    - should return the updated user
  - destroy 
    - should return status code 204
    - should delete the user

- Use the faker gem to generate fake data for the user model.

<details>
  <summary>Solution</summary>


```bash
rails g model User name:string email:string
```

```bash
rails db:migrate
```

```bash
rails g controller Users index create show update destroy
```

**spec/factories/users.rb**

```ruby
FactoryBot.define do
  factory :user do
    name { Faker::Name.name }
    email { Faker::Internet.email }
  end
end
```

**spec/requests/users_spec.rb**

```ruby
RSpec.describe 'Users API', type: :request do
  describe 'POST /users' do
    let(:valid_attributes) { { name: 'John Doe', email: 'johndoe123@gmail.com' } }

    context 'when the request is valid' do
      before { post '/users', params: { user: valid_attributes } }

      it 'creates a new user' do
        expect {
          post '/users', params: { user: valid_attributes }
        }.to change(User, :count).by(1)
      end

      it 'returns status code 201' do
        expect(response).to have_http_status(201)
      end

      it 'returns the created user' do
        expect(json['name']).to eq('John Doe')
        expect(json['email']).to eq('johndoe123@gmail.com')
      end

      it 'saves the user with the correct attributes' do
        user = User.last
        expect(user.name).to eq('John Doe')
        expect(user.email).to eq('johndoe123@gmail.com')
      end

    end

    context 'when the request is invalid' do
      before { post '/users', params: { user: { name: '', email: '' } } }

      it 'returns status code 422' do
        expect(response).to have_http_status(422)
      end

      it 'returns a validation failure message' do
        expect(json['name']).to include("can't be blank")
        expect(json['email']).to include("can't be blank")
      end
    end

  end

  describe 'GET /users' do
    let!(:users) { create_list(:user, 10) } # creating 10 users using Factory Bot

    before { get '/users' }

    it 'returns users' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json.size).to eq(10)
    end

    it 'returns users with the correct structure' do
      # Assuming each user has 'name' and 'email'
      json.each do |user|
        expect(user).to include('name', 'email')
      end
    end
  end

  describe 'GET /users/:id' do
    let!(:user) { create(:user) }

    before { get "/users/#{user.id}" }

    it 'returns the user' do
      expect(response).to have_http_status(200)
      expect(json).not_to be_empty
      expect(json['id']).to eq(user.id)
    end

    it 'should have the correct structure' do
      expect(json).to include('name', 'email')
    end

  end

  describe 'PUT /users/:id' do
    let!(:user) { create(:user) }

    context 'when the request is valid' do
      before { put "/users/#{user.id}", params: { user: { name: 'Jane Doe', email: 'janedoe123@gmail.com' } } }

      it 'updates the user' do
        expect(response).to have_http_status(200)
        expect(json['name']).to eq('Jane Doe')
        expect(json['email']).to eq('janedoe123@gmail.com') 
      end
    end

    context 'when the request is invalid' do
      before { put "/users/#{user.id}", params: { user: { name: '', email: '' } } }

      it 'returns status code 422' do
        expect(response).to have_http_status(422)
      end

      it 'returns a validation failure message' do
        expect(json['name']).to include("can't be blank")
        expect(json['email']).to include("can't be blank")
      end
    end

  end

  describe 'DELETE /users/:id' do
    let!(:user) { create(:user) }

    before { delete "/users/#{user.id}" }

    it 'returns status code 204' do
      expect(response).to have_http_status(204)
    end
  end

  def json
    JSON.parse(response.body)
  end

end

```

**config/routes.rb**

```ruby
Rails.application.routes.draw do
  resources :posts
  resources :users
end
```

**app/controllers/users_controller.rb**

```ruby
# app/controllers/users_controller.rb

class UsersController < ApplicationController
  def create
    user = User.new(user_params)
    if user.save
      render json: user, status: :created
    else
      render json: user.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: User.all
  end

  def show 
    user = User.find(params[:id])

    if user 
      render json: user, status: :ok 
    else 
      render json: {message: 'not found'}, status: :not_found
    end
  end

  def update 
    user = User.find(params[:id])

    if user.update(user_params)
      render json: user, status: :ok 
    else 
      render json: user.errors, status: :unprocessable_entity
    end
  end

  def destroy
    user = User.find(params[:id])

    if user.destroy
      # return a response with only headers and no body
      head :no_content
    else 
      render json: user.errors, status: :unprocessable_entity
    end
  end

  private

  def user_params
    params.require(:user).permit(:email, :name)
  end
end
```

</details>

## Refactoring with Confidence 

Now that we have our tests, we can refactor our code with confidence. Let's refactor our `PostsController` to use the `before_action` method.

**app/controllers/posts_controller.rb**

```ruby
# app/controllers/posts_controller.rb

class PostsController < ApplicationController
  before_action :set_post, only: [:show, :update, :destroy]

  def create
    post = Post.new(post_params)
    if post.save
      render json: post, status: :created
    else
      render json: post.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: Post.all
  end

  def show 
    render json: @post, status: :ok 
  end

  def update 
    if @post.update(post_params)
      render json: @post, status: :ok 
    else 
      render json: @post.errors, status: :unprocessable_entity
    end
  end

  def destroy
    if @post.destroy
      # return a response with only headers and no body
      head :no_content
    else 
      render json: @post.errors, status: :unprocessable_entity
    end
  end

  private

  def post_params
    params.require(:post).permit(:title, :content)
  end

  def set_post
    @post = Post.find(params[:id])
  end
end
```

Let's run our tests again:

```bash
bundle exec rspec
```

Great! Our tests are still passing.

#### Practice Problem

Refactor the `UsersController` to use the `before_action` method.

<details>
  <summary>Solution</summary>

**app/controllers/users_controller.rb**
  
  ```ruby
  # app/controllers/users_controller.rb

class UsersController < ApplicationController

  before_action :set_user, only: [:show, :update, :destroy]

  def create
    user = User.new(user_params)
    if user.save
      render json: user, status: :created
    else
      render json: user.errors, status: :unprocessable_entity
    end
  end

  def index 
    render json: User.all
  end

  def show 
    render json: @user, status: :ok 
  end

  def update 
    if @user.update(user_params)
      render json: @user, status: :ok 
    else 
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  def destroy
    if @user.destroy
      # return a response with only headers and no body
      head :no_content
    else 
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  private

  def user_params
    params.require(:user).permit(:email, :name)
  end

  def set_user
    @user = User.find(params[:id])
  end
end
  ```

</details>

## Conclusion

We've managed to introduce testing to the world of Ruby on Rails. We learned about the different types of tests and how to write them. As we continue to build our applications, we will continue to write tests to ensure that our applications work as expected.
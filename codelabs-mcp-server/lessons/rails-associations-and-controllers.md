---
title: Associations and Controllers
---

# Associations and Controllers

<img src= "https://gloriumtech.com/wp-content/uploads/2023/08/Backend-Development-for-Mobile-Applications.jpg" />

**Table of Contents**

-   Associations in-depth
    -   has_one Association
    -   belongs_to Association
    -   has_many :through Association
    -   has_and_belongs_to_many Association
    -   Polymorphic association
    -   self-join association
-   Controllers and Routes
    -   Users controller
    -   Postman
    -   Index
    -   Show
    -   Put
    -   Destroy
-   Conclusion



## Associations in-depth

In the previous lesson, we created a one-to-one relationship and a one-to-many relationship. In this lesson, we will be going over the different types of associations that can be created in Rails.

Here is a list of the different types of associations that can be created in Rails:

- **has_one Association**: This is used in the model that contains the foreign key. It specifies that each instance of the model has one instance of another model. For example, if a User model has one Profile, you would define it in the User model as has_one :profile.
- **belongs_to Association**: This is used in the model that is owned by another model. In the Profile model, you would use belongs_to :user to indicate that each profile is associated with a specific user.
-   **has-many-through**: A has-many-through association is when a record in a table can belong to many records in another table through a third table. For example, a user has many doctors through appointments. A doctor has many users through appointments. Whereas a many-to-many association would be a patient has many doctors and a doctor has many patients.
-   **has_and_belongs_to_many**: A has_and_belongs_to_many association is when a record in a table can belong to many records in another table and vice versa. For example, a user has many friends and a friend has many users. This is similar to a has-many-through association, but the difference is that a has-many-through association requires a third model and a has_and_belongs_to_many association does not.
-   **polymorphic**: A polymorphic association is when a record in a table can belong to more than one record from other tables. For example, a comment can belong to a post or a comment can belong to a photo.
-   **self-join**: A self-join association is when a record in a table can belong to another record in the same table. For example, a user can have many friends and a friend can be a user. Followers and following is another example of a self-join association.

Let's demonstrate how to create each of these associations.

In each section, we will be creating a new Rails API to demonstrate each association.

### has_one Association 

Create a new Rails project configured to be an API called `rails_one_to_one_association_api`

A one-to-one association is when one record in a table is associated with one record in another table. For example, a user has one profile. A profile belongs to a user.

Let's create a one-to-one association between a user and a profile. First, we need to create a user model and a profile model. We can do this by running the following command in the terminal:

```bash
rails g model User name:string email:string
rails g model Profile user:references bio:text
```

In a one-to-one association in Rails, only the "belongs_to" side of the association (in this case, the Profile model) needs to have a foreign key column in its table. The "has_one" side (here, the User model) does not require a foreign key column in its table.

**app/models/user.rb**

```ruby
class User < ApplicationRecord
  has_one :profile
end
```

**app/models/profile.rb**

```ruby
class Profile < ApplicationRecord
  belongs_to :user
end
```

Now any time we create a user, we can create a profile for that user. Let's create a user and a profile in the Rails console:

```bash
rails db:migrate

rails c
```

```ruby
user = User.create(name: "John", email: "test@test.com")
profile = Profile.create(bio: "I am a user", user: user)
user.profile = profile
```

### has_many Association

A one-to-many association is when one record in a table is associated with many records in another table. For example, a user has many posts. A post belongs to a user.

Create a new Rails project configured to be an API called `rails_one_to_many_association_api`

Let's create a one-to-many association between a user and a post. First, we need to create a user model and a post model. We can do this by running the following command in the terminal:

```bash
rails g model User name:string email:string
rails g model Post title:string body:text user:references
```

In a one-to-many association in Rails, only the "belongs_to" side of the association (in this case, the Post model) needs to have a foreign key column in its table. The "has_many" side (here, the User model) does not require a foreign key column in its table.

**app/models/user.rb**

```ruby
class User < ApplicationRecord
  has_many :posts
end
```

**app/models/post.rb**

```ruby
class Post < ApplicationRecord
  belongs_to :user
end
```

Now any time we create a user, we can create a post for that user. Let's create a user and a post in the Rails console:

```bash
rails db:migrate

rails c
```

```ruby
user = User.create(name: "John", email: "test@example.com")
post = Post.create(title: "My first post", body: "This is my first post", user: user)

user.posts << post
```

### has_many :through Association

Create a new Rails project configured to be an API called `rails_many_to_many_association_api`

A has-many-through association is when a record in a table can belong to many records in another table through a third table. A has-many-through requires a third model. For example, a user has many doctors through appointments. A doctor has many users through appointments. Whereas a many-to-many association would be a patient has many doctors and a doctor has many patients.

Create a new Rails API to demonstrate a has-many-through association.

Let's create a has-many-through association with physicians, patients, and appointments. First, we need to create a physician model, a patient model, and an appointment model. We can do this by running the following command in the terminal:

```bash
rails g model Physician name:string
rails g model Patient name:string
rails g model Appointment physician:references patient:references
```

The third table is going to be the appointments table. The appointments table will have a physician_id column and a patient_id column. The appointments table will be the join table between the physicians table and the patients table.

**app/models/physician.rb**

```ruby
class Physician < ApplicationRecord
  has_many :appointments
  has_many :patients, through: :appointments
end
```

Let's break this down:

-   has_many :appointments: This line of code is saying that a physician has many appointments from the appointments table.
-   has_many :patients, through: :appointments: This line of code is saying that a physician has many patients through the appointments table.

**app/models/patient.rb**

```ruby
class Patient < ApplicationRecord
  has_many :appointments
  has_many :physicians, through: :appointments
end
```

Let's break this down:

-   has_many :appointments: This line of code is saying that a patient has many appointments from the appointments table.
-   has_many :physicians, through: :appointments: This line of code is saying that a patient has many physicians through the appointments table.

**app/models/appointment.rb**

```ruby
class Appointment < ApplicationRecord
  belongs_to :physician
  belongs_to :patient
end
```

Here we see

-   belongs_to :physician: This line of code is saying that an appointment belongs to a physician.
-   belongs_to :patient: This line of code is saying that an appointment belongs to a patient.

Now any time we create a physician, we can create an appointment for that physician. Let's create a physician and an appointment in the Rails console:

```bash
rails db:migrate

rails c
```

```ruby
physician = Physician.create(name: "Dr. Smith")
patient = Patient.create(name: "John Doe")
appointment = Appointment.create(physician: physician, patient: patient)

physician.appointments
patient.appointments
```

Now we can see that the physician has an appointment and the patient has an appointment. We can also see that the physician has a patient and the patient has a physician.

> **Need help understanding has_many :through?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"Can you explain how a has_many :through association works in Rails, and when I should use it instead of has_and_belongs_to_many?"_

### has_and_belongs_to_many Association

Create a new Rails project configured to be an API called `rails_has_and_belongs_to_many_association_api`

A has-and-belongs-to-many association is when a record in a table can belong to many records in another table and vice versa. For example, a user has many friends and a friend has many users. This is similar to a has-many-through association, but the difference is that a has-many-through association requires a third model and a has-and-belongs-to-many association does not.

Create a new Rails API to do the following:

Let's create a has-and-belongs-to-many association with authors and books. First, we need to create an author model and a book model. We can do this by running the following command in the terminal:

```bash
rails g model Author name:string
rails g model Book title:string
```

The third table is going to be the authors_books table. The authors_books table will have an author_id column and a book_id column. The authors_books table will be the join table between the authors table and the books table.

Let's generate a migration file to create the authors_books table:

```bash
rails g migration CreateJoinTableAuthorBook author book
```

This will generate a migration file that looks like this:

```ruby
class CreateJoinTableAuthorBook < ActiveRecord::Migration[6.0]
  def change
    create_join_table :authors, :books do |t|
      # t.index [:author_id, :book_id]
      # t.index [:book_id, :author_id]
    end
  end
end
```

Let's uncomment the two lines of code:

```ruby
class CreateJoinTableAuthorBook < ActiveRecord::Migration[6.0]
  def change
    create_join_table :authors, :books do |t|
      t.index [:author_id, :book_id]
      t.index [:book_id, :author_id]
    end
  end
end
```

Now we can run the migration:

```bash
rails db:migrate
```

Now we can create the association between the author model and the book model:

**app/models/author.rb**

```ruby
class Author < ApplicationRecord
  has_and_belongs_to_many :books
end
```

**app/models/book.rb**

```ruby
class Book < ApplicationRecord
  has_and_belongs_to_many :authors
end
```

Now any time we create an author, we can create a book for that author. Let's create an author and a book in the Rails console:

```bash
rails c
```

```ruby
author = Author.create(name: "John Doe")
book = Book.create(title: "My first book")

author.books << book
```

### Polymporphic association

A polymorphic association is when a record in a table can belong to more than one other record in another table. For example, a comment can belong to a post or a comment can belong to a photo.

Create a new Rails API called `rails_polymorphic_association_api`

Let's create a polymorphic association with comments, posts, and photos. First, we need to create a comment model, a post model, and a photo model. We can do this by running the following command in the terminal:

```bash
rails g model Comment body:text commentable:references{polymorphic}
rails g model Post title:string body:text
rails g model Photo title:string
```

The third table is going to be the comments table. The comments table will have a commentable_id column and a commentable_type column. The comments table will be the join table between the posts table and the photos table.

Let's generate a migration file to create the comments table:

```bash
rails g migration CreateComments
```

This will generate a migration file that looks like this:

```ruby
class CreateComments < ActiveRecord::Migration[6.0]
  def change
    create_table :comments do |t|
      t.text :body
      t.references :commentable, polymorphic: true, null: false

      t.timestamps
    end
  end
end
```

Now we can run the migration:

```bash
rails db:migrate
```

Now we can create the association between the comment model, the post model, and the photo model:

**app/models/comment.rb**

```ruby
class Comment < ApplicationRecord
  belongs_to :commentable, polymorphic: true
end
```

**app/models/post.rb**

```ruby
class Post < ApplicationRecord
  has_many :comments, as: :commentable
end
```

**app/models/photo.rb**

```ruby
class Photo < ApplicationRecord
  has_many :comments, as: :commentable
end
```

Now any time we create a post, we can create a comment for that post. Let's create a post and a comment in the Rails console:

```bash
rails c
```

```ruby
post = Post.create(title: "My first post", body: "This is my first post")
comment = Comment.create(body: "This is my first comment", commentable: post)

post.comments

photo = Photo.create(title: "My first photo")
comment = Comment.create(body: "This is my first comment", commentable: photo)

photo.comments
```

Now we can see that the post has a comment and the photo has a comment. We can also see that the comment has a post and the comment has a photo.

> **Curious about polymorphic associations?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"What are some real-world examples of polymorphic associations in Rails, and how do I access the parent object from a comment?"_

### self-join association

A self-join association is when a record in a table can belong to another record in the same table. For example, a user can have many friends and a friend can be a user. Followers and following is another example of a self-join association.

In a self-join association, you don't necessarily need a third table like a typical many-to-many relationship. Instead, you can use a single table (users) with a join table that references it twice (once for each side of the relationship). In the case of users and friends, the users table holds all user records, and the friendships table is used to link users together.

```bash
rails g model User name:string
```

```bash
rails g model Friendship user:references friend:references
```

The migration file should look like this:

```ruby
class CreateFriendships < ActiveRecord::Migration[6.0]
  def change
    create_table :friendships do |t|
      t.references :user, null: false, foreign_key: true
      t.references :friend, null: false, foreign_key: { to_table: :users }

      t.timestamps
    end
  end
end
```

Note that for the friend column, we specify `foreign_key: { to_table: :users }` to indicate that this is a self-reference to the users table.

**app/models/user.rb**

```ruby
class User < ApplicationRecord
  has_many :friendships
  has_many :friends, through: :friendships, source: :friend
end
```

**app/models/friendship.rb:**

```ruby
class Friendship < ApplicationRecord
  belongs_to :user
  belongs_to :friend, class_name: 'User'
end
```

```ruby
user1 = User.create(name: "Alice")
user2 = User.create(name: "Bob")

user1.friends << user2

user1.friends
```

## Controllers and Routes

We have spent a lot of time learning about models and associations. Now let's learn about controllers and routes.

Controllers are the middlemen between models and views. They are responsible for processing requests and sending responses. They are also responsible for handling the logic of the application. For example, if we want to create a user, the controller will handle the logic of creating a new user.

Routes, on the other hand, are responsible for mapping URLs to controller actions. A controller action is a method that is defined in the controller's class. For example, if we want to create a user, we will make a POST request to the create action in the users controller.

Let's start off by creating a user.

### Users controller

Let's create a brand new Rails API to demonstrate controllers and routes.

We will create a brand new Rails application:

```bash
rails new controllers_and_routes_api --api 
```

Now let's create a user model

```bash
rails g model User name:string email:string
```

Now let's run the migration:

```bash
rails db:migrate
```

Now let's create a users controller. We can do this by running the following command in the terminal:

```bash
rails g controller Users
```

This will create a controller file in app/controllers/users_controller.rb. Let's open up this file and add the following code:

```ruby
class UsersController < ApplicationController
end
```

This file is where we will be adding what are called actions. Actions are methods that are defined in the controller an are responsible for handling requests and sending responses.

Let's add an action called create to the users controller:

```ruby
class UsersController < ApplicationController
  def create
  end
end
```

The purpose of this action is to create a new user. Let's add the logic to create a new user:

```ruby
class UsersController < ApplicationController
  def create
    @user = User.new(name: params[:name], email: params[:email])
    if @user.save
      render json: @user
    else
      render json: { error: "Unable to create user." }
    end
  end
end
```

Here we are creating a new user with the name and email that are passed in as parameters. We see the we can access params by using the params hash.

The params hash is a hash that contains all of the parameters that are passed in from the request. For example, if we make a POST request to the create action with the following parameters:

```json
{
	"name": "John",
	"email": "johndoe123@example.com"
}
```

Then the params hash will look like this:

```ruby
{
  name: "John",
 email: "johndoe123@example.com"
}
```

From there we check to see if the user was saved. If the user was saved, then we render the user as JSON. If the user was not saved, then we render an error message as JSON.

This is a typical pattern that you will see in Rails. If the action is successful, then render the resource as JSON. If the action is not successful, then render an error message as JSON.

Now let's add a route to the routes file. Let's open up the routes file in config/routes.rb and add the following code:

```ruby
Rails.application.routes.draw do
  resources :users
end
```

The resources method is a method that is provided by Rails. It is a method that is used to create routes for a resource.

The resources method will create the following routes, here's a table

```text
| HTTP Verb | Path       | Controller#Action | Used for                    |
| --------- | ---------- | ----------------- | --------------------------- |
| GET       | /users     | users#index       | display a list of all users |
| POST      | /users     | users#create      | create a new user           |
| GET       | /users/:id | users#show        | display a specific user     |
| PATCH/PUT | /users/:id | users#update      | update a specific user      |
| DELETE    | /users/:id | users#destroy     | delete a specific user      |
```

Let's break this table down:

-   HTTP Verb: This is the HTTP verb that is used to make the request. For example,
    -   A GET request is used to get a resource.
    -   A POST request is used to create a resource.
    -   A PUT request is used to update a resource.
    -   A DELETE request is used to delete a resource.
-   Path: This is the path that is used to make the request. For example,
    -   the path for a GET request to get all users is /users.
    -   The path for a POST request to create a user is /users.
    -   The path for a GET request to get a specific user is /users/:id.
    -   The path for a PUT request to update a specific user is /users/:id.
    -   The path for a DELETE request to delete a specific user is /users/:id.
-   Controller#Action: This is the controller and action that is used to handle the request. For example,
    -   Get all users is users#index.
    -   Create a user is users#create.
    -   Get a specific user is users#show.
    -   Update a specific user is users#update.
    -   Delete a specific user is users#destroy.

Since we are only using the create action for now, we can specify the only action we like to use in the resources method.

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create]
```

Now let's test out our create action. Let's start up our Rails server by running the following command in the terminal:

```bash
rails s
```

Now let's make a POST request to the create action.

This indicates the name of the controller, the name of the controller file, and the name of the controller class.

```text
| HTTP Verb | Path   | Controller#Action | Used for                    |
| --------- | ------ | ----------------- | --------------------------- |
| POST      | /users | users#create      | create a new user           |
```

Let's open up this file.

Now let's add the create action to the users controller:

```ruby
class UsersController < ApplicationController
  def create
    user = User.new(name: params[:name], email: params[:email])
    if user.save
      render json: user
    else
      render json: { error: "Unable to create user." }
    end
  end
end
```

Let's break this down together: 

```ruby 
class UsersController < ApplicationController
.
.
.
end
```

We are defining a class called UsersController in which is where we define our actions.

Notice how the class is inheriting from ApplicationController. ApplicationController is a class that is provided by Rails to define the class as a controller. There are certain methods that are provided by ApplicationController that are used to handle requests and send responses such as:

- render: This method is used to render a view or render a resource as JSON.
- redirect_to: This method is used to redirect to a different route.
- params: This method is used to access the parameters that are passed in from the request.
- request: This method is used to access the request object.
- and more..

Next, we have defined an action called create. Actions are methods that are defined in the controller an are responsible for handling requests and sending responses. This action is responsible for creating a new user.  

```ruby 
class UsersController < ApplicationController
  def create
 
  end
end
```

Remember, an action is in the context of the controller is just a method defined in the controller class. 

In the create action, 

```ruby
    user = User.new(name: params[:name], email: params[:email])
```

We are creating a new user with the name and email that are passed in as parameters. We see the we can access params by using the params hash. The params hash is a hash that contains all of the parameters that are passed in from the request. For example, if we make a POST request to the create action, in which we will do shortly, with the following parameters:

```json
{
	"name": "John",
	"email": "johndoe123@example.com"
}
```

Then the params hash will look like this:

```ruby
{
  name: "John",
  email: "johndoe123@example.com"
}
```

The `new` method is a method that is provided by ActiveRecord. It will fill the attributes of the record but will not save until we call the `save` method. 

```ruby
    if user.save
      render json: user
    else
      render json: { error: "Unable to create user." }
    end
  end
end
```

Here we use a conditional to check if the user was saved. If the user was saved, then we render the user as JSON. If the user was not saved, then we render an error message as JSON.  

This is a typical pattern that you will see in Rails. If the action is successful, then render the resource as JSON. If the action is not successful, then render an error message as JSON.

Let's go ahead and make our very first request to our Rails API.

### Postman

To send requests to our server we will be using a tool called Postman. Postman is a commonly used tool for testing APIs. 

You can download Postman here: https://www.postman.com/downloads/.

**Be sure to download the desktop app since the web version cannot send requests to localhost.**

Also be sure to create an account, it is free.

You will go through a series of steps

1. Full name and role
   <img src="https://imgur.com/LmhzXTX.png" />

2. Create a team: Creating a team in postman revolves around inviting other people to collaborate with you. You can leave this as is.

<img src ="https://imgur.com/olyMBUl.png" />

3. You will then see your workspaces

<img src = "https://imgur.com/jTKhLBN.png" />

4. Create a workspace

<img src = "https://imgur.com/nNnnVOn.png" />

5. blank template
6. name: codelabs
7. access: personal

Great after you have created your workspace you will see this screen

<img src = "https://imgur.com/J4duDOC.png" />

Let's create a collection. A collection is a group of requests. We will be creating a collection for our Rails API.

<img src = "https://imgur.com/4u6pOT7.png" />

Call this `rails-postman-test`

Let's go ahead and create our very first request in postman.

Click on the ellipsis of the collection and click on `Add request`

<img src = "https://imgur.com/fDoBq2Q.png" />

1. Call this request `create user`

2. The url will be `http://localhost:3000/users`
3. Change the request to `POST`
4. Navigate to the `Body` tab and select `raw` and `JSON`

Paste in a json object such as

```json
{
	"name": "john doe",
	"email": "johndoe123@example.com"
}
```

5. Click `send` and you should see a response like in the image below

<img src = "https://imgur.com/BCTk2da.png" />

Great! We have successfully created a user. Now let's create the rest of the actions.

### Index

Another action that we will be creating is the index action. This is on of the actions defined in the RESTful routes. Here is a reminder of what our routes look like:

```text
| HTTP Verb | Path       | Controller#Action | Used for                    |
| --------- | ---------- | ----------------- | --------------------------- |
| GET       | /users     | users#index       | display a list of all users |
| POST      | /users     | users#create      | create a new user           |
| GET       | /users/:id | users#show        | display a specific user     |
| PATCH/PUT | /users/:id | users#update      | update a specific user      |
| DELETE    | /users/:id | users#destroy     | delete a specific user      |
```

The purpose of the index action is to display a list of all users.

Let's add an index action to the users controller:

```ruby
class UsersController < ApplicationController
  def index
    @users = User.all
    render json: @users
  end

  def create
    @user = User.new(name: params[:name], email: params[:email])
    if @user.save
      render json: @user
    else
      render json: { error: "Unable to create user." }
    end
  end
end
```

Here we are getting all of the users and rendering them as JSON.

Now let's add a route to the routes file. Let's open up the routes file in config/routes.rb and add the following code:

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create, :index]
end
```

Again each action name is tied to a route name.

This will create the following routes:

```text
| HTTP Verb | Path   | Controller#Action | Used for                    |
| --------- | ------ | ----------------- | --------------------------- |
| GET       | /users | users#index       | display a list of all users |
| POST      | /users | users#create      | create a new user           |
```

In order to trigger the index action in our users controller, we need to make a GET request to the /users route.

Let's test this out in Postman. Let's make a GET request to the /users route.

Make a new request in Postman and call it `get users`

Make sure it is a get request and the url is `http://localhost:3000/users`

Once you are ready click `send` and you should see a response like this

<img src = "https://imgur.com/oGuT6zX.png" />

### Show

The purpose of the show action is to get a specific user.

Let's add a show action to the users controller:

```ruby
class UsersController < ApplicationController
  def index
    @users = User.all
    render json: @users
  end

  def show
    @user = User.find(params[:id])
    render json: @user
  end

  def create
    @user = User.new(name: params[:name], email: params[:email])
    if @user.save
      render json: @user
    else
      render json: { error: "Unable to create user." }
    end
  end
end
```

Here we are finding a user by the id that is passed in as a parameter and rendering the user as JSON.

Now let's add a route to the routes file. Let's open up the routes file in config/routes.rb and add the following code:

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create, :index, :show]
end
```

Again each action name is tied to a route name.

This will create the following routes:

```text
| HTTP Verb | Path       | Controller#Action | Used for                    |
| --------- | ---------- | ----------------- | --------------------------- |
| GET       | /users     | users#index       | display a list of all users |
| POST      | /users     | users#create      | create a new user           |
| GET       | /users/:id | users#show        | display a specific user     |
```

The show action is mapped to a special route since it requires an id or parameter.

In order to trigger the show action in our users controller, we need to make a GET request to the /users/:id route.

Let's test this out in Postman. Let's make a GET request to the /users/:id route.

Make a new request in Postman and call it `get user`

Make sure it is a get request and the url is `http://localhost:3000/users/1` since we currently have a user of id 1.

Once you are ready click send and you should see a response like this

<img src ='https://imgur.com/g9ekqWD.png' />

### Put

The purpose of the put action is to update a specific user.

Let's add a put action to the users controller:

```ruby

class UsersController < ApplicationController
  def index
    @users = User.all
    render json: @users
  end

  def show
    @user = User.find(params[:id])
    render json: @user
  end

  def create
    @user = User.new(name: params[:name], email: params[:email])
    if @user.save
      render json: @user
    else
      render json: { error: "Unable to create user." }
    end
  end

  def update
    @user = User.find(params[:id])
    if @user.update(name: params[:name], email: params[:email])
      render json: @user
    else
      render json: { error: "Unable to update user." }
    end
  end
end
```

Here we are finding a user by the id that is passed in as a parameter and updating the user with the name and email that are passed in as parameters. We see the we can access params by using the params hash.

Let's update the route to include the update action:

```ruby
Rails.application.routes.draw do
  resources :users, only: [:create, :index, :show, :update]
end
```

Again each action name is tied to a route name.

This will create the following routes:

```text
| HTTP Verb | Path       | Controller#Action | Used for                    |
| --------- | ---------- | ----------------- | --------------------------- |
| GET       | /users     | users#index       | display a list of all users |
| POST      | /users     | users#create      | create a new user           |
| GET       | /users/:id | users#show        | display a specific user     |
| PATCH/PUT | /users/:id | users#update      | update a specific user      |
```

Go ahead and create a new request on postman and call it `update user`

Make sure it is a put request and the url is `http://localhost:3000/users/1` since we currently have a user of id 1.

Navigate to the `Body` tab and select `raw` and `JSON`

Paste in a json object such as

```json
{
	"name": "john doe",
	"email": "johnnyjames456@example.com"
}
```

Be sure to test this out by clicking send. You should see a successful response.

### Destroy

The purpose of the destroy action is to delete a specific user.

Let's add a destroy action to the users controller:

```ruby
class UsersController < ApplicationController
  def index
    @users = User.all
    render json: @users
  end

  def show
    @user = User.find(params[:id])
    render json: @user
  end

  def create
    @user = User.new(name: params[:name], email: params[:email])
    if @user.save
      render json: @user
    else
      render json: { error: "Unable to create user." }
    end
  end

  def update
    @user = User.find(params[:id])
    if @user.update(name: params[:name], email: params[:email])
      render json: @user
    else
      render json: { error: "Unable to update user." }
    end
  end

  def destroy
    @user = User.find(params[:id])
    if @user.destroy
      render json: { message: "Successfully deleted user." }
    else
      render json: { error: "Unable to delete user." }
    end
  end
end
```

Here we are finding a user by the id that is passed in as a parameter and deleting the user. Since we are using all 5 routes, we don't need to exclude any, so we can remove the `only` option.

Let's update the route to include the destroy action:

```ruby
Rails.application.routes.draw do
  resources :users
end
```

Again each action name is tied to a route name.

This will create the following routes:

```text
| HTTP Verb | Path       | Controller#Action | Used for                    |
| --------- | ---------- | ----------------- | --------------------------- |
| GET       | /users     | users#index       | display a list of all users |
| POST      | /users     | users#create      | create a new user           |
| GET       | /users/:id | users#show        | display a specific user     |
| PATCH/PUT | /users/:id | users#update      | update a specific user      |
| DELETE    | /users/:id | users#destroy     | delete a specific user      |

```
Use postman to create a new request called `delete user` and delete the user with id 1. You should see a successful response.

> **💡 Stuck on controllers or routes?**  
> Ask the [Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant):  
> Ask: _"How do I create custom actions in a Rails controller, and how do I add routes for them in Rails 8?"_

## Conclusion

In this lesson, we explore the comprehensive guide to associations and controllers in Rails. The powerful building block of associations allows us to create complex data relationships between models, while controllers and routes handle the flow of data between the user interface and the database. By understanding these core concepts, you will be able to build robust and dynamic web applications using Ruby on Rails.

As you continue to explore and build with Rails, remember that the power of this framework lies in its ability to simplify complex tasks, allowing you to focus on creating unique and powerful web solutions.
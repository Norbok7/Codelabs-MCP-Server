---
title: Action Mailer and More
---

# Action Mailer and More

**Table of Contents**

- Action Mailer
- Using Sendgrid for Email

## Introduction to Emails

Emails are a crucial part of any application. They are used to send notifications, confirmations, and other important information to users. In this section, we will learn how to send emails using Action Mailer and how to use Sendgrid to send emails.

There are couple of ways we can send emails from our environments (prod, dev, test). It depends on the application of course but most of the time, it makes sense to preview the email in development and test environments and send the email in production.

For production, we will use sendgrid to send emails. Sendgrid is a cloud-based email delivery platform that assists businesses with email delivery. It is a great tool to send emails from your application.

For development and test environments, we will use letter opener. Letter opener is a gem that opens a preview of the email in the browser instead of sending it. This is a great tool to preview the email before sending it.

You're more than welcome to use sendgrid for development and test environments as well. It's just a matter of preference.

### Setup

Please continue with the previous lesson to set up the application. This assumes the API is deployed to render.

Let's also be sure to add email to the user model.

```bash
rails g migration AddEmailToUsers email:string
```

Then run the migration:

```bash
rails db:migrate
```

## Action Mailer

Action Mailer is a part of the Action Pack library in Rails. It is used to send emails from your API and craft the email content.

### Letter Opener

To use letter opener, add the following to your Gemfile:

```ruby
group :development do
  gem 'letter_opener'
end
```

Then run `bundle install` to install the gem.

In your `config/environments/development.rb` file, add the following:

```ruby
config.action_mailer.delivery_method = :letter_opener
config.action_mailer.perform_deliveries = true
config.action_mailer.default_url_options = { host: 'localhost', port: 3000 }
```

Now, when you send an email in development, it will open a preview in your browser instead of sending it.

Let's create a the email content.

### Generating a Mailer

Let's create an action mailer to send an email. Run the following command to generate a mailer:

```bash
rails generate mailer UserMailer
```

This will create a new file in `app/mailers/user_mailer.rb`. Add the following code to the file:

```ruby
class UserMailer < ApplicationMailer
  default from: 'email@email.com'

  def welcome_email(user)
    @user = user
    mail(to: @user.email, subject: 'Welcome to My Awesome Site')
  end
end
```

Next we will create the view for the email. Create a file in `app/views/user_mailer/welcome_email.html.erb` and add the following code:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to My Awesome Site</title>
  </head>
  <body>
    <h1>Welcome <%= @user.username %> to My Awesome Site</h1>
    <p>You have successfully signed up to My Awesome Site.</p>
  </body>
</html>
```

Now we can send the email. In your controller, add the following code:

```ruby
  def create
    user = User.new(username: params[:username], email: params[:email])

    if user.save
      UserMailer.welcome_email(user).deliver_now
      render json: user, status: :created
    else
      render json: user.errors, status: :unprocessable_entity
    end
  end
```

Now try creating a user and you should see the email preview in your browser.

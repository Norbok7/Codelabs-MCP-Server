---
title: Live Coding - Schedulers using Sidekiq and Redis
---

<img src ='https://sidekiq.org/assets/sidekiq.png'/>

## Introduction

Schedulers are a crucial part of any application. They help in automating tasks that need to be performed at regular intervals. In this lesson, we will learn how to implement a scheduler using Sidekiq for a Ruby on Rails API.

What is a scheduler?

A scheduler is a system that allows you to schedule tasks to be executed at a specific time or at regular intervals. These tasks can be anything from sending emails, generating reports, or performing maintenance tasks.

Why use a scheduler?

Schedulers are essential for automating repetitive tasks, ensuring that they are executed at the right time and in the right order. They help in improving the performance and reliability of an application by offloading time-consuming tasks to a background process.

What are examples of tasks that can be scheduled?

Some common examples of tasks that can be scheduled include:

-   Sending reminder emails to users
-   Generating daily/weekly reports
-   Cleaning up old data
-   Performing backups
-   Running maintenance tasks
-   Importing data from external sources
-   Running periodic checks and updates
-   Even a leader board can be updated at regular intervals

## The Problem

Let's say that we have a leader board. Whenever a user goes to the leader board, we want to show the latest scores. We can't calculate the scores every time a user visits the leader board because it would be too slow and resource-intensive. Especially, if we have a large number of users and scores to calculate. This is where a scheduler comes in.

Instead, we want to calculate the scores at regular intervals and update the leader board accordingly.

## The Solution

We will use Sidekiq to create a background job that calculates the scores and updates the leader board. We will then use Sidekiq's scheduling feature to run this job at regular intervals.

## Sidekiq and Redis

In order for us to implement a scheduler, we will be using Sidekiq, a popular background job processing library for Ruby. Sidekiq uses Redis as a broker for managing background jobs. Redis is an in-memory data store that is used as a message broker for Sidekiq.

What is Redis?
Redis is an open-source, in-memory data store that can be used as a database, cache, and message broker. It is known for its high performance, scalability, and support for various data structures. Redis is widely used and is a popular choice for building real-time applications, caching, and queuing systems.

What is a background job?

A background job is a task that is executed outside the normal request-response cycle of a web application. It allows you to perform time-consuming or resource-intensive tasks without blocking the main application process. This is important because it ensures that the application remains responsive and can handle multiple requests concurrently.

So sidekiq will help us in running these background jobs and Redis will help us in managing these jobs.

Let's get started with the implementation.

## Installation and Setup

Please visit the [redis site](https://redis.io/docs/install/install-redis/) and follow the instructions to install Redis on your machine.

As far as Sidekiq is concerned, you can add it to your Gemfile and run `bundle install` to install it.

```ruby
gem 'sidekiq'
```

Although sidekiq is free, it also has a pro version which you can use if you need more features. You can find more information about the pro version [here](https://sidekiq.org/).

We will be using the free version where we can schedule jobs.

### API Setup

Let's create a new Rails API application.

```bash
rails new sidekiq-tutorial --api
```

Include two gems in your Gemfile.

```ruby
gem "sidekiq"
gem "sidekiq-scheduler"
```

The sidekiq gem is used for running background jobs and the sidekiq-scheduler gem is used for scheduling jobs.

Let's create a new job using the following command.

```bash
 rails generate sidekiq:job HelloWorld
```

We get the following code

```ruby
class HelloWorldJob
  include Sidekiq::Job

  def perform(*args)
  end
end
```

Here we have a job called `HelloWorldJob`. This job will be executed by Sidekiq. We can add our logic inside the `perform` method which will be executed by Sidekiq.

```ruby
  def perform(*args)
    puts 'Hello, world!'
  end
```

Now, let's schedule this job to run at regular intervals.

```ruby
class HelloWorldJob
  include Sidekiq::Job

  def perform(*args)
    puts 'Hello, world!'
  end
end
```

We can schedule the job to run at regular intervals by adding the following line to the `config/sidekiq.yml` file. Be sure to create this file.

```yaml
:scheduler:
    :schedule:
        hello_world:
            cron: '*/1 * * * *'
            class: HelloWorldJob
```

Here we are scheduling the `HelloWorldJob` to run every minute. You can change the cron expression to run the job at different intervals.

Let's break this down

```yaml
:scheduler
```

This is required to set up the scheduler. It is a top-level key in the configuration file.

```yaml
:schedule
```

This is the name of the schedule. You can have multiple schedules in the same file.

```yaml
hello_world
```

This is the name of the job. You can have multiple jobs in the same schedule.

```yaml
cron: '*/1 * * * *'
```

This is the cron expression. It is used to specify the schedule for the job. Here, we are scheduling the job to run every minute.

So, `*/1 * * * *` translates to:

-   Every 1 minute
-   Of every hour
-   Of every day of the month
-   Of every month
-   And every day of the week

This may be a little confusing at first, but you can use a cron expression generator to help you create the expression. You can find one [here](https://crontab.guru/).

Simply edit the the asterisks to get the desired schedule.

For example,

```yaml
cron: '5 4 * 1 *'
```

Means that the job will run at 04:05 in January.

Now let's preview the scheduler in action.

Make sure your Redis server is running in one terminal.

```bash
redis-server
```

Make sure your Rails server is running in another terminal.

```bash
rails s
```

Now, let's start the sidekiq server in another terminal.

```bash
bundle exec sidekiq
```

So you should have three terminals running. One for Redis, one for Rails, and one for Sidekiq.

After a few minutes you should see the following output in the sidekiq terminal.

```bash
2021-08-25T12:00:00.000Z 1 TID-ovz8z HelloWorldJob JID-1234a5678b90cdef1g23h456 INFO: start
Hello, world!
2021-08-25T12:00:00.000Z 1 TID-ovz8z HelloWorldJob JID-1234a5678b90cdef1g23h456 INFO: done: 0.001 sec
```

You can see that the `HelloWorldJob` is executed every minute.

## Sidekiq UI and Monitoring

Sidekiq provides a web-based dashboard for monitoring and managing background jobs. You can access the dashboard by visiting the `/sidekiq` path in your application.

Include the following code in your routes.rb file.

```ruby
require "sidekiq/web"

Rails.application.routes.draw do
  Sidekiq::Web.use ActionDispatch::Cookies
  Sidekiq::Web.use ActionDispatch::Session::CookieStore, key: "_interslice_session"
  mount Sidekiq::Web, at: "/sidekiq"
end
```   

Let's navigate to `http://localhost:3000/sidekiq` to see the dashboard. You can see the number of jobs that are running, the number of jobs that have failed, and the number of jobs that are scheduled to run in the future. It does take a few minutes for the jobs to appear in the dashboard and for the dashboard to update. We won't worry so much about the UI but it's good to know that it's there.

## Using Sidekiq on Deployment

Unfortunately, we aren't able to use background workers also called background jobs on Render as it is a paid service. You're welcome to explore pricing options and see if it fits your needs. 

## Conclusion

Background jobs are a powerful tool for automating tasks in a Ruby on Rails application. They allow you to offload time-consuming or resource-intensive tasks to a background process, ensuring that your application remains responsive and can handle multiple requests concurrently. In this lesson, we learned how to use Sidekiq to create a background job and schedule it to run at regular intervals. We also learned how to use Redis as a message broker for managing background jobs. I hope you found this lesson helpful. If you have any questions, feel free to ask. Happy coding!
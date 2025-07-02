---
title: Real Time Communication with Pusher
---

# Real Time Communication with Pusher

## Introduction to Real-Time Web Technologies

Real-time web technologies have transformed the way users interact with web applications by allowing them to receive information as soon as it is published. This has led to the development of real-time web applications that provide users with instant updates and notifications. It also means that users don't have to refresh the page to see new content.

In traditional web communication, the client sends a request to the server, and the server responds with the requested information. This is known as a request-response model. In order for the client to receive new or updated information, it must initiate a new request (page reload or action). This can lead to laggy and disjointed user experience. However, real-time web technologies use a different model called publish-subscribe. In this model, the server publishes information, and the client subscribes to receive updates instantly.

Real-time maintain a persistent connection between the client and the server, allowing the server to push updates to the client as soon as they are available without the need for the client to request them. The most common protocol for real-time communication is WebSockets. WebSockets provide a full-duplex communication channel over a single TCP connection. This allows for low-latency communication between the client and the server. TCP is a reliable protocol that ensures that messages are delivered in the order they were sent and that they are not lost or duplicated.

Use cases for real time features in web applications vary:

- **Chat Applications**: Real-time messaging apps allow users to send and receive messages instantly, mirroring face-to-face conversations more closely than traditional messaging services.
- **Live Notifications**: Applications like social media platforms use real-time technologies to inform users about new posts, comments, likes, or other interactions without the need for refreshing the page.
- **Real-Time Updates**: Financial trading platforms, sports scores websites, and news outlets use real-time updates to provide the latest information without delay, which is critical for users who rely on timely data.
- **Collaborative Editing**: Tools like Google Docs allow multiple users to edit documents simultaneously, with changes reflected in real-time for all participants, enhancing teamwork and productivity.
- **IoT Applications**: Internet of Things (IoT) devices often send data to servers in real-time, enabling immediate monitoring and control of home appliances, security systems, and industrial machinery.

Here are some of the pros of using real-time web technologies:

- Enhanced User Experience
- Increase Interactivity
- Improved Efficiency
- Reduced Server Load 
- Support for New Application Types

Here are some of the cons of using real-time web technologies:

- Increased Complexity
- Security Concerns
- Scalability Challenges
- Potential for Overuse: Real-time features can be overused, leading to a cluttered and overwhelming user experience.

### Understanding WebSockets

WebSockets are a protocol that provides a full-duplex communication channel over a single TCP connection. This allows for low-latency communication between the client and the server. WebSockets maintain a persistent connection between the client and the server, allowing the server to push updates to the client as soon as they are available without the need for the client to request them. This technology is a key enabler of real-time communication in web applications, allowing for instant data transfer in both directions without the need for repeatedly establishing new connections or polling the server for updates.

Once a WebSocket connection is established, the client and server can freely send data back and forth until the connection is closed. This is achieved through an initial handshake over the HTTP protocol, where the client requests an upgrade to WebSockets, and the server responds to acknowledge this upgrade. The protocol used then switches from HTTP to WebSockets (ws:// or wss:// for secure connections).

It's difficult to overstate the impact of WebSockets on the web development landscape. Before WebSockets, real-time communication was achieved using techniques like long polling, which involved the client repeatedly sending requests to the server to check for new data. This was inefficient and led to high server load and latency. WebSockets have revolutionized real-time web technologies by providing a more efficient and reliable way to maintain a persistent connection between the client and the server.

However, there are challenges implementing WebSockets, such as the need for additional server resources, potential security vulnerabilities, and the complexity of managing real-time connections. Despite these challenges, WebSockets have become a fundamental part of modern web development, enabling a wide range of real-time features and applications.

### Action Cable vs Pusher

Action Cable is a real-time communication framework for Rails applications. It provides a built-in WebSocket server and client-side JavaScript library to enable real-time features in Rails applications. Action Cable is integrated with the rest of the Rails stack, making it easy to use and well-suited for applications that are primarily built with Rails.

However, Action Cable has some limitations. It requires additional configuration and setup, and it may not be the best choice for applications that are not built entirely with Rails. Additionally, Action Cable may not be the most efficient solution for applications that require high scalability and performance. 

The reason for this is that Action Cable is designed to work with a single server, and it may not be the best choice for applications that require a distributed architecture or need to handle a large number of concurrent connections.

Therefore, another choice of action is to use Pusher, a third-party service that provides real-time communication features for web and mobile applications. Pusher offers a simple and reliable way to add real-time features to applications without the need to manage the infrastructure and complexity of WebSockets. Pusher provides a set of client libraries and server-side SDKs that make it easy to integrate real-time features into applications built with a variety of technologies, including Ruby on Rails.

We will build a small chat application using Pusher to demonstrate how to integrate real-time communication features into a Rails API and a separate front-end application.

### Getting Started 

Be sure to navigate to the [Pusher website](https://pusher.com/) and sign up for an account. It's simple to sign up and we can use the sandbox plan. Once you have signed up, you will be able to create a new app and obtain the credentials needed to integrate Pusher into your application.

Create a new Rails application using the following command:

```bash
rails new pusher_chat_app --api
```

### Integrating Pusher with Rails

Let's go ahead and add the Pusher gem to our Rails application. We will use the `pusher` gem, which provides a Ruby client for the Pusher Channels service.

Add the `pusher` gem to your `Gemfile` to include it in all environments:

```ruby
gem 'pusher'
```

Then run `bundle install` to install the gem.

Let's gather the necessary credentials from the Pusher dashboard. Once you have created a new app in the Pusher dashboard,

<img src="https://imgur.com/MoI5tIi.png" />

<img src="https://imgur.com/xKyOdWd.png" />

Here I will leave the default settings and click on the "Create my app" button. Keep in mind that if you are deploying your application, it may be wise to check the `Create apps for multiple environments` option to create separate apps for development, staging, and production environments.


Navigate to `App Keys` and you will be able to obtain the following credentials:

- `app_id`
- `key`
- `secret`
- `cluster`

<img src = "https://imgur.com/LlHAVU2.png" />

We will use these credentials to configure Pusher in our Rails API.

Let's encrypt our credentials using Rails credentials. Run the following command to edit the credentials file:

```bash
EDITOR="code --wait" bin/rails credentials:edit --environment=development
```

By Adding the `--environment=development` flag, we are specifying that we want to edit the credentials for the development environment. You can also specify other environments such as `test` or `production`. Previously we made the main `credentials.yml.enc` file for production. If you like to separate the credentials for each environment, you can do so by specifying the environment flag.

Add the Pusher credentials to the credentials file:

```yaml
pusher:
  app_id: "17536051"
  key: "6ed6as5d0c1fff140be76a"
  secret: "034a2c9c01f31f8e4064d"
  cluster: "us2"
```

Close the file to save. 

Now let's test this out, by default when we access the console, as you know it will be in the development environment. And it will decrypt the credentials for the development environment.

```ruby
  Rails.application.credentials.pusher[:app_id]
# => "17536051"
```

Awesome. 

Let's now configure Pusher in our Rails API. Create a new file called `pusher.rb` in the `config/initializers` directory:

```ruby
require 'pusher'

Pusher.app_id = Rails.application.credentials.pusher[:app_id]
Pusher.key = Rails.application.credentials.pusher[:key]
Pusher.secret = Rails.application.credentials.pusher[:secret]
Pusher.cluster = Rails.application.credentials.pusher[:cluster]
Pusher.logger = Rails.logger
```

Great we have configured Pusher in our Rails API.

Let's start using Pusher

### Using Pusher to Broadcast Messages

We will create a simple chat application where users can send and receive messages in real-time. We will use Pusher to broadcast messages to all connected clients whenever a new message is sent. We won't be using any authentication for this example, but in a real-world application, you would need to implement authentication and authorization to ensure that only authorized users can send and receive messages.

Let's start by creating a new model called `Message` to represent the chat messages. Run the following command to generate the model:

```bash
rails g model Message content:text
```

Then run the migration to create the `messages` table in the database:

```bash
rails db:migrate
```

Next, let's create a new controller called `MessagesController` to handle the creation and retrieval of messages. Run the following command to generate the controller:

```bash
rails g controller Messages
```

Open the `app/controllers/messages_controller.rb` file and add the following code to define the actions for creating and retrieving messages:

```ruby
class MessagesController < ApplicationController
  def index
    messages = Message.all
    render json: messages
  end

  def create
    message = Message.new(message_params)

    if message.save
      Pusher.trigger('chat', 'new_message', message.as_json)
      render json: message, status: :created
    else
      render json: message.errors, status: :unprocessable_entity
    end
  end

  private

  def message_params
    params.permit(:content)
  end
end
```

```ruby
  def create
    message = Message.new(message_params)

    if message.save
      Pusher.trigger('chat', 'new_message', message.as_json)
      render json: message, status: :created
    else
      render json: message.errors, status: :unprocessable_entity
    end
  end
```

```ruby
      Pusher.trigger('chat', 'new_message', message.as_json)
```

As a user creates a new message, it will fire off a new event called `new_message` to the `chat` channel. This event will be broadcasted to all connected clients, allowing them to receive the new message in real-time.

Next, let's define the routes for the messages controller. Open the `config/routes.rb` file and add the following code to define the routes:

```ruby
Rails.application.routes.draw do
  resources :messages, only: [:index, :create]
end
```

### Configuring CORS

We need to configure Cross-Origin Resource Sharing (CORS) to allow the front-end application to make requests to the Rails API. We will use the `rack-cors` gem to configure CORS in our Rails API.

Add the `rack-cors` gem to your `Gemfile`:

```ruby
gem "rack-cors"
```

Then run `bundle install` to install the gem.

Next, the file called `cors.rb` in the `config/initializers` directory add the following:

```ruby
Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins "*"

    resource "*",
      headers: :any,
      methods: [:get, :post, :put, :patch, :delete, :options, :head]
  end
end
```

Now that we have set up the Rails API to broadcast messages using Pusher, let's create a separate front-end application to consume the messages and display them in real-time.

### Front End Setup

We will be using Angular 17 to create a simple chat application that consumes the messages from the Rails API and displays them in real-time. We will use the `pusher-js` library to subscribe to the `chat` channel and receive new messages as they are broadcasted.

```bash
ng new fe-pusher-chat-app
```

For our front-end application, we need to install the [Pusher JavaScript library](https://github.com/pusher/pusher-js) to enable real-time communication with the Pusher service. The Pusher JavaScript library provides a client-side interface for subscribing to channels and receiving real-time updates.

Navigate to the `fe-pusher-chat-app` directory and install the `pusher-js` library using npm:

```bash
npm install pusher-js
```

Next, let's create a new service called `message.service.ts` to handle the communication with the Rails API and the Pusher channel. Run the following command to generate the service:

```bash
ng generate service message
```

Open the `src/app/message.service.ts` file and add the following code to define the service:

```typescript
import { Injectable } from '@angular/core';
import Pusher from 'pusher-js';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class MessageService {
  private pusher: any;
  private channel: any;

  constructor(private http: HttpClient) {
    this.pusher = new Pusher('6ed32465d0c1fff140be76a', {
      cluster: 'us2'
    });
    this.channel = this.pusher.subscribe('chat');
  }

  getMessages(): Observable<any> {
    return this.http.get('http://localhost:3000/messages');
  }

  sendMessage(message: string): Observable<any> {
    return this.http.post('http://localhost:3000/messages', { content: message });
  }

  subscribeToNewMessages(callback: (message: any) => void): void {
    this.channel.bind('new_message', callback);
  }

  unsubscribeFromNewMessages(): void {
    this.channel.unbind('new_message');
  }

}
```

Let's break this down. 

```ts
import { Injectable } from '@angular/core';
import Pusher from 'pusher-js';
.
.
.
export class MessageService {
  private pusher: any;
  private channel: any;

  constructor(private http: HttpClient) {
    this.pusher = new Pusher('6ed32465d0c1fff140be76a', {
      cluster: 'us2'
    });
    this.channel = this.pusher.subscribe('chat');
  }
```

We import the Pusher library to use it. 

In the constructor of the `MessageService` class, we create a new instance of the Pusher client and subscribe to the `chat` channel. We use the `app_id` and `cluster` credentials from the Pusher dashboard to initialize the Pusher client. The channel is the same channel that we are broadcasting the messages to from the Rails API.

```ts
  getMessages(): Observable<any> {
    return this.http.get('http://localhost:3000/messages');
  }

  sendMessage(message: string): Observable<any> {
    return this.http.post('http://localhost:3000/messages', { content: message });
  }
```

Here we defined two methods to get and send messages.

In order to setup the service to be able to make requests to our Rails API, we need to configure the app.config.ts file. This is the Angular 17 equivalent of the app.module.ts file.

```typescript 
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(routes), provideHttpClient()]
};
```

Here I am importing providedHttpClient from the @angular/common/http module and providing it in the appConfig. This will allow us to use the HttpClient module in our service.

### Adding Real-Time Features

Now that we have set up the `MessageService` to communicate with the Rails API and the Pusher channel, let's create a simple chat interface to display the messages and allow users to send new messages.

Open the `src/app/app.component.html` file and add the following code to define the chat interface:

```html
<div style="text-align:center">
  <h1>
    Welcome to Pusher Chat App
  </h1>
</div>
<div>
  @for (message of messages; track message.id) {
    <p>{{ message.content }}</p>
  }
</div>
<div>
  <input type="text" [(ngModel)]="newMessage" />
  <button (click)="sendMessage()">Send</button>
</div>
```

Open the `src/app/app.component.ts` file and add the following code to define the component logic:

```typescript
import { Component, OnInit } from '@angular/core';
import { MessageService } from './message.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  messages: any[] = [];
  newMessage: string = '';

  constructor(private messageService: MessageService) {}

  ngOnInit(): void {
    this.messageService.getMessages().subscribe((messages: any) => {
      this.messages = messages;
    });

    this.messageService.subscribeToNewMessages((message: any) => {
      this.messages.push(message);
    });
  }

  sendMessage(): void {
    this.messageService.sendMessage(this.newMessage).subscribe((message: any) => {
      this.messages.push(message);
      this.newMessage = '';
    });
  }
}
```

Great test it out yourself!

<img src="https://imgur.com/RHVwrA1.png" />

The problem we face is if the user sends a message, then the message will be added to the messages array twice. This is because we are pushing the message to the array when the user sends a message and also when the message is received from the Pusher channel. To fix this, we can check if the message already exists in the array before pushing it.

```typescript
  sendMessage(): void {
    this.messageService.sendMessage(this.newMessage).subscribe((message: any) => {
      if (!this.messages.find((m: any) => m.id === message.id)) {
        this.messages.push(message);
      }
      this.newMessage = '';
    });
  }
```

### Conclusion

Awesome! Now we have a simple chat application that allows users to send and receive messages in real-time using Pusher. This is just a basic example to demonstrate how to integrate real-time communication features into a Rails API and a separate front-end application using Pusher.
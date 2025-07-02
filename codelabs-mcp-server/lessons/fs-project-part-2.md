---
title: Full Stack Project Part 2 - Todo List
---

# Full Stack Project Part 2 - Todo List

Continuing from the previous lesson [Full Stack Project Part 1](https://www.codelabsdash.com/reading-material/backend/library/ruby-on-rails/fs-project-part-1), we will be including authentication and authorization in our application.

## Incorporating Authentication

```bash
rails generate model User username:string password_digest:string
```

```bash
rails db:migrate
```

We will be using the `has_secure_password` method to add authentication to our application. This method expects a password_digest attribute in your database (which you have) and virtual attributes password and password_confirmation for the model.

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

#### Creating Users Controller

```bash
rails g controller users
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

#### Creating Sessions Controller

Let's go ahead and add the following to our Gemfile:

```ruby
gem 'jwt'
```

```bash
bundle install
```

```bash
rails g controller sessions create
```

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

In our routes file, we need to add the following:

```ruby
Rails.application.routes.draw do
  post '/login', to: 'sessions#create'
  resources :todos
  resources :users, only: [:create]
end
```

#### Authenticating Requests

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

## Adding Auth to Front End

There's some additional work to be done on the front end to handle the authentication.

We will implement the following:

-   Login
-   Logout

Let's begin.

### Adding Login

The process of logging in will involve sending a POST request to the server with the user's credentials. If the credentials are correct, the server will respond with a token. We will store this token in local storage and use it to authenticate future requests.

Let's set up an auth service to handle the login and logout functionality.

```bash
ng g service services/authentication
```

Our service is going to need the following methods:

-   `login` - This method will send a POST request to the server with the user's credentials.
-   `setToken` - This method will store the token in local storage.
-   `getToken` - This method will retrieve the token from local storage.
-   `isLoggedIn` - This method will check if the user is logged in.
-   `logout` - This method will remove the token from local storage.

**services/authentication.service.ts**

```typescript
// authentication.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
	providedIn: 'root',
})
export class AuthenticationService {
	private readonly tokenSubject = new BehaviorSubject<string | null>(null);

	constructor(private http: HttpClient, private router: Router) {}

	login(username: string, password: string) {
		return this.http.post<{ token: string }>('http://localhost:3000/login', {
			username,
			password,
		});
	}

	setToken(token: string) {
		localStorage.setItem('token', token);
		this.tokenSubject.next(token);
	}

	getToken() {
		return localStorage.getItem('token');
	}

	isLoggedIn() {
		return !!this.getToken();
	}

	logout() {
		localStorage.removeItem('token');
		this.tokenSubject.next(null);
		this.router.navigate(['/login']);
	}
}
```

Notice the url in the `login` method. We are using the `HttpClient` to send a POST request to the server.

```typescript
  login(username: string, password: string) {
    return this.http.post<{ token: string }>('http://localhost:3000/login', {
      username,
      password,
    });
  }
```

Realistically speaking we would want to store the url in an environment variable to avoid hardcoding the url. Remember, there exist different environments such as development, production, and testing and more.

Great, let's move on to creating the login component.

```bash
ng g c login --standalone
```

Our login component is going to need the following:

-   A form with two inputs for the username and password.
-   A method to handle the form submission and call the `login` method from the `AuthenticationService`.
-   A method to handle the response from the server and store the token in local storage.

```typescript
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from '../services/authentication.service';

@Component({
	selector: 'app-login',
	standalone: true,
	imports: [FormsModule],
	templateUrl: './login.component.html',
	styleUrl: './login.component.scss',
})
export class LoginComponent {
	username: string = '';
	password: string = '';

	constructor(private authService: AuthenticationService, private router: Router) {}

	login() {
		this.authService.login(this.username, this.password).subscribe({
			next: (res: any) => {
				console.log('Logged in with token:', res.token);
				this.authService.setToken(res.token);
				this.router.navigate(['/todo-list']);
			},
			error: (error: any) => {
				console.error('Login error', error);
			},
		});
	}
}
```

**login.component.html**

```html
<!-- login.component.html -->
<form (ngSubmit)="login()">
	<input type="text" [(ngModel)]="username" name="username" placeholder="Username" required />
	<input type="password" [(ngModel)]="password" name="password" placeholder="Password" required />
	<button type="submit">Login</button>
</form>
```

Let's add the login route to our app routes to preview the login.

**app.routes.ts**

```typescript
import { Routes } from '@angular/router';

export const routes: Routes = [
	{ path: '', redirectTo: 'login', pathMatch: 'full' },
	{
		path: 'login',
		loadComponent: () => import('./login/login.component').then((m) => m.LoginComponent),
	},
];
```

Add router outlet to app.component.html to render components based on the route.

**app.component.ts**

```typescript
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
	selector: 'app-root',
	standalone: true,
	templateUrl: './app.component.html',
	styleUrl: './app.component.scss',
	imports: [RouterOutlet],
})
export class AppComponent {}
```

```html
<router-outlet />
```

Let's preview the login by navigating to the login route so we can view the login form.

**login.component.scss**

```scss
/* login.component.scss */
form {
	max-width: 400px;
	margin: 2rem auto;
	padding: 2rem;
	background-color: #f9f9f9;
	border-radius: 8px;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	display: flex;
	flex-direction: column;
	gap: 1rem;
}

input[type='text'],
input[type='password'] {
	padding: 0.75rem;
	border: 1px solid #ccc;
	border-radius: 4px;
	font-size: 1rem;
	color: #333;
	background-color: white;
	transition: border-color 0.3s;
}

input[type='text']:focus,
input[type='password']:focus {
	border-color: #007bff; /* Light blue border for focus */
	outline: none;
}

button[type='submit'] {
	padding: 0.75rem;
	border: none;
	border-radius: 4px;
	background-color: #007bff; /* Light blue background */
	color: white;
	font-size: 1rem;
	font-weight: bold;
	cursor: pointer;
	transition: background-color 0.3s;
}

button[type='submit']:hover {
	background-color: #0056b3; /* Darker blue on hover */
}
```

Great, we have our login component set up.

#### Adding Guards

Since certain routes will require the user to be logged in, we will need to create a guard to protect these routes.

```bash
ng generate guard auth
```

```bash
Which type of guard would you like to create? (Press <space> to select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)
❯◉ CanActivate
 ◯ CanActivateChild
 ◯ CanDeactivate
 ◯ CanMatch
```

Choose CanActivate and press enter.

```typescript
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthenticationService } from './services/authentication.service';

export const authGuard: CanActivateFn = (route, state) => {
	const authService = inject(AuthenticationService);
	const router = inject(Router);

	if (authService.isLoggedIn()) {
		return true;
	} else {
		router.navigate(['/login']);
		return false;
	}
};
```

Here we are using the `CanActivateFn` interface to create a guard that will check if the user is logged in. If the user is logged in, the guard will return `true` and the user will be allowed to access the route. If the user is not logged in, the guard will redirect the user to the login page and return `false`.

Let's add the guard to our routes, specifically the todo list route.

**app.routes.ts**

```typescript
import { Routes } from '@angular/router';
import { authGuard } from './auth.guard';

export const routes: Routes = [
	{ path: '', redirectTo: 'login', pathMatch: 'full' },
	{
		path: 'login',
		loadComponent: () => import('./login/login.component').then((m) => m.LoginComponent),
	},
	{
		path: 'todo-list',
		loadComponent: () => import('./todo-list/todo-list.component').then((m) => m.TodoListComponent),
		canActivate: [authGuard],
	},
];
```

### No Auth Guard

Let's add a guard for routes that should be accessible only when the user is not logged in.

```bash
ng generate guard no-auth
```

```bash
germancruz@Code-Coach-Three fe_todo_list_v2 % ng generate guard no-auth
? Which type of guard would you like to create? (Press <space> to select, <a> to toggle all, <i> to invert selection, and <enter> to proceed)
❯◉ CanActivate
 ◯ CanActivateChild
 ◯ CanDeactivate
 ◯ CanMatch
```

Choose CanActivate and press enter.

```typescript
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthenticationService } from './services/authentication.service';

export const noAuthGuard: CanActivateFn = (route, state) => {
	const authService = inject(AuthenticationService);
	const router = inject(Router);

	if (authService.isLoggedIn()) {
		router.navigate(['/todo-list']);
		return false;
	} else {
		return true;
	}
};
```

Here we are using the `CanActivateFn` interface to create a guard that will check if the user is logged in. If the user is logged in, the guard will redirect the user to the todo list page and return `false`. If the user is not logged in, the guard will return `true` and the user will be allowed to access the route.

Let's apply this guard to the login route.

**app.routes.ts**

```typescript
import { Routes } from '@angular/router';
import { authGuard } from './auth.guard';
import { noAuthGuard } from './no-auth.guard';

export const routes: Routes = [
	{ path: '', redirectTo: 'login', pathMatch: 'full' },
	{
		path: 'login',
		loadComponent: () => import('./login/login.component').then((m) => m.LoginComponent),
		canActivate: [noAuthGuard],
	},
	{
		path: 'todo-list',
		loadComponent: () => import('./todo-list/todo-list.component').then((m) => m.TodoListComponent),
		canActivate: [authGuard],
	},
];
```

Create a user in the Rails console.

```bash
rails c
```

```ruby
User.create(username: 'test', password: 'password', password_confirmation: 'password')
```

Now we should be able to login and test the guards. Be sure to have both the Rails server and the Angular server running.

Make sure there are no tokens in local storage called `token`. If there are, delete them.

-   Once logged in, try going to the login page and you should be redirected to the todo list page.

-   Be sure you are on the todo list page. Try deleting the token from local storage and refresh the page. You should be redirected to the login page.

Great! We have successfully added authentication to our application as well as protected our routes.

>**💡 Practice with the Codelabs Learning Assistant**
>
>Try this: _"Can you explain how JWT tokens work in a full stack app with Angular and Rails?"_  
>[Ask the Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

### Adding Logout

Since the token we are sending to the client is a JWT, this means that the server is not responsible for keeping track of the user's session. This means that we can simply delete the token from local storage to log the user out.

```bash
ng g c navbar --standalone
```

**navbar.component.ts**

```typescript
import { Component } from '@angular/core';
import { AuthenticationService } from '../services/authentication.service';
import { RouterLink } from '@angular/router';

@Component({
	selector: 'app-navbar',
	standalone: true,
	imports: [RouterLink],
	templateUrl: './navbar.component.html',
	styleUrl: './navbar.component.scss',
})
export class NavbarComponent {
	constructor(public authService: AuthenticationService) {}

	logout() {
		this.authService.logout();
	}
}
```

**navbar.component.html**

```html
<!-- navbar.component.html -->
<nav class="stellar-navbar">
	<div class="brand-name">
		<a routerLink="/">Todo List</a>
	</div>
	<div class="nav-links">
		@if (authService.isLoggedIn()){
		<button (click)="logout()">Logout</button>
		}@else {
		<a routerLink="/login">Login</a>
		}
	</div>
</nav>
```

**navbar.component.scss**

```scss
/* navbar.component.css */
.stellar-navbar {
	display: flex;
	justify-content: space-between;
	align-items: center;
	background-color: #007bff; /* Primary color for the navbar */
	color: white;
	padding: 0.5rem 1rem;
}

.stellar-navbar .brand-name a {
	font-size: 1.5rem;
	font-weight: bold;
	color: white; /* Keeps the brand name white */
	text-decoration: none;
}

.stellar-navbar .nav-links {
	display: flex;
	align-items: center;
	gap: 1rem; /* Adds space between navigation items */
}

.stellar-navbar .nav-links a,
.stellar-navbar .nav-links button {
	background: none;
	border: 1px solid white; /* Border makes it stand out */
	border-radius: 4px;
	color: white;
	padding: 0.5rem 1rem;
	text-decoration: none;
	font-size: 1rem;
	cursor: pointer;
	transition: background-color 0.3s, color 0.3s;
}

.stellar-navbar .nav-links a:hover,
.stellar-navbar .nav-links button:hover {
	background-color: white;
	color: #007bff; /* Inverse the color scheme on hover */
}

/* Specific style for the logout button to differentiate it, if needed */
.stellar-navbar .nav-links button {
	background-color: transparent;
	color: white;
	border-color: white;
}

.stellar-navbar .nav-links button:hover {
	color: #007bff;
	background-color: white;
	border-color: #007bff;
}
```

In `style.scss`, add the following to remove the default margin and padding from the body.

```scss
*,
html,
body {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	font-family: 'Roboto', sans-serif;
}
```

In the app component, import the navbar component and add it to the template.

```typescript
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from './navbar/navbar.component';

@Component({
	selector: 'app-root',
	standalone: true,
	templateUrl: './app.component.html',
	styleUrl: './app.component.scss',
	imports: [RouterOutlet, NavbarComponent],
})
export class AppComponent {}
```

```html
<app-navbar /> <router-outlet />
```

Let's test the logout functionality! Login and then click the logout button. You should be redirected to the login page. If you refresh the page, you should still be on the login page.

>**💡 Practice with the Codelabs Learning Assistant**
>
>Try this: _"Give me 3 practice questions about route guards in Angular and how they relate to authentication."_  
>[Ask the Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

Great! We have successfully added authentication to our application

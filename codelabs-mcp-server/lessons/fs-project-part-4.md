---
title: Full Stack Project Part 4 - Todo List
---

# Full Stack Project Part 4 - Todo List

Continuing from the previous lesson [Full Stack Project Part 2](https://www.codelabsdash.com/reading-material/backend/library/ruby-on-rails/fs-project-part-2), we will be including a sign-up process to our application.

## Signing Up A New User

We will need to create a sign-up form to allow new users to create an account.

Let's go ahead and first update our authentication service to include a method to sign up a new user.

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

  signUp(user: any) {
    return this.http.post('http://localhost:3000/users', user);
  }

  .
  .
  .
```

Next, make a sign-up component.

```bash
ng g c signup --standalone
```

**signup.component.ts**

```typescript
import { Component } from '@angular/core';
import { AuthenticationService } from '../services/authentication.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
	selector: 'app-signup',
	standalone: true,
	imports: [FormsModule],
	templateUrl: './signup.component.html',
	styleUrls: './signup.component.scss',
})
export class SignupComponent {
	user = {
		username: '',
		password: '',
		password_confirmation: '',
	};

	constructor(private authService: AuthenticationService, private router: Router) {}

	onSubmit() {
		if (this.user.password === this.user.password_confirmation) {
			this.authService.signUp(this.user).subscribe({
				next: (res: any) => {
					console.log('Sign up successful', res);
					// Redirect to login or another page
					this.router.navigate(['/login']);
				},
				error: (error: any) => {
					console.error('Sign up failed', error);
					// Handle error (e.g., show error message)
				},
			});
		} else {
			console.error('Passwords do not match');
			// Handle password mismatch (e.g., show error message)
		}
	}
}
```

```html
<!-- signup.component.html -->
<div class="signup-container">
	<h2>Sign Up</h2>
	<form (ngSubmit)="onSubmit()" #signupForm="ngForm">
		<div class="form-group">
			<label for="username">Username</label>
			<input type="text" id="username" [(ngModel)]="user.username" name="username" required />
		</div>
		<div class="form-group">
			<label for="password">Password</label>
			<input type="password" id="password" [(ngModel)]="user.password" name="password" required />
		</div>
		<div class="form-group">
			<label for="password_confirmation">Confirm Password</label>
			<input
				type="password"
				id="password_confirmation"
				[(ngModel)]="user.password_confirmation"
				name="password_confirmation"
				required
			/>
		</div>
		<button type="submit" class="btn" [disabled]="!signupForm.valid">Sign Up</button>
	</form>
</div>
```

```scss
/* signup.component.scss */
.signup-container {
	max-width: 400px;
	margin: 2rem auto;
	padding: 2rem;
	background-color: #f7f7f7;
	border-radius: 8px;
	box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-group {
	margin-bottom: 1rem;
}

.form-group label {
	display: block;
	margin-bottom: 0.5rem;
	font-weight: bold;
}

.form-group input {
	width: 100%;
	padding: 0.75rem;
	border: 1px solid #ccc;
	border-radius: 4px;
	font-size: 1rem;
	color: #333;
}

.btn {
	display: inline-block;
	background-color: #007bff;
	color: white;
	padding: 0.75rem 1.5rem;
	border: none;
	border-radius: 4px;
	cursor: pointer;
	font-size: 1rem;
	text-align: center;
	width: 100%;
	transition: background-color 0.3s ease;
}

.btn:hover {
	background-color: #0056b3;
}

/* Additional styles for error messages or validation feedback */
.error-message {
	color: #ff3860;
	margin-top: 0.5rem;
}

/* Style adjustments for better responsiveness on smaller screens */
@media (max-width: 576px) {
	.signup-container {
		padding: 1rem;
		margin: 1rem;
	}
}
```

Then, add the route for the sign-up page.

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
		path: 'signup',
		loadComponent: () => import('./signup/signup.component').then((m) => m.SignupComponent),
		canActivate: [noAuthGuard],
	},
	{
		path: 'todo-list',
		loadComponent: () => import('./todo-list/todo-list.component').then((m) => m.TodoListComponent),
		canActivate: [authGuard],
	},
];
```

Be sure to add the sign-up link to the navbar.

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
		<a routerLink="/signup">Sign Up</a>
		}
	</div>
</nav>
```

Voilà! We have successfully added a sign-up page to our application.

Test the app by signing up a new user and then logging in with the new user's credentials.

### Grabbing the User's Todos

You're probably wondering, if the user is logged in, how do we fetch the user's todos? This is a great question. The question revolves around the concept of authorization and security. We need to ensure that the user is authorized to fetch their todos. Otherwise, we could be exposing sensitive information to unauthorized users and this is a big no-no. Therefore, for certain requests, we will need to include the user's token in the request headers. This will allow the server to verify the user's identity and respond with the user's todos.

Let's allow the user to fetch their todos.

We will set this up in the back end. We will need to add a user_id column to the todos table.

```bash
rails g migration add_user_id_to_todos user:references
```

```ruby
class AddUserIdToTodos < ActiveRecord::Migration[6.1]
  def change
    add_reference :todos, :user, null: false, foreign_key: true
  end
end
```

```bash
rails db:migrate
```

You may get into an error if you have existing todos. When I created todos, I received this error:

```bash
germancruz@codecoachthree todo_list_api_3 % rails db:migrate
== 20240219185952 AddUserIdToTodos: migrating =================================
-- add_reference(:todos, :user, {:null=>false, :foreign_key=>true})
bin/rails aborted!
StandardError: An error has occurred, this and all later migrations canceled:

SQLite3::ConstraintException: NOT NULL constraint failed: todos.user_id
/Users/germancruz/Documents/todo_list_api_3/db/migrate/20240219185952_add_user_id_to_todos.rb:3:in `change'

Caused by:
ActiveRecord::NotNullViolation: SQLite3::ConstraintException: NOT NULL constraint failed: todos.user_id
/Users/germancruz/Documents/todo_list_api_3/db/migrate/20240219185952_add_user_id_to_todos.rb:3:in `change'

Caused by:
SQLite3::ConstraintException: NOT NULL constraint failed: todos.user_id
/Users/germancruz/Documents/todo_list_api_3/db/migrate/20240219185952_add_user_id_to_todos.rb:3:in `change'
Tasks: TOP => db:migrate
(See full trace by running task with --trace)
```

This is because the todos table already has todos and the user_id column is not nullable. Let's reset the database and then migrate. This is a lesson, when you add a foreign key to a table that already has data, you may run into this issue.

```bash
rails db:reset
```
This will drop the database, create the database, load the schema, and then seed the database.

```bash
rails db:migrate
```

Great!


```ruby
class Todo < ApplicationRecord
  validates :body, presence: true, length: { maximum: 255 }
  validates :is_completed, inclusion: { in: [true, false] }

  belongs_to :user

end
```

```ruby
class User < ApplicationRecord
  has_secure_password
  validates :username, presence: true

  has_many :todos
end
```

> **💡 Want to see examples of custom validation methods or error messages in Rails?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): “Show me how to write a custom validation and display a custom error message in a Rails model.”

Let's add a route to fetch the user's todos.

```ruby
Rails.application.routes.draw do
  post '/login', to: 'sessions#create'
  resources :todos
  resources :users, only: [:create]

  get '/my_todos', to: 'todos#my_todos'
end
```

In the todos controller, we will add the `my_todos` methods to fetch the user's todos.

Be sure to add the `authenticate_request` method to ensure that the user is authorized to fetch their todos. We will also do it for every other action.

```ruby
class TodosController < ApplicationController
  before_action :set_todo, only: [:show, :update, :destroy]
  before_action :authenticate_request

  .
  .
  .

  def my_todos
    todos = @current_user.todos

    render json: TodoBlueprint.render(todos, view: :normal), status: :ok
  end
```

Now that we have our back end setup, let's move to our front end.

You'll notice if we login and notice the console, we get a 401 unauthorized error when trying to fetch the user's todos. This is because we are not including the user's token in the request headers.

Before doing that, let's change the todo service to include a method to fetch the user's todos.

**app/services/todo.service.ts**

```typescript
.
.
.
  getMyTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(`http://localhost:3000/my_todos`);
  }
.
.
.
```

Then let's navigate to the todo list component and replace getTodos with getMyTodos.

**app/todo-list/todo-list.component.ts**
```typescript
  ngOnInit(): void {
    this.todoService.getMyTodos().subscribe(todos => this.todos = todos);
  }
```

Now, we need to include the user's token in the request headers.

Because most of our requests will require the user's token, we will create a interceptor to include the user's token in the request headers.

```bash
ng generate interceptor auth-token
```

```typescript
import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { AuthenticationService } from './services/authentication.service';

export const authTokenInterceptor: HttpInterceptorFn = (req, next) => {
	const authService = inject(AuthenticationService);
	const authToken = authService.getToken();

	const authReq = authToken
		? req.clone({
				headers: req.headers.set('Authorization', `Bearer ${authToken}`),
		  })
		: req;
	return next(authReq);
};
```

Here we are using the `HttpInterceptorFn` interface to create an interceptor that will include the user's token in the request headers. If the user is logged in, the interceptor will include the user's token in the request headers. If the user is not logged in, the interceptor will not include the user's token in the request headers.

Add the interceptor in the app.config.ts file.

```typescript
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideHttpClient, withInterceptors } from '@angular/common/http';
import { authTokenInterceptor } from './auth-token.interceptor';

export const appConfig: ApplicationConfig = {
	providers: [provideRouter(routes), provideHttpClient(withInterceptors([authTokenInterceptor]))],
};
```

Great, now we can fetch the user's todos. If you don't see the user's todos, that's fine. We aren't able to create a todo just yet so let's fix that.

### Create a Todo

Since we changed our todos controller to account for the authentication of a request, we need to update our `create` method.

```ruby
  def create
    todo = @current_user.todos.new(todo_params)

    if todo.save
      render json: TodoBlueprint.render(todo, view: :normal), status: :created
    else
      render json: todo.errors, status: :unprocessable_entity
    end
  end
```

Remember, when a request needs to be authenticated, we are able to decode the JWT and extract the user's id in which we have knowledge of the current user who is sending the request.

Therefore, we can do the following:

```ruby
    todo = @current_user.todos.new(todo_params)
```

Great, be sure to test the following:

-   Create a todo
-   Fetch the user's todos by refreshing the page
-   Logout then login as another user and fetch their todos and create a todo

<iframe
  frameborder="0"
  width="100%"
  height="800px"
  src="https://replit.com/@german8/todolistapiCL?embed=true">
</iframe>

## In Conclusion

We have successfully added authentication and authorization to our application. Of course there are additional features that we can add to our back end and or front end to account for things like password reset, email verification, token expiration and more. However, this is a great start.

> **💡 Want to learn more about handling authentication errors in Rails or Angular?**  
> Ask the [Codelabs Learning Assistant](https://chatgpt.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant): “What are common authentication errors in Rails and Angular, and how can I display helpful error messages to users?”

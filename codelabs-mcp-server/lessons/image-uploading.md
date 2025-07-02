---
title: Image Uploading with Cloudinary
---

# Image Uploading

**Table of Contents**

-   Introduction to Images
-   Active Storage in Ruby on Rails
-   Uploading Images with Cloudinary
-   Credentials and Storage Configuration

## Introduction to Images

Images are a crucial part of any web application. They are used to make the application more visually appealing and to provide a better user experience. In this lesson, we will learn how to upload images to a web application using Ruby on Rails.

## About Image Uploading

Allowing users to upload images enriches the user experience and opens up a wide range of possibilities for web applications. As we know, it allows users to share their own content, such as photos, videos, and other media. It also allows for more interactive and engaging features, such as profile pictures, avatars, and image galleries.

However, image uploading also comes with its own set of challenges and considerations. For example, it requires handling file uploads, processing images, and managing storage. It also requires ensuring security and performance, as well as optimizing images for web use. Another concern is bandwidth usage, as large images can slow down the application and consume more resources.

To understand image uploading, we need to understand the following concepts:

-   **File Handling:** _File Handling_ in Ruby on Rails involves working with the file system to manage files and directories. It includes reading, writing, updating, and deleting files, which is crucial when dealing with uploads. Understanding file handling is key to implementing image or file upload functionality in a Ruby on Rails application. This includes working with libraries like Active Storage for file operations and understanding paths and buffers.
-   **Image Processing:** _Image Processing_ in web applications involves receiving, modifying, and storing images. Key aspects include resizing, formatting, and optimizing images for web use. Efficient image handling ensures better performance and storage management, particularly for applications that frequently deal with image content.
-   **Active Storage:** Active Storage is a built-in library in Ruby on Rails that provides a way to upload files to a cloud storage service like Amazon S3 or Google Cloud Storage. It also provides a way to attach files to Active Record models, which makes it easy to manage file uploads in a Ruby on Rails application.
-   **Cloud Storage:** Cloud storage services like Amazon S3 and Google Cloud Storage provide a way to store and manage files in the cloud. They offer features like scalability, security, and reliability, which make them a popular choice for storing files in web applications.

### Image Optimization

Image Optimization is the process of reducing the file size of an image without significantly affecting its visual quality. This is important for web applications because it can improve performance and reduce bandwidth usage. There are several techniques for optimizing images, including compression, resizing, and format conversion.

Since image optimization contributes to faster loading time, it also improves search engine rankings. Another benefit is that it reduces the amount of storage space required for images, which can lead to cost savings.

The trade-off is that image optimization can sometimes result in a loss of visual quality, so it's important to find the right balance between file size and visual quality. This is where tools like Active Storage in Ruby on Rails come in handy, as they provide features for image optimization and resizing.

Depending on the application, it may be necessary to optimize images for different use cases, such as creating thumbnails, avatars, or images for different screen sizes. This requires understanding the different techniques for image optimization and how to apply them in a web application. If you have a web application that frequently deals with images, it's important to understand how to optimize images for web use. And for photography or image-heavy applications, image optimization is a crucial aspect of performance and user experience.

So choosing the right optimization technique and level of compression requires understanding of various image formats and their best use cases.

### Image Resizing

Image Resizing is the process of changing the dimensions of an image. This is useful for creating thumbnails, avatars, and images for different screen sizes. It's also important for optimizing images for web use, as it can reduce file size and improve performance.

Here are the pros:

-   Responsive Design
-   Bandwidth Efficiency
-   Faster Load Times
-   Storage Optimization

Some cons include:

-   May introduce additional overhead on the server
-   Complexity
-   Potentially unused data.

> **💡 Practice with the Codelabs Learning Assistant**
>
> Try this: _"Why do we need to resize images in web applications, and what problems can happen if we don't resize them?"_  
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

## Active Storage in Ruby on Rails

In Ruby on Rails, image processing can be done using the Active Storage library. Active Storage provides a way to upload images and attach them to Active Record models. It also provides features like image resizing and optimization, which makes it easy to handle images in a Ruby on Rails application.

There are several ways to process images in Ruby on Rails:

-   **Image Resizing:** Active Storage provides a way to resize images to a specific size. This is useful for creating thumbnails or other versions of an image that are optimized for different use cases. Why is this so important? Because it allows you to create different versions of an image for different use cases, which can improve performance and reduce bandwidth usage.
-   **Image Optimization:** Active Storage also provides a way to optimize images for web use. This includes compressing images to reduce file size and improve performance.
-   **Image Cropping:** Active Storage provides a way to crop images to a specific size. This is useful for creating images that are optimized for a specific aspect ratio or use case.
-   **Image Conversion:** Active Storage provides a way to convert images to different formats. This is useful for creating images that are optimized for different use cases, such as converting images to WebP format for better performance on the web.

To implement active storage, please continue from the previous lesson of [deployment](/reading-material/backend/library/ruby-on-rails/deployment). Since Active storage includes storage locally, whereas in deployment, we will use Cloudinary. So please, continue from the previous lesson.

## Adding Active Storage to a Ruby on Rails API

We will start off by running the following command to add Active Storage to our Ruby on Rails API:

```bash
rails active_storage:install
```

This will create a migration file that will add the necessary tables to the database.

This creates the following:

```ruby
# This migration comes from active_storage (originally 20170806125915)
class CreateActiveStorageTables < ActiveRecord::Migration[7.0]
  def change
    # Use Active Record's configured type for primary and foreign keys
    primary_key_type, foreign_key_type = primary_and_foreign_key_types

    create_table :active_storage_blobs, id: primary_key_type do |t|
      t.string   :key,          null: false
      t.string   :filename,     null: false
      t.string   :content_type
      t.text     :metadata
      t.string   :service_name, null: false
      t.bigint   :byte_size,    null: false
      t.string   :checksum

      if connection.supports_datetime_with_precision?
        t.datetime :created_at, precision: 6, null: false
      else
        t.datetime :created_at, null: false
      end

      t.index [ :key ], unique: true
    end

    create_table :active_storage_attachments, id: primary_key_type do |t|
      t.string     :name,     null: false
      t.references :record,   null: false, polymorphic: true, index: false, type: foreign_key_type
      t.references :blob,     null: false, type: foreign_key_type

      if connection.supports_datetime_with_precision?
        t.datetime :created_at, precision: 6, null: false
      else
        t.datetime :created_at, null: false
      end

      t.index [ :record_type, :record_id, :name, :blob_id ], name: :index_active_storage_attachments_uniqueness, unique: true
      t.foreign_key :active_storage_blobs, column: :blob_id
    end

    create_table :active_storage_variant_records, id: primary_key_type do |t|
      t.belongs_to :blob, null: false, index: false, type: foreign_key_type
      t.string :variation_digest, null: false

      t.index [ :blob_id, :variation_digest ], name: :index_active_storage_variant_records_uniqueness, unique: true
      t.foreign_key :active_storage_blobs, column: :blob_id
    end
  end

  private
    def primary_and_foreign_key_types
      config = Rails.configuration.generators
      setting = config.options[config.orm][:primary_key_type]
      primary_key_type = setting || :primary_key
      foreign_key_type = setting || :bigint
      [primary_key_type, foreign_key_type]
    end
end
```

Essentially what this migration does is create three tables: `active_storage_blobs`, `active_storage_attachments`, and `active_storage_variant_records`.

Ruby on Rails uses the `active_storage_blobs` table to store information about the files that are uploaded. The `active_storage_attachments` table is used to associate files with Active Record models. The `active_storage_variant_records` table is used to store information about image variants that are created using Active Storage.

We can then run the migration using the following command:

```bash
rails db:migrate
```

Including active storage tables means that we can now attach files to Active Record models. We can simply do this by adding the following line to the model:

```ruby
class User < ApplicationRecord
  has_one_attached :image
end
```

```ruby
has_one_attached :image
```

Here we are using the `has_one_attached` method to attach an image to the `User` model. This means that we can now upload an image and associate it with a user. Now you can attach as many images as you want to a user.

For example,

```ruby
class User < ApplicationRecord
  has_one_attached :avatar
  has_one_attached :cover_photo
  has_many_attached :images
end
```

You get the idea. Let's include a simple example of how to upload an image to a user.

```ruby
class User < ApplicationRecord
  has_one_attached :image
end
```

Let's test this out in the console by checking if the association is working.

```bash
rails c
```

```ruby
user = User.create(username: "test")
user.image.attached? # false
```

Great. Let's create a route to upload an image.

```ruby
# config/routes.rb
Rails.application.routes.draw do
  resources :users do
    post 'upload_image', to: 'users#upload_image'
  end
end
```

```ruby
  def upload_image
    user = User.find(params[:user_id])

    if user.image.attach(params[:image])
      render json: { message: "Image uploaded" }, status: :ok

    else
      render json: { message: "Image upload failed" }, status: :unprocessable_entity
    end
  end
```

Attach an image using Postman to send a POST request to `http://localhost:3000/users/1/upload_image` with the image as a form-data.

<img src="https://imgur.com/gisebCt.png" />

1. Click the `body` tab
2. Choose `form-data`
3. Add a key of `image` and change the type to `file`
4. Choose a file to upload
5. Click `Send`

If successful, you should see a response of `{"message":"Image uploaded"}`.

Now if you go to the rails console and run the following:

```bash
rails c
```

```ruby
user = User.first
user.image.attached? # true
```

Great! You have successfully uploaded an image to a user.

## Send Image URL in Response

You can also send the URL of the image in the response. This can be done by using the `rails_blob_path` helper method.

```ruby
class UsersController < ApplicationController
.
.
.
  def upload_image
    user = User.find(params[:user_id])

    if params[:image] && user.image.attach(params[:image])
      render json: { message: "Image uploaded", url: rails_blob_url(user.image, only_path: false) }, status: :ok
    else
      render json: { message: "Image upload failed" }, status: :unprocessable_entity
    end
  end
end
```

Here's an example of a response:

```json
{
	"message": "Image uploaded",
	"url": "http://localhost:3000/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6MTEsInB1ciI6ImJsb2JfaWQifX0=--d90b205184baccb59c2d5613796003bbb9d70efb/angular-logo-1200-628.png"
}
```

To test whether the image is being displayed, you can enter the URL in your browser. You should see the image you uploaded via Postman.

## Uploading Images with Cloudinary

We will use Active Storage locally, whereas in deployment, we will use Cloudinary. Cloudinary is a cloud-based image and video management service. It provides a way to upload, store, and manage images and videos in the cloud. Please [sign up](https://cloudinary.com/users/register_free) for a free account.

Once done, install the `cloudinary` gem by adding it to your `Gemfile`:

```ruby
# Gemfile
group :production do
  gem 'pg'
  gem 'cloudinary'
end
```

Then run:

```bash
bundle install
```

Next, you will need to configure the `cloudinary` gem. You can do this by adding the following to your `config/environments/production.rb` file:

**config/environments/production.rb**

```ruby
require "active_support/core_ext/integer/time"

Rails.application.configure do
  # Settings specified here will take precedence over those in config/application.rb.
.
.
.
  config.active_storage.service = :cloudinary

.
.
.
```

Replace `config.active_storage.service = :local` with `config.active_storage.service = :cloudinary`.

This will configure Active Storage to use Cloudinary as the storage service in production. In development, we will use local storage.

## Credentials and Storage Configuration

We then need to add the `cloudinary` configuration to `storage.yml`. The `storage.yml` file is used to configure the storage services that are used by Active Storage.

```yaml
test:
    service: Disk
    root: <%= Rails.root.join("tmp/storage") %>

local:
    service: Disk
    root: <%= Rails.root.join("storage") %>
```

We are going to need to add the `cloud_name`, `api_key`, and `api_secret` to the `storage.yml` file. Let's go to our Cloudinary account to get these details.

Navigate to your Cloudinary dashboard and you should see your `cloud_name`, `api_key`, and `api_secret`. Copy these details and add them to the `storage.yml` file.

<img src="https://imgur.com/hc9Wuvl.png" />

After grabbing the `cloud_name`, `api_key`, and `api_secret` from your Cloudinary account, you can add them to the `storage.yml` file.

```yaml
test:
    service: Disk
    root: <%= Rails.root.join("tmp/storage") %>

local:
    service: Disk
    root: <%= Rails.root.join("storage") %>

cloudinary:
    service: Cloudinary
    cloud_name: 'your_cloud_name'
    api_key: 'your_api_key'
    api_secret: 'your_api_secret'

```

The problem with this is that the `cloud_name`, `api_key`, and `api_secret` are exposed. To fix this, we can use the credentials file to store the `cloudinary` configuration.

The credentials file is used to store sensitive information like API keys and secrets. This is important because it allows you to keep sensitive information out of your codebase and manage it securely.

To edit the credentials file, you can run the following command:

```bash
EDITOR="code --wait" bin/rails credentials:edit
```

This will open a new file in your code editor. Windows users may run into an issue with the `EDITOR` command. If you do, you can simply run `rails credentials:edit` and then open the file manually.

The only reason we can do this is because we have a master key in our project folder. The master key is used to decrypt the `credentials.yml.enc` file.

It's important to understand that the creator of the project has to share the master key since it won't be pushed to the repository. So if you happen to clone an existing Rails project, be sure to share the master key unless there is a security reason not to share it. When I mean sharing I mean, copying and sending the master key to the person who needs it via direct messages or any other secure means.

Here we will store sensitive information like the `cloud_name`, `api_key`, and `api_secret` in the `credentials.yml.enc` file.

```yaml
# aws:
#   access_key_id: 123
#   secret_access_key: 345

cloudinary:
    cloud_name: 'djlttsuf3'
    api_key: '1165244111841913'
    api_secret: 'pJPGYiJv3fhIC1ezruSQWjbkOJjk'

# Used as the base secret for all MessageVerifiers in Rails, including the one protecting cookies.
secret_key_base: 908a3dca583e7754b741df137fb9a3b2c756c47448a349eacadfc4202c38f8682e5e3753f0dc858c22f7536e5ead6934ac5f8be3c48ca62f268a348ed409fdae
```

Make sure your cloudinary input is formatted correctly or you will get an error.

Close the file so it can be saved.

Now you can access the `cloudinary` configuration in your `storage.yml` file.

```yaml
test:
    service: Disk
    root: <%= Rails.root.join("tmp/storage") %>

local:
    service: Disk
    root: <%= Rails.root.join("storage") %>

cloudinary:
    service: Cloudinary
    cloud_name: <%= Rails.application.credentials.cloudinary[:cloud_name] %>
    api_key: <%= Rails.application.credentials.cloudinary[:api_key] %>
    api_secret: <%= Rails.application.credentials.cloudinary[:api_secret] %>
```

For us to access the values from the `credentials.yml.enc` file, we use the `Rails.application.credentials` method followed by the key and the value we want to access.

Push to the repository and let's test this out in production.

In production, be sure to have created a user before attempting to upload an image for the user. Once you have done that, you can use Postman to send a POST request to `https://your-app-name.onrender.com/users/1/upload_image
` with the image as a form-data.

<img src="https://imgur.com/qO7sc7s.png" />

Great! You have successfully uploaded an image using Cloudinary.

You can view your uploaded images in your Media Library in Cloudinary.

> **💡 Practice with the Codelabs Learning Assistant**
>
> Try this: _"How does Cloudinary work with Rails Active Storage, and what are the main benefits of using Cloudinary for image uploads?"_  
> [Ask the Codelabs Learning Assistant](https://chat.openai.com/g/g-68484cbcb348819181c3f4137b0b7c49-codelabs-learning-assistant)

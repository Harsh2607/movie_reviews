# Movie Reviews Application

## Description

The Movie Reviews Application is a web application built with Django and Django REST Framework. It allows users to register, log in, and manage movie reviews. Users can view movies fetched from The Movie Database (TMDb) API, write reviews, and get movie recommendations. The application includes features like user authentication, movie management, review management, and a recommendation system.

## Features

- User Authentication
  - Register and log in via API endpoints.
  - Only authenticated users can create, update, or delete reviews.
  - Users can log out.

- Movie Management
  - Fetch movie data using the TMDb API.
  - Store movie information such as title, description, release date, genre, and poster.
  - View movie details and list.

- Review Management
  - Users can create, read, update, and delete reviews for movies.
  - Reviews include a rating, comment, and are associated with a movie and user.

- Recommendation System
  - Provides movie recommendations based on user reviews and ratings using collaborative filtering.

- API Functionalities
  - Implement searching and filtering for movies and reviews.
  - Implement pagination for movie and review lists.

- Documentation
  - API documentation using Swagger/OpenAPI.

- Postman Testing Instructions
  - Includes a Postman collection with example requests and detailed instructions.

## Setup and Running the Project Locally

### Prerequisites

- Python 3.8 or later
- Django 3.1 or later
- Django REST Framework
- Requests library
- Django Simple JWT

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/moviereviews.git
   cd moviereviews
   ```
2. Create and activate a virtual environment:
    ```
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```
    python manage.py migrate
    ```
5. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
6. Fetch movie data using the TMDb API:
  - Add your TMDb API key to your environment variables or settings file.
  - Run the management command to fetch movie data:
    ```
    python manage.py fetch_movies
    ```
7. Run the development server:
    ```
    python manage.py runserver
    ```
8. Open your browser and navigate to http://127.0.0.1:8000.

## Example API Requests using Postman

### Register User

- Endpoint: `/auth/register/`

- Method: `POST`

- Body:
```
{
  "username": "testuser",
  "password": "testpassword",
  "email": "testuser@example.com"
}
```

### Login User

- Endpoint: `/auth/login/`

- Method: `POST`

- Body:
```
{
  "username": "testuser",
  "password": "testpassword"
}

```

### Fetch Movies

- Endpoint: `/api/movies/`

- Method: `GET`


### Add a Review

- Endpoint: `/api/reviews/`

- Method: `POST`

- Body:
```
{
  "rating": 5,
  "comment": "Great movie!",
  "movie": 1
}
```

### Update a Review

- Endpoint: `/api/reviews/<review_id>/`

- Method: `PUT`

- Body:
```
{
  "rating": 3,
  "comment": "After watching it again, I've changed my mind."
}
```

### Delete a Review

- Endpoint: `/api/reviews/<review_id>/`

- Method: `DELETE`

### Get Recommendations

- Endpoint: `/api/recommendations/`

- Method: `GET`



## Link to the Postman Collection
You can find the Postman collection [here](https://drive.google.com/file/d/1lXY6QDsPmMeY7uYezqr7H5Rr6b4C3HOi/view?usp=sharing).


## Postman Testing Instructions
- Download and install [Postman](https://www.postman.com/downloads/).
- Import the provided Postman collection.
- Use the collection to test various API endpoints.
- Follow the comments in each request for detailed instructions and required parameters.

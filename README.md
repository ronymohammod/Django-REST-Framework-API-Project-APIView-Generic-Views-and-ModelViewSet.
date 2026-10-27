Django REST Framework API Project

A Django REST Framework project demonstrating different approaches to building RESTful APIs using APIView, Generic Views, and ModelViewSet.

The project contains two Django applications:

apiclass_app — Blog CRUD API using APIView.
generic_viewset_app — Blog APIs using Generic Views and Course CRUD APIs using ModelViewSet.

The project also includes models and serializers for course categories and subjects.

Features
Blog CRUD operations using APIView
List and retrieve operations using Generic Views
Retrieve and update operations using RetrieveUpdateAPIView
Automatic CRUD endpoints using ModelViewSet
Model serialization with ModelSerializer
JSON request and response handling
URL routing with Django REST Framework routers
Database integration using Django ORM
Technologies Used
Python
Django
Django REST Framework
SQLite (default Django database)
REST API
JSON
Project Structure
text
django-api-project/
│
├── manage.py
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apiclass_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── generic_viewset_app/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── README.md


Note: project_name represents your actual Django project package. Your exact folder structure may differ.

Installation and Setup
1. Clone the repository
bash
git clone <your-repository-url>
cd <your-project-directory>


Replace the placeholders with your actual repository URL and project directory.

2. Create a virtual environment
bash
python -m venv venv


Activate the virtual environment.

Windows:

bash
venv\Scripts\activate


Linux / macOS:

bash
source venv/bin/activate

3. Install dependencies
bash
pip install django djangorestframework

4. Configure installed apps

Add both applications and Django REST Framework to INSTALLED_APPS in settings.py.

python
INSTALLED_APPS = [
    # Default Django apps
    'rest_framework',
    'apiclass_app',
    'generic_viewset_app',
]


Make sure the app names match your actual Django application directories.

5. Run migrations
bash
python manage.py makemigrations
python manage.py migrate

6. Start the server
bash
python manage.py runserver


The development server will be available at:

http://127.0.0.1:8000/

Application 1: apiclass_app

This application implements Blog CRUD operations using Django REST Framework's APIView.

Blog Model

The BlogModel contains the following fields:

Field	Description
id	Automatically generated primary key
blog_title	Title of the blog
content	Blog content
author	Author's name
category	Blog category
API Endpoints

Assuming the app is included under the /api/ prefix and its URL patterns are configured accordingly:

HTTP Method	Endpoint	Description
GET	/api/blogs/	Retrieve all blogs
POST	/api/blogs/	Create a new blog
GET	/api/blogs/<id>/	Retrieve a blog by ID
PUT	/api/blogs/<id>/	Update a blog
DELETE	/api/blogs/<id>/	Delete a blog

The paths above are illustrative. Configure your actual URL patterns to match these endpoints.

Example: Create a Blog

POST request body:

json
{
    "blog_title": "Django REST Framework",
    "content": "Learning API development",
    "author": "Rahim",
    "category": "Programming"
}

Example: Successful Response
json
{
    "success": true,
    "message": "Blog Created Successfully",
    "data": {
        "id": 1,
        "blog_title": "Django REST Framework",
        "content": "Learning API development",
        "author": "Rahim",
        "category": "Programming"
    }
}


The exact response depends on the response structure implemented in your view.

Application 2: generic_viewset_app

This application demonstrates Django REST Framework Generic Views and ModelViewSet.

1. BlogListAPI
python
class BlogListAPI(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


Purpose: Retrieves a list of all blog posts.

Method	Operation
GET	List all blogs
2. BlogGetAPI
python
class BlogGetAPI(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


Purpose: Retrieves a single blog post using its primary key.

3. BlogIndividual
python
class BlogIndividual(generics.RetrieveUpdateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer


Purpose: Retrieves and updates an individual blog post.

Supported methods:

GET — Retrieve a blog
PUT — Update a blog
PATCH — Partially update a blog
Generic Blog API Endpoints

Based on the supplied urls.py:

HTTP Method	Endpoint	Description
GET	/generic-blog-list/	Retrieve all blogs
GET	/generic-blog-get/<pk>/	Retrieve a blog by primary key
GET	/all/<pk>/	Retrieve an individual blog
PUT	/all/<pk>/	Update an individual blog
PATCH	/all/<pk>/	Partially update a blog

These routes assume the app's URL configuration is included at the root URL path.

Course API Using ModelViewSet

The project uses ModelViewSet to provide standard CRUD functionality for courses.

python
class CourseViewSet(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


Unlike individual Generic Views, ModelViewSet provides multiple actions through a single class.

Course Model
Field	Description
id	Automatically generated primary key
course_title	Course title
description	Course description
course_fee	Course fee
admission_date	Admission date
Course API Endpoints

The DefaultRouter registers the CourseViewSet using the prefix course.

HTTP Method	Endpoint	Description
GET	/course/	List all courses
POST	/course/	Create a course
GET	/course/<pk>/	Retrieve a course
PUT	/course/<pk>/	Update a course
PATCH	/course/<pk>/	Partially update a course
DELETE	/course/<pk>/	Delete a course
Example: Create a Course

POST request body:

json
{
    "course_title": "Python Programming",
    "description": "Learn Python from basics",
    "course_fee": 5000.0,
    "admission_date": "2026-11-15"
}


The admission_date must use the YYYY-MM-DD format.

Example: Course Response
json
{
    "id": 1,
    "course_title": "Python Programming",
    "description": "Learn Python from basics",
    "course_fee": 5000.0,
    "admission_date": "2026-11-15"
}


The response structure depends on your serializer fields and database records.

Additional Models and Serializers

The generic_viewset_app also defines models and serializers for course categories and subjects.

CourseCategoryModel
Field	Description
id	Automatically generated primary key
category_name	Category name
description	Category description
SubjectModel
Field	Description
id	Automatically generated primary key
cname	Subject name
category	Category value
description	Subject description
teacher_name	Teacher's name
credit	Credit value

The project defines CourseCategorySerializer and SubjectSerializer for these models. Their API endpoints must be configured separately if you want to expose them through HTTP.

Understanding Serializers

The project uses ModelSerializer to convert Django model instances into JSON-compatible data and validate incoming request data.

Example:

python
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'

ModelSerializer automatically generates fields from the model.
model specifies which model to serialize.
fields = '__all__' includes all model fields.
Testing the APIs

You can test the API endpoints using:

Postman
Insomnia
cURL
Django REST Framework's browsable API

For POST, PUT, and PATCH requests, select JSON as the request body format and set the Content-Type header to application/json.

Key Differences: APIView vs Generic Views vs ModelViewSet
Feature	APIView	Generic Views	ModelViewSet
Customization	High	Moderate	High
Built-in CRUD actions	Must implement manually	Provides specific actions	Provides standard CRUD actions
Code required	More	Less	Less
Routing	Manually configured	Manually configured	Can use a router
Best suited for	Custom API logic	Standard individual operations	Full CRUD APIs
Future Improvements
Add authentication and permission classes
Add pagination and search functionality
Add filtering and ordering
Implement automated API tests
Improve validation and error handling
Add category and subject endpoints
Add API documentation using Swagger or OpenAPI
Use environment variables for production settings
License

This project is intended for educational and learning purposes. Add an appropriate license before distributing it publicly.

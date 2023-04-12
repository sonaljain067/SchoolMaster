# SchoolMaster

It's a web based APIs designed to manage school, students and administration. It provide set of RESTful APIs for creating, managing and updating data for administrators, schools, students. 

## Installation:
#### 1. Clone the repository
`git clone https://github.com/sonaljain067/SchoolMaster.git
`

#### 2. Create a virtual environment
`cd SchoolMaster` <br/>
`python3 -m venv env` or `virtualenv env` 
to create virtual environment named `env`

#### 3. Activate the virtual environment
In Ubuntu: `source env/bin/activate` <br/>
In Windows: `.\env\Scripts\activate`

#### 4. Install dependencies
`pip install -r requirements.txt`

#### 5. Setup database 
`python manage.py migrate`

#### 6. Run the server
`python manage.py runserver`

## Authentication 
Authentication of APIs is done using JSON Web Token(JWT). To obtain token for active & valid user, send a post request ot `/api/token/` with valid email and password. The access and refresh token will be returned in the response.

To authenticate & use the APIs, add the token to the `Authorization` header as:

`Authorization: Bearer <access_token>`

## Permissions 
The SchoolMaster has three types of users i.e administators, schools and students.

- Administators can read & filter the data of all schools and students in the database
- Schools can create, update and read their own data(i.e the data associated with the particular school)
- Students can read and update their data but cannot create their data.

## API Endpoints:
`GET api/school/list` - Admin view to get lists of school <br/>
`GET api/school-student/list` - Admin view to get lists of students with school and can filter by grade & school <br/>
`POST api/grade/create` - Admin can create grades to be used by school / student  <br/>
`POST api/school/create` - School view to register themselves  <br/>
`POST api/school/student/create` - School view to add their student details <br/>
`GET api/school/student/list` - School view to list their institute students only <br/>
`PATCH api/student/update/<int:id>` - School / Student view to update particular student's information <br/>
`POST api/token` - JWT inbuilt method to create auth token for active users (Admin / School / Student) <br/>
`POST api/token/refresh` - JWT inbuilt method for refresh token for active users (Admin / School / Student) <br/>


## API Documentation
The SchoolMaster API is documented using Postman. You can import the [Postman Collection](https://elements.getpostman.com/redirect?entityId=17433654-df143c25-3c41-4f6f-a35e-29403f08dce1&entityType=collection) to get started.

### user-service

## Clone the following repo on your local
```bash
git clone https://github.com/itsanand/user-service.git
git clone https://github.com/itsanand/user-interaction-service.git
git clone https://github.com/itsanand/content-service.git
```

## From user-service folder run the below command 
```bash
docker-compose build
docker-compose up

or

docker-compose up --build
```

### Swagger Docs can be accessed for each service from below urls
```bash
http://localhost:7000/docs
http://localhost:8000/docs
http://localhost:7000/docs
```

![](user_service\static\service_design.png)

## User-service Database

```py
class User:
    """User model"""

    __tablename__ = "User"
    id: Column = Column(String, primary_key=True) # auto generated id
    firstName: Column = Column(String)
    lastName: Column = Column(String)
    phoneNumber: Column = Column(String, unique=True)
    emailID: Column = Column(String, unique=True)
```

## User-Interaction-service Database

```py
class Interaction:
    """User model"""

    __tablename__ = "Interaction"
    userID: Column = Column(String)
    contentTitle: Column = Column(String)
    operationType: Column = Column(Enum(OperationType))

    __table_args__ = (PrimaryKeyConstraint("userID", "contentTitle", "operationType"),)
```

## Content-service Database

```py
class Content:
    """Content model"""

    __tablename__ = "Content"
    title: Column = Column(String, primary_key=True)
    story: Column = Column(String)
    publishedDate: Column = Column(DateTime)
```


# User Service - Low-Level Design

## UserService Class

The `UserService` class provides asynchronous methods for handling user-related operations in the database using Starlette.

### Methods

#### `create_user_service(payload: dict[str, str]) -> dict[str, str]`

Creates a new user entity, generates a unique ID, and stores the record in the `User` table.

- Input:
  - `payload`: A dictionary containing user details.
- Output:
  - Returns the created user payload.

#### `update_user_service(payload: dict[str, str]) -> dict[str, str]`

Updates user details in the database.

- Input:
  - `payload`: A dictionary containing updated user details.
- Output:
  - Returns the updated user payload.

#### `read_user_service(user_id: str) -> dict[str, str]`

Retrieves user details based on the user ID.

- Input:
  - `user_id`: ID of the user to fetch.
- Output:
  - Returns a dictionary containing user details.

#### `delete_user_service(user_id: str) -> None`

Deletes a user record from the database.

- Input:
  - `user_id`: ID of the user to delete.

## Starlette Endpoints

The Starlette application exposes the following endpoints for user-related operations:

- `POST /user`: Creates a new user.
- `PATCH /user/{id}`: Updates user details.
- `GET /user/{id}`: Retrieves user details.
- `DELETE /user/{id}`: Deletes a user.

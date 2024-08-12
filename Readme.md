# FastAPI Library System

## Overview

This is a simple CRUD application built using FastAPI and PostgreSQL. The application manages a basic library system with two primary entities:

- **Author**: Represents authors of books.
- **Book**: Represents books in the library, each associated with an author.

## Features

- Create, read, update, and delete authors and books.
- Demonstrates relationships between authors and books using foreign keys.
- API documentation available via FastAPI's interactive Swagger UI.

## Requirements

- Python 3.8 or higher
- PostgreSQL

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/avnisharma31/library_crud.git
    cd library_crud
    ```

2. **Set Up the Virtual Environment**

    ```bash
    python -m venv venv
    source venv/Scripts/activate  
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL**

    Ensure PostgreSQL is installed and running. Create a database and update the connection URL in `database.py`:

    ```python
    # database.py
    SQLALCHEMY_DATABASE_URL = "postgresql://username:password@localhost/library_db"
    ```

    Replace `username`, `password`, and `library_db` with your PostgreSQL credentials and desired database name.

5. **Create the Database Tables**

    Run the following command to create the necessary database tables:

    ```bash
    python -c "from models import Base; from database import engine; Base.metadata.create_all(bind=engine)"
    ```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload

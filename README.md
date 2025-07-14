# music_application

Music Application (GraphQL API)

Description:
A lightweight GraphQL API built with Flask, Ariadne, and SQLAlchemy for managing music data (songs, artists). Provides structured querying via GraphQL with a focus on flexibility and typed responses.

Key Features:

GraphQL Schema: Predefined types (Song, Artist) and queries (e.g., getSongs).

SQLAlchemy ORM: PostgreSQL integration for data storage.

Minimalist Flask Server: Single /graphql endpoint for all operations.

Tech Stack:

Backend: Python (Flask)

GraphQL: Ariadne (schema-first)

Database: SQLAlchemy (SQLite/PostgreSQL)

Example Query:

graphql
query {
  getSongs {
    title
    artist { name }
  }
}

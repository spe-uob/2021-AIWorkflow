# 1. AI Workflow Database Documentation

---

## 1.1. Table of Contents

- [1. AI Workflow Database Documentation](#1-ai-workflow-database-documentation)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. Database Schema](#12-database-schema)
  - [1.3. Accessing the Database Manually](#13-accessing-the-database-manually)
  - [1.4. Accessing through backend](#14-accessing-through-backend)

---

## 1.2. Database Schema

![database_schema_diagam](db_diagram.png)

---

## 1.3. Accessing the Database Manually

To access the database after deploying:

1. Install [mongosh][https://www.mongodb.com/docs/mongodb-shell/]
2. access the database:

```sh
mongosh "mongodb://<DATABASE_IP>:<PORT>/db"
```

---

## 1.4. Accessing through backend

Consult the backend documentation for more information.

If deployed, you can also check the docs directly on the `/docs` endpoint of your backend

---
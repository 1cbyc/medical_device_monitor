Setting Up the Database

We'd use PostgreSQL, so let me show you how  to set up the database:

**1. Install PostgreSQL**

Download and install PostgreSQL from the [official website](https://www.postgresql.org/download/). Follow the installation instructions specific to your operating system.


**2. Create a Database and User**

* Open the PostgreSQL command line interface (psql) and create a new database and user.

```bash
psql -U postgres
```
* Create a new database and user:

```sql
CREATE DATABASE medical_device_db;
CREATE USER medical_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE medical_device_db TO medical_user;
```

**3. Update the .env File:**

you should your .env file with the correct database connection details:

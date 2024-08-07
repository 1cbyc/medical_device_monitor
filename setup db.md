# Time to Setup the Database

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

```plaintext
DB_NAME=medical_device_db
DB_USER=medical_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

**4. Create Tables and Insert Sample Data**

Create the necessary tables and insert sample data. You can do this by connecting to the database using a tool like pgAdmin or through the command line.

```sql
CREATE TABLE your_table (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    heart_rate INTEGER,
    device_id INTEGER,
    status VARCHAR(50)
);

INSERT INTO your_table (timestamp, heart_rate, device_id, status) VALUES
('2024-01-01 00:00:00', 70, 1, 'active'),
('2024-01-01 01:00:00', 75, 1, 'active'),
('2024-01-01 02:00:00', 72, 1, 'active');
```



# For testing Purposes

I decided to use SQLAlchemy. Which meant I'd install in the code and run:

**1. You should install SQLAlchemy and Flask-SQLAlchemy**

If you have downloaded the SQLAlchemy WHL file, you can install it using pip:

```bash
pip install c:/1cbyc/sqlalchemy.whl
```
Also, install Flask-SQLAlchemy:

```bash
pip install Flask-SQLAlchemy
```

**2. Configure SQLAlchemy in Your Flask Application**

start by updating your `.env` file to include the database URL for SQLAlchemy:

```plaintext
SQLALCHEMY_DATABASE_URI=postgresql://medical_user:your_password@localhost:5432/medical_device_db
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

3. I updated the init script to introduce SQLALchemy
4. I also created a new models.py file in my app dir to define the db models
5. Ofcourse, i had to adjust the routes.py file to use sqlalchemy too

ps: i used pgadmin cause i was already tired of writing commands o

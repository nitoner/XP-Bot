CREATE TABLE users (
    user_id    INTEGER PRIMARY KEY,
    name        VARCHAR(30),
    exp         INTEGER,
    FOREIGN KEY(role_id) REFERENCES roles(role_id)
 );

CREATE TABLE roles (
    role_id    INTEGER PRIMARY KEY,
    range       VARCHAR(10)
);

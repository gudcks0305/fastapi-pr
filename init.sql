USE todos;

-- User Table
CREATE TABLE IF NOT EXISTS user
(
    id       INT          NOT NULL AUTO_INCREMENT,
    username VARCHAR(256) NOT NULL,
    password VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Todo Table with user_id as a foreign key referencing user(id)
CREATE TABLE IF NOT EXISTS todo
(
    id       INT          NOT NULL AUTO_INCREMENT,
    user_id  INT,
    contents VARCHAR(256) NOT NULL,
    is_done  BOOLEAN      NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES user (id)
);


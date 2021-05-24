DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS comment;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usertype boolean,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE question (
  questionID INTEGER PRIMARY KEY AUTOINCREMENT,
  heading TEXT NOT NULL,
  body TEXT NOT NULL,
  username TEXT UNIQUE NOT NULL,
  FOREIGN KEY (username) REFERENCES user(username)
);

CREATE TABLE comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  questionID INTEGER,
  username TEXT,
  content TEXT,
  isSublayer boolean,
  layer INTEGER,
  FOREIGN KEY (questionID) REFERENCES question(questionID),
  FOREIGN KEY (username) REFERENCES user(username)
);

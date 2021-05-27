DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS comment;
DROP TABLE IF EXISTS code;
DROP TABLE IF EXISTS interview;

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
  username TEXT NOT NULL,  --面试官
  answer TEXT NOT NULL,
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

CREATE TABLE code(
    questionID INTEGER,
    username TEXT,  --面试者
    code TEXT,
    result INTEGER,  --0：未批改 1：AC 2：WA
    FOREIGN KEY (questionID) REFERENCES question(questionID),
    FOREIGN KEY (username) REFERENCES user(username)
);

CREATE TABLE interview(
    sessionID INTEGER,
    username TEXT, 	--面试官
    applicant TEXT, 	--面试者数组
    questionNumber INTEGER,
    questionID TEXT,	--面试题ID数组
    createWay boolean,  --true：自主命题；false：系统抽题
    status boolean,  --面试者参加面试状态 true：已参加；false：未参加
    FOREIGN KEY (questionID) REFERENCES question(questionID),
    FOREIGN KEY (username) REFERENCES user(username),
    FOREIGN KEY (applicant) REFERENCES user(username)
)

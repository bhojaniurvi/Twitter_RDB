-- DS4300: Homework 1
-- Urvi Bhojani, Rishita Shroff
-- Create Database for two relational databases

DROP DATABASE IF EXISTS twitter_engineering;
CREATE DATABASE twitter_engineering;

USE twitter_engineering;

CREATE TABLE TWEET (
  tweet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  tweet_ts DATETIME NOT NULL,
  tweet_text VARCHAR(140) NOT NULL
);

CREATE TABLE FOLLOW (
	user_id INT NOT NULL,
    follows_id INT NOT NULL
);

DELIMITER //
CREATE PROCEDURE createTweet (IN tweet_id_p INT, IN user_id_p INT, IN tweet_ts_p DATETIME, IN tweet_text_p VARCHAR(140))
BEGIN
  INSERT INTO TWEET (tweet_id, user_id, tweet_ts, tweet_text)
  VALUES (tweet_id_p, user_id_p, tweet_ts_p, tweet_text_p);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE readFollowing()
BEGIN
	SELECT * FROM FOLLOW;
END//

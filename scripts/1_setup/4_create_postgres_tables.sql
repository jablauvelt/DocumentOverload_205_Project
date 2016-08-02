---
CREATE DATABASE finalproject;
---
--- text_email_parser.py --------------------------------------------------------
---
CREATE TABLE email_from       (filename   TEXT,
                               email_from TEXT);
---
CREATE TABLE email_to         (filename TEXT,
                               email_to TEXT);
---
CREATE TABLE email_cc         (filename TEXT,
                               email_cc TEXT);
---
CREATE TABLE email_subject    (filename TEXT,
                               email_subject TEXT);
---
CREATE TABLE email_date       (filename TEXT,
                               email_date TEXT);
---
CREATE TABLE email_sdoc       (filename TEXT,
                               email_sdoc TEXT);
---
CREATE TABLE email_zlid       (filename TEXT,
                               email_zlid TEXT);
---
CREATE TABLE email_body       (filename TEXT,
                               email_body TEXT);
---
--- zipcode_phone.py & zipcode_long_lat.py(Python 2.7 required/virtual) ---------
---
CREATE TABLE zipcode_filename (filename TEXT,
                               zipcode TEXT,
                               address TEXT,
                               longitude TEXT,
                               latitude TEXT);
CREATE INDEX zf_update_go_fast ON zipcode_filename (zipcode);
---
CREATE TABLE phone_filename   (filename TEXT,
                               phone TEXT);
---
--- wordcount.py & wordcount_textfile_combine.py --------------------------------
---
CREATE TABLE word_count       (word TEXT,
                               count int);
---
--- machine_learning.py & machine_learning.json --------------------------------
---
CREATE TABLE machine_learning (filename TEXT,
                               probability_positive DECIMAL(17,15),
                               probability_negative DECIMAL(17,15),
                               conclusion TEXT);
---
--- enron_email_rank.py --------------------------------
---
CREATE TABLE email_rank (email TEXT,
                         rank TEXT);
---
---------------------------------------------------------------------------------
---

# MyPSE.ie (My Passport for Special Education)

## Overview

MyPSE.ie is a full stack web application, designed to support pupils with special educational needs (SEN), during educational transitions.  

<img src="../docs/readme_images/mockup_placeholder.png">

<br>

For SEN pupils, parents and school staff, periods of transition between learning environments can be extremely challenging.

The National Council for Special Education (NCSE) recommends that during these periods, SEN pupils carry with them a document that will allow new teachers and support workers access to vital information about ther care needs, learning supports, communication difficulties and more.  

Commonly reffered to as 'passports' within the Irish education system. These documents can make an immesurable difference into understanding and providing care for SEN pupils during periods of transition.

MyPSE.ie allows authenticated and authorised pupils and parents to design, view and update passports reflecting not only each individual pupil's special educational needs, but also a nuanced overview of their personality and style. Teachers can then view the passports that have been assigned to them by entering their unique registration number issued by the Irish Teaching Council.

Because of the highly personal and sensitive nature of the data stored within the site, protection of this data is paramount which is why MyPSE will only allow passports to be created for pupils who have been added to a separate database table by their school administration.

Utilising the power of coding frameworks like Django and Bootstrap, MyPSE.ie has been rapidly and thoughtfully designed to 
provide users with an enjoyable and meaningful experience as they securely access, create and organise SEN passports.

<br>

[Live project:](https://mypse.herokuapp.com/)

<br>


# Planning & Research

## User Experience Design
<br>


### User Stories
<br>

#### __General User Stories__
<br>

* As a User, I would like the app to be intuitive and easy to navigate in order to access information efficiently.

* As a User I want to be Informed when I have submitted a task or action within the app so I can be confident it has been successfully completed.

* As a User I want the app to be easy to read, consistent in design and pleasing to the eye so I will have a positive user experience.

* As a User I would like to access an About page in order to learn more about myPSE.ie

<br>

#### __User Stories__: *Site Owner*
<br>


* As a Site Owner, I would like to prevent the ability to create a passport unless a pupils details have been registered by their school in order to prevent misuse of the site.

* As a Site Owner, I would like to limit the number of passports to one passport per pupil in order to prevent misuse of the site and prevent misidentification of the pupil.

* As a Site Owner, I would like to restrict access to passports to authorised and authenticated users only in order to protect pupil data. 

* As a Site Owner, I would like to restrict access to passports based on user role in order to protect pupil data.

* As a Site Owner I would like to automate the transfer of passport teacher permissions in order to protect user data.

* As a Site Owner I would like to automatically delete passports when pupil is no longer enrolled in school in order to protect user data.

<br>

#### __User Stories__: *Role -- School Admin*
<br>

* As a School Administrator, I would like to create pupil records in order to facilitate the use of myPSE.ie  passports.

* As a School Administrator, I would like to securely login and out of the application in order to prevent unauthorised access to pupil information. 

* As a School Administrator, I would like to view a list of Enrolled Pupils in order to maintain a record of pupils who can benefit from myPSE.ie.

* As a School Administrator, I would like to update and delete pupil details in order to maintain accurate records.

<br>

#### __User Stories__: *Role -- Parent*
<br>

* As a Parent, I would like to create a ‘passport’ for my SEN child to support them during educational transitions.

* As a Parent, I would like to securely login and out of the application in order to prevent unauthorised access to my child’s data.

* As a Parent, I would like to view a list created passports in order to keep track of and access them. 

* As a Parent, I would like to select, edit and delete any Passports I have created in order to maintain accurate data, as well as protect my child’s data.

* As a Parent I would like the User Experience of myPSE.ie to be intuitive and illicit a positive emotional response in order to encourage repeat visits to the app.

* As a Parent, I would like to customise my child’s passport to reflect their personality and tastes in order to provide a more accurate profile of my child. 

* As a Parent, I would like the option to print a ‘printer friendly’ version of my child’s passport in order to provide people outwith the education system with information that will help during a non-educational transition. (Respite facilities, youth clubs, sports teams etc.)

<br>

#### __User Stories__: *Role -- SEN Pupil*
<br>

* As an SEN Pupil I would like to create a passport to help others understand my needs, personality, tastes and abilities so they are better informed and equipped to assist me as I transition between Special Educational environments.

* As an SEN Pupil, I would like to securely login and out of the application in order to prevent unauthorised access to my data.

* As an SEN Pupil, I would like the User Experience of myPSE.ie to be intuitive and illicit a positive emotional response in order to encourage repeat visits to the app.

* As an SEN Pupil, I would like to view and edit my passport in order to maintain accurate data across time.

* As an SEN Pupil, I would like myPSE.ie to provide me with the ability to delete my own Passport as is my right.

* As an SEN Pupil, I would like  to customise my passport to reflect my personality and tastes in order to help people understand me.

* As an SEN Pupil, I would like the option to print a ‘printer friendly’ version of my passport in order to provide people outwith the education system with information that will help during a non-educational transition. (Respite facilities, youth clubs, sports teams etc.)

<br>

#### __User Stories__: *Role -- Teacher*
<br>


* As an Teacher, I would like to securely login and out of the application in order to prevent unauthorised access to pupil data.

* As a Teacher, I would like to view the passports of children transitioning into my class in order to prepare supports, staff and educational resources to better facilitate their transition.

* As a Teacher, I would like to print a ‘printer friendly’ version of a passport in order to provide an easy reference chart for both staff & pupils during the transitional period.

* As a Teacher, I would like to upload pictures to a gallery section of a pupils passport in order to provide examples of classroom activities. 

* As a Teacher, I would like the ability to comment on pictures in the gallery in order to provide further feedback to pupils, parents and future teachers.


<br>

# Deployment

## Deployment errors and issues

### Security Key.

Whilst setting up the development environment for this project I made the error of accidentally pushing to Github (ergo exposing) the SECURITY_KEY variable within the settings.py file. This variable was part of the code institute's student project template which I used in order to expidiate the initial setup phase of project. I imediately changed this variable and concealed it within the env.py file which was then subsequently added to .gitignore. The CI's variable was never at any point used as a functioning key during the development or deployment of the app.  


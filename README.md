# Corruption search web service

## Solution Description
### Task
This repository is analogous to "https://github.com/LevProg/ai-corruption" except for the solution presentation. If in the first repository the solution is presented as a Desktop application, then in this one the Web application.

The basic concept is the same: analyze the file for the presence of corruption factors and highlight the paragraph in which there is a high probability of the presence of a corruption factor.

To write it, was used framework Django. The architecture was built using the standard Django MVC pattern.

### Solution implementation
To write it, was used framework Django. The architecture was built using the standard Django MVC pattern.

There are only two views in the project: login to the account and the main page with a list of all available files + the ability to upload new ones.

![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/files.png?raw=true) 

![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/login.png?raw=true)

SQLite was used as a DBMS.
The project has a standard Django user database and a database of uploaded files, database link: one-to-many.
Each user can view and delete only files uploaded by him.

All files are stored on the server:

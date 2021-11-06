# Corruption search web service

## Solution Description
### Task
This repository is analogous to "https://github.com/LevProg/ai-corruption" except for the solution presentation. If in the first repository the solution is presented as a Desktop application, then in this one the Web application.

The basic concept is the same: analyze the file for the presence of corruption factors and highlight the paragraph in which there is a high probability of the presence of a corruption factor.

### Solution implementation
To write it, was used framework Django. The architecture was built using the standard Django MVT pattern.

There are only two views in the project: 

1)Account login view

![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/login.png?raw=true)

2)Main page with a list of all available files + the ability to upload new ones.

![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/files.png?raw=true)

Description of the web application:

User sent the file => The Server processed it => If the format (.docx) is correct, the Server predicts the presence of corruptogenic factors and highlights them in the text => Server saves the modified file => User can download the modified file to his device and delete the file

### More about database
SQLite was used as a DBMS in the project.
The project has a standard Django user database and a database of uploaded files, database link: one-to-many.
Each user can view and delete only files uploaded by him.

All files are stored on the server as /media/USER/FILENAME
 
Example:
![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/media_files.png?raw=true)

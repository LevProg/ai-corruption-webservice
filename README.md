# Corruption search web service

## Solution Description
### Task
The task of this repository is similar to my [other](https://github.com/LevProg/ai-corruption). Only in the first repository the solution is presented as a desktop application, and in this one it is a web application.

The basic concept is the same: analyze the file for the presence of corruption factors and highlight the paragraph in which there is a high probability of the presence of a corruption factor.

### Solution implementation
To write it, was used framework Django. The architecture was built using the standard Django MVT pattern.


User sent the file => The Server processed it => If the format (.docx) is correct, the Server predicts the presence of corruptogenic factors and highlights them in the text => Server saves the modified file => User can download the modified file to his device and delete the file

There are only two views in the project: 

+ Account login view
+ Main page with a list of all available files + the ability to upload new ones.

All screenshots of the implementation are in the corresponding project folder

Description of the web application:

### More about database
SQLite was used as a DBMS in the project.
The project has a standard Django user database and a database of uploaded files, database link: one-to-many.
Each user can view and delete only files uploaded by him.

All files are stored on the server as /media/USER/FILENAME
 
Example:

![](https://github.com/LevProg/ai-corruption-webservice/blob/master/Scrins/media_files.png?raw=true)

## Model
An ensemble of more than 10 neural networks was used as an artificial intelligence model, each for recognizing its own corruption-generating factor.

Model training script: https://github.com/LevProg/ai-corruption/blob/master/research.ipynb
## Server start
First you need to change the current directory to the project directory
```cmd
    cd project_path
```
Next, we activate the virtual environment
```cmd
    env\Scripts\activate.bat
```
And at the end we start the server
```cmd
    python manage.py runserver
```

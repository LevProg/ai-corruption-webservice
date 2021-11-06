# ai-corruption-webservice
## This repository is analogous to "https://github.com/LevProg/ai-corruption" except for the solution presentation. If in the first repository the solution is presented as a Desktop application, then in this one the Web application.

The basic concept is the same: analyze the file for the presence of corruption factors and highlight the paragraph in which there is a high probability of the presence of a corruption factor.

To write it, the Django framework was used, SQLite was used as a DBMS.

The project has a standard Django user database and a database of uploaded files, database link: one-to-many.
Each user has access only to the files uploaded by him.

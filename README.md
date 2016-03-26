# sel-ex
My Experiments with Selenium :)

Prerequisite : pip install -U selenium

### website_visit.py

Basic script which visits youtube.com and runs test - output in image_outputs/website_visit.png


### code.py

This script executes the following procedure using Selenium - Coding in codepad followed by (delusional) interaction through comments and login. Base Inspiration [here](https://gist.github.com/hugs/830011)

image_outputs/delusional_talk.gif illustrates a random procedure:

* User enters python command in shell and submits
* Command gets printed
* Another person comments on it
* Directed to login page as login required to comment
* Credentials entered
* Comment gets posted
* Initial user replies back to it in the shell


### codepad_code_test.py

output in image_outputs/codepad_code.png

Contains tests for :
* Accessing Codepad website
* Output after entering correct code in codepad
* Output after entering incorrect syntax code in codepad


### codepad_credential_test.py

output in image_outputs/codepad_credential.png

Contains tests for :
* User logging in to codepad with valid credentials
* User logging in to codepad with invalid credentials
* User logout

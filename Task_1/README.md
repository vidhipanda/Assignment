TASK: 
Take any sample hello world application from the internet or build a simple one of your own. 
Write a dockerfile and package it into a docker image. Build the docker image and push it to the docker hub using terraform.

Solution:
This task has 4 parts:
1. Taking sample hello world app.
2. Create docker file.
3. Create docker image.
4. Push docker image to dockerhub using terraform.

Here,
app.py --> simple python hello world program.

Dockerfile --> Used to create the docker image.

Terraform files --> [main.tf , terraform.tfvars, vars.tf] are the tf files used to push the docker image to docker hub
1. main.tf --> Contains code to push docker image to dockerhub registry
2. vars.tf --> Contains the variable declaration used in main.tf
3. terraform.tfvars --> Coantains the value of the varibales mentioned in vars.tf 

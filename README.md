## Terraform/EKS Exercise 
1. Take any sample hello world application from the internet or build a simple one of your own. 
Write a dockerfile and package it into a docker image. Build the docker image and push it to the docker hub using terraform.
2. Build a 3-tier VPC with public and private subnets in each availability zone and deploy an EKS cluster in the above VPC.
3. Extend the terraform code or provide an automation solution to  Create a k8s namespace - "exercise", 
Deploy 2 replicas of pods from the above built image in the "exercise" namespace, and 
Expose the deployment using service type LoadBalancer and share the endpoint.

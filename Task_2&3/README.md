TASK 2:
Build a 3-tier VPC with public and private subnets in each availability zone and deploy an EKS cluster in the above VPC.

Solution:

Once you create the main.tf, output and vars.tf file do a terraform init, plan and apply --> this will create vpc in the specified aws region.

To configure and deploy eks cluster onto that vpc we need to run the following commands.
1.  aws eks --region us-east-1 update-kubeconfig --name rattle-eks-cluster.
    # To verifiy the nodes run
     kubectl get nodes
2. To deploy apps run
     kubectl apply -f https://k8s.io/examples/application/deployment.yaml


Task 3: 
Extend the terraform code or provide an automation solution to create a k8s namespace - "exercise", 
Deploy 2 replicas of pods from the above built image in the "exercise" namespace, and 
Expose the deployment using service type LoadBalancer and share the endpoint.
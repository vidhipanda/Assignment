# outputs.tf

output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_ids" {
  value = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  value = aws_subnet.private[*].id
}

output "eks_cluster_name" {
  value = aws_eks_cluster.rattle_cluster.name
}

# Outputs the LoadBalancer URL
output "loadbalancer_url" {
  value = kubernetes_service.exercise_service.status[0].load_balancer[0].ingress[0].hostname
}
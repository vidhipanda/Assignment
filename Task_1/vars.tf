# variables.tf
variable "dockerhub_username" {
  description = "Docker Hub Username"
  type        = string
}

variable "dockerhub_password" {
  description = "Docker Hub Password"
  type        = string
  sensitive   = true
}

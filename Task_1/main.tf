provider "docker" {
  host = "unix:///var/run/docker.sock"
}

provider "docker" {
  username = var.dockerhub_username
  password = var.dockerhub_password
}

resource "docker_image" "hello_world_image" {
  name         = "vidhism/hello-world:latest"
  build {
    context    = "./" 
    dockerfile = "Dockerfile"
  }
}

resource "docker_registry_image" "hello_world_image_push" {
  name = docker_image.hello_world_image.name
  push = true
}

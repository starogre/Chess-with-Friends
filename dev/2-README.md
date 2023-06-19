# DevBox Docker Environment

Set up a Docker-based development environment on WSL Ubuntu. This guide should also work on Ubuntu/PopOS Linux.

## Prerequisites
- WSL Ubuntu or similar Linux system
- You have sudo access on your system

## Installation Steps

1. **Docker Installation**

    Install Docker on your WSL Ubuntu environment using the provided script. You only need to do this once after installing WSL Ubuntu.

    ```bash
    ./00-docker-install-ubuntu.sh
    ```

2. **Add User to Docker Group**

    Add yourself to the Docker group to enable running Docker commands. Replace `<username>` with your actual username.

    ```bash
    sudo usermod -aG docker <username>
    ```

3. **Build Docker Image**

    Use the provided script to build the Docker image. This image is named `devbox` and includes all necessary tools and configurations.

    ```bash
    ./01-build.sh
    ```

4. **Enter the Docker Container**

    Start a Docker container from the `devbox` image using the script. This will open a zsh shell inside the container. Note that any changes made inside the `/app` directory will persist across container runs.

    ```bash
    ./02-enter.sh
    ```

5. **SSH for Github**

    Generate an SSH key for secure communication with GitHub.This is to be done inside the Docker container. Replace `"your_email@example.com"` with your GitHub email.

    ```bash
    ssh-keygen -t ed25519 -C "your_email@example.com"
    cat /root/.ssh/id_ed25519.pub
    ```

    After generating your key, add it to your GitHub account.

6. **Clone Git Repository**

    Clone your Git repositories inside the `/app` directory in the Docker container. This will persist even if the container is deleted or exited.

    ```bash
    cd /app
    git clone git@github.com:JackFUrton/Chess-with-Friends.git
    ```

## Additional Docker Commands

Here are some useful Docker commands:

```bash
docker --help
docker ps # view running containers
docker ps -a # view all containers
docker volume ls # view docker volumes
docker images # view built or pulled images
docker rm -vf $(docker ps -aq) # remove all running containers
docker rmi -f $(docker images -aq) # remove all images
docker system prune -a # remove stopped containers, unused networks, all images without a container, and all build cache

Docker containers are ephemeral. The Dockerfile provides build instructions, so you can recreate your container using the 01-build.sh script. However, deleting the Docker volumes for my_project_files and my_ssh_keys will cause loss of work within your locally cloned Chess repo and your SSH key, respectively. Avoid deleting Docker volumes to prevent loss of work.


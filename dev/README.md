# DevBox Docker Environment

This will set up a development environment using Docker 

This guide assumes that you're using WSL Ubuntu(will work on Ubuntu/PopOS Linux as well)

## Step 1: Docker Installation

Run the `00-docker-install-ubuntu.sh` script to install Docker on your WSL Ubuntu environment. 

./00-docker-install-ubuntu.sh
(this script only needs to be run once after WSL Ubuntu is installed)

Run the following to add yourself to docker group so you can run docker commands

whoami (make note of username)
sudo -i (switch to root user)
usermod -aG docker <username>
su <username>

## Step 2: Build Docker Image

Once Docker is installed, you can build the Docker image using the `01-build.sh` script.

./01-build.sh

This script builds a Docker image named devbox from the Dockerfile in the current directory. The image includes all the necessary tools and configurations defined in the Dockerfile.

## Step 3: Enter the Docker Container

Once the image is built, you can start a Docker container from the devbox image using the `02-enter.sh` script.

./02-enter.sh

This script starts a Docker container and opens a Zsh shell inside it. The container has two volumes mounted: my_ssh_keys at /root/.ssh and my_project_files at /app.

Docker volumes are used to persist data. The my_ssh_keys volume is used to store SSH keys, which allows you to access Git repositories securely from within the Docker container. The my_project_files volume is where you can clone your Git repositories, i.e Chess-with-Friends repo. Any changes to the data in these volumes will persist across different runs of the Docker container. Cloning Chess repo into /app directory will persist the repo between entering/exiting/destroying container.

exit - lets you exit container once you are inside
re-rerunning ./02-enter.sh will re-initialize/enter container

## Step 4: SSH for Github

ssh-keygen -t ed25519 -C "your_email@example.com"

Follow the prompts to save the key in the default location (/root/.ssh/id_ed25519) and optionally set a passphrase.

Once you have generated the SSH key, you need to add it to your GitHub account. Run this command to display your public SSH key:

cat /root/.ssh/id_ed25519.pub

## Step 5: Clone Git Repo

Clone your Git repositories inside the /app directory in the Docker container
cd /app
git clone git@github.com:JackFUrton/Chess-with-Friends.git

## Extra Notes:

docker --help
docker ps - view running containers
docker ps -a - view all containers (including exited ones)
docker volume ls - view docker volumes
docker images - view docker images that have been built or pulled

Extra commands for deleting containers/removing images:

docker rm -vf $(docker ps -aq) - removes all running containers (be careful with this one)
docker rm --help for more details
docker rmi -f $(docker images -aq) - removes/untags all docker images
docker rmi --help
docker system prune -a - This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all images without at least one container associated to them
  - all build cache

Deleting and removing docker containers/images is ok, containers are ephemeral

Deleting the docker volumes of my_project_files and my_ssh_keys will cause loss of work within your locally cloned Chess repo and loss of SSH key respectively

## Important points:

/app directory inside container is where to clone repos/files you want to persist across exits/deletion of this docker container
The 2 docker volumes (primarily my_project_files that is attached to /app directory inside container) will hold your data across deletion and exits of the container

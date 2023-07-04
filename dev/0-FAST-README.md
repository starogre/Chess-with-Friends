# Quick Guide: Setting Up and Using WSL with Docker

This guide provides a high-level overview of the steps required to install and use Windows Subsystem for Linux (WSL) with Docker on your machine.

## Prerequisites

- Windows system with Virtual Machine Platform enabled
- WSL installed from the Microsoft Store
- Ubuntu installed within WSL
- Windows Terminal installed for accessing WSL

For more detailed steps on setting up the prerequisites, refer to `1-WSL-README.md`.

## Initial Setup

1. Reboot your system after installing WSL.

2. Run the setup scripts in the following order:

   - On your WSL terminal, navigate to the directory where the scripts are located.
   - Run `./00-docker-install-ubuntu.sh`.
   - Run `./01-build.sh`.
   - Run `./02-enter.sh`.

## Working within the Docker Container

1. Once inside the Docker container:

   - Generate an SSH key with `ssh-keygen -t ed25519 -C "your_email@example.com"`.
   - Display your new public key with `cat /root/.ssh/id_ed25519.pub`.
   
2. Navigate to the `/app` directory (this directory will persist your information across entering/exiting containers).

3. Clone the Chess-with-Friends repository: `git clone git@github.com:JackFUrton/Chess-with-Friends.git`.

You are now ready to work within your Docker container.

## Important Notes

- To exit the Docker container, simply type `exit`.

- To re-enter the Docker container:

   - If you've exited but not removed the Docker container, run `./02-enter.sh` in your WSL terminal.
   
   - If you've removed the Docker container, you'll need to run `./01-build.sh` and then `./02-enter.sh` again.
   
- The `./00-docker-install-ubuntu.sh` script only needs to be run once on your WSL terminal.
- The `./01-build.sh` script only needs to be run if you've removed the Docker container.

Remember that each time you enter the Docker container, it will refresh/create the Neovim configurations. For detailed instructions on each step and additional information about the processes, refer to the other README.md files.


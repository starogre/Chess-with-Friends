#!/bin/bash
docker run -v my_ssh_keys:/root/.ssh -v my_project_files:/app -it devbox /usr/bin/zsh

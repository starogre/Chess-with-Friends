# Quick README for the important stuff

## Fast Overview of Steps Needed

Install WSL on Host Machine (these steps also work on apt based distros)

Follow steps within 1-WSL-README.md
Summary from `1-WSL-README.md`:
`Windows Features` --> enable `Virtual Machine Platform`
`Microsoft Store` --> `WSL` install --> `Ubuntu` install --> `Windows Terminal` install
Open `Windows Terminal` --> click `Drop Down Bar` --> `Ubuntu`
If it errors theres some troubleshooting steps in `1-WSL-README.md`

Run the following scripts in order 

On Host Machine WSL:
`./00-docker-install-ubuntu.sh`
`./01-build.sh`
`./02-enter.sh`

Once inside container:
`ssh-keygen -t ed25519 -C "your_email@example.com"`
`cat /root/.ssh/id_ed25519.pub`
`cd /app` (important directory that will persist your information across entering/exiting containers)
`git clone git@github.com:JackFUrton/Chess-with-Friends.git`

You're good to go now

`exit` while inside contianer will take you out of container
`./02-enter.sh` while on WSL Ubuntu takes you back into container (assuming you did not delete/remove container image, in which case re-run `./01-build.sh` then `./02-enter.sh`

`./00-docker-install-ubuntu.sh` only needs to be run once on Host Machine WSL
`./01-build.sh` only needs to be run if you remove the docker image (does not need to be re-ran if `exit` from inside container)
`./02-enter.sh` will be your go to for rejoining the container

nvim <-- each enter of docker container will cause nvim to repull/create configs

The other README.md's have more specific info of how to perform each step and a bit more about what is happening

# Installing WSL

## 3 Good References
These are 3 good references for WSL but the steps I wrote below I believe will work as well.

https://learn.microsoft.com/en-us/windows/wsl/install#prerequisites
https://learn.microsoft.com/en-us/windows/wsl/install
https://www.youtube.com/watch?v=clZCrVZH4Gg&ab_channel=Dave%27sGarage

## Enable Virtualization

Head to `Windows Features` --> enable `Virtual Machine Platform` (this should be all you need to enable here but if not you can enable `Hyper-V` and `Windows Hypervisor Platform`

You can also enable `Windows Subsystem for Linux` here but I usually just install it from Microsoft Store.

NIT: In general most modern systems will support hardware virtualization (VT-x for Intel, AMD-V for AMD) so you shouldn't have to check your BIOS for enabled Virtualization. This could be kind of a last resort check after Virtualization has been enabled within Windows Features. This paragraph can be ignored most likely, just thought I'd mention in case WSL complains even after Windows Features have been turned on.

## Microsoft store

If you did not enable `Windows Subsystem for Linux` in `Windows Features`:

Head to Microsoft Store search `WSL` --> install WSL and then install `Ubuntu`

While you are in Microsoft Store also install `Windows Terminal` <-- great terminal for windows

## Open Windows Terminal

The drop down bar should now have `Ubuntu` listed, click on this
This should start installing Ubuntu WSL

Change default terminal from powershell to Ubuntu by clicking `Arrow Drop Down On Terminal` --> `Settings` --> `Startup / Default Profile`

`sudo apt update && sudo apt upgrade` <-- good commands to run in Linux to keep you updated

## Ready to run 00-docker-install-ubuntu.sh

You are now ready to run the docker install script

Head to 2-README.md for more info

## Powershell WSL commands
`wsl -l -v` lists current Linux images on machine
`wsl --list --online` lists currently installable Linux images

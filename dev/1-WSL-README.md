# Installing Windows Subsystem for Linux (WSL)

This guide outlines the steps required to install the Windows Subsystem for Linux (WSL) on your system.

## Useful References

Here are some additional references that provide in-depth information on installing and using WSL:

- [Microsoft's Official WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install#prerequisites)
- [Dave's Garage YouTube tutorial on installing WSL](https://www.youtube.com/watch?v=clZCrVZH4Gg&ab_channel=Dave%27sGarage)

## Steps

1. **Enable Virtualization:** Open `Windows Features` and enable `Virtual Machine Platform`. Most modern systems support hardware virtualization, so you likely won't need to check your BIOS settings. You can optionally enable `Hyper-V` and `Windows Hypervisor Platform`.

2. **Install WSL and Ubuntu:** Go to the Microsoft Store and search for `WSL`. Install WSL and then install `Ubuntu`.

3. **Install Windows Terminal:** While still in the Microsoft Store, search for `Windows Terminal` and install it. This is a versatile terminal emulator for Windows.

4. **Reboot your system** after installing WSL.

5. **Open Windows Terminal:** In the drop-down menu, you should now see `Ubuntu` listed. Click on it to start the Ubuntu WSL installation.

6. **Set Ubuntu as Default Terminal:** Click on the drop-down arrow in the Terminal, go to `Settings` -> `Startup / Default Profile`, and set the default to Ubuntu.

7. **Update Ubuntu Packages:** Run `sudo apt update && sudo apt upgrade` in the Ubuntu terminal to update your Linux packages.

8. **Ready to run 00-docker-install-ubuntu.sh:** At this point, you are ready to run the Docker install script. Refer to `2-README.md` for more information.

## Additional WSL Commands

Here are some additional commands you may find useful when working with WSL:

- `wsl -l -v`: Lists the current Linux distributions installed on your machine.
- `wsl --list --online`: Lists the Linux distributions currently available for installation.


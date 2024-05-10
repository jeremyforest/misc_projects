#!/bin/bash
 
# partially copied from here:  https://raw.githubusercontent.com/hjaltiatla/ubuntu-desktop-automated/master/setup.sh

#update
sudo apt update -y && sudo apt upgrade -y
 
#Install Vim and net tools
sudo apt install -y net-tools && sudo apt install -y vim
 
#Install wget & curl
sudo apt install -y wget && sudo apt install -y curl
 
#Install htop
sudo apt install -y htop
 
#Install Docker
sudo apt install -y docker.io
 
#Install guake Terminal
sudo apt install -y guake
 
#install glances
sudo apt install -y glances

#Install AppImageLauncher
sudo apt install software-properties-common
sudo add-apt-repository ppa:appimagelauncher-team/stable
sudo apt update
sudo apt install -y appimagelauncher
appimagelauncherd

#Install Logseq 0.8.12
wget https://github.com/logseq/logseq/releases/download/0.8.12/Logseq-linux-x64-0.8.12.AppImage 
mv Logseq-linux-x64-0.8.12.AppImage /home/jeremy/Applications

#Install Zoom
wget https://zoom.us/client/5.12.9.367/zoom_amd64.deb
sudo apt install -y ./zoom_amd64.deb
rm zoom_amd64.deb

#Install Slack using snap
sudo snap install slack --classic
 
#Install draw.io snap
sudo snap install drawio

#Install Pycharm snap
sudo snap install pycharm-community --classic

#Install VS code - repository and key installed manually:
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt install -y apt-transport-https
sudo apt update -y
sudo apt install -y code
 
#Enable docker service at Bootup
sudo systemctl enable docker
 
#edit "username" - Add the "username" user to docker and libvirt group
sudo usermod -aG docker jeremy 
sudo usermod -aG libvirt jeremy

# Copy over .bashrc file

#update mounts
source ~/.bashrc
sudo mkdir /mnt/home_nas 
refresh-mount

#Todo after Install 
# 1) - Need to copy .config , .vscode , .mozilla , .ssh from old computer



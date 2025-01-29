# Download and Install Docker on Rocky Linux
sudo dnf check-update
echo "Adding repo to package manager"
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
echo "Installing docker"
sudo dnf install docker-ce docker-ce-cli containerd.io

echo "Start docker"
sudo systemctl start docker

echo "Enabling docker"
sudo systemctl enable docker

# Create and enable swap file
sudo fallocate -l 3G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo cp /etc/fstab /etc/fstab.bak
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Add Docker's official GPG key
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the Docker repository to Apt sources and install
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install and configure Nginx and OpenSSH
sudo apt install nginx
sudo ufw allow 'Nginx Full'
sudo ufw allow 'OpenSSH'  # Don't lock yourself out of your server!
sudo ufw enable

# Create a non root user and give privileges
sudo adduser fsd
usermod -a -G sudo fsd
chown -R fsd:fsd /etc/nginx/sites-available/default
usermod -aG docker fsd
# Then switch to the fsd user and cd to home directory
su fsd
cd ~

# Follow the instructions from github actions runners settings for up to date versions and your specific api token
# Create a folder for the actions runner
mkdir actions-runner && cd actions-runner

# Download the latest runner package
curl -o actions-runner-linux-x64-2.319.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-x64-2.319.1.tar.gz

# Unzip
tar xzf ./actions-runner-linux-x64-2.319.1.tar.gz

# Create the runner and start the configuration experience
./config.sh --url https://github.com/<your_github_profile>/FullStackDev --token X?X?X?X?X?X?X?X?X?X

# Name the runner work folder
fsd_deploy_work_folder

# Install and launch the runner service
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status

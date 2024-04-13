# Change PWD to the docker directory
cd /home/goug76/docker/appdata/traefik/acme/

# Create .env file
sudo mv acme.example acme.json

# Set permissions to the .env file to 600
sudo chmod 600 /home/goug76/docker/appdata/traefik/acme/acme.json
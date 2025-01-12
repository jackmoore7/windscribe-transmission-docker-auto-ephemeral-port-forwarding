A little script for automatically updating your ephemerally forwarded port via Windscribe in your Transmission container via RPC.

### Usage
Create an .env file and set:
- TRANSMISSION_PORT=your-current-transmission-port
- TRANSMISSION_HOST=your-host-ip
- TRANSMISSION_USERNAME=your-transmission-username
- TRANSMISSION_PASSWORD=your-transmission-password
- DOCKER_PASSWORD=your-docker-password (this is the password to whatever you're running Docker on, not the container itself)
- DOCKER_PASSWORD=your-docker-password

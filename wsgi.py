from app import create_app
from waitress import serve
import socket

app = create_app()

# Get the outbound IP address assigned by Render
outbound_ip = socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    # Use the outbound IP address and the port specified by Render
    serve(app, host=outbound_ip, port=5000)
import os
# Retrieves the hostname/IP address from the "HOST" environment variable.
HOST = os.getenv("HOST", "0.0.0.0")
# Retrieves the port number from the "PORT" environment variable, defaults to 5000 if not set.
PORT = int(os.getenv("PORT", 5000))

CONN = "mongodb+srv://atgnooijen:LFudILmmPS6CA4d2@cluster0.wgj9dp1.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"
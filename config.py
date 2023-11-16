from decouple import config
from dotenv import load_dotenv

load_dotenv()


SERVICE_PORT = config('SERVICE_PORT', cast=int, default=8585)

XRAY_API_PORT = config('XRAY_API_PORT', cast=int, default=8586)
XRAY_EXECUTABLE_PATH = config("XRAY_EXECUTABLE_PATH", default="/usr/local/bin/xray2")
XRAY_ASSETS_PATH = config("XRAY_ASSETS_PATH", default="/usr/local/share/xray2")

SSL_CERT_FILE = config("SSL_CERT_FILE", default="/var/lib/marzban-node2/ssl_cert.pem")
SSL_KEY_FILE = config("SSL_KEY_FILE", default="/var/lib/marzban-node2/ssl_key.pem")
SSL_CLIENT_CERT_FILE = config("SSL_CLIENT_CERT_FILE", default="")

DEBUG = config("DEBUG", cast=bool, default=False)

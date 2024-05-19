from src.auth.jwt_handler import JWTHandler
from src.config.segurity import auth_algorithm, auth_secret_key
auth_handler = JWTHandler(auth_secret_key, auth_algorithm)
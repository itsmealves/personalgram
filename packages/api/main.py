import dotenv
import falcon
from resources import ResourceManager

dotenv.load_dotenv()

api = falcon.API()
ResourceManager.load_resources(api)

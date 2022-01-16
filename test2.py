# Global Variables:
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)
WEBSITE_PATH = os.getenv("WEBSITE_PATH")
print('WEBSITE_PATH: ' + str(WEBSITE_PATH))
# art_gallery_path = '/var/www/musimatic/images/ArtGallery'
art_gallery_path = str(WEBSITE_PATH) + str("/images/ArtGallery")
print('art_gallery_path: ' + str(art_gallery_path))
WEBSITE_ADDRESS = os.getenv("WEBSITE_ADDRESS")
print('WEBSITE_ADDRESS: ' + str(WEBSITE_ADDRESS))
WEBSITE_FULL_ADDRESS = os.getenv("WEBSITE_FULL_ADDRESS")
print('WEBSITE_FULL_ADDRESS: ' + str(WEBSITE_FULL_ADDRESS))

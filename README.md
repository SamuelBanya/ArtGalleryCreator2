# ArtGalleryCreator2
This is a spinoff project from my initial 'ArtGalleryCreator' project, but more specifically for my art portfolio website, 'sambanya.com'

This is an attempt to make it make this project a bit more management with an '.env' environment variable file.

Feel free to utilize this for your website, but DO modify the '.env' file accordingly to suit your 'nginx' based website.

To be on the safe side, within your '/var/www/yourwebsite' directory on your site, you should create the following empty directories:
- css    
- favicon
- images 
- js

NOTE: Under 'images', also create another subdirectory called 'ArtGallery'.

# Installation Instructions
Make sure you are using an 'nginx' based website on any desired VPS of your choice (Digital Ocean, Vultr, etc.)

Then, git clone this project onto the root of your website onto a sample directory.

Ex: '/deploy_scripts'

Then, make sure that the same directory is owned by the user with 'chown' commands recursively.

Ex: sudo chown -R tom /deploy-scripts 

Then, install the dependencies required by the project for that given user, ex: 'tom' by using pip3 install.

You could get fancy and use 'venv' but to keep it simple, just make a new user on the given 'nginx' box and install the Python 3 dependencies as needed within the 'import' sections of the 'main.py' file.

You can then manually run the file as the given user, ex: 'tom', by using python3 /deploy_scripts/ArtGalleryCreator2/main.py.

Or, you can set the same task to a crontab job using 'crontab -e', and using the following syntax:
*/60 * * * * python3 /deploy_scripts/ArtGalleryCreator/main.py > /tmp/artgallerycreator_error.log 2>&1

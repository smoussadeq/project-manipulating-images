import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

#TODO: Loop over all files in the working directory.

for filename in os.listdir('originals'):
    if not(filename.endswith('.png') or filename.endswith('.jpg'))\
       or filename == LOGO_FILENAME:
        continue 
    im = Image.open(os.path.join('originals',filename))
    width, height = im.size

#TODO: Check if file image needs to be resized.
    
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        
#TODO: Calculate the new width and height to resize to.
        
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE

        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

#Resize the image.
            
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))
      
#TODO: Add the logo.
        
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    
#TODO: Save changes.
        
        im.save(os.path.join('withLogo', filename))


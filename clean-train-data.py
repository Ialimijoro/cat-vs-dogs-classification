import os

path = 'data/train'
cat_path = 'data/train/cat'
dog_path = 'data/train/dog'

folder = os.fsencode(path)

filenames = []

for file in os.listdir(folder):
  filename = os.fsdecode(file)

  if filename.endswith( ('.jpeg', '.png', '.gif', '.jpg') ): # whatever file types you're using...
    filenames.append(filename)
    image_src = path + '/'+ filename

    if filename.find('cat') != -1 :
      os.rename(image_src, cat_path + '/' + filename)
    elif filename.find('dog') != -1 : 
      os.rename(image_src, dog_path + '/' + filename)
        
filenames.sort() # now you have the filenames and 
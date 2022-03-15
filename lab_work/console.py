import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# album_repository.delete_all()
# artist_repository.delete_all()

artist1 = Artist("John")
artist_repository.save(artist1)

album1 = Album("Song", "rock", artist1)
album_repository.save(album1)

albums = album_repository.select_all()

for album in albums:
    print(album.__dict__)

pdb.set_trace()
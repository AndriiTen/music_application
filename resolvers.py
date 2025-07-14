from ariadne import ObjectType
from models import db, Song, Artist

query = ObjectType("Query")
mutation = ObjectType("Mutation")

@query.field("songs")
def resolve_songs(*_):
    return Song.query.all()

@query.field("song")
def resolve_song(*_, id):
    return Song.query.get(id)

@query.field("artists")
def resolve_artists(*_):
    return Artist.query.all()

@query.field("artist")
def resolve_artist(*_, id):
    return Artist.query.get(id)

@mutation.field("addSong")
def resolve_add_song(*_, title, artist_id, duration):
    song = Song(title=title, artist_id=artist_id, duration=duration)
    db.session.add(song)
    db.session.commit()
    return song

@mutation.field("addArtist")
def resolve_add_artist(*_, name):
    artist = Artist(name=name)
    db.session.add(artist)
    db.session.commit()
    return artist
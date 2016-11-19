#!/usr/bin/env python

import spotipy as sy
sp = sy.Spotify(auth=None)

def get_songs(words, moods=None):
	if (moods):
		return get_playlist(words)
	return get_tracks(words)

def get_playlist(words):
	return sp.search(q=' '.join(words), type='playlist')

def get_tracks(words):
	tracks = sp.search(q=' '.join(words), type='track', limit=50)['tracks']['items']
	tracks = {t['id']: t for t in tracks}
	try:
		features = get_audio_features(tracks.keys())
		for f in features:
			tracks[f['id']].update(f)
	except:
		pass
	return map(get_relevant_data, tracks.values())

def get_audio_features(tracks):
	return sp.audio_features(list(tracks))

def get_relevant_data(track):
	return {
		'artist': track['artists'][0]['name'],
		'album': track['album']['name'],
		'id': track['id'],
		'name': track['name'],
		'url': track['external_urls']['spotify'],
		'key': track.get('key'),
		'loudness': track.get('loudness'),
		'tempo': track.get('tempo'),
	}

def get_track_features(track_id):
	pass
	

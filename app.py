from flask import Flask, request, jsonify

app = Flask(__name__)

playlists = []

def find_playlist_by_id(playlist_id):
    for playlist in playlists:
        if playlist["id"] == playlist_id:
            return playlist
    return None

def find_song_by_id(playlist, song_id):
    for song in playlist["songs"]:
        if song["id"] == song_id:
            return song
    return None

@app.route('/')
def index():
    return 'Welcome to the Playlist Management System!'

@app.route('/playlists', methods = ["GET"])
def view_all_playlists():
    return jsonify(playlists)

@app.route('/playlist/<int:playlist_id>', methods = ['GET'])
def view_playlist_by_id(playlist_id):
    playlist = find_playlist_by_id(playlist_id)
    if playlist:
        return jsonify(playlist)
    else:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404

@app.route('/playlist/create', methods = ["POST"])
def create_playlist():
    data = request.json
    if data:
        playlists.append(data)
        return jsonify({"Message": "Success: Playlist Created!"}), 201
    else:
        return jsonify({"Message": "Error: Invalid Data."}), 400
    
@app.route('/playlist/update/<int:playlist_id>', methods = ["PUT"])
def update_playlist(playlist_id):
    playlist = find_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404
    else:
        data = request.json
        playlist.update(data)
        return jsonify ({"Message": "Success: Playlist Updated!"})
    
@app.route('/playlist/delete/<int:playlist_id>', methods = ["DELETE"])
def delete_playlist(playlist_id):
    playlist = find_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404
    else:
        playlists.remove(playlist)
        return jsonify ({"Message": "Success: Playlist Deleted!"})

@app.route('/playlist/<int:playlist_id>/add_song', methods = ["POST"])
def add_song(playlist_id):
    data = request.json
    playlist = find_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404
    else:
        if data:
            playlist["songs"].append(data)
            return jsonify({"Message": "Success: Song Added!"}), 201
        else:
            return jsonify({"Message": "Error: Invalid Data."}), 400

@app.route('/playlist/<int:playlist_id>/delete_song/<int:song_id>', methods = ["DELETE"])
def delete_song(playlist_id, song_id):
    playlist = find_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404
    song = find_song_by_id(playlist, song_id)
    if not song:
        return jsonify({"Message": "Error: Song Not Found."}), 404
    playlist["songs"].remove(song)
    return jsonify ({"Message": "Success: Song Deleted!"})

@app.route('/playlist/<int:playlist_id>/<int:song_id>', methods = ["GET"])
def view_song_by_id(playlist_id, song_id):
    playlist = find_playlist_by_id(playlist_id)
    if not playlist:
        return jsonify({"Message": "Error: Playlist Not Found."}), 404
    song = find_song_by_id(playlist, song_id)
    if not song:
        return jsonify({"Message": "Error: Song Not Found."}), 404
    else:
        return jsonify(song)

if __name__ == '__main__':
    app.run(debug=True)
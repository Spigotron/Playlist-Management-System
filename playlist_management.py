class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Cannot dequeue from an empty queue')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Cannot peek from an empty queue')

    def size(self):
        return len(self.items)

playlists = [
    {
        "id": 1,
        "name": "rock",
        "description": "a playlist of rock music",
        "songs": [
            {}
        ]
    }
]

playlists_queue = Queue()

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

    def __str__(self):
        return str(self.song)

    def __repr__(self):
        return f"<Node|{self.song}>"

class SongList:
    def __init__(self):
        self.head = None

    def append(self, new_song):
        new_node = Node(new_song)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove(self, song_id):
        if self.head is None:
            print('List is empty, nothing to remove')
            return
        if self.head.song['id'] == song_id:
            self.head = self.head.next
            return
        prev_node = self.head
        current_node = self.head.next
        while current_node:
            if current_node.song['id'] == song_id:
                prev_node.next = current_node.next
                return
            prev_node = current_node
            current_node = current_node.next

playlists[0]['songs'] = SongList()

def add_song_to_playlist(playlist, song):
    playlist['songs'].append(song)

song = {
    "id": 1,
    "title": "Holy Diver",
    "artist": "Dio"
}

add_song_to_playlist(playlists[0], song)

def view_all_songs_in_playlist(playlist_index):
    current_node = playlists[playlist_index]['songs'].head
    while current_node:
        print(current_node)
        current_node = current_node.next
    if not current_node:
        print(f"There are no songs in the playlist.")

view_all_songs_in_playlist(0)

def remove_song_from_playlist(playlist, song_id):
    playlist['songs'].remove(song_id)

remove_song_from_playlist(playlists[0], 1)

view_all_songs_in_playlist(0)

def binary_search_playlist(playlist, song_title):
    current_node = playlist['songs'].head
    list1 = []
    while current_node:
        list1.append(current_node.song['title'])
        current_node = current_node.next
    list1.sort()
    low = 0
    high = len(list1) - 1
    num_checks = 0
    while low <= high:
        mid = (low + high) // 2
        num_checks += 1
        if song_title == list1[mid]:
            return f"'{song_title}' is in the playlist at index {mid} and it took {num_checks} checks"
        elif song_title > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    print(f"'{song_title}' is not in the playlist.")
    return -1

print(binary_search_playlist(playlists[0], "Holy Diver"))

def list_all_songs_recursive(playlist_index, current_node=None):
    if playlist_index >= len(playlists):
        return
    if current_node is None:
        current_node = playlists[playlist_index]['songs'].head
    print(f"Playlist: {playlists[playlist_index]['name']}")
    if current_node:
        print(f"Song: {current_node.song['title']} by {current_node.song['artist']}")
        list_all_songs_recursive(playlist_index, current_node.next)
    else:
        print(f"There are no songs in the playlist.")
    list_all_songs_recursive(playlist_index + 1)

list_all_songs_recursive(0)
songs = []

def add_song():
  title = input("Nhập tên bài hát: ")
  artist = input("Nhập tên ca sĩ: ")
  duration = int(input("Nhập thời lượng (giây): "))

  songs.append({
    'title': title,
    'artist': artist,
    'duration': duration
  })

  print("Đã thêm bài hát vào playlist.")

def view_playlist():
  if not songs:
    print("Playlist trống.")
    return

  print("\n--- DANH SÁCH PHÁT ---")
  for i, song in enumerate(songs, start=1):
    print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")

def search_by_artist():
  name = input("Nhập tên ca sĩ cần tìm: ")
  found = False

  print(f"\n--- KẾT QUẢ TÌM KIẾM: {name} ---")
  for song in songs:
    if name.lower() in song['artist'].lower():
      print(f"- {song['title']} ({song['duration']}s)")
      found = True

  if not found:
    print("Không tìm thấy bài hát nào.")


def main():
  while True:
    print("\n--- MUSIC PLAYLIST MANAGER ---")
    print("1. Thêm bài hát")
    print("2. Xem danh sách phát")
    print("3. Tìm bài hát theo ca sĩ")
    print("4. Thoát")
    choice = input("Chọn chức năng: ")
    if choice == '1':
      add_song()
    elif choice == '2':
      view_playlist()
    elif choice == '3':
      search_by_artist()
    elif choice == '4':
      print("Kết thúc chương trình.")
      break
    else:
      print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
  main()
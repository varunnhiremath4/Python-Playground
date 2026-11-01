print("="*30)
print("     Welcome to File Organiser")
print("="*30)
import os
folder = "D://Python Practise"
items = os.listdir(folder)
print("Initially the Directory contains:")
for k in items:
    print(k)
print("-"*30)
print("The respective extension and type is:")
images = [".jpg", ".jpeg", ".png"]
music = [".mp3", ".wav"]
videos = [".mp4", ".mkv"]
documents = [".txt", ".pdf", ".docx", ".py"]    
for i in items:
    Path = os.path.join(folder, i)
    if os.path.isfile(Path):
        name , extension = os.path.splitext(i)
        if extension.lower() in images:
            print(i, "->", extension, "->", "Image")
        elif extension.lower() in music:
            print(i, "->", extension, "->", "Music")
        elif extension.lower() in videos:
            print(i, "->", extension, "->", "Video")
        elif extension.lower() in documents:
            print(i, "->", extension, "->", "Document")
        else:
            print(i, "->", extension, "->", "Other")
print("-"*30)

os.makedirs(os.path.join(folder, "Images"), exist_ok=True)
os.makedirs(os.path.join(folder, "Videos"), exist_ok=True)
os.makedirs(os.path.join(folder, "Documents"), exist_ok=True)
os.makedirs(os.path.join(folder, "Musics"), exist_ok=True)
os.makedirs(os.path.join(folder, "Others"), exist_ok=True)

def organise_files(file_name):
    exe_dict = {
        ".png" : "Images",
        ".jpg" : "Images",
        ".jpeg" : "Images",
        ".mp3" : "Musics",
        ".wav" : "Musics",
        ".mp4" : "Videos",
        ".mkv" : "Videos",
        ".txt" : "Documents",
        ".pdf" : "Documents",
        ".docx" : "Documents",
        ".py" : "Documents",
    }
    name , extension = os.path.splitext(file_name)
    destination = exe_dict.get(extension, "Others")
    before_move = os.path.join(folder, file_name)
    after_move = os.path.join(folder, destination, file_name)
    os.rename(before_move, after_move)

for j in items:
    if os.path.isfile(os.path.join(folder, j)):
        organise_files(j)
print("Organised Successfully")
print("="*30)
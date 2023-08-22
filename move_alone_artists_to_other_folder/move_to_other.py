import os
import shutil

def count_music_files(directory):
    music_extensions = ['.mp3', '.wav', '.flac']  # Add more if needed
    count = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in music_extensions):
                count += 1
    
    return count

def move_artist_folder(artist_path, target_path):
    artist_name = os.path.basename(artist_path)
    new_artist_path = os.path.join(target_path, artist_name)
    
    if not os.path.exists(new_artist_path):
        os.makedirs(new_artist_path)
    
    for root, _, files in os.walk(artist_path):
        for file in files:
            item_path = os.path.join(root, file)
            new_item_path = os.path.join(new_artist_path, file)
            shutil.move(item_path, new_item_path)
    
    shutil.rmtree(artist_path)

def main():
    source_directory = input("Enter the source directory: ")
    other_artists_directory = os.path.join(source_directory, "Other")
    min_music_files = 5
    
    if not os.path.exists(other_artists_directory):
        os.makedirs(other_artists_directory)
    
    for artist_name in os.listdir(source_directory):
        artist_path = os.path.join(source_directory, artist_name)
        
        if os.path.isdir(artist_path):
            num_music_files = count_music_files(artist_path)
            
            if num_music_files < min_music_files:
                move_artist_folder(artist_path, other_artists_directory)
                print(f"'{artist_name}' moved to 'Other Artists'")
    
    print("Processing complete.")

if __name__ == "__main__":
    main()


from PIL import Image
import hashlib

def sha1_hash_image(image_path):
    with open(image_path, "rb") as f:
        image_data = f.read()
        
        sha1_hash = hashlib.sha1(image_data).hexdigest()
        
        return sha1_hash

image_path = "./img.png"  # Путь к изображению
sha1_hash = sha1_hash_image(image_path)
print("SHA1 хеш изображения:", sha1_hash)

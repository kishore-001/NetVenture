import random, time, numpy
from PIL import Image

def randomize(img, seed):
    random.seed(seed)
    new_y = list(range(img.shape[0]))
    new_x = list(range(img.shape[1]))
    random.shuffle(new_y)
    random.shuffle(new_x)

    new = numpy.empty_like(img)
    for i, y in enumerate(new_y):
        for j, x in enumerate(new_x):
            new[i][j] = img[y][x]
    return numpy.array(new)

if __name__ == "__main__":
    original_image_path = "flag_qr.png"  # Ensure you have a QR code image with your flag
    img = Image.open(original_image_path)
    img_array = numpy.array(img)
    
    seed = int(time.time())  # Current timestamp as seed
    print(f"Using seed: {seed}")
    
    scrambled_img_array = randomize(img_array, seed)
    scrambled_img = Image.fromarray(scrambled_img_array)
    scrambled_img.save("encrypted.png")
    print("Scrambled image saved as encrypted.png")

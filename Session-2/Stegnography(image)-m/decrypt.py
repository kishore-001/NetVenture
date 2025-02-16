import random, numpy
from PIL import Image

def randomize(img, seed):
    random.seed(seed)

    orig_y = list(range(img.shape[0]))
    orig_x = list(range(img.shape[1]))
    random.shuffle(orig_y)
    random.shuffle(orig_x)

    original = numpy.empty_like(img)

    for i, y in enumerate(orig_y):
        for j, x in enumerate(orig_x):
            original[y][x] = img[i][j]

    return original

if __name__ == "__main__":

    path = "encrypted.png"
    encImage = Image.open(path)
    encArray = numpy.array(encImage)

    seed = 1739701622
    
    revImageArray = randomize(encArray, seed)
    revImage = Image.fromarray(revImageArray)
    revImage.save("flag.png")
    print("Process Done!")
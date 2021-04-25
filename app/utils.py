from PIL import Image
from numpy import zeros
from tensorflow.keras.preprocessing.image import img_to_array
from .apps import AppConfig

model = AppConfig.model


def getMultiplier(n):
    q = n // 256
    r = n % 256
    return q + 1 if r > 0 else q


def resize_image(img):
    baseheight = 256
    hpercent = baseheight / float(img.size[1])
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)
    left = (img.size[0] - 256) // 2
    if left <= 0:
        left = 0
    img = img.crop((left, 0, 356, 256))
    return img


def load_and_generate(img, resize=True):
    image = Image.open(img)
    print("\nOriginal Image size:", image.size)
    if resize:
        image = resize_image(image)
        print("Resized Image size:", image.size)

    data = img_to_array(image)
    y = data.shape[0]
    x = data.shape[1]
    img = zeros((256 * getMultiplier(y), 256 * getMultiplier(x), 3))
    img[: data.shape[0], : data.shape[1], :] = data
    img = (img - 127.5) / 127.5
    x = img.shape[1]
    y = img.shape[0]
    subImages = []
    i = 256
    j = 256
    while i <= y:
        while j <= x:
            subImages.append(img[i - 256 : i, j - 256 : j, :])
            j += 256
        j = 256
        i += 256
    gen = []
    for i in range(len(subImages)):
        out = model.predict(subImages[i].reshape(1, 256, 256, 3))
        out = out * 127.5 + 127.5
        gen.append(out)
    full = zeros((y, x, 3), dtype="uint8")
    i = 256
    j = 256
    k = 0
    while i <= y:
        while j <= x:
            full[i - 256 : i, j - 256 : j, :] = gen[k]
            k += 1
            j += 256
        j = 256
        i += 256
    finalImage = Image.fromarray(full)
    # print(finalImage)
    return finalImage

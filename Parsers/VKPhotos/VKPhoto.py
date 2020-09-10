import vk
import urllib.request
from math import ceil

saveDir = r"G:\Документы\Иностранные языки\English\EnglishWords"

appID = '6334888'
login = '79113298797'
password = 'QweQaz123$'

session = vk.AuthSession(appID, login,
                         password, scope='photos')  # param 'scope' tells which API method we'll be able to use
api = vk.API(session)


# function needs quantity of images in the group
def get_photos(img_quantity):
    # next code block calculates number of iterations to get all photos
    # it's so because API method 'get' can give information only about 1000 images
    if img_quantity <= 1000:
        iters_num = 1
    else:
        iters_num = ceil(img_quantity / 1000)

    photo_list = []
    for i in range(0, iters_num):
        shift = i * 1000

        # we become a list with info about images
        photos_info_list = api.photos.get(owner_id=-121488750, album_id='wall', extended=0, count=1000, offset=shift)

        for photo_inf in photos_info_list:
            # trying to get photo with the best quality
            try:
                img = photo_inf['src_xxbig']  # getting url to the biggest image
            except KeyError:
                try:
                    img = photo_inf['src_xbig']
                except KeyError:
                    try:
                        img = photo_inf['src_big']
                    except KeyError:
                        pass
            photo_list.append(img)

    return photo_list  # function returns a list with links to all images

photoArr = get_photos(57)

# the last block is for getting photos and saving them to directory
count = 1
for link in photoArr:
    url = link
    response = urllib.request.urlopen(url).read()  # becoming a photo as a bytearray
    number = '{0:0>4}'.format(count)  # giving a beautiful look to images' names
    print(number)

    # saving photo to 'saveDir' direcroty
    filename = saveDir + "\\" + number + ".jpg"
    with open(filename, 'wb') as imgfile:
        imgfile.write(response)
    count += 1

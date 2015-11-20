import cv2

path = '/home/godel/opencv/opencv-examples/images/'
# insere o olho do cebolinha no lugar do oculos do GUIDO
# e na parte de cima da imagem do guido nova,
#  insere a logo do python


def get_olho(img):
    x, y, _ = img.shape
    x0, y0 = int(x/4), int(y/4)
    img2 = img[x0:x0*2, y0*2:y0*3]
    img2 = cv2.resize(img2, None, fx=4, fy=2,interpolation=cv2.INTER_CUBIC)
    return img2


def insert_guido(guido, olhos):
    x, y, _ = guido.shape
    ox, oy, _ = olhos.shape
    x0, y0 = int(x/4), int(y/4)
    guido[(ox*2)-50: (ox*3)-50, y0+50:oy+y0+50] = olhos
    return guido


def insert_logo(guidoceb, logo):
    x, y, _ = guidoceb.shape
    logo = cv2.resize(logo, None, fx=0.5, fy=0.5)
    lx, ly, _ = logo.shape 
    guidoceb[0:lx, 90:ly+90] = logo
    return guidoceb

# load imagens
cebol = cv2.imread(path+'chola.png')
guido = cv2.imread(path+'guido.jpg')
logo = cv2.imread(path+'python.png')

# pega os olhos
olhos_cebol = get_olho(cebol)
# insere no guido
guido_cebol = insert_guido(guido, olhos_cebol)
# insere a logo do python
image_final = insert_logo(guido_cebol, logo)
# salva a imagem
cv2.imwrite(path+"guidolinha.jpg", image_final)

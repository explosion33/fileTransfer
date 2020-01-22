import qrcode
import PIL
import sys, pygame

# change run state back to True
file = open("pgSettings.txt", "w")
file.write("True")
file.close()

# creates a QR image 
def createQR(data):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(str(data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    return img

# save image as PNG
qr = createQR(str(sys.argv[1])).convert("RGB")
qr.save("qr.png")

# initialize pygame screen, icon, and title
pygame.init()
pygame.display.set_caption('File Trnasfer')

ico = pygame.image.load("icon.png")
pygame.display.set_icon(ico)

size = (740,740)
screen = pygame.display.set_mode(size)
screen.fill((255,255,255))

# load QR image as surface
py_image = pygame.image.load("qr.png")
py_image = pygame.transform.scale(py_image, size)

RUN = "True"

while RUN == "True":
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(py_image, (0,0))
    pygame.display.flip()

    # check if RUN is false and should exit
    file = open("pgSettings.txt", "r")
    RUN = file.read()

import qrcode
img = qrcode.make("https://www.linkedin.com/in/syed-akber-shah-a03547234/") #yahan inverted commas k andar kuch bhi likh do uska qr code bn jayga
print(type(img))
img.save("akber-linkedin.png")
print('QR Code Generated')
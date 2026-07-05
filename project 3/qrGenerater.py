import qrcode

# Take the text or URL that should be encoded into the QR code
data = input('Enter the text or URL: ').strip()

# Take the filename to save the generated QR code image as
filename = input('Enter the filename: ').strip()

# Create a QRCode object
# box_size -> size of each box (pixel block) in the QR code
# border -> thickness of the white border around the QR code
qr = qrcode.QRCode(box_size=10, border=4)

# Add the data that needs to be encoded
qr.add_data(data)

# Generate the actual QR code image
# fill_color -> color of the QR pattern
# back_color -> background color of the image
image = qr.make_image(fill_color='black', back_color='white')

# Save the generated image to disk with the given filename
image.save(filename)

print(f'QR code saved as {filename}')
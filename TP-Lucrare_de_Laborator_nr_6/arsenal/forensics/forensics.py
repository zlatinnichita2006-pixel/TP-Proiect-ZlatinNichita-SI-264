
# Partea 2

# B1
print("=" * 80)
print("B1")

def tip_real(cale):
    cap = open(cale, "rb").read(8)
    if cap.startswith(b"%PDF"):
        return "pdf"
    elif cap.startswith(b"\x89PNG"):
        return "png"
    elif cap.startswith(b"\xff\xd8"):
        return "jpg"
    elif cap.startswith(b"PK\x03\x04"):
        return "zip/docx"
    else:
         return cap.hex()
print(tip_real("../../foto.jpg"))
print(tip_real("../../ascuns.png"))

# B2
print("=" * 80)
print("B2")

import re
date = open("../../ascuns.png", "rb").read()
for m in re.findall(rb"[ -~]{4,}", date):
    print(m.decode())


# B3
print("=" * 80)
print("B3")

from PIL import Image
from PIL.ExifTags import TAGS

exif = Image.open("../../foto.jpg")._getexif() or {}
for id, val in exif.items():
    print(TAGS.get(id, id), "=", val)

if 34853 in exif:
    gps = exif[34853]
    lat_dms = gps[2]
    lat_ref = gps[1]
    lon_dms = gps[4]
    lon_ref = gps[3] 


    lat_dms_zec = float(lat_dms[0] + (lat_dms[1]/60) + (lat_dms[2]/3600))
    lon_dms_zec = float(lon_dms[0] + (lon_dms[1]/60) + (lon_dms[2]/3600))

    if lat_ref == "S":
          lat_dms_zec =  lat_dms_zec * -1
    if lon_ref  == "V" or lon_ref  == "W":
        lon_dms_zec = lon_dms_zec * -1

    print("Latitudine:", lat_dms_zec)
    print("Longitudine:", lon_dms_zec)



# B4
print("=" * 80)
print("B4")
   
date = open("../../ascuns.png", "rb").read()
i = date.find(b"PK\x03\x04")
if i != -1:
    variabila = date[i:]
    with open("gasit.zip", "wb") as file:
        file.write(variabila)
    print("arhiva extrasa de la octetul", i)


# B5
print("=" * 80)
print("B5")

from PIL import Image
img = Image.open("../../foto.jpg").convert("RGB")
px = list(img.getdata())
mesaj = b"FLAG{ascuns_in_pixeli}"
biti = "".join(f"{x:08b}" for x in mesaj)
px_nou = []
for i, (r, g, b) in enumerate(px):
    if i < len(biti):
        bit = int(biti[i])
        r = (r & ~1) | bit
    px_nou.append((r, g, b))

img.putdata(px_nou)
img.save("stego.png")



# B6
print("=" * 80)
print("B6")

px = list(Image.open("stego.png").convert("RGB").getdata())
biti = ""
for (r, g, b) in px:
    biti += str(r & 1)

octeti = []
for i in range(0, len(biti), 8):
    octet = biti[i:i+8]
    if len(octet) < 8:
        break
    valoare = int(octet, 2)
    if valoare == 0:
        break
    octeti.append(valoare)

text = "".join(chr(o) for o in octeti)
print(text)

print("=" * 80)
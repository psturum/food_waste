import qrcode
from PIL import Image

Vegetable = qrcode.make('Vegetable-data')
Fruit = qrcode.make('Fruit-data')
Meat = qrcode.make('Meat-data')
Dairy = qrcode.make('Dairy-data')
Non_organic = qrcode.make('Non_organic-data')
Organic = qrcode.make('Organic-data')
Grains = qrcode.make('Grains-data')

Vegetable.save("Vegetable.png")
Grains.save("Grains.png")
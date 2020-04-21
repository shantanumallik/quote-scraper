from flask import Flask, jsonify
from flask_cors import CORS
from dbhandler import *
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_quote():
    data=getQuote()
    img = Image.new('RGB', (1600, 1200), color = (73, 109, 137))
    font=ImageFont.truetype("AmaticSC-Regular.ttf", 48, encoding="unic")
    d = ImageDraw.Draw(img)
    d.text((300,300), data[0][1], font=font, fill=(255,255,0))
    img.save('pil_text.png')
    return jsonify(id=data[0][0],
                   quote=data[0][1])

if __name__ == "__main__":
    app.run()



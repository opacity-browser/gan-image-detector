from flask import Flask, request, jsonify
from detect_gan_image import detect_gan_image

app = Flask(__name__)

@app.route('/detect', methods=['GET'])
def detect():
  img_url = request.args.get('imgUrl')
    
  if not img_url:
    return jsonify({"error": "imgUrl parameter is required"}), 400

  try:
    print(f"Processing image URL: {img_url}")
    is_gan = detect_gan_image(img_url)
    return jsonify({"is_gan": is_gan})
  except Exception as e:
    print(f"Error in detect route: {e}")
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777)
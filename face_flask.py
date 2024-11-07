# 接口：8000

# 人脸识别
from flask import Flask, request, jsonify
import face_recognition
import os

app = Flask(__name__)

@app.route('/detectface', methods=['POST'])
def detect_face():
    # 获取 faceid 值，如果未提供，则默认为空字符串
    faceid = request.form.get('faceid', '')

    # 接口调用失败
    if 'facefile' not in request.files:
        return jsonify({"code": 5, "error": "No file part"}), 400

    file = request.files['facefile']
    if file.filename == '':
        return jsonify({"code": 5, "error": "No selected file"}), 400

    if file:
        # 保存临时文件
        filepath = os.path.join('/tmp', file.filename)
        file.save(filepath)

        # 加载图片并检测人脸
        image = face_recognition.load_image_file(filepath)
        face_locations = face_recognition.face_locations(image)

        # 清理临时文件
        os.remove(filepath)

        # 接口调用成功，返回检测结果
        if len(face_locations) == 0:
            return jsonify({
                "code": 0,
                "message": "error",
                "data": {
                    "faceid":faceid,
                    "detect": 0,  # 未检测到人脸
                } ,
            }), 200
        else:
            return jsonify({
                "code": 0,
                "message": "OK",
                "data": {
                    "faceid":faceid,
                    "detect": 1,  # 检测到人脸
                },
                
            }), 200

if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')

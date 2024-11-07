import gradio as gr
import face_recognition

def detect_and_warn(image_path):
    # 加载图片并检测人脸
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)

    # 检测是否有人脸
    if len(face_locations) == 0:
        return "未检测到人脸，请重新上传图片。"
    else:
        return f"检测到{len(face_locations)}张人脸，可以继续执行后续操作。"

def main():
    with gr.Blocks() as demo:
        with gr.Row():
            with gr.Column():
                # 图片上传组件
                image_input = gr.Image(label="上传图片", type="filepath")
                # 用于显示警告或确认消息的文本框
                message_output = gr.Textbox(label="信息")
                # 检测按钮
                detect_button = gr.Button("检测人脸")

        detect_button.click(fn=detect_and_warn, inputs=image_input, outputs=message_output)

    return demo

if __name__ == "__main__":
    face_detect_demo = main()
    face_detect_demo.launch(server_port=7998, server_name='0.0.0.0')

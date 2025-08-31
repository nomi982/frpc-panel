# app.py
from flask import Flask, render_template, request, jsonify, send_file
import tomli
import tomli_w
import os

app = Flask(__name__)

# 配置
TOML_FILE_PATH = "frpc.toml"  # 默认TOML文件路径

@app.route('/')
def index():
    """主页面，显示TOML编辑器"""
    return render_template('index.html')

@app.route('/api/read_toml', methods=['GET'])
def read_toml():
    """读取TOML文件内容"""
    file_path = request.args.get('file_path', TOML_FILE_PATH)
    
    try:
        if not os.path.exists(file_path):
            return jsonify({"error": f"文件 {file_path} 不存在"}), 404
            
        with open(file_path, 'rb') as f:
            data = tomli.load(f)
            
        return jsonify({"content": data, "file_path": file_path})
    except Exception as e:
        return jsonify({"error": f"读取文件时出错: {str(e)}"}), 500

@app.route('/api/write_toml', methods=['POST'])
def write_toml():
    """写入TOML文件内容"""
    data = request.json
    content = data.get('content', {})
    file_path = data.get('file_path', TOML_FILE_PATH)
    
    try:
        # 确保目录存在
        if os.path.dirname(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, 'wb') as f:
            # 使用tomli-w的dump函数，它会自动处理字符串引号
            tomli_w.dump(content, f)
            
        return jsonify({"message": "文件保存成功", "file_path": file_path})
    except Exception as e:
        return jsonify({"error": f"保存文件时出错: {str(e)}"}), 500

@app.route('/api/list_files', methods=['GET'])
def list_files():
    """列出当前目录下的TOML文件"""
    directory = request.args.get('directory', '.')
    try:
        files = [f for f in os.listdir(directory) if f.endswith('.toml')]
        return jsonify({"files": files, "directory": directory})
    except Exception as e:
        return jsonify({"error": f"读取目录时出错: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

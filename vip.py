from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 配置 CORS，允许所有来源的请求
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://vip-video-player.li2901607140.workers.dev"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route('/api/open_site', methods=['GET', 'OPTIONS'])
def open_site():
    if request.method == 'OPTIONS':
        return '', 200
    site = request.args.get('site')
    sites = {
        'iqiyi': 'https://www.iqiyi.com',
        'tencent': 'https://v.qq.com',
        'youku': 'https://www.youku.com/'
    }
    
    if site in sites:
        url = sites[site]
        
        # 返回URL，让前端打开
        return jsonify({'success': True, 'url': url})
    else:
        return jsonify({'success': False, 'message': '未知网站'})

@app.route('/api/parse_video', methods=['POST', 'OPTIONS'])
def parse_video():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.json
    video_url = data.get('video_url')
    
    if not video_url:
        return jsonify({'success': False, 'message': '视频URL不能为空'})
    
    # 返回解析后的URL
    parsed_url = 'https://jx.xmflv.cc/?url=' + video_url
    return jsonify({'success': True, 'parsed_url': parsed_url})

if __name__ == '__main__':
    # 开发环境使用
    app.run(debug=True, port=5000) 
from http.server import BaseHTTPRequestHandler
import json

def handle_request(event):
    try:
        # 获取请求体
        body = json.loads(event.get('body', '{}'))
        video_url = body.get('video_url')
        
        if not video_url:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({'success': False, 'message': '视频URL不能为空'})
            }
        
        # 返回解析后的URL
        parsed_url = 'https://jx.xmflv.cc/?url=' + video_url
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'success': True, 'parsed_url': parsed_url})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'success': False, 'message': str(e)})
        }

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 处理 CORS 预检请求
        if self.path == '/api/parse_video' and self.headers.get('Access-Control-Request-Method'):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            return

        # 处理实际请求
        if self.path == '/api/parse_video':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            
            response = handle_request({
                'body': body.decode('utf-8')
            })
            
            self.send_response(response['statusCode'])
            for header, value in response['headers'].items():
                self.send_header(header, value)
            self.end_headers()
            self.wfile.write(response['body'].encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 
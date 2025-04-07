from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs
import json

def handle_request(event):
    # 获取查询参数
    query_string = event.get('queryStringParameters', {}) or {}
    site = query_string.get('site', [''])[0]
    
    sites = {
        'iqiyi': 'https://www.iqiyi.com',
        'tencent': 'https://v.qq.com',
        'youku': 'https://www.youku.com/'
    }
    
    if site in sites:
        url = sites[site]
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'success': True, 'url': url})
        }
    else:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'success': False, 'message': '未知网站'})
        }

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 处理 CORS 预检请求
        if self.path == '/api/open_site' and self.headers.get('Access-Control-Request-Method'):
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            return

        # 处理实际请求
        if self.path.startswith('/api/open_site'):
            response = handle_request({
                'queryStringParameters': parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
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
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 
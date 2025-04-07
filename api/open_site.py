from cloudflare_workers import Worker, Response
import json

def handle_request(request):
    # 获取查询参数
    url = request.url
    params = dict(url.searchParams)
    site = params.get('site', '')
    
    sites = {
        'iqiyi': 'https://www.iqiyi.com',
        'tencent': 'https://v.qq.com',
        'youku': 'https://www.youku.com/'
    }
    
    if site in sites:
        url = sites[site]
        return Response(
            json.dumps({'success': True, 'url': url}),
            headers={
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        )
    else:
        return Response(
            json.dumps({'success': False, 'message': '未知网站'}),
            status=400,
            headers={
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        )

worker = Worker()

@worker.route('/api/open_site', methods=['GET', 'OPTIONS'])
def open_site(request):
    if request.method == 'OPTIONS':
        return Response('', headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        })
    return handle_request(request) 
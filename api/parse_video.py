from cloudflare_workers import Worker, Response
import json

async def handle_request(request):
    try:
        # 获取请求体
        body = await request.json()
        video_url = body.get('video_url')
        
        if not video_url:
            return Response(
                json.dumps({'success': False, 'message': '视频URL不能为空'}),
                status=400,
                headers={
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                }
            )
        
        # 返回解析后的URL
        parsed_url = 'https://jx.xmflv.cc/?url=' + video_url
        return Response(
            json.dumps({'success': True, 'parsed_url': parsed_url}),
            headers={
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        )
    except Exception as e:
        return Response(
            json.dumps({'success': False, 'message': str(e)}),
            status=500,
            headers={
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            }
        )

worker = Worker()

@worker.route('/api/parse_video', methods=['POST', 'OPTIONS'])
async def parse_video(request):
    if request.method == 'OPTIONS':
        return Response('', headers={
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        })
    return await handle_request(request) 
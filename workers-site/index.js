import { getAssetFromKV } from '@cloudflare/kv-asset-handler'

/**
 * The DEBUG flag will do two things that help during development:
 * 1. we will skip caching on the edge, which makes it easier to
 *    debug.
 * 2. we will return an error message on exception in your Response rather
 *    than the default 404.html page.
 */
const DEBUG = false
const API_BASE_URL = 'http://localhost:5000'  // 修改为本地 Python 后端地址

addEventListener('fetch', event => {
  try {
    event.respondWith(handleEvent(event))
  } catch (e) {
    if (DEBUG) {
      return event.respondWith(
        new Response(e.message || e.toString(), {
          status: 500,
        }),
      )
    }
    event.respondWith(new Response('Internal Error', { status: 500 }))
  }
})

async function handleEvent(event) {
  const url = new URL(event.request.url)
  
  try {
    // 处理 API 请求
    if (url.pathname.startsWith('/api/')) {
      // 创建新的请求，转发到 Vercel 后端
      const apiUrl = new URL(url.pathname + url.search, API_BASE_URL)
      const newRequest = new Request(apiUrl.toString(), {
        method: event.request.method,
        headers: event.request.headers,
        body: event.request.body,
        redirect: 'follow'
      })
      
      return await fetch(newRequest)
    }
    
    // 处理静态资源
    let response = await getAssetFromKV(event)
    
    // 如果资源不存在，返回 index.html
    if (!response) {
      response = await getAssetFromKV(event, {
        mapRequestToAsset: req => new Request(`${new URL(req.url).origin}/index.html`, req),
      })
    }
    
    return response
  } catch (e) {
    // 如果资源不存在，返回 index.html 以支持单页应用路由
    if (e.status === 404) {
      try {
        let notFoundResponse = await getAssetFromKV(event, {
          mapRequestToAsset: req => new Request(`${new URL(req.url).origin}/index.html`, req),
        })

        return new Response(notFoundResponse.body, {
          ...notFoundResponse,
          status: 200,
        })
      } catch (e) {}
    }

    return new Response(e.message || e.toString(), { status: 500 })
  }
}

// 处理 API 请求的函数
async function handleApiRequest(event) {
  const url = new URL(event.request.url)
  
  // 根据不同的 API 路径处理不同的请求
  if (url.pathname === '/api/parse_video') {
    return await handleParseVideo(event)
  }
  
  // 如果没有匹配的 API 路径，返回 404
  return new Response('API not found', { status: 404 })
}

// 处理视频解析 API
async function handleParseVideo(event) {
  try {
    const { video_url } = await event.request.json()
    
    if (!video_url) {
      return new Response(JSON.stringify({
        success: false,
        message: '请提供视频URL'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      })
    }

    // 这里实现你的视频解析逻辑
    // 示例: 为了演示，直接返回一个假的解析结果
    return new Response(JSON.stringify({
      success: true,
      parsed_url: `https://player.example.com/play?url=${encodeURIComponent(video_url)}`
    }), {
      headers: { 'Content-Type': 'application/json' }
    })
  } catch (error) {
    return new Response(JSON.stringify({
      success: false,
      message: '解析失败，请稍后重试'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    })
  }
} 
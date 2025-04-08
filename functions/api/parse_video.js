export async function onRequestPost(context) {
  try {
    const { video_url } = await context.request.json();
    
    if (!video_url) {
      return new Response(JSON.stringify({
        success: false,
        message: '请提供视频URL'
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // 这里添加你的视频解析逻辑
    // 示例：使用第三方API进行解析
    const apiUrl = `https://api.example.com/parse?url=${encodeURIComponent(video_url)}`;
    const response = await fetch(apiUrl);
    const data = await response.json();

    return new Response(JSON.stringify({
      success: true,
      parsed_url: data.url
    }), {
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    return new Response(JSON.stringify({
      success: false,
      message: '解析失败，请稍后重试'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
} 
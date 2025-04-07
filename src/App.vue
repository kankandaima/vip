<template>
  <div class="app-container">
    <div class="video-container">
      <video 
        class="tutorial-video" 
        src="/videos/使用方法视频.mp4"
        controls
        preload="metadata"
        poster="./src/jpg/nian.jpg"
      >
      </video>
    </div>
    <header class="app-header">
      <h1 style="font-size:60px;color:black">VIP视频播放</h1>
      <p style="font-size:30px;color:skyblue">aichifan.xyz</p>
      
      <div class="site-icons">
      <a href="https://www.iqiyi.com" target="_blank" class="site-icon-link">
        <img src="https://www.iqiyi.com/favicon.ico" alt="爱奇艺" class="site-icon">
        <span>爱奇艺</span>
      </a>
      <a href="https://v.qq.com" target="_blank" class="site-icon-link">
        <img src="https://v.qq.com/favicon.ico" alt="腾讯视频" class="site-icon">
        <span>腾讯视频</span>
      </a>
      <a href="https://www.youku.com" target="_blank" class="site-icon-link">
        <img src="https://www.youku.com/favicon.ico" alt="优酷视频" class="site-icon">
        <span>优酷视频</span>
      </a>
    </div>
      
      <div class="input-container">
        <input v-model="videoUrl" type="text" placeholder="请输入VIP视频链接">
        <button @click="clearInput" class="clear-btn">清空</button>
        <button @click="parseVideo" class="play-button">
          <i class="play-icon">▶</i> 播放VIP视频
        </button>
      </div>
    </header>
    
    <div class="main-content">
      <nav class="side-nav">
        <ul>
          <li :class="{ active: currentSite === 'iqiyi' }">
            <a @click.prevent="switchSite('iqiyi')">
              <img src="https://www.iqiyi.com/favicon.ico" alt="爱奇艺" class="site-icon">
              爱奇艺
            </a>
          </li>
          <li :class="{ active: currentSite === 'tencent' }">
            <a @click.prevent="switchSite('tencent')">
              <img src="https://v.qq.com/favicon.ico" alt="腾讯视频" class="site-icon">
              腾讯视频
            </a>
          </li>
          <li :class="{ active: currentSite === 'youku' }">
            <a @click.prevent="switchSite('youku')">
              <img src="https://www.youku.com/favicon.ico" alt="优酷视频" class="site-icon">
              优酷视频
            </a>
          </li>
        </ul>
      </nav>
      
      <main class="app-content">
        <IqiyiContent v-if="currentSite === 'iqiyi'" @load-video="loadVideo" />
        <TencentContent v-if="currentSite === 'tencent'" @load-video="loadVideo" />
        <YoukuContent v-if="currentSite === 'youku'" @load-video="loadVideo" />
      </main>
    </div>
    
    <MessageToast 
      ref="toast"
      :message="toastMessage"
      :type="toastType"
    />
  </div>
</template>

<script>
import axios from 'axios';
import MessageToast from './components/成功或错误操作.vue';
import IqiyiContent from './components/爱奇艺.vue';
import TencentContent from './components/腾讯视频.vue';
import YoukuContent from './components/优酷.vue';
import tutorialVideo from './jpg/使用方法视频.mp4';

export default {
  name: 'App',
  components: {
    MessageToast,
    IqiyiContent,
    TencentContent,
    YoukuContent
  },
  data() {
    return {
      videoUrl: '',
      toastMessage: '',
      toastType: 'info',
      currentSite: 'iqiyi',
      apiBaseUrl: 'http://localhost:5000/api',
      tutorialVideo: tutorialVideo
    };
  },
  methods: {
    switchSite(site) {
      this.currentSite = site;
    },
    clearInput() {
      this.videoUrl = '';
    },
    loadVideo(url) {
      this.videoUrl = url;
    },
    async parseVideo() {
      if (!this.videoUrl) {
        this.showMessage({ type: 'warning', text: '请输入视频网址' });
        return;
      }
      
      try {
        const response = await axios.post(`${this.apiBaseUrl}/parse_video`, {
          video_url: this.videoUrl
        });
        
        if (response.data.success) {
          window.open(response.data.parsed_url, '_blank');
          this.showMessage({ type: 'success', text: '视频解析成功，正在打开...' });
        } else {
          this.showMessage({ type: 'error', text: response.data.message });
        }
      } catch (error) {
        console.error('解析视频失败:', error);
        this.showMessage({ type: 'error', text: '解析视频失败，请检查网络连接' });
      }
    },
    showMessage({ type, text }) {
      this.toastMessage = text;
      this.toastType = type;
      this.$refs.toast.show();
    }
  }
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif;
  background-color: #f5f7fa;
  color: #333;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  min-height: 100vh;
}

.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  min-height: 100vh;
}

.app-header {
  text-align: center;
  margin-bottom: 30px;
  padding: 20px 0;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.app-header h1 {
  font-size: 32px;
  color: #333;
  margin-bottom: 10px;
}

.input-container {
  display: flex;
  margin: 20px auto;
  max-width: 800px;
  align-items: center;
}

.input-container input {
  flex: 1;
  padding: 12px;
  margin-right: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  transition: border 0.3s;
}

.input-container input:focus {
  border-color: #4CAF50;
  outline: none;
}

.clear-btn {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 8px 15px;
  cursor: pointer;
  transition: all 0.3s;
  margin-right: 10px;
}

.clear-btn:hover {
  background-color: #e0e0e0;
}

.play-button {
  background-color: #ff3e3e;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 20px;
  cursor: pointer;
  font-weight: bold;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.play-button:hover {
  background-color: #e62e2e;
  transform: translateY(-2px);
}

.play-icon {
  margin-right: 8px;
  font-size: 14px;
}

.main-content {
  display: flex;
}

.side-nav {
  width: 200px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-right: 20px;
}

.side-nav ul {
  list-style: none;
  padding: 0;
}

.side-nav li {
  margin-bottom: 15px;
}

.side-nav a {
  display: flex;
  align-items: center;
  text-decoration: none;
  color: #333;
  font-weight: bold;
  padding: 10px;
  border-radius: 5px;
  transition: all 0.3s;
  cursor: pointer;
}

.side-nav a:hover {
  background-color: #f5f5f5;
}

.side-nav li.active a {
  background-color: #f0f0f0;
  color: #ff3e3e;
}

.site-icon {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

.app-content {
  flex: 1;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.site-content {
  margin-bottom: 30px;
}

.site-content h2 {
  margin-bottom: 20px;
  padding-bottom: 10px;
  border-bottom: 1px solid #eee;
}

.recommendations {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
}

.recommendation-item {
  border: 1px solid #eee;
  border-radius: 5px;
  padding: 10px;
  transition: all 0.3s;
}

.recommendation-item:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.recommendation-item img {
  width: 100%;
  border-radius: 5px;
  margin-bottom: 10px;
}

.recommendation-item h3 {
  font-size: 16px;
  margin-bottom: 5px;
}

.recommendation-item p {
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.recommendation-item button {
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
  transition: all 0.3s;
  width: 100%;
}

.recommendation-item button:hover {
  background-color: #45a049;
}

.site-icons {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin: 5px 0;
  padding: 5px;
  background-color: #eee;
  border-radius: 5px;
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(3px);
}

.site-icon-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: #333;
  transition: all 0.3s ease;
  padding: 10px;
  border-radius: 12px;
  background-color: #eee;
}

.site-icon-link:hover {
  transform: translateY(-5px);
  background-color: #eee;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

.site-icon {
  width: 48px;
  height: 48px;
  margin-bottom: 12px;
  border-radius: 12px;
  padding: 8px;
  background-color: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.site-icon-link:hover .site-icon {
  transform: scale(1.1);
  box-shadow: 0 4px 15px #eee;
}

.site-icon-link span {
  font-size: 16px;
  font-weight: 600;
  color: #2c3e50;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.video-container {
  position: fixed;
  top: 20px;
  left: 20px;
  z-index: 1000;
  background-color: #fff;
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.video-container:hover {
  transform: scale(1.02);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.tutorial-video {
  width: 300px;
  border-radius: 5px;
  cursor: pointer;
}

@media (max-width: 768px) {
  .app-container {
    padding: 15px;
  }
  
  .app-header h1 {
    font-size: 24px;
  }
  
  .main-content {
    flex-direction: column;
  }
  
  .side-nav {
    width: 100%;
    margin-right: 0;
    margin-bottom: 20px;
  }
  
  .side-nav ul {
    display: flex;
    justify-content: space-between;
  }
  
  .side-nav li {
    margin-bottom: 0;
  }
  
  .input-container {
    flex-direction: column;
  }
  
  .input-container input {
    margin-right: 0;
    margin-bottom: 10px;
  }
  
  .clear-btn {
    margin-right: 0;
    margin-bottom: 10px;
    width: 100%;
  }
  
  .play-button {
    width: 100%;
  }

  .site-icons {
    gap: 20px;
    padding: 15px;
  }

  .site-icon {
    width: 40px;
    height: 40px;
    margin-bottom: 8px;
  }

  .site-icon-link span {
    font-size: 14px;
  }

  .video-container {
    position: relative;
    top: 0;
    left: 0;
    margin: 20px auto;
    width: 100%;
    max-width: 300px;
  }

  .tutorial-video {
    width: 100%;
  }
}
</style>
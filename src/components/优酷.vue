<template>
  <div class="site-content">
    <h2>优酷视频推荐</h2>
    
    <div class="content-nav">
      <ul>
        <li :class="{ active: currentType === 'drama' }">
          <a @click.prevent="switchType('drama')">电视剧</a>
        </li>
        <li :class="{ active: currentType === 'movie' }">
          <a @click.prevent="switchType('movie')">电影</a>
        </li>
        <li :class="{ active: currentType === 'variety' }">
          <a @click.prevent="switchType('variety')">综艺</a>
        </li>
        <li :class="{ active: currentType === 'anime' }">
          <a @click.prevent="switchType('anime')">动漫</a>
        </li>
      </ul>
    </div>
    
    <div class="recommendations" v-if="currentType === 'drama'">
      <div class="recommendation-item" v-for="(item, index) in dramaRecommendations" :key="index">
        <img :src="item.image" :alt="item.title">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <button @click="loadVideo(item.url)">观看</button>
      </div>
    </div>
    
    <div class="recommendations" v-if="currentType === 'movie'">
      <div class="recommendation-item" v-for="(item, index) in movieRecommendations" :key="index">
        <img :src="item.image" :alt="item.title">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <button @click="loadVideo(item.url)">观看</button>
      </div>
    </div>
    
    <div class="recommendations" v-if="currentType === 'variety'">
      <div class="recommendation-item" v-for="(item, index) in varietyRecommendations" :key="index">
        <img :src="item.image" :alt="item.title">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <button @click="loadVideo(item.url)">观看</button>
      </div>
    </div>
    
    <div class="recommendations" v-if="currentType === 'anime'">
      <div class="recommendation-item" v-for="(item, index) in animeRecommendations" :key="index">
        <img :src="item.image" :alt="item.title">
        <h3>{{ item.title }}</h3>
        <p>{{ item.description }}</p>
        <button @click="loadVideo(item.url)">观看</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'YoukuContent',
  data() {
    return {
      currentType: 'drama',
      dramaRecommendations: [
        {
          title: '优酷热门电视剧',
          description: '以美之名',
          image: 'https://liangcang-material.alicdn.com/prod/upload/171dd903d1d24e9ca24ff006dfab5fe1.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBTV_JINGXUAN.drawer1.d_zj1_1&s=ecbb7b0542434defa7e5&scm=20140719.manual.48443.show_ecbb7b0542434defa7e5'
        },
        {
          title: '优酷热门电视剧',
          description: '沙尘暴',
          image: 'https://liangcang-material.alicdn.com/prod/upload/708050d7249d4565886639165417e5a0.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBTV_JINGXUAN.drawer1.d_zj1_2&s=dbcb67bec6d04235a82b&scm=20140719.manual.48443.show_dbcb67bec6d04235a82b'
        },
        {
          title: '优酷热门电视剧',
          description: '一人之下',
          image: 'https://liangcang-material.alicdn.com/prod/upload/686558d72dc84de79eb57c1a8165b231.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门电视剧',
          description: '千里挑花一世开',
          image: 'https://liangcang-material.alicdn.com/prod/upload/e04dce91c8c144229ab8bcde192a66c2.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        }
      ],
      movieRecommendations: [
        {
          title: '优酷热门电影',
          description: '速度与激情10',
          image: 'https://liangcang-material.alicdn.com/prod/upload/47357ac205c34f88a4c80773d63cc8b5.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBMOVIE_JINGXUAN.drawer2.d_zj1_2&s=aedcbf2b65b9416fb421&scm=20140719.rcmd.48446.show_aedcbf2b65b9416fb421'
        },
        {
          title: '优酷热门电影',
          description: '变形金刚5最后的骑士',
          image: 'https://liangcang-material.alicdn.com/prod/upload/01c3677ad97e4f008d89432b5e9dc073.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门电影',
          description: '海王',
          image: 'https://liangcang-material.alicdn.com/prod/upload/257c9994834c455bb3357a7472b69350.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门电影',
          description: '孤注一掷',
          image: 'https://liangcang-material.alicdn.com/prod/upload/afcffbb4016445f08c9502661d42b12b.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        }
      ],
      varietyRecommendations: [
        {
          title: '优酷热门综艺',
          description: '盒子里的猫 第二季',
          image: 'https://liangcang-material.alicdn.com/prod/upload/39cc44ef23a148f99a2c631de5a13ae0.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBVARIETY_JINGXUAN.drawer1.d_zj1_1&s=adeb5177f9d74bb5bfa6&scm=20140719.manual.48451.show_adeb5177f9d74bb5bfa6'
        },
        {
          title: '优酷热门综艺',
          description: '无限超越班',
          image: 'https://liangcang-material.alicdn.com/prod/upload/43f43101684c46acaa2df3881d8c4180.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门综艺',
          description: '我是隐藏款',
          image: 'https://liangcang-material.alicdn.com/prod/upload/d1ed3634487e4ce6a04c1a06dd795fc0.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门综艺',
          description: '群英会',
          image: 'https://m.ykimg.com/05840000658E8388C847B71BC2A7BA97?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        }
      ],
      animeRecommendations: [
        {
          title: '优酷热门动漫',
          description: '名侦探柯南',
          image: 'https://liangcang-material.alicdn.com/prod/upload/7eef151176f04423a876c88b2de446d5.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBCOMIC_JINGXUAN.drawer1.d_zj1_6&s=cc003400962411de83b1&scm=20140719.manual.48456.show_cc003400962411de83b1'
        },
        {
          title: '优酷热门动漫',
          description: '沧元图',
          image: 'https://liangcang-material.alicdn.com/prod/upload/f3de74d1df6943f99c967134af12dafe.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门动漫',
          description: '开心锤锤',
          image: 'https://liangcang-material.alicdn.com/prod/upload/c07ca70d075f494788ef7be00ef8cc65.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: ''
        },
        {
          title: '优酷热门动漫',
          description: '神墓',
          image: 'https://liangcang-material.alicdn.com/prod/upload/9c16fe1a0a4e414586e6ac9cc649189c.webp.jpg?x-oss-process=image/resize,w_352/interlace,1/quality,Q_70',
          url: 'https://v.youku.com/video?spm=a2hkl.14919748_WEBCOMIC_JINGXUAN.drawer1.d_zj1_9&s=fcaa728a97b5497a9175&scm=20140719.manual.48456.show_fcaa728a97b5497a9175'
        }
      ]
    };
  },
  methods: {
    switchType(type) {
      this.currentType = type;
    },
    loadVideo(url) {
      this.$emit('load-video', url);
    }
  }
};
</script>

<style scoped>
.content-nav {
  margin-bottom: 20px;
}

.content-nav ul {
  display: flex;
  list-style: none;
  padding: 0;
  border-bottom: 1px solid #eee;
}

.content-nav li {
  margin-right: 20px;
}

.content-nav a {
  display: block;
  padding: 10px 15px;
  color: #333;
  text-decoration: none;
  font-weight: bold;
  cursor: pointer;
}

.content-nav li.active a {
  color: #00a6ff;
  border-bottom: 2px solid #00a6ff;
}
</style> 
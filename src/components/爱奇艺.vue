<template>
  <div class="site-content">
    <h2>爱奇艺推荐</h2>
    
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
  name: 'IqiyiContent',
  data() {
    return {
      currentType: 'drama',
      dramaRecommendations: [
        {
          title: '爱奇艺热门电视剧',
          description: '乌云之上',
          image: 'src/jpg/wyzs.jpg',
          url: 'https://www.iqiyi.com/v_1vu4ie7fpx8.html?a=image&vfrmblk=pca_2_hot&r=6701794845453601&bstp=3&stype=0&block=pca_2_hot&rpage=pcw_dianshiju&rseat=image_1&position=2&vfrm=pcw_dianshiju&vfrmrst=image_1'
        },
        {
          title: '爱奇艺热门电视剧',
          description: '消失的痕迹',
          image: 'src/jpg/xsdhj.jpg',
          url: 'https://www.iqiyi.com/v_dsb5mcling.html?a=image&vfrmblk=pca_2_rank_list_2&r=2646846485329401&bstp=3&stype=0&block=pca_2_rank_list_2&rpage=pcw_dianshiju&rseat=image_2&position=4&vfrm=pcw_dianshiju&vfrmrst=image_2'
        },
        {
          title: '爱奇艺热门电视剧',
          description: '错位',
          image: 'src/jpg/cw.jpg',
          url: 'https://www.iqiyi.com/v_11uoxvywau0.html?a=image&vfrmblk=pca_2_rank_list_2&r=6791637420395001&bstp=3&stype=0&block=pca_2_rank_list_2&rpage=pcw_dianshiju&rseat=image_3&position=4&vfrm=pcw_dianshiju&vfrmrst=image_3'
        },
        {
          title: '爱奇艺热门电视剧',
          description: '北上',
          image: 'src/jpg/bs.jpg',
          url: 'https://www.iqiyi.com/v_21bivc1c9tc.html?a=image&vfrmblk=pca_2_rank_list_1&r=1971422841566301&bstp=3&stype=0&block=pca_2_rank_list_1&rpage=pcw_dianshiju&rseat=image_4&position=4&vfrm=pcw_dianshiju&vfrmrst=image_4'
        }
      ],
      movieRecommendations: [
        {
          title: '爱奇艺热门电影',
          description: '误杀',
          image: 'src/jpg/wusha.jpg',
          url: 'https://www.iqiyi.com/v_1c00si2nsk0.html?vfrmblk=pca_list_perview&bstp=18&e=ba4d987f2ff59d4372f08557fec0976a&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_staging&rseat=area_5&rpage=category_lib.1&position=1&vfrm=category_lib.1&hoverBlock=pca_list_perview&vfrmrst=area_5'
        },
        {
          title: '爱奇艺热门电影',
          description: '749局',
          image: 'src/jpg/749.jpg',
          url: 'https://www.iqiyi.com/v_1xwkjlzbhqw.html?vfrmblk=pca_list_perview&bstp=18&e=ba4d987f2ff59d4372f08557fec0976a&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_staging&rseat=area_24&rpage=category_lib.1&position=1&vfrm=category_lib.1&hoverBlock=pca_list_perview&vfrmrst=area_24'
        },
        {
          title: '爱奇艺热门电影',
          description: '焚城',
          image: 'src/jpg/fen.jpg',
          url: 'https://www.iqiyi.com/v_1uqtiudebc4.html?vfrmblk=pca_list_perview&bstp=18&e=ba4d987f2ff59d4372f08557fec0976a&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_staging&rseat=area_7&rpage=category_lib.1&position=1&vfrm=category_lib.1&hoverBlock=pca_list_perview&vfrmrst=area_7'
        },
        {
          title: '爱奇艺热门电影',
          description: '海贼王：红发歌姬',
          image: 'src/jpg/hongfa.jpg',
          url: 'https://www.iqiyi.com/v_jrtu36pju0.html?vfrmblk=pca_list_perview&bstp=18&e=ba4d987f2ff59d4372f08557fec0976a&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_staging&rseat=area_4&rpage=category_lib.1&position=1&vfrm=category_lib.1&hoverBlock=pca_list_perview&vfrmrst=area_4'
        }
      ],
      varietyRecommendations: [
      {
          title: '爱奇艺热门综艺',
          description: '时代风尚',
          image: 'src/jpg/shidai.jpg',
          url: 'https://www.iqiyi.com/v_23fiz4v2vgc.html?a=image&vfrmblk=pca_6_rank_list_2&r=2560212573777701&bstp=3&stype=0&block=pca_6_rank_list_2&rpage=pcw_zongyi&rseat=image_8&position=4&vfrm=pcw_zongyi&vfrmrst=image_8'
        },
        {
          title: '爱奇艺热门综艺',
          description: '奔跑吧',
          image: 'src/jpg/gogogo.jpg',
          url: 'https://www.iqiyi.com/v_19rro0o1ds.html?a=image&vfrmblk=pca_6_rank_list_5&r=202142401&bstp=3&stype=0&block=pca_6_rank_list_5&rpage=pcw_zongyi&rseat=image_2&position=4&vfrm=pcw_zongyi&vfrmrst=image_2'
        },
        {
          title: '爱奇艺热门综艺',
          description: '五哈',
          image: 'src/jpg/wuhaha.jpg',
          url: 'https://www.iqiyi.com/v_nqd5yh7lg4.html?playrecord=false&rpage=pcw_zongyi&block=pca_6_hot&rseat=image_3&r=2504060966803000&position=2&a=image&bstp=3&stype=0'
        },
        {
          title: '爱奇艺热门综艺',
          description: '种地吧',
          image: 'src/jpg/zhongdi.jpg',
          url: 'https://www.iqiyi.com/v_qt9c4dwzh0.html?playrecord=false&rpage=pcw_zongyi&block=pca_6_hot&rseat=image_1&r=2772786525790200&position=2&a=image&bstp=3&stype=0'
        }
      ],
      animeRecommendations: [
        {
          title: '独播动漫',
          description: '念无双',
          image: 'src/jpg/nian.jpg',
          url: 'https://www.iqiyi.com/v_1cjd7975090.html?vfrmblk=pca_list_perview&bstp=18&e=451d98d3f76ca72b93bf9c37aa8e8157&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_online&rseat=area_23&rpage=category_lib.4&position=1&vfrm=category_lib.4&hoverBlock=pca_list_perview&vfrmrst=area_23'
        },
        {
          title: '独播动漫',
          description: '黑色四叶草',
          image: 'src/jpg/siyecao.jpg',
          url: 'https://www.iqiyi.com/v_19rrdzingg.html?vfrmblk=pca_list_perdoc&r=214955601&block=pca_list_perdoc&rpage=category_lib.4&rseat=image_64&vfrm=category_lib.4&vfrmrst=image_64'
        },
        {
          title: '独播动漫',
          description: '苍兰绝',
          image: 'src/jpg/cang.jpg',
          url: 'hhttps://www.iqiyi.com/v_2e8uk5o6gm0.html?vfrmblk=pca_list_perview&bstp=18&e=451d98d3f76ca72b93bf9c37aa8e8157&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_online&rseat=area_38&rpage=category_lib.4&position=1&vfrm=category_lib.4&hoverBlock=pca_list_perview&vfrmrst=area_38'
        },
        {
          title: '独播动漫',
          description: '海贼王',
          image: 'src/jpg/hai.jpg',
          url: 'https://www.iqiyi.com/v_19rrok4nt0.html?vfrmblk=pca_list_perview&bstp=18&e=451d98d3f76ca72b93bf9c37aa8e8157&block=pca_list_perview&bkt=list_main,greeting_pcw1_e,list_online&rseat=area_1&rpage=category_lib.4&position=1&vfrm=category_lib.4&hoverBlock=pca_list_perview&vfrmrst=area_1'
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
  color: #ff6600;
  border-bottom: 2px solid #ff6600;
}
</style> 
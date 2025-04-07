<template>
  <div class="site-content">
    <h2>腾讯视频推荐</h2>
    
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
  name: 'TencentContent',
  data() {
    return {
      currentType: 'drama',
      dramaRecommendations: [
        {
          title: '腾讯热门电视剧',
          description: '棋士',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200htmlstu1736045822632/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200htmlstu/p41000u31ui.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '我的后半生',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200rb0xufo1743130151183/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200rb0xufo/s4100uvwhla.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '鹊刀门传奇2',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200vashbcc1737520355349/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200vashbcc/j41001q0xxn.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '庆余年第二季',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc002002kqssyu1715223183563/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc002002kqssyu/q4100dpkd26.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '雁回时',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200m92miea1742294504737/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200m92miea/m41004bm6ah.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '值得爱',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200o4ikbtq1735802990111/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200o4ikbtq/r4100irklsg.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '滤镜',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200i5j3efb1740111329299/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200i5j3efb/x4100raa15f.html'
        },
        {
          title: '腾讯热门电视剧',
          description: '似锦',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200fbyr29e1738814419034/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200fbyr29e/p4100nfp6q3.html'
        },



      ],
      movieRecommendations: [
        {
          title: '腾讯热门电影',
          description: '哪吒之魔童闹海',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200tjkzeps1733816869241/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200tjkzeps/m4100h7wyy8.html'
        },
        {
          title: '腾讯热门电影',
          description: '假爸爸',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200pa18nf91738044757094/350?imageView2/2/w/287/h/402',
          url: 'https://v.qq.com/x/cover/mzc00200pa18nf9/t4100x61dbb.html'
        },
        {
          title: '腾讯热门电影',
          description: '间谍过家家 代号：白',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200bafkjvr1738005519850/350?imageView2/2/w/287/h/402',
          url: 'https://v.qq.com/x/cover/mzc00200bafkjvr/v4100x8bf3x.html'
        },
        {
          title: '腾讯热门电影',
          description: '恶行之外',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200ms48zl01734926379176/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200ms48zl0/l410088z32g.html'
        },
        {
          title: '腾讯热门电影',
          description: '大画王',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200jmk5j0k1741922379005/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200jmk5j0k/g410067mrac.html'
        },
        {
          title: '腾讯热门电影',
          description: '因果报应',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200dwcfd4w1731640475895/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200dwcfd4w/x4100336v0f.html'
        },
        {
          title: '腾讯热门电影',
          description: '喜剧之王',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc002002r057wc1740541300458/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc002002r057wc/x4100l0aure.html'
        },
        {
          title: '腾讯热门电影',
          description: '刺猬索尼克3',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200uwc0flc1724815773448/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200uwc0flc/q41002isx1o.html'
        }
      ],
      varietyRecommendations: [
        {
          title: '腾讯热门综艺',
          description: '半熟恋人 第4季',
          image: 'https://puui.qpic.cn/vpic_cover/z4100x51fc1/z4100x51fc1_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc002002jck4mc/i4100pqfo8u.html'
        },
        {
          title: '腾讯热门综艺',
          description: '斗笑社 第3季',
          image: 'https://puui.qpic.cn/vpic_cover/e41003j8e4c/e41003j8e4c_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc002003m81vxv/t4100vzqen4.html'
        },
        {
          title: '腾讯热门综艺',
          description: '开始捉迷藏',
          image: 'https://puui.qpic.cn/vpic_cover/s41003xocmf/s41003xocmf_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc00200n8zc9tb/z4100rq5897.html'
        },
        {
          title: '腾讯热门综艺',
          description: '现在就出发 第2季',
          image: 'https://puui.qpic.cn/vpic_cover/w4100b8kxeq/w4100b8kxeq_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc00200y41tzil/b410012vcz1.html'
        },
        {
          title: '腾讯热门综艺',
          description: '演员请注意',
          image: 'https://puui.qpic.cn/vpic_cover/g4100yrxwi8/g4100yrxwi8_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc002009pn2c2r/m4100k3tji7.html'
        },
        {
          title: '腾讯热门综艺',
          description: '开始推理吧-第二季',
          image: 'https://puui.qpic.cn/vpic_cover/z4100afwnb7/z4100afwnb7_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc00200dyitrcy/j410028qhnv.html'
        },
        {
          title: '腾讯热门综艺',
          description: '最强大脑第12季',
          image: 'https://puui.qpic.cn/vpic_cover/n4100gyj2me/n4100gyj2me_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc00200zl7s8ov/m4100wrt55g.html'
        },
        {
          title: '腾讯热门综艺',
          description: '乐在旅途 第3季',
          image: 'https://puui.qpic.cn/vpic_cover/p410022ildc/p410022ildc_hz.jpg/640?imageView2/2/w/381/h/213',
          url: 'https://v.qq.com/x/cover/mzc00200a3tp0np/x4100aj65c0.html'
        }

      ],
      animeRecommendations: [
        {
          title: '腾讯热门动漫',
          description: '画江湖之不良人第七季',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200s5j9upv1737603032866/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200s5j9upv/s4100vpgxmz.html'
        },
        {
          title: '腾讯热门动漫',
          description: '斗破苍穹年番',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc0020027yzd9e1723195259313/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc0020027yzd9e/q0043cz9x20.html'
        },
        {
          title: '腾讯热门动漫',
          description: '吞噬星空',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/324olz7ilvo2j5f1727746451859/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/324olz7ilvo2j5f/i00350r6rf4.html'
        },
        {
          title: '腾讯热门动漫',
          description: '遮天',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200n53vkqc1740479282101/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200n53vkqc/v0046otbtmj.html'
        },
        {
          title: '腾讯热门动漫',
          description: '仙逆',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc00200aaogpgh1731229785085/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc00200aaogpgh/r0047gdjpw6.html'
        },
        {
          title: '腾讯热门动漫',
          description: '完美世界',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mcv8hkc8zk8lnov1735544792841/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mcv8hkc8zk8lnov/x0036x5qqsr.html'
        },
        {
          title: '腾讯热门动漫',
          description: '剑来',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc0020072zgk611721874669799/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc0020072zgk61/t4100wuibew.html'
        },
        {
          title: '腾讯热门动漫',
          description: '斩神',
          image: 'https://vcover-vt-pic.puui.qpic.cn/vcover_vt_pic/0/mzc002006znrsl71721095123461/350?imageView2/2/w/278/h/391',
          url: 'https://v.qq.com/x/cover/mzc002006znrsl7/u4100kftrz6.html'
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
  color: #2a94e7;
  border-bottom: 2px solid #2a94e7;
}
</style>



<!-- {
  title: '腾讯热门动漫',
  description: '热门动漫',
  image: '',
  url: ''
}, -->
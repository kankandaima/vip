<template>
  <div class="message-toast" :class="[type, { show: visible }]">
    <div class="message-content">
      <i class="message-icon" :class="iconClass"></i>
      <span>{{ message }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MessageToast',
  props: {
    message: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'info',
      validator: value => ['info', 'success', 'warning', 'error'].includes(value)
    },
    duration: {
      type: Number,
      default: 3000
    }
  },
  data() {
    return {
      visible: false,
      timer: null
    };
  },
  computed: {
    iconClass() {
      const icons = {
        info: 'info-icon',
        success: 'success-icon',
        warning: 'warning-icon',
        error: 'error-icon'
      };
      return icons[this.type];
    }
  },
  methods: {
    show() {
      clearTimeout(this.timer);
      this.visible = true;
      
      this.timer = setTimeout(() => {
        this.visible = false;
      }, this.duration);
    },
    hide() {
      this.visible = false;
      clearTimeout(this.timer);
    }
  },
  beforeUnmount() {
    clearTimeout(this.timer);
  }
};
</script>

<style scoped>
.message-toast {
  position: fixed;
  top: -100px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 9999;
  min-width: 300px;
  max-width: 80%;
  padding: 15px 20px;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  opacity: 0;
}

.message-toast.show {
  top: 20px;
  opacity: 1;
}

.message-content {
  display: flex;
  align-items: center;
}

.message-icon {
  margin-right: 10px;
  font-size: 18px;
}

/* 图标样式 */
.info-icon::before {
  content: 'ℹ️';
}

.success-icon::before {
  content: '✅';
}

.warning-icon::before {
  content: '⚠️';
}

.error-icon::before {
  content: '❌';
}

/* 不同类型的消息样式 */
.info {
  background-color: #e6f7ff;
  border: 1px solid #91d5ff;
  color: #1890ff;
}

.success {
  background-color: #f6ffed;
  border: 1px solid #b7eb8f;
  color: #52c41a;
}

.warning {
  background-color: #fffbe6;
  border: 1px solid #ffe58f;
  color: #faad14;
}

.error {
  background-color: #fff2f0;
  border: 1px solid #ffccc7;
  color: #ff4d4f;
}

@media (max-width: 768px) {
  .message-toast {
    min-width: 250px;
  }
}
</style> 
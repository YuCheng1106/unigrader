<script lang="ts" setup>
import { ref } from 'vue';

import {
  Button as AButton,
  Card as ACard,
  Statistic as AStatistic,
  Tag as ATag,
  Upload as AUpload,
  message,
} from 'ant-design-vue';

// 模拟数据
const examDetails = ref({
  name: '2023年秋季学期期中考试',
  createTime: '2023-11-01T08:00:00',
  endTime: '2023-11-30T23:59:59',
  participantCount: 243,
  status: 'active',
});

// 上传状态
const paperFileList = ref([]);
const answerFileList = ref([]);
const uploading = ref(false);

// 时间格式化函数
const formatTime = (timeString: string) => {
  const date = new Date(timeString);
  return date
    .toLocaleString('zh-CN', {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
    })
    .replaceAll('/', '-');
};

// 文件上传前校验
const beforeUpload = (file, type) => {
  const isPDF = file.type === 'application/pdf';
  const isDoc = file.type.includes('msword') || file.type.includes('document');
  const isAllowed = isPDF || isDoc;

  if (!isAllowed) {
    message.error(`只能上传 PDF 或 Word 文件!`);
  }

  // 限制只能上传一个文件
  if (type === 'paper' && paperFileList.value.length > 0) {
    message.warning('只能上传一份试卷文件');
    return false;
  }
  if (type === 'answer' && answerFileList.value.length > 0) {
    message.warning('只能上传一份答案文件');
    return false;
  }

  return isAllowed;
};

// 文件上传处理
const handleUpload = (info, type) => {
  const fileList = [...info.fileList];

  // 限制只保留最新上传的文件
  const latestFile = fileList.slice(-1);

  if (type === 'paper') {
    paperFileList.value = latestFile;
  } else {
    answerFileList.value = latestFile;
  }

  if (info.file.status === 'done') {
    message.success(`${info.file.name} 文件上传成功`);
  } else if (info.file.status === 'error') {
    message.error(`${info.file.name} 文件上传失败`);
  }
};

// 提交上传
const handleSubmit = () => {
  uploading.value = true;
  // 这里添加实际的上传逻辑
  setTimeout(() => {
    uploading.value = false;
    message.success('文件提交成功');
  }, 1500);
};
</script>

<template>
  <ACard title="测验详情" :bordered="false" size="small" class="mb-4">
    <template #extra>
      <ATag color="success">进行中</ATag>
    </template>
    <div class="flex justify-between">
      <div>
        <div class="text-lg font-semibold">{{ examDetails.name }}</div>
        <div class="mt-2 text-gray-500">
          <span>创建时间：{{ formatTime(examDetails.createTime) }}</span>
          <span class="ml-4">
            截止时间：{{ formatTime(examDetails.endTime) }}
          </span>
        </div>
      </div>
      <div>
        <AStatistic title="参与人数" :value="examDetails.participantCount" />
      </div>
    </div>

    <!-- 文件上传区域 -->
    <div class="mt-6">
      <div class="mb-4">
        <h4 class="mb-2 font-medium">试卷文件上传</h4>
        <AUpload
          v-model:file-list="paperFileList"
          :before-upload="(file) => beforeUpload(file, 'paper')"
          :custom-request="() => {}"
          @change="(info) => handleUpload(info, 'paper')"
          :max-count="1"
          accept=".pdf,.doc,.docx"
        >
          <AButton>点击上传试卷</AButton>
          <template #tip>
            <div class="mt-1 text-xs text-gray-500">
              支持 PDF 或 Word 格式，文件大小不超过 10MB
            </div>
          </template>
        </AUpload>
      </div>

      <div class="mb-4">
        <h4 class="mb-2 font-medium">答案文件上传</h4>
        <AUpload
          v-model:file-list="answerFileList"
          :before-upload="(file) => beforeUpload(file, 'answer')"
          :custom-request="() => {}"
          @change="(info) => handleUpload(info, 'answer')"
          :max-count="1"
          accept=".pdf,.doc,.docx"
        >
          <AButton>点击上传答案</AButton>
          <template #tip>
            <div class="mt-1 text-xs text-gray-500">
              支持 PDF 或 Word 格式，文件大小不超过 10MB
            </div>
          </template>
        </AUpload>
      </div>

      <AButton
        type="primary"
        :loading="uploading"
        :disabled="paperFileList.length === 0 || answerFileList.length === 0"
        @click="handleSubmit"
      >
        提交文件
      </AButton>
    </div>
  </ACard>
</template>

<style scoped>
/* 自定义样式 */
.mb-4 {
  margin-bottom: 1rem;
}
.text-lg {
  font-size: 1.125rem;
}
.font-semibold {
  font-weight: 600;
}
.text-gray-500 {
  color: #6b7280;
}
.ml-4 {
  margin-left: 1rem;
}
.mt-2 {
  margin-top: 0.5rem;
}
.mt-6 {
  margin-top: 1.5rem;
}
.mb-2 {
  margin-bottom: 0.5rem;
}
.flex {
  display: flex;
}
.justify-between {
  justify-content: space-between;
}
.font-medium {
  font-weight: 500;
}
</style>

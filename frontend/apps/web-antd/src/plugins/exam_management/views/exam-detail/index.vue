<script lang="ts" setup>
import type { VbenFormProps } from '@vben/common-ui';

import type {
  OnActionClickParams,
  VxeTableGridOptions,
} from '#/adapter/vxe-table';
import type { MyUserInfo } from '#/api';
import type {
  CreateSysExamParams,
  SysExamResult,
} from '#/plugins/exam_management/api';

import { computed, onMounted, ref } from 'vue';

import { Page, useVbenDrawer, useVbenModal } from '@vben/common-ui';
import { $t } from '@vben/locales';
import { traverseTreeValues } from '@vben/utils';

import { Card as ACard, message } from 'ant-design-vue';

import { useVbenForm } from '#/adapter/form';
import { useVbenVxeGrid } from '#/adapter/vxe-table';
import { getSysRoleMenuApi, getUserInfoApi } from '#/api';
import {
  createSysExamApi,
  deleteSysExamApi,
  getSysExamListApi,
  updateSysExamApi,
} from '#/plugins/exam_management/api/exam';

import { querySchema, schema, useColumns } from './data';
import ExamInfoCard from './paper-detail-card.vue';
import ExtraDrawer from './perm-drawer.vue';

const userinfo = ref<MyUserInfo>();

const fetchUserInfo = async () => {
  try {
    userinfo.value = await getUserInfoApi();
  } catch (error) {
    console.error(error);
  }
};

const formOptions: VbenFormProps = {
  collapsed: true,
  showCollapseButton: true,
  submitButtonOptions: {
    content: $t('common.form.query'),
  },
  schema: querySchema,
};

const gridOptions: VxeTableGridOptions<SysExamResult> = {
  rowConfig: {
    keyField: 'id',
  },
  checkboxConfig: {
    highlight: true,
  },
  height: 'auto',
  exportConfig: {},
  printConfig: {},
  toolbarConfig: {
    export: true,
    print: true,
    refresh: { code: 'query' },
    custom: true,
    zoom: true,
  },
  columns: useColumns(onActionClick),
  proxyConfig: {
    ajax: {
      query: async ({ page }, formValues) => {
        return await getSysExamListApi({
          page: page.currentPage,
          size: page.pageSize,
          ...formValues,
        });
      },
    },
  },
};

const [Grid, girdApi] = useVbenVxeGrid({ formOptions, gridOptions });

function onRefresh() {
  girdApi.query();
}

function onActionClick({ code, row }: OnActionClickParams<SysExamResult>) {
  switch (code) {
    case 'delete': {
      deleteSysExamApi([row.id]).then(() => {
        message.success({
          content: $t('ui.actionMessage.deleteSuccess', [row.name]),
          key: 'action_process_msg',
        });
        onRefresh();
      });
      break;
    }
    case 'edit': {
      modalApi.setData(row).open();
      break;
    }
    case 'perm': {
      // 改成跳转到/exam/${row.id}
      // router.push(`/exam/${row.id}`);
      openDrawer(row.id);
      break;
    }
  }
}

const [Form, formApi] = useVbenForm({
  layout: 'vertical',
  showDefaultActions: false,
  schema,
});

interface formSysExamParams extends CreateSysExamParams {
  id?: number;
}

const formData = ref<formSysExamParams>();

const modalTitle = computed(() => {
  return formData.value?.id
    ? $t('ui.actionTitle.edit', ['测验'])
    : $t('ui.actionTitle.create', ['测验']);
});

const [Modal, modalApi] = useVbenModal({
  destroyOnClose: true,
  async onConfirm() {
    const { valid } = await formApi.validate();
    if (valid) {
      modalApi.lock();
      const data = await formApi.getValues<CreateSysExamParams>();
      try {
        if (!userinfo.value) await fetchUserInfo(); // 确保用户数据存在

        await (formData.value?.id
          ? updateSysExamApi(formData.value.id, data)
          : createSysExamApi({
              ...data,
              creator_id: userinfo.value?.id || 1,
            }));
        await modalApi.close();
        onRefresh();
      } finally {
        modalApi.unlock();
      }
    }
  },
  onOpenChange(idOpen) {
    if (idOpen) {
      const data = modalApi.getData<formSysExamParams>();
      formApi.resetForm();
      if (data) {
        formData.value = data;
        formApi.setValues(data);
      }
    }
  },
});

const [Drawer, drawerApi] = useVbenDrawer({
  connectedComponent: ExtraDrawer,
});

const openDrawer = async (pk: number) => {
  try {
    const roleMenu = await getSysRoleMenuApi(pk);
    drawerApi
      .setData({
        pk,
        checkedRoleMenu: traverseTreeValues(roleMenu, (item: any) => item.id),
      })
      .open();
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  fetchUserInfo();
});
</script>

<template>
  <Page auto-content-height>
    <!-- 顶部详情卡片 -->
    <ExamInfoCard />

    <!-- 中间表格 -->
    <Grid />

    <!-- 底部分析卡片 -->
    <ACard title="数据分析" :bordered="false" size="small" class="mt-4">
      <div class="grid grid-cols-3 gap-4">测验分析</div>
    </ACard>

    <!-- 弹窗和抽屉 -->
    <Modal :title="modalTitle">
      <Form />
    </Modal>
    <Drawer />
  </Page>
</template>

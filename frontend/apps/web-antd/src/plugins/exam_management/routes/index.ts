import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    name: 'exam',
    path: '/exam',
    component: () =>
      import('#/plugins/exam_management/views/exam-list/index.vue'),
    meta: {
      icon: 'mingcute:profile-line',
      title: '测验管理',
      hideInMenu: false,
    },
  },
  {
    name: 'exam-details',
    path: '/exam/:id',
    component: () =>
      import('#/plugins/exam_management/views/exam-detail/index.vue'),
    meta: {
      icon: 'mingcute:profile-line',
      title: '测验详情',
      hideInMenu: true,
    },
    props: true,
  },
];

export default routes;

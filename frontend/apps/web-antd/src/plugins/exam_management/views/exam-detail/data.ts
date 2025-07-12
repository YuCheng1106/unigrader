import type { VbenFormSchema } from '#/adapter/form';
import type { OnActionClickFn, VxeGridProps } from '#/adapter/vxe-table';
import type { SysRoleResult } from '#/api';
import type { SysExamResult } from '#/plugins/exam_management/api';

import { $t } from '@vben/locales';

export const querySchema: VbenFormSchema[] = [
  {
    component: 'Input',
    fieldName: 'name',
    label: '姓名',
  },
  {
    component: 'Select',
    componentProps: {
      allowClear: true,
      options: [
        {
          label: '待提交',
          value: 1,
        },
        {
          label: '已停用',
          value: 0,
        },
        {
          label: '已提交',
          value: 2,
        },
        {
          label: '批改中',
          value: 3,
        },
        {
          label: '待审核',
          value: 4,
        },
        {
          label: '已完成',
          value: 5,
        },
      ],
    },
    fieldName: 'status',
    label: $t('common.form.status'),
  },
];

export function useColumns(
  onActionClick?: OnActionClickFn<SysExamResult>,
): VxeGridProps['columns'] {
  return [
    {
      field: 'seq',
      title: $t('common.table.id'),
      type: 'seq',
      width: 50,
    },
    { field: 'name', title: '姓名' },
    {
      field: 'status',
      title: '状态',
      cellRender: {
        name: 'CellTag',
      },
      width: 100,
    },
    { field: 'remark', title: '得分' },
    { field: 'remark', title: '评语' },
    {
      field: 'created_time',
      title: $t('common.table.created_time'),
      width: 168,
    },
    {
      field: 'updated_time',
      title: $t('common.table.updated_time'),
      width: 168,
    },
    {
      field: 'operation',
      title: $t('common.table.operation'),
      align: 'center',
      fixed: 'right',
      width: 200,
      cellRender: {
        attrs: {
          nameField: 'name',
          onClick: onActionClick,
        },
        name: 'CellOperation',
        options: [
          {
            code: 'perm',
            text: '查看',
          },
          'edit',
          {
            code: 'delete',
            text: '删除',
          },
        ],
      },
    },
  ];
}

export const schema: VbenFormSchema[] = [
  {
    component: 'Input',
    fieldName: 'name',
    label: '测验名称',
    rules: 'required',
  },
  {
    component: 'Select',
    componentProps: {
      allowClear: true,
      options: [
        { label: '一年级一班', value: 'class1' },
        { label: '一年级二班', value: 'class2' },
        { label: '二年级一班', value: 'class3' },
        { label: '二年级二班', value: 'class4' },
        { label: '三年级一班', value: 'class5' },
        { label: '三年级二班', value: 'class6' },
      ],
    },
    defaultValue: 'class1',
    fieldName: 'banji',
    label: '班级',
    rules: 'required',
  },
  {
    component: 'Select',
    componentProps: {
      allowClear: true,
      options: [
        { label: '语文', value: 'chinese' },
        { label: '数学', value: 'math' },
        { label: '英语', value: 'english' },
      ],
    },
    defaultValue: 'math',
    fieldName: 'subject',
    label: '学科',
    rules: 'required',
  },
  {
    component: 'Textarea',
    fieldName: 'remark',
    label: '备注',
  },
];

export const drawerQuerySchema: VbenFormSchema[] = [
  {
    component: 'Input',
    fieldName: 'title',
    label: '菜单标题',
  },
];

export const drawerColumns: VxeGridProps['columns'] = [
  {
    type: 'checkbox',
    title: '标题',
    align: 'left',
    fixed: 'left',
    treeNode: true,
    minWidth: 150,
  },
  {
    field: 'icon',
    title: '图标',
    slots: { default: 'icon' },
  },
  {
    field: 'type',
    title: '类型',
    cellRender: {
      name: 'CellTag',
      options: [
        { color: 'orange', label: '目录', value: 0 },
        { color: 'default', label: '菜单', value: 1 },
        { color: 'blue', label: '按钮', value: 2 },
        { color: 'warning', label: '内嵌', value: 3 },
        { color: 'success', label: '外链', value: 4 },
      ],
    },
  },
  { field: 'perms', title: '权限标识' },
  { field: 'remark', title: '备注' },
];

export function drawerDataScopeColumns(
  onActionClick?: OnActionClickFn<SysRoleResult>,
): VxeGridProps['columns'] {
  return [
    {
      type: 'checkbox',
      title: '范围名称',
      align: 'left',
      fixed: 'left',
      minWidth: 150,
    },
    {
      field: 'status',
      title: '状态',
      cellRender: {
        name: 'CellTag',
      },
      width: 100,
    },
    {
      field: 'operation',
      title: $t('common.table.operation'),
      align: 'center',
      fixed: 'right',
      width: 200,
      cellRender: {
        attrs: {
          nameField: 'name',
          onClick: onActionClick,
        },
        name: 'CellOperation',
        options: [
          {
            code: 'details',
            text: '规则详情',
          },
        ],
      },
    },
  ];
}

export const drawerDataRuleColumns: VxeGridProps['columns'] = [
  {
    field: 'seq',
    title: $t('common.table.id'),
    type: 'seq',
    width: 50,
  },
  { field: 'name', title: '规则名称' },
];

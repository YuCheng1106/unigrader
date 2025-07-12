import type { RouteRecordStringComponent } from '@vben/types';

import { requestClient } from '#/api/request';

export interface SysExamParams {
  name?: string;
  status?: number;
  page?: number;
  size?: number;
}

export interface SysExamResult {
  id: number;
  creator_id: number;
  name: string;
  banji: string;
  subject: string;
  status: number;
  remark?: string;
  paper_file?: string;
  answer_file?: string;
  created_time: string;
  updated_time: string;
}

export interface CreateSysExamParams {
  name: string;
  status: number;
  banji: string;
  subject: string;
  remark?: string;
  paper_file?: string;
  answer_file?: string;
  creator_id: number;
}

/**
 * 获取测验列表
 */
export async function getSysExamListApi(params: SysExamParams) {
  return requestClient.get<SysExamResult[]>('/api/v1/sys/exams', { params });
}

export async function getAllSysExamApi() {
  return requestClient.get<SysExamResult[]>('/api/v1/sys/exams/all');
}

export async function getSysExamMenuApi(pk: number) {
  return requestClient.get<RouteRecordStringComponent[]>(
    `/api/v1/sys/exams/${pk}/menus`,
  );
}

export async function getSysExamDataScopesApi(pk: number) {
  return requestClient.get<number[]>(`/api/v1/sys/exams/${pk}/scopes`);
}

export async function createSysExamApi(data: CreateSysExamParams) {
  return requestClient.post('/api/v1/sys/exams', data);
}

export async function updateSysExamApi(pk: number, data: CreateSysExamParams) {
  return requestClient.put(`/api/v1/sys/exams/${pk}`, data);
}

export async function updateSysExamMenuApi(pk: number, menus: number[]) {
  return requestClient.put(`/api/v1/sys/exams/${pk}/menus`, { menus });
}

export async function updateSysExamDataScopesApi(pk: number, scopes: number[]) {
  return requestClient.put(`/api/v1/sys/exams/${pk}/scopes`, { scopes });
}

export async function deleteSysExamApi(pks: number[]) {
  return requestClient.delete(`/api/v1/sys/exams`, { data: { pks } });
}

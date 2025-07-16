-- 考试插件菜单和权限初始化

-- 插入考试管理主菜单
insert into sys_menu (id, title, name, path, sort, icon, type, component, perms, status, display, cache, link, remark, parent_id, created_time, updated_time)
values
(1000, '考试管理', 'ExamManagement', '/exam', 10, 'mdi:school', 0, null, null, 1, 1, 1, '', '考试管理模块', null, now(), null);

-- 插入学科管理菜单
insert into sys_menu (id, title, name, path, sort, icon, type, component, perms, status, display, cache, link, remark, parent_id, created_time, updated_time)
values
(1001, '学科管理', 'SubjectManagement', '/exam/subject', 1, 'mdi:book-open-page-variant', 1, '/exam/subject/index', null, 1, 1, 1, '', '学科管理', 1000, now(), null),
(1002, '新增学科', 'AddSubject', null, 0, null, 2, null, 'sys:subject:add', 1, 0, 1, '', null, 1001, now(), null),
(1003, '修改学科', 'EditSubject', null, 0, null, 2, null, 'sys:subject:edit', 1, 0, 1, '', null, 1001, now(), null),
(1004, '删除学科', 'DeleteSubject', null, 0, null, 2, null, 'sys:subject:del', 1, 0, 1, '', null, 1001, now(), null);

-- 插入考试管理菜单
insert into sys_menu (id, title, name, path, sort, icon, type, component, perms, status, display, cache, link, remark, parent_id, created_time, updated_time)
values
(1005, '考试管理', 'ExamManage', '/exam/manage', 2, 'mdi:clipboard-text', 1, '/exam/manage/index', null, 1, 1, 1, '', '考试管理', 1000, now(), null),
(1006, '新增考试', 'AddExam', null, 0, null, 2, null, 'sys:exam:add', 1, 0, 1, '', null, 1005, now(), null),
(1007, '修改考试', 'EditExam', null, 0, null, 2, null, 'sys:exam:edit', 1, 0, 1, '', null, 1005, now(), null),
(1008, '删除考试', 'DeleteExam', null, 0, null, 2, null, 'sys:exam:del', 1, 0, 1, '', null, 1005, now(), null);

-- 插入考试题目管理菜单
insert into sys_menu (id, title, name, path, sort, icon, type, component, perms, status, display, cache, link, remark, parent_id, created_time, updated_time)
values
(1009, '题目管理', 'ExamQuestionManage', '/exam/question', 3, 'mdi:help-circle', 1, '/exam/question/index', null, 1, 1, 1, '', '考试题目管理', 1000, now(), null),
(1010, '新增题目', 'AddExamQuestion', null, 0, null, 2, null, 'sys:exam_question:add', 1, 0, 1, '', null, 1009, now(), null),
(1011, '修改题目', 'EditExamQuestion', null, 0, null, 2, null, 'sys:exam_question:edit', 1, 0, 1, '', null, 1009, now(), null),
(1012, '删除题目', 'DeleteExamQuestion', null, 0, null, 2, null, 'sys:exam_question:del', 1, 0, 1, '', null, 1009, now(), null);

-- 插入班级管理菜单
insert into sys_menu (id, title, name, path, sort, icon, type, component, perms, status, display, cache, link, remark, parent_id, created_time, updated_time)
values
(1013, '班级管理', 'BanjiManage', '/exam/banji', 4, 'mdi:account-group', 1, '/exam/banji/index', null, 1, 1, 1, '', '班级管理', 1000, now(), null),
(1014, '新增班级', 'AddBanji', null, 0, null, 2, null, 'sys:banji:add', 1, 0, 1, '', null, 1013, now(), null),
(1015, '修改班级', 'EditBanji', null, 0, null, 2, null, 'sys:banji:edit', 1, 0, 1, '', null, 1013, now(), null),
(1016, '删除班级', 'DeleteBanji', null, 0, null, 2, null, 'sys:banji:del', 1, 0, 1, '', null, 1013, now(), null);

-- 为测试角色分配考试管理权限
insert into sys_role_menu (id, role_id, menu_id)
values
(1000, 1, 1000),
(1001, 1, 1001),
(1002, 1, 1002),
(1003, 1, 1003),
(1004, 1, 1004),
(1005, 1, 1005),
(1006, 1, 1006),
(1007, 1, 1007),
(1008, 1, 1008),
(1009, 1, 1009),
(1010, 1, 1010),
(1011, 1, 1011),
(1012, 1, 1012),
(1013, 1, 1013),
(1014, 1, 1014),
(1015, 1, 1015),
(1016, 1, 1016);
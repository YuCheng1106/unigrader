/*
 Navicat Premium Dump SQL

 Source Server         : localhost_3306_2
 Source Server Type    : MySQL
 Source Server Version : 80041 (8.0.41)
 Source Host           : localhost:3306
 Source Schema         : fba

 Target Server Type    : MySQL
 Target Server Version : 80041 (8.0.41)
 File Encoding         : 65001

 Date: 14/07/2025 21:30:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sys_banji
-- ----------------------------
DROP TABLE IF EXISTS `sys_banji`;
CREATE TABLE `sys_banji`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '班级名称',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_banji_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '班级表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_banji
-- ----------------------------

-- ----------------------------
-- Table structure for sys_config
-- ----------------------------
DROP TABLE IF EXISTS `sys_config`;
CREATE TABLE `sys_config`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '名称',
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '类型',
  `key` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '键名',
  `value` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '键值',
  `is_frontend` tinyint(1) NOT NULL COMMENT '是否前端',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `key`(`key` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_config_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '参数配置表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_config
-- ----------------------------

-- ----------------------------
-- Table structure for sys_data_rule
-- ----------------------------
DROP TABLE IF EXISTS `sys_data_rule`;
CREATE TABLE `sys_data_rule`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '名称',
  `model` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'SQLA 模型名，对应 DATA_PERMISSION_MODELS 键名',
  `column` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '模型字段名',
  `operator` int NOT NULL COMMENT '运算符（0：and、1：or）',
  `expression` int NOT NULL COMMENT '表达式（0：==、1：!=、2：>、3：>=、4：<、5：<=、6：in、7：not_in）',
  `value` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '规则值',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_data_rule_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '数据规则表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_data_rule
-- ----------------------------
INSERT INTO `sys_data_rule` VALUES (1, '部门名称等于测试', '部门', 'name', 1, 0, '测试', '2025-07-12 23:18:10', NULL);
INSERT INTO `sys_data_rule` VALUES (2, '父部门 ID 等于 1', '部门', 'parent_id', 0, 0, '1', '2025-07-12 23:18:10', NULL);

-- ----------------------------
-- Table structure for sys_data_scope
-- ----------------------------
DROP TABLE IF EXISTS `sys_data_scope`;
CREATE TABLE `sys_data_scope`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '名称',
  `status` int NOT NULL COMMENT '状态（0停用 1正常）',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_data_scope_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '数据范围表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_data_scope
-- ----------------------------
INSERT INTO `sys_data_scope` VALUES (1, '测试部门数据权限', 1, '2025-07-12 23:18:10', NULL);
INSERT INTO `sys_data_scope` VALUES (2, '测试部门及以下数据权限', 1, '2025-07-12 23:18:10', NULL);

-- ----------------------------
-- Table structure for sys_data_scope_rule
-- ----------------------------
DROP TABLE IF EXISTS `sys_data_scope_rule`;
CREATE TABLE `sys_data_scope_rule`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `data_scope_id` bigint NOT NULL COMMENT '数据范围 ID',
  `data_rule_id` bigint NOT NULL COMMENT '数据规则 ID',
  PRIMARY KEY (`id`, `data_scope_id`, `data_rule_id`) USING BTREE,
  UNIQUE INDEX `ix_sys_data_scope_rule_id`(`id` ASC) USING BTREE,
  INDEX `data_scope_id`(`data_scope_id` ASC) USING BTREE,
  INDEX `data_rule_id`(`data_rule_id` ASC) USING BTREE,
  CONSTRAINT `sys_data_scope_rule_ibfk_1` FOREIGN KEY (`data_scope_id`) REFERENCES `sys_data_scope` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_data_scope_rule_ibfk_2` FOREIGN KEY (`data_rule_id`) REFERENCES `sys_data_rule` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_data_scope_rule
-- ----------------------------
INSERT INTO `sys_data_scope_rule` VALUES (1, 1, 1);
INSERT INTO `sys_data_scope_rule` VALUES (2, 2, 1);
INSERT INTO `sys_data_scope_rule` VALUES (3, 2, 2);

-- ----------------------------
-- Table structure for sys_dept
-- ----------------------------
DROP TABLE IF EXISTS `sys_dept`;
CREATE TABLE `sys_dept`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '部门名称',
  `sort` int NOT NULL COMMENT '排序',
  `leader` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '负责人',
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱',
  `status` int NOT NULL COMMENT '部门状态(0停用 1正常)',
  `del_flag` tinyint(1) NOT NULL COMMENT '删除标志（0删除 1存在）',
  `parent_id` bigint NULL DEFAULT NULL COMMENT '父部门ID',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_dept_id`(`id` ASC) USING BTREE,
  INDEX `ix_sys_dept_parent_id`(`parent_id` ASC) USING BTREE,
  CONSTRAINT `sys_dept_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `sys_dept` (`id`) ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '部门表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_dept
-- ----------------------------
INSERT INTO `sys_dept` VALUES (1, '测试', 0, NULL, NULL, NULL, 1, 0, NULL, '2025-07-12 23:18:10', NULL);
INSERT INTO `sys_dept` VALUES (2, '高三八班', 0, '玉麟', '18573071275', '1458927283@qq.com', 1, 0, 1, '2025-07-12 23:20:23', '2025-07-12 23:20:50');

-- ----------------------------
-- Table structure for sys_dict_data
-- ----------------------------
DROP TABLE IF EXISTS `sys_dict_data`;
CREATE TABLE `sys_dict_data`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `type_code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '对应的字典类型编码',
  `label` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '字典标签',
  `value` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '字典值',
  `sort` int NOT NULL COMMENT '排序',
  `status` int NOT NULL COMMENT '状态（0停用 1正常）',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `type_id` bigint NOT NULL COMMENT '字典类型关联ID',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_dict_data_id`(`id` ASC) USING BTREE,
  INDEX `type_id`(`type_id` ASC) USING BTREE,
  CONSTRAINT `sys_dict_data_ibfk_1` FOREIGN KEY (`type_id`) REFERENCES `sys_dict_type` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '字典数据表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_dict_data
-- ----------------------------

-- ----------------------------
-- Table structure for sys_dict_type
-- ----------------------------
DROP TABLE IF EXISTS `sys_dict_type`;
CREATE TABLE `sys_dict_type`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '字典类型名称',
  `code` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '字典类型编码',
  `status` int NOT NULL COMMENT '状态（0停用 1正常）',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `code`(`code` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_dict_type_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '字典类型表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_dict_type
-- ----------------------------

-- ----------------------------
-- Table structure for sys_exam
-- ----------------------------
DROP TABLE IF EXISTS `sys_exam`;
CREATE TABLE `sys_exam`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '考试标题',
  `subject` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '考试的学科',
  `banji` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '考试对应的班级 应该和class表对应',
  `creator_id` bigint NULL DEFAULT NULL COMMENT '创建者的 ID',
  `status` int NOT NULL COMMENT '状态（0：隐藏、1：显示）',
  `paper_file` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '试卷文件链接',
  `answer_file` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '标答文件链接',
  `answer_card` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '答题卡对应链接',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_exam_id`(`id` ASC) USING BTREE,
  INDEX `creator_id`(`creator_id` ASC) USING BTREE,
  CONSTRAINT `sys_exam_ibfk_1` FOREIGN KEY (`creator_id`) REFERENCES `sys_user` (`id`) ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '考试表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_exam
-- ----------------------------

-- ----------------------------
-- Table structure for sys_login_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_login_log`;
CREATE TABLE `sys_login_log`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `user_uuid` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户UUID',
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
  `status` int NOT NULL COMMENT '登录状态(0失败 1成功)',
  `ip` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '登录IP地址',
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '国家',
  `region` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '地区',
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '城市',
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '请求头',
  `os` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '浏览器',
  `device` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '设备',
  `msg` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '提示消息',
  `login_time` datetime NOT NULL COMMENT '登录时间',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_login_log_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '登录日志表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_login_log
-- ----------------------------
INSERT INTO `sys_login_log` VALUES (1, '6bb8dc02-5f33-11f0-ae78-ecd68abaf3f2', 'admin', 1, '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '登录成功', '2025-07-12 23:18:22', '2025-07-12 23:18:22');

-- ----------------------------
-- Table structure for sys_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_menu`;
CREATE TABLE `sys_menu`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '菜单标题',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '菜单名称',
  `path` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '路由地址',
  `sort` int NOT NULL COMMENT '排序',
  `icon` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '菜单图标',
  `type` int NOT NULL COMMENT '菜单类型（0目录 1菜单 2按钮 3内嵌 4外链）',
  `component` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '组件路径',
  `perms` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '权限标识',
  `status` int NOT NULL COMMENT '菜单状态（0停用 1正常）',
  `display` int NOT NULL COMMENT '是否显示（0否 1是）',
  `cache` int NOT NULL COMMENT '是否缓存（0否 1是）',
  `link` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '外链地址',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `parent_id` bigint NULL DEFAULT NULL COMMENT '父菜单ID',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_menu_id`(`id` ASC) USING BTREE,
  INDEX `ix_sys_menu_parent_id`(`parent_id` ASC) USING BTREE,
  CONSTRAINT `sys_menu_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `sys_menu` (`id`) ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1017 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '菜单表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_menu
-- ----------------------------
INSERT INTO `sys_menu` VALUES (1, '概览', 'Dashboard', '/dashboard', 0, 'ant-design:dashboard-outlined', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (2, '分析页', 'Analytics', '/analytics', 0, 'lucide:area-chart', 1, '/dashboard/analytics/index', NULL, 1, 1, 1, '', NULL, 1, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (3, '工作台', 'Workspace', '/workspace', 1, 'carbon:workspace', 1, '/dashboard/workspace/index', NULL, 1, 1, 1, '', NULL, 1, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (4, '系统管理', 'System', '/system', 1, 'eos-icons:admin', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (5, '部门管理', 'SysDept', '/system/dept', 1, 'mingcute:department-line', 1, '/system/dept/index', NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (6, '新增', 'AddSysDept', NULL, 0, NULL, 2, NULL, 'sys:dept:add', 1, 0, 1, '', NULL, 5, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (7, '修改', 'EditSysDept', NULL, 0, NULL, 2, NULL, 'sys:dept:edit', 1, 0, 1, '', NULL, 5, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (8, '删除', 'DeleteSysDept', NULL, 0, NULL, 2, NULL, 'sys:dept:del', 1, 0, 1, '', NULL, 5, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (9, '用户管理', 'SysUser', '/system/user', 2, 'ant-design:user-outlined', 1, '/system/user/index', NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (10, '删除', 'DeleteSysUser', NULL, 0, NULL, 2, NULL, 'sys:user:del', 1, 0, 1, '', NULL, 9, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (11, '角色管理', 'SysRole', '/system/role', 3, 'carbon:user-role', 1, '/system/role/index', NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (12, '新增', 'AddSysRole', NULL, 0, NULL, 2, NULL, 'sys:role:add', 1, 0, 1, '', NULL, 11, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (13, '修改', 'EditSysRole', NULL, 0, NULL, 2, NULL, 'sys:role:edit', 1, 0, 1, '', NULL, 11, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (14, '修改角色菜单', 'EditSysRoleMenu', NULL, 0, NULL, 2, NULL, 'sys:role:menu:edit', 1, 0, 1, '', NULL, 11, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (15, '修改角色数据范围', 'EditSysRoleScope', NULL, 0, NULL, 2, NULL, 'sys:role:scope:edit', 1, 0, 1, '', NULL, 11, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (16, '删除', 'DeleteSysRole', NULL, 0, NULL, 2, NULL, 'sys:role:del', 1, 0, 1, '', NULL, 11, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (17, '菜单管理', 'SysMenu', '/system/menu', 4, 'ant-design:menu-outlined', 1, '/system/menu/index', NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (18, '新增', 'AddSysMenu', NULL, 0, NULL, 2, NULL, 'sys:menu:add', 1, 0, 1, '', NULL, 17, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (19, '修改', 'EditSysMenu', NULL, 0, NULL, 2, NULL, 'sys:menu:edit', 1, 0, 1, '', NULL, 17, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (20, '删除', 'DeleteSysMenu', NULL, 0, NULL, 2, NULL, 'sys:menu:del', 1, 0, 1, '', NULL, 17, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (21, '数据权限', 'SysDataPermission', '/system/data-permission', 5, 'icon-park-outline:permissions', 0, NULL, NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (22, '数据范围', 'SysDataScope', '/system/data-scope', 6, 'cuida:scope-outline', 1, '/system/data-permission/scope/index', NULL, 1, 1, 1, '', NULL, 21, '2025-06-26 20:29:06', '2025-06-26 20:37:26');
INSERT INTO `sys_menu` VALUES (23, '新增', 'AddSysDataScope', NULL, 0, NULL, 2, NULL, 'data:scope:add', 1, 0, 1, '', NULL, 22, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (24, '修改', 'EditSysDataScope', NULL, 0, NULL, 2, NULL, 'data:scope:edit', 1, 0, 1, '', NULL, 22, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (25, '修改数据范围规则', 'EditDataScopeRule', NULL, 0, NULL, 2, NULL, 'data:scope:rule:edit', 1, 0, 1, '', NULL, 22, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (26, '删除', 'DeleteSysDataScope', NULL, 0, NULL, 2, NULL, 'data:scope:del', 1, 0, 1, '', NULL, 22, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (27, '数据规则', 'SysDataRule', '/system/data-rule', 7, 'material-symbols:rule', 1, '/system/data-permission/rule/index', NULL, 1, 1, 1, '', NULL, 21, '2025-06-26 20:29:06', '2025-06-26 20:37:40');
INSERT INTO `sys_menu` VALUES (28, '新增', 'AddSysDataRule', NULL, 0, NULL, 2, NULL, 'data:rule:add', 1, 0, 1, '', NULL, 27, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (29, '修改', 'EditSysDataRule', NULL, 0, NULL, 2, NULL, 'data:rule:edit', 1, 0, 1, '', NULL, 27, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (30, '删除', 'DeleteSysDataRule', NULL, 0, NULL, 2, NULL, 'data:rule:del', 1, 0, 1, '', NULL, 27, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (31, '插件管理', 'SysPlugin', '/system/plugin', 8, 'clarity:plugin-line', 1, '/system/plugin/index', NULL, 1, 1, 1, '', NULL, 4, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (32, '安装', 'InstallSysPlugin', NULL, 0, NULL, 2, NULL, 'sys:plugin:install', 1, 0, 1, '', NULL, 31, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (33, '卸载', 'UninstallSysPlugin', NULL, 0, NULL, 2, NULL, 'sys:plugin:uninstall', 1, 0, 1, '', NULL, 31, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (34, '修改', 'EditSysPlugin', NULL, 0, NULL, 2, NULL, 'sys:plugin:edit', 1, 0, 1, '', NULL, 31, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (35, '任务调度', 'Scheduler', '/scheduler', 2, 'material-symbols:automation', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (36, '调度管理', 'SchedulerManage', '/scheduler/manage', 1, 'ix:scheduler', 1, '/scheduler/manage/index', NULL, 1, 1, 1, '', NULL, 35, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (37, '调度记录', 'SchedulerRecord', '/scheduler/record', 2, 'ix:scheduler', 1, '/scheduler/record/index', NULL, 1, 1, 1, '', NULL, 35, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (38, '日志管理', 'Log', '/log', 3, 'carbon:cloud-logging', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (39, '登录日志', 'LoginLog', '/log/login', 1, 'mdi:login', 1, '/log/login/index', NULL, 1, 1, 1, '', NULL, 38, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (40, '删除', 'DeleteLoginLog', NULL, 0, NULL, 2, NULL, 'log:login:del', 1, 0, 1, '', NULL, 39, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (41, '清空', 'EmptyLoginLog', NULL, 0, NULL, 2, NULL, 'log:login:clear', 1, 0, 1, '', NULL, 39, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (42, '操作日志', 'OperaLog', '/log/opera', 2, 'carbon:operations-record', 1, '/log/opera/index', NULL, 1, 1, 1, '', NULL, 38, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (43, '删除', 'DeleteOperaLog', NULL, 0, NULL, 2, NULL, 'log:opera:del', 1, 0, 1, '', NULL, 42, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (44, '清空', 'EmptyOperaLog', NULL, 0, NULL, 2, NULL, 'log:opera:clear', 1, 0, 1, '', NULL, 42, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (45, '系统监控', 'Monitor', '/monitor', 4, 'mdi:monitor-eye', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (46, '在线用户', 'Online', '/log/online', 1, 'wpf:online', 1, '/monitor/online/index', NULL, 1, 1, 1, '', NULL, 45, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (47, '下线', 'KickOutOnline', NULL, 0, NULL, 2, NULL, 'sys:session:delete', 1, 0, 1, '', NULL, 46, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (48, 'Redis', 'Redis', '/monitor/redis', 2, 'devicon:redis', 1, '/monitor/redis/index', NULL, 1, 1, 1, '', NULL, 45, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (49, 'Server', 'Server', '/monitor/server', 3, 'mdi:server-outline', 1, '/monitor/server/index', NULL, 1, 1, 1, '', NULL, 45, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (50, '项目', 'Project', '/fba', 5, 'https://wu-clan.github.io/picx-images-hosting/logo/fba.png', 0, NULL, NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (51, '文档', 'Document', '/fba/document', 1, 'lucide:book-open-text', 4, '/_core/fallback/iframe.vue', NULL, 1, 1, 1, 'https://fastapi-practices.github.io/fastapi_best_architecture_docs', NULL, 50, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (52, 'Github', 'Github', '/fba/github', 2, 'ant-design:github-filled', 4, '/_core/fallback/iframe.vue', NULL, 1, 1, 1, 'https://github.com/fastapi-practices/fastapi_best_architecture', NULL, 50, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (53, 'Apifox', 'Apifox', '/fba/apifox', 3, 'simple-icons:apifox', 3, '/_core/fallback/iframe.vue', NULL, 1, 1, 1, 'https://apifox.com/apidoc/shared-28a93f02-730b-4f33-bb5e-4dad92058cc0', NULL, 50, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (54, '个人中心', 'Profile', '/profile', 6, 'ant-design:profile-outlined', 1, '/_core/profile/index', NULL, 1, 0, 1, '', NULL, NULL, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (55, '参数管理', 'PluginConfig', '/plugins/config', 7, 'codicon:symbol-parameter', 1, '/plugins/config/views/index', NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', '2025-06-26 20:34:51');
INSERT INTO `sys_menu` VALUES (56, '新增', 'AddConfig', NULL, 0, NULL, 2, NULL, 'sys:config:add', 1, 0, 1, '', NULL, 55, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (57, '修改', 'EditConfig', NULL, 0, NULL, 2, NULL, 'sys:config:edit', 1, 0, 1, '', NULL, 55, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (58, '删除', 'DeleteConfig', NULL, 0, NULL, 2, NULL, 'sys:config:del', 1, 0, 1, '', NULL, 55, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (59, '字典管理', 'PluginDict', '/plugins/dict', 8, 'fluent-mdl2:dictionary', 1, '/plugins/dict/views/index', NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', '2025-06-26 20:35:07');
INSERT INTO `sys_menu` VALUES (60, '新增类型', 'AddDictType', NULL, 0, NULL, 2, NULL, 'dict:type:add', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (61, '修改类型', 'EditDictType', NULL, 0, NULL, 2, NULL, 'dict:type:edit', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (62, '删除类型', 'DeleteDictType', NULL, 0, NULL, 2, NULL, 'dict:type:del', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (63, '新增数据', 'AddDictData', NULL, 0, NULL, 2, NULL, 'dict:data:add', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (64, '修改数据', 'EditDictData', NULL, 0, NULL, 2, NULL, 'dict:data:edit', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (65, '删除数据', 'DeleteDictData', NULL, 0, NULL, 2, NULL, 'dict:data:del', 1, 0, 1, '', NULL, 59, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (66, '通知公告', 'PluginNotice', '/plugins/notice', 9, 'fe:notice-push', 1, '/plugins/notice/views/index', NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', '2025-06-26 20:35:14');
INSERT INTO `sys_menu` VALUES (67, '新增', 'AddNotice', NULL, 0, NULL, 2, NULL, 'sys:notice:add', 1, 0, 1, '', NULL, 66, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (68, '修改', 'EditNotice', NULL, 0, NULL, 2, NULL, 'sys:notice:edit', 1, 0, 1, '', NULL, 66, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (69, '删除', 'DeleteNotice', NULL, 0, NULL, 2, NULL, 'sys:notice:del', 1, 0, 1, '', NULL, 66, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (70, '代码生成', 'PluginCodeGenerator', '/plugins/code-generator', 10, 'tabler:code', 1, '/plugins/code_generator/views/index', NULL, 1, 1, 1, '', NULL, NULL, '2025-06-26 20:29:06', '2025-06-26 20:35:25');
INSERT INTO `sys_menu` VALUES (71, '新增业务', 'AddGenCodeBusiness', '', 0, NULL, 2, NULL, 'codegen:business:add', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', '2025-06-26 20:45:16');
INSERT INTO `sys_menu` VALUES (72, '修改业务', 'EditGenCodeBusiness', NULL, 0, NULL, 2, NULL, 'codegen:business:edit', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (73, '删除业务', 'DeleteGenCodeBusiness', NULL, 0, NULL, 2, NULL, 'codegen:business:del', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (74, '新增模型', 'AddGenCodeModel', NULL, 0, NULL, 2, NULL, 'codegen:model:add', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (75, '修改模型', 'EditGenCodeModel', NULL, 0, NULL, 2, NULL, 'codegen:model:edit', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (76, '删除模型', 'DeleteGenCodeModel', NULL, 0, NULL, 2, NULL, 'codegen:model:del', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (77, '导入', 'ImportGenCode', NULL, 0, NULL, 2, NULL, 'codegen:table:import', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (78, '写入', 'WriteGenCode', NULL, 0, NULL, 2, NULL, 'codegen:local:write', 1, 0, 1, '', NULL, 70, '2025-06-26 20:29:06', NULL);
INSERT INTO `sys_menu` VALUES (1000, '考试管理', 'ExamManagement', '/exam', 10, 'mdi:school', 0, NULL, NULL, 1, 1, 1, '', '考试管理模块', NULL, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1001, '学科管理', 'SubjectManagement', '/exam/subject', 1, 'mdi:book-open-page-variant', 1, '/exam/subject/index', NULL, 1, 1, 1, '', '学科管理', 1000, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1002, '新增学科', 'AddSubject', NULL, 0, NULL, 2, NULL, 'sys:subject:add', 1, 0, 1, '', NULL, 1001, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1003, '修改学科', 'EditSubject', NULL, 0, NULL, 2, NULL, 'sys:subject:edit', 1, 0, 1, '', NULL, 1001, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1004, '删除学科', 'DeleteSubject', NULL, 0, NULL, 2, NULL, 'sys:subject:del', 1, 0, 1, '', NULL, 1001, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1005, '考试管理', 'ExamManage', '/exam/manage', 2, 'mdi:clipboard-text', 1, '/exam/manage/index', NULL, 1, 1, 1, '', '考试管理', 1000, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1006, '新增考试', 'AddExam', NULL, 0, NULL, 2, NULL, 'sys:exam:add', 1, 0, 1, '', NULL, 1005, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1007, '修改考试', 'EditExam', NULL, 0, NULL, 2, NULL, 'sys:exam:edit', 1, 0, 1, '', NULL, 1005, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1008, '删除考试', 'DeleteExam', NULL, 0, NULL, 2, NULL, 'sys:exam:del', 1, 0, 1, '', NULL, 1005, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1009, '题目管理', 'ExamQuestionManage', '/exam/question', 3, 'mdi:help-circle', 1, '/exam/question/index', NULL, 1, 1, 1, '', '考试题目管理', 1000, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1010, '新增题目', 'AddExamQuestion', NULL, 0, NULL, 2, NULL, 'sys:exam_question:add', 1, 0, 1, '', NULL, 1009, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1011, '修改题目', 'EditExamQuestion', NULL, 0, NULL, 2, NULL, 'sys:exam_question:edit', 1, 0, 1, '', NULL, 1009, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1012, '删除题目', 'DeleteExamQuestion', NULL, 0, NULL, 2, NULL, 'sys:exam_question:del', 1, 0, 1, '', NULL, 1009, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1013, '班级管理', 'BanjiManage', '/exam/banji', 4, 'mdi:account-group', 1, '/exam/banji/index', NULL, 1, 1, 1, '', '班级管理', 1000, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1014, '新增班级', 'AddBanji', NULL, 0, NULL, 2, NULL, 'sys:banji:add', 1, 0, 1, '', NULL, 1013, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1015, '修改班级', 'EditBanji', NULL, 0, NULL, 2, NULL, 'sys:banji:edit', 1, 0, 1, '', NULL, 1013, '2025-07-14 21:20:20', NULL);
INSERT INTO `sys_menu` VALUES (1016, '删除班级', 'DeleteBanji', NULL, 0, NULL, 2, NULL, 'sys:banji:del', 1, 0, 1, '', NULL, 1013, '2025-07-14 21:20:20', NULL);

-- ----------------------------
-- Table structure for sys_notice
-- ----------------------------
DROP TABLE IF EXISTS `sys_notice`;
CREATE TABLE `sys_notice`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '标题',
  `type` int NOT NULL COMMENT '类型（0：通知、1：公告）',
  `author` varchar(16) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '作者',
  `source` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '信息来源',
  `status` int NOT NULL COMMENT '状态（0：隐藏、1：显示）',
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '内容',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_notice_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '系统通知公告表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_notice
-- ----------------------------

-- ----------------------------
-- Table structure for sys_opera_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_opera_log`;
CREATE TABLE `sys_opera_log`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `trace_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '请求跟踪 ID',
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '用户名',
  `method` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '请求类型',
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '操作模块',
  `path` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '请求路径',
  `ip` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'IP地址',
  `country` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '国家',
  `region` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '地区',
  `city` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '城市',
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '请求头',
  `os` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '操作系统',
  `browser` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '浏览器',
  `device` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '设备',
  `args` json NULL COMMENT '请求参数',
  `status` int NOT NULL COMMENT '操作状态（0异常 1正常）',
  `code` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '操作状态码',
  `msg` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '提示消息',
  `cost_time` float NOT NULL COMMENT '请求耗时（ms）',
  `opera_time` datetime NOT NULL COMMENT '操作时间',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_opera_log_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 84 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '操作日志表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_opera_log
-- ----------------------------
INSERT INTO `sys_opera_log` VALUES (1, '94b3fa308b4742989b34f467920174ee', NULL, 'POST', '用户登录', '/api/v1/auth/login', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"json\": {\"captcha\": \"9KU2\", \"password\": \"123456\", \"username\": \"admin\", \"selectAccount\": \"admin\"}}', 1, '404', '用户名或密码有误', 30.5945, '2025-07-12 23:08:49', '2025-07-12 23:08:49');
INSERT INTO `sys_opera_log` VALUES (2, '683cb424cdac49f68fa5cc6d26730233', NULL, 'GET', '获取登录验证码', '/api/v1/auth/captcha', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 12.9847, '2025-07-12 23:18:16', '2025-07-12 23:18:16');
INSERT INTO `sys_opera_log` VALUES (3, '6a91723adb2c468ab03606e9669995b0', NULL, 'POST', '用户登录', '/api/v1/auth/login', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"json\": {\"captcha\": \"phif\", \"password\": \"123456\", \"username\": \"admin\", \"selectAccount\": \"admin\"}}', 1, '200', 'Success', 213.904, '2025-07-12 23:18:21', '2025-07-12 23:18:22');
INSERT INTO `sys_opera_log` VALUES (4, '5723f16592004b1aa24670910c2e2239', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 15.9999, '2025-07-12 23:18:22', '2025-07-12 23:18:22');
INSERT INTO `sys_opera_log` VALUES (5, '4ee7c9528267483592f5f79e98636e14', 'admin', 'GET', '获取所有授权码', '/api/v1/auth/codes', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.7028, '2025-07-12 23:18:22', '2025-07-12 23:18:22');
INSERT INTO `sys_opera_log` VALUES (6, '60f32375a9014a2bb18a4a1f3c768d5c', 'admin', 'GET', '获取用户菜单侧边栏', '/api/v1/sys/menus/sidebar', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.0877, '2025-07-12 23:18:22', '2025-07-12 23:18:22');
INSERT INTO `sys_opera_log` VALUES (7, '14b689f94b88480e9361732116d403a5', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 2.7773, '2025-07-12 23:18:29', '2025-07-12 23:18:29');
INSERT INTO `sys_opera_log` VALUES (8, '73b2a10fa9364f9aa5119527670182c4', 'admin', 'GET', '分页获取所有角色', '/api/v1/sys/roles', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 6.9294, '2025-07-12 23:18:36', '2025-07-12 23:18:36');
INSERT INTO `sys_opera_log` VALUES (9, '065820bf649749849422f6aa4f801775', 'admin', 'GET', '分页获取所有角色', '/api/v1/sys/roles', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 5.385, '2025-07-12 23:18:48', '2025-07-12 23:18:48');
INSERT INTO `sys_opera_log` VALUES (10, 'd61955cd83634bd2afce6bff7a336193', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.8317, '2025-07-12 23:18:55', '2025-07-12 23:18:55');
INSERT INTO `sys_opera_log` VALUES (11, '5277ca7803bc42b78a9809305618127d', 'admin', 'GET', '获取所有角色', '/api/v1/sys/roles/all', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 3.8883, '2025-07-12 23:18:55', '2025-07-12 23:18:55');
INSERT INTO `sys_opera_log` VALUES (12, 'efad4984132f4c25a409f7ff4af28cab', 'admin', 'GET', '分页获取所有用户', '/api/v1/sys/users', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 9.9607, '2025-07-12 23:18:55', '2025-07-12 23:18:55');
INSERT INTO `sys_opera_log` VALUES (13, '32128c5c44a9405a873f037db0d9c5ac', 'admin', 'GET', '获取菜单树', '/api/v1/sys/menus', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 6.4962, '2025-07-12 23:19:00', '2025-07-12 23:19:00');
INSERT INTO `sys_opera_log` VALUES (14, 'c68be0df75744559984f99f7d6a45ebd', 'admin', 'GET', '分页获取所有用户', '/api/v1/sys/users', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"dept\": \"1\", \"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 8.9697, '2025-07-12 23:19:09', '2025-07-12 23:19:09');
INSERT INTO `sys_opera_log` VALUES (15, '88567090949e48caaaf1f44ab4ae50b2', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 3.9997, '2025-07-12 23:19:11', '2025-07-12 23:19:11');
INSERT INTO `sys_opera_log` VALUES (16, 'e35660a05dab46aeae5d160c16de93a4', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.1541, '2025-07-12 23:19:13', '2025-07-12 23:19:13');
INSERT INTO `sys_opera_log` VALUES (17, 'c84a8fd457be41c08e1fa4afa48dff49', 'admin', 'GET', '获取菜单树', '/api/v1/sys/menus', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.8121, '2025-07-12 23:19:25', '2025-07-12 23:19:25');
INSERT INTO `sys_opera_log` VALUES (18, '0c50b936cfb44db0bce7c1323ad3a6ed', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.2206, '2025-07-12 23:19:47', '2025-07-12 23:19:47');
INSERT INTO `sys_opera_log` VALUES (19, 'a421111ca50a4f44bb8a3393f7d1a02d', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.1133, '2025-07-12 23:19:55', '2025-07-12 23:19:55');
INSERT INTO `sys_opera_log` VALUES (20, '22fab249177949b8937faacc8b92850f', 'admin', 'POST', '创建部门', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"json\": {\"name\": \"南昌第一中学\", \"email\": \"1458927283@qq.com\", \"phone\": \"18573071275\", \"leader\": \"玉麟\", \"status\": 1, \"parent_id\": 1}}', 1, '200', 'Success', 16.9915, '2025-07-12 23:20:23', '2025-07-12 23:20:23');
INSERT INTO `sys_opera_log` VALUES (21, 'd99fb2382df647d1973b4f95e10f3cc7', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.5143, '2025-07-12 23:20:23', '2025-07-12 23:20:23');
INSERT INTO `sys_opera_log` VALUES (22, '535b53e2bdcc4f50a81dbcf7294f9716', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.6174, '2025-07-12 23:20:31', '2025-07-12 23:20:31');
INSERT INTO `sys_opera_log` VALUES (23, '2b67a3a555b54d298e2df53192e04de3', 'admin', 'PUT', '更新部门', '/api/v1/sys/depts/2', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"json\": {\"name\": \"高三八班\", \"email\": \"1458927283@qq.com\", \"phone\": \"18573071275\", \"leader\": \"玉麟\", \"status\": 1, \"parent_id\": 1}}', 1, '200', 'Success', 16.228, '2025-07-12 23:20:50', '2025-07-12 23:20:50');
INSERT INTO `sys_opera_log` VALUES (24, 'c4921c186c454051afb0cd16a23a1217', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 7.6897, '2025-07-12 23:20:50', '2025-07-12 23:20:50');
INSERT INTO `sys_opera_log` VALUES (25, 'be06ff9b50bf4154b7bcb54236b783d9', 'admin', 'GET', '分页获取所有用户', '/api/v1/sys/users', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 7.7565, '2025-07-12 23:21:00', '2025-07-12 23:21:00');
INSERT INTO `sys_opera_log` VALUES (26, '215f7890ef2249afacc487585332c6f9', 'admin', 'GET', '是否存在插件变更', '/api/v1/sys/plugins/changed', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.0384, '2025-07-12 23:21:15', '2025-07-12 23:21:15');
INSERT INTO `sys_opera_log` VALUES (27, '6074dbbddeeb45cebf3fbce1479d8c71', 'admin', 'GET', '获取所有插件', '/api/v1/sys/plugins', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 6.606, '2025-07-12 23:21:15', '2025-07-12 23:21:15');
INSERT INTO `sys_opera_log` VALUES (28, '4107b22cbc7247458b5e988fad7dca85', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.6651, '2025-07-12 23:21:54', '2025-07-12 23:21:54');
INSERT INTO `sys_opera_log` VALUES (29, '1191a5d36a134be191934509261ebdb0', 'admin', 'GET', '获取菜单树', '/api/v1/sys/menus', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.6561, '2025-07-12 23:22:21', '2025-07-12 23:22:21');
INSERT INTO `sys_opera_log` VALUES (30, '222dd7470b784135b73792bd0cebdd79', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.6562, '2025-07-12 23:22:50', '2025-07-12 23:22:50');
INSERT INTO `sys_opera_log` VALUES (31, '2a25377d5a134d7cb919f5bc4fa9053e', 'admin', 'GET', '获取部门树', '/api/v1/sys/depts', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 3.8091, '2025-07-12 23:22:56', '2025-07-12 23:22:56');
INSERT INTO `sys_opera_log` VALUES (32, '1b334896452d41808b512410cc6d80bf', 'admin', 'GET', '分页获取所有角色', '/api/v1/sys/roles', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', '{\"query_params\": {\"page\": \"1\", \"size\": \"20\"}}', 1, '200', 'Success', 5.4581, '2025-07-12 23:24:56', '2025-07-12 23:24:56');
INSERT INTO `sys_opera_log` VALUES (33, '5a5374ab183942efb67b52a1d477f87a', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 9.7533, '2025-07-13 00:13:32', '2025-07-13 00:13:32');
INSERT INTO `sys_opera_log` VALUES (34, '9bcb90b915f14f95a23c6346f14dbce4', 'admin', 'GET', '获取用户菜单侧边栏', '/api/v1/sys/menus/sidebar', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 14.1833, '2025-07-13 00:13:32', '2025-07-13 00:13:32');
INSERT INTO `sys_opera_log` VALUES (35, '9ff89916672e44f3b8e5f0fba193581d', 'admin', 'GET', '是否存在插件变更', '/api/v1/sys/plugins/changed', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 4.8596, '2025-07-13 00:13:36', '2025-07-13 00:13:36');
INSERT INTO `sys_opera_log` VALUES (36, '3baef57bdde74d6da0fc03f633ee105f', 'admin', 'GET', '获取所有插件', '/api/v1/sys/plugins', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 8.1378, '2025-07-13 00:13:36', '2025-07-13 00:13:36');
INSERT INTO `sys_opera_log` VALUES (37, 'ff4340e72b564076b7f4e5d0705445b2', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 7.4748, '2025-07-13 00:34:25', '2025-07-13 00:34:25');
INSERT INTO `sys_opera_log` VALUES (38, 'c3e4bb27b7654f56a41ba4f59546267b', 'admin', 'GET', '获取用户菜单侧边栏', '/api/v1/sys/menus/sidebar', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 28.7987, '2025-07-13 00:34:25', '2025-07-13 00:34:25');
INSERT INTO `sys_opera_log` VALUES (39, '63221e7601cd49bb8b676f77747d0384', 'admin', 'GET', '是否存在插件变更', '/api/v1/sys/plugins/changed', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 20.9317, '2025-07-13 00:34:25', '2025-07-13 00:34:25');
INSERT INTO `sys_opera_log` VALUES (40, 'f6ccebdc78c9467097ffbd92bb0ccb92', 'admin', 'GET', '获取所有插件', '/api/v1/sys/plugins', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 25.0145, '2025-07-13 00:34:25', '2025-07-13 00:34:25');
INSERT INTO `sys_opera_log` VALUES (41, '2117028f563a42bd981e823ba76d8506', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 6.3311, '2025-07-13 15:26:56', '2025-07-13 15:26:56');
INSERT INTO `sys_opera_log` VALUES (42, 'f0ab17dcbabd4676a97be6f295727886', 'admin', 'GET', '获取用户菜单侧边栏', '/api/v1/sys/menus/sidebar', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 14.9213, '2025-07-13 15:26:56', '2025-07-13 15:26:56');
INSERT INTO `sys_opera_log` VALUES (43, '582cb06fdb3d4862bacd96535e07717c', 'admin', 'GET', '是否存在插件变更', '/api/v1/sys/plugins/changed', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.8137, '2025-07-13 15:26:56', '2025-07-13 15:26:56');
INSERT INTO `sys_opera_log` VALUES (44, 'dbf9f973ac1d491e8dbea9d0ef307b7f', 'admin', 'GET', '获取所有插件', '/api/v1/sys/plugins', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 8.5348, '2025-07-13 15:26:56', '2025-07-13 15:26:56');
INSERT INTO `sys_opera_log` VALUES (45, '78dbd77ca9bd4dd4909f489b6060fb8d', 'admin', 'GET', '获取当前用户信息', '/api/v1/sys/users/me', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 3.0047, '2025-07-13 15:32:08', '2025-07-13 15:32:08');
INSERT INTO `sys_opera_log` VALUES (46, '953f6b228a2c4c9d8195e917baadde55', 'admin', 'GET', '获取用户菜单侧边栏', '/api/v1/sys/menus/sidebar', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 5.4754, '2025-07-13 15:32:08', '2025-07-13 15:32:08');
INSERT INTO `sys_opera_log` VALUES (47, 'e1eacaaafd964477818a5720a2ae32ae', 'admin', 'GET', '是否存在插件变更', '/api/v1/sys/plugins/changed', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 2.624, '2025-07-13 15:32:09', '2025-07-13 15:32:09');
INSERT INTO `sys_opera_log` VALUES (48, '5fce58d08bb043e784d1b4be6569db33', 'admin', 'GET', '获取所有插件', '/api/v1/sys/plugins', '127.0.0.1', 'None', 'None', '内网IP', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0', 'Windows 10', 'Edge 138.0.0', 'PC', 'null', 1, '200', 'Success', 3.6375, '2025-07-13 15:32:09', '2025-07-13 15:32:09');
INSERT INTO `sys_opera_log` VALUES (49, '9248bcc11a654eeb9b29496f89ead06f', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 2.923, '2025-07-14 20:33:39', '2025-07-14 20:33:39');
INSERT INTO `sys_opera_log` VALUES (50, 'c780a19aa4544ca8b04b5c22e34e4a1a', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 2.9549, '2025-07-14 20:40:44', '2025-07-14 20:40:44');
INSERT INTO `sys_opera_log` VALUES (51, '6ab64b7cbef84e8faa57b6b6f19117a6', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 2.8776, '2025-07-14 20:41:26', '2025-07-14 20:41:26');
INSERT INTO `sys_opera_log` VALUES (52, 'a7b007d1b3374e278b96fe7efcec5068', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 2.9559, '2025-07-14 20:41:38', '2025-07-14 20:41:38');
INSERT INTO `sys_opera_log` VALUES (53, '672b63208fcb48ed91e58cf2ed4118c5', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 3.0981, '2025-07-14 20:48:41', '2025-07-14 20:48:41');
INSERT INTO `sys_opera_log` VALUES (54, '90044d1819c14deb92d2bbf661cb84c0', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 3.0276, '2025-07-14 20:49:43', '2025-07-14 20:49:43');
INSERT INTO `sys_opera_log` VALUES (55, '403c21b4b855429b8437ac24d20a02d1', 'admin', 'POST', '', '/api/v1/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '404', 'Not Found', 2.7251, '2025-07-14 20:50:22', '2025-07-14 20:50:22');
INSERT INTO `sys_opera_log` VALUES (56, 'a3d797c895904653ad013ee9363854ab', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.8274, '2025-07-14 20:50:54', '2025-07-14 20:50:54');
INSERT INTO `sys_opera_log` VALUES (57, '8faef37311ce4ac493a60f6c59006177', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.2545, '2025-07-14 20:55:35', '2025-07-14 20:55:35');
INSERT INTO `sys_opera_log` VALUES (58, 'bfdcfed4797d4064a1a550c7183812a8', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 18.2043, '2025-07-14 20:55:49', '2025-07-14 20:55:49');
INSERT INTO `sys_opera_log` VALUES (59, 'da9edd6987984d75a3729d3926d6758a', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.7362, '2025-07-14 20:56:20', '2025-07-14 20:56:20');
INSERT INTO `sys_opera_log` VALUES (60, '0abc194851d647a8ab8e3b7273ecce7c', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, '200', 'Success', 0, '2025-07-14 20:56:20', '2025-07-14 20:56:20');
INSERT INTO `sys_opera_log` VALUES (61, 'f5830114cece42b1a0f078ea2c0ee74f', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 20.9535, '2025-07-14 20:56:59', '2025-07-14 20:56:59');
INSERT INTO `sys_opera_log` VALUES (62, '59630336b20c4f2f82c087adb50908e8', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, '200', 'Success', 0, '2025-07-14 20:57:00', '2025-07-14 20:57:00');
INSERT INTO `sys_opera_log` VALUES (63, '442ba8cd093749da8e4a79be15853974', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 21.3604, '2025-07-14 20:59:20', '2025-07-14 20:59:20');
INSERT INTO `sys_opera_log` VALUES (64, 'b0e9b1dae257438b888c8a02ce24c726', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, '200', 'Success', 0, '2025-07-14 20:59:21', '2025-07-14 20:59:21');
INSERT INTO `sys_opera_log` VALUES (65, 'abeb1588dfcf4242ab72a87c9a99e50a', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.6383, '2025-07-14 21:01:25', '2025-07-14 21:01:25');
INSERT INTO `sys_opera_log` VALUES (66, 'a75525d6b36e46f39087831d981eefc9', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, '200', 'Success', 0, '2025-07-14 21:01:26', '2025-07-14 21:01:26');
INSERT INTO `sys_opera_log` VALUES (67, '8ffa953978b64787af813957743f684c', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.545, '2025-07-14 21:02:12', '2025-07-14 21:02:12');
INSERT INTO `sys_opera_log` VALUES (68, '00807a68b8704b5bb0c1c360412db4a6', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.1052, '2025-07-14 21:03:20', '2025-07-14 21:03:20');
INSERT INTO `sys_opera_log` VALUES (69, '808ee97f928c47ad88aaa24e1ee2dfd5', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, '200', 'Success', 0, '2025-07-14 21:03:21', '2025-07-14 21:03:21');
INSERT INTO `sys_opera_log` VALUES (70, '7afff6573a6e416e83a83bff12e7498e', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 19.8771, '2025-07-14 21:11:18', '2025-07-14 21:11:18');
INSERT INTO `sys_opera_log` VALUES (71, '0f6892c9391b443797dd1239eb67c4c3', 'admin', 'GET', '分页获取所有学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"query_params\": {\"page\": \"1\", \"size\": \"10\"}}', 0, 'e3q8', 'Success', 0, '2025-07-14 21:11:19', '2025-07-14 21:11:19');
INSERT INTO `sys_opera_log` VALUES (72, '26d5f2ccc2214e6b9bdaa41b7cec21f6', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.4571, '2025-07-14 21:15:36', '2025-07-14 21:15:36');
INSERT INTO `sys_opera_log` VALUES (73, '99c8859b74a24049adfe1cd1f92067b9', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.1428, '2025-07-14 21:16:09', '2025-07-14 21:16:09');
INSERT INTO `sys_opera_log` VALUES (74, '9945fa9637274794a71eec3f4cf25fb0', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.3492, '2025-07-14 21:16:42', '2025-07-14 21:16:42');
INSERT INTO `sys_opera_log` VALUES (75, 'a6b9d85a6eb84ab28e5e4708ad009ccf', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.5943, '2025-07-14 21:20:50', '2025-07-14 21:20:50');
INSERT INTO `sys_opera_log` VALUES (76, '7077d055e7cc48fa908b4e67bc4aa54c', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.3258, '2025-07-14 21:21:09', '2025-07-14 21:21:09');
INSERT INTO `sys_opera_log` VALUES (77, 'da0cc646797e4d49b5006e162ca305d6', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 3.953, '2025-07-14 21:21:33', '2025-07-14 21:21:33');
INSERT INTO `sys_opera_log` VALUES (78, '0c6bb89a02a24461a05f2795e942f2be', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 3.7893, '2025-07-14 21:22:08', '2025-07-14 21:22:08');
INSERT INTO `sys_opera_log` VALUES (79, 'fd11a26e71e44917838c3e6a143b015f', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.0851, '2025-07-14 21:22:33', '2025-07-14 21:22:33');
INSERT INTO `sys_opera_log` VALUES (80, '9da0d6428247488892a01c6ac8cfd49a', 'admin', 'DELETE', '批量删除学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"ids\": [null]}}', 1, '422', '请求参数非法: 0 输入应为有效的整数，输入：None', 4.9363, '2025-07-14 21:24:05', '2025-07-14 21:24:05');
INSERT INTO `sys_opera_log` VALUES (81, '7d88a396e2ec469ca44e4ef8f8e4c4a3', 'admin', 'POST', '创建学科', '/api/v1/subjects', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', '{\"json\": {\"name\": \"数学\", \"remark\": \"数学学科\"}}', 1, '200', 'Success', 23.6753, '2025-07-14 21:24:36', '2025-07-14 21:24:36');
INSERT INTO `sys_opera_log` VALUES (82, '4c04990d1d26489a88016b443a1ec2ad', 'admin', 'GET', '获取学科详情', '/api/v1/subjects/None', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', 'null', 1, '422', '请求参数非法: pk 输入应为有效的整数，无法将字符串解析为整数，输入：None', 3.4179, '2025-07-14 21:25:00', '2025-07-14 21:25:00');
INSERT INTO `sys_opera_log` VALUES (83, 'b9cd23e15d794a37b67ef8300b0b9547', 'admin', 'GET', '获取学科详情', '/api/v1/subjects/None', '127.0.0.1', 'None', 'None', '内网IP', 'python-httpx/0.27.0', 'Other', 'Other', 'Other', 'null', 1, '422', '请求参数非法: pk 输入应为有效的整数，无法将字符串解析为整数，输入：None', 3.785, '2025-07-14 21:25:30', '2025-07-14 21:25:30');

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '角色名称',
  `status` int NOT NULL COMMENT '角色状态（0停用 1正常）',
  `is_filter_scopes` tinyint(1) NOT NULL COMMENT '过滤数据权限(0否 1是)',
  `remark` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_role_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '角色表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES (1, '测试', 1, 1, NULL, '2025-07-12 23:18:10', NULL);

-- ----------------------------
-- Table structure for sys_role_data_scope
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_data_scope`;
CREATE TABLE `sys_role_data_scope`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `role_id` bigint NOT NULL COMMENT '角色 ID',
  `data_scope_id` bigint NOT NULL COMMENT '数据范围 ID',
  PRIMARY KEY (`id`, `role_id`, `data_scope_id`) USING BTREE,
  UNIQUE INDEX `ix_sys_role_data_scope_id`(`id` ASC) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  INDEX `data_scope_id`(`data_scope_id` ASC) USING BTREE,
  CONSTRAINT `sys_role_data_scope_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_role_data_scope_ibfk_2` FOREIGN KEY (`data_scope_id`) REFERENCES `sys_data_scope` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role_data_scope
-- ----------------------------

-- ----------------------------
-- Table structure for sys_role_menu
-- ----------------------------
DROP TABLE IF EXISTS `sys_role_menu`;
CREATE TABLE `sys_role_menu`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `role_id` bigint NOT NULL COMMENT '角色ID',
  `menu_id` bigint NOT NULL COMMENT '菜单ID',
  PRIMARY KEY (`id`, `role_id`, `menu_id`) USING BTREE,
  UNIQUE INDEX `ix_sys_role_menu_id`(`id` ASC) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  INDEX `menu_id`(`menu_id` ASC) USING BTREE,
  CONSTRAINT `sys_role_menu_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_role_menu_ibfk_2` FOREIGN KEY (`menu_id`) REFERENCES `sys_menu` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1017 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role_menu
-- ----------------------------
INSERT INTO `sys_role_menu` VALUES (1, 1, 1);
INSERT INTO `sys_role_menu` VALUES (2, 1, 2);
INSERT INTO `sys_role_menu` VALUES (3, 1, 3);
INSERT INTO `sys_role_menu` VALUES (4, 1, 54);
INSERT INTO `sys_role_menu` VALUES (1000, 1, 1000);
INSERT INTO `sys_role_menu` VALUES (1001, 1, 1001);
INSERT INTO `sys_role_menu` VALUES (1002, 1, 1002);
INSERT INTO `sys_role_menu` VALUES (1003, 1, 1003);
INSERT INTO `sys_role_menu` VALUES (1004, 1, 1004);
INSERT INTO `sys_role_menu` VALUES (1005, 1, 1005);
INSERT INTO `sys_role_menu` VALUES (1006, 1, 1006);
INSERT INTO `sys_role_menu` VALUES (1007, 1, 1007);
INSERT INTO `sys_role_menu` VALUES (1008, 1, 1008);
INSERT INTO `sys_role_menu` VALUES (1009, 1, 1009);
INSERT INTO `sys_role_menu` VALUES (1010, 1, 1010);
INSERT INTO `sys_role_menu` VALUES (1011, 1, 1011);
INSERT INTO `sys_role_menu` VALUES (1012, 1, 1012);
INSERT INTO `sys_role_menu` VALUES (1013, 1, 1013);
INSERT INTO `sys_role_menu` VALUES (1014, 1, 1014);
INSERT INTO `sys_role_menu` VALUES (1015, 1, 1015);
INSERT INTO `sys_role_menu` VALUES (1016, 1, 1016);

-- ----------------------------
-- Table structure for sys_subject
-- ----------------------------
DROP TABLE IF EXISTS `sys_subject`;
CREATE TABLE `sys_subject`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '学科名称',
  `remark` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '备注',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_subject_id`(`id` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '学科模型' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_subject
-- ----------------------------
INSERT INTO `sys_subject` VALUES (1, '数学', '数学学科', '2025-07-14 20:50:54', NULL);
INSERT INTO `sys_subject` VALUES (2, '数学', '数学学科', '2025-07-14 20:55:35', NULL);
INSERT INTO `sys_subject` VALUES (3, '数学', '数学学科', '2025-07-14 20:55:49', NULL);
INSERT INTO `sys_subject` VALUES (4, '数学', '数学学科', '2025-07-14 20:56:20', NULL);
INSERT INTO `sys_subject` VALUES (5, '数学', '数学学科', '2025-07-14 20:56:59', NULL);
INSERT INTO `sys_subject` VALUES (6, '数学', '数学学科', '2025-07-14 20:59:20', NULL);
INSERT INTO `sys_subject` VALUES (7, '数学', '数学学科', '2025-07-14 21:01:25', NULL);
INSERT INTO `sys_subject` VALUES (8, '数学', '数学学科', '2025-07-14 21:02:12', NULL);
INSERT INTO `sys_subject` VALUES (9, '数学', '数学学科', '2025-07-14 21:03:20', NULL);
INSERT INTO `sys_subject` VALUES (10, '数学', '数学学科', '2025-07-14 21:11:18', NULL);
INSERT INTO `sys_subject` VALUES (11, '数学', '数学学科', '2025-07-14 21:24:36', NULL);

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `uuid` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `username` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
  `nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '昵称',
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '密码',
  `salt` varbinary(255) NOT NULL COMMENT '加密盐',
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '邮箱',
  `phone` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机号',
  `avatar` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像',
  `status` int NOT NULL COMMENT '用户账号状态(0停用 1正常)',
  `is_superuser` tinyint(1) NOT NULL COMMENT '超级权限(0否 1是)',
  `is_staff` tinyint(1) NOT NULL COMMENT '后台管理登陆(0否 1是)',
  `is_multi_login` tinyint(1) NOT NULL COMMENT '是否重复登陆(0否 1是)',
  `join_time` datetime NOT NULL COMMENT '注册时间',
  `last_login_time` datetime NULL DEFAULT NULL COMMENT '上次登录',
  `dept_id` bigint NULL DEFAULT NULL COMMENT '部门关联ID',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `uuid`(`uuid` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_user_id`(`id` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_user_username`(`username` ASC) USING BTREE,
  UNIQUE INDEX `ix_sys_user_email`(`email` ASC) USING BTREE,
  INDEX `dept_id`(`dept_id` ASC) USING BTREE,
  INDEX `ix_sys_user_status`(`status` ASC) USING BTREE,
  CONSTRAINT `sys_user_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `sys_dept` (`id`) ON DELETE SET NULL ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (1, '6bb8dc02-5f33-11f0-ae78-ecd68abaf3f2', 'admin', '用户88888', '$2b$12$8y2eNucX19VjmZ3tYhBLcOsBwy9w1IjBQE4SSqwMDL5bGQVp2wqS.', 0x24326224313224387932654E7563583139566A6D5A33745968424C634F, 'admin@example.com', NULL, NULL, 1, 1, 1, 1, '2025-07-12 23:18:10', '2025-07-14 21:25:30', 1, '2025-07-12 23:18:10', '2025-07-14 21:25:30');
INSERT INTO `sys_user` VALUES (2, '6bb8def2-5f33-11f0-ae78-ecd68abaf3f2', 'test', '用户66666', '$2b$12$BMiXsNQAgTx7aNc7kVgnwedXGyUxPEHRnJMFbiikbqHgVoT3y14Za', 0x24326224313224424D6958734E514167547837614E63376B56676E7765, 'test@example.com', NULL, NULL, 1, 0, 0, 0, '2025-07-12 23:18:10', '2025-07-12 23:18:10', 1, '2025-07-12 23:18:10', NULL);

-- ----------------------------
-- Table structure for sys_user_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_role`;
CREATE TABLE `sys_user_role`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `user_id` bigint NOT NULL COMMENT '用户ID',
  `role_id` bigint NOT NULL COMMENT '角色ID',
  PRIMARY KEY (`id`, `user_id`, `role_id`) USING BTREE,
  UNIQUE INDEX `ix_sys_user_role_id`(`id` ASC) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  INDEX `role_id`(`role_id` ASC) USING BTREE,
  CONSTRAINT `sys_user_role_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `sys_user_role_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `sys_role` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_role
-- ----------------------------
INSERT INTO `sys_user_role` VALUES (1, 1, 1);
INSERT INTO `sys_user_role` VALUES (2, 2, 1);

-- ----------------------------
-- Table structure for sys_user_social
-- ----------------------------
DROP TABLE IF EXISTS `sys_user_social`;
CREATE TABLE `sys_user_social`  (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键 ID',
  `sid` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '第三方用户 ID',
  `source` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '第三方用户来源',
  `user_id` bigint NOT NULL COMMENT '用户关联ID',
  `created_time` datetime NOT NULL COMMENT '创建时间',
  `updated_time` datetime NULL DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ix_sys_user_social_id`(`id` ASC) USING BTREE,
  INDEX `user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `sys_user_social_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `sys_user` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户社交表（OAuth2）' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user_social
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;

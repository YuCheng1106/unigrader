CREATE TABLE `school` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `uuid` varchar(24) UNIQUE NOT NULL,
  `name` varchar(225) NOT NULL,
  `description` text,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `user` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `uuid` varchar(24) UNIQUE NOT NULL,
  `school_id` integer NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `email` varchar(100) UNIQUE,
  `phone` varchar(20) UNIQUE,
  `avatar_url` varchar(255),
  `status` enum(active,suspended,graduated) DEFAULT 'active',
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `student` (
  `user_id` integer PRIMARY KEY,
  `student_number` varchar(50) UNIQUE,
  `enrollment_date` date
);

CREATE TABLE `teacher` (
  `user_id` integer PRIMARY KEY,
  `teacher_number` varchar(50) UNIQUE,
  `hire_date` date
);

CREATE TABLE `advisor` (
  `user_id` integer PRIMARY KEY
);

CREATE TABLE `role` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `role_name` varchar(50) UNIQUE NOT NULL,
  `description` varchar(255),
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `permission` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `permission_name` varchar(50) UNIQUE NOT NULL,
  `description` varchar(255)
);

CREATE TABLE `banji` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) UNIQUE NOT NULL,
  `academic_year` varchar(20),
  `description` text,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `subject` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(100) UNIQUE NOT NULL,
  `description` text,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `exam` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `uuid` varchar(24) UNIQUE NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text,
  `creator_id` integer NOT NULL,
  `banji_id` integer NOT NULL,
  `subject_id` integer,
  `start_time` datetime NOT NULL,
  `duration_minutes` integer NOT NULL DEFAULT 120,
  `exam_type` enum(quiz,test,exam) DEFAULT 'exam',
  `status` enum(draft,published,ongoing,finished,graded,archived) DEFAULT 'draft',
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `deleted_at` timestamp
);

CREATE TABLE `exam_question` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `exam_id` integer NOT NULL,
  `question_type` enum(single_choice,multiple_choice,true_false,short_answer,essay) NOT NULL,
  `question_content` text NOT NULL,
  `options` json COMMENT 'For multiple choice questions',
  `correct_answer` text,
  `points` float NOT NULL,
  `sequence` integer NOT NULL,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `student_exam` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `student_id` integer NOT NULL,
  `exam_id` integer NOT NULL,
  `start_time` datetime,
  `end_time` datetime,
  `total_score` decimal(5,2),
  `status` enum(not_started,in_progress,submitted,graded) DEFAULT 'not_started',
  `attempt_number` integer DEFAULT 1,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP),
  `updated_at` timestamp DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `student_answer` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `student_exam_id` integer NOT NULL,
  `question_id` integer NOT NULL,
  `answer_content` text,
  `is_correct` boolean,
  `score` float,
  `feedback` text,
  `graded_by` integer,
  `submitted_at` timestamp,
  `graded_at` timestamp
);

CREATE TABLE `user_has_role` (
  `user_id` integer NOT NULL,
  `role_id` integer NOT NULL,
  `created_at` timestamp DEFAULT (CURRENT_TIMESTAMP)
);

CREATE TABLE `role_has_permission` (
  `role_id` integer NOT NULL,
  `permission_id` integer NOT NULL
);

CREATE TABLE `teacher_has_subject` (
  `user_id` integer NOT NULL,
  `subject_id` integer NOT NULL,
  `is_primary` boolean DEFAULT false
);

CREATE TABLE `teacher_has_banji` (
  `user_id` integer NOT NULL,
  `banji_id` integer NOT NULL,
  `role` enum(head_teacher,subject_teacher) DEFAULT 'subject_teacher'
);

CREATE TABLE `student_has_banji` (
  `user_id` integer NOT NULL,
  `banji_id` integer NOT NULL,
  `enrollment_date` date DEFAULT (CURRENT_DATE)
);

CREATE TABLE `student_has_advisor` (
  `user_id` integer NOT NULL,
  `advisor_id` integer NOT NULL,
  `start_date` date DEFAULT (CURRENT_DATE),
  `end_date` date
);

CREATE UNIQUE INDEX `user_index_0` ON `user` (`email`);

CREATE UNIQUE INDEX `user_index_1` ON `user` (`phone`);

CREATE UNIQUE INDEX `student_exam_index_2` ON `student_exam` (`student_id`, `exam_id`, `attempt_number`);

CREATE UNIQUE INDEX `user_has_role_index_3` ON `user_has_role` (`user_id`, `role_id`);

CREATE UNIQUE INDEX `role_has_permission_index_4` ON `role_has_permission` (`role_id`, `permission_id`);

CREATE UNIQUE INDEX `teacher_has_subject_index_5` ON `teacher_has_subject` (`user_id`, `subject_id`);

CREATE UNIQUE INDEX `teacher_has_banji_index_6` ON `teacher_has_banji` (`user_id`, `banji_id`);

CREATE UNIQUE INDEX `student_has_banji_index_7` ON `student_has_banji` (`user_id`, `banji_id`);

CREATE UNIQUE INDEX `student_has_advisor_index_8` ON `student_has_advisor` (`user_id`, `advisor_id`);

ALTER TABLE `school` ADD FOREIGN KEY (`id`) REFERENCES `user` (`school_id`) ON DELETE CASCADE;

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `user_has_role` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `role` ADD FOREIGN KEY (`id`) REFERENCES `user_has_role` (`role_id`) ON DELETE CASCADE;

ALTER TABLE `teacher` ADD FOREIGN KEY (`user_id`) REFERENCES `teacher_has_subject` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `subject` ADD FOREIGN KEY (`id`) REFERENCES `teacher_has_subject` (`subject_id`) ON DELETE CASCADE;

ALTER TABLE `teacher` ADD FOREIGN KEY (`user_id`) REFERENCES `teacher_has_banji` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `banji` ADD FOREIGN KEY (`id`) REFERENCES `teacher_has_banji` (`banji_id`) ON DELETE CASCADE;

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `student` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `banji` ADD FOREIGN KEY (`id`) REFERENCES `student_has_banji` (`banji_id`) ON DELETE CASCADE;

ALTER TABLE `student` ADD FOREIGN KEY (`user_id`) REFERENCES `student_has_banji` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `student` ADD FOREIGN KEY (`user_id`) REFERENCES `student_has_advisor` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `advisor` ADD FOREIGN KEY (`user_id`) REFERENCES `student_has_advisor` (`advisor_id`) ON DELETE CASCADE;

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `advisor` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `user` ADD FOREIGN KEY (`id`) REFERENCES `teacher` (`user_id`) ON DELETE CASCADE;

ALTER TABLE `role` ADD FOREIGN KEY (`id`) REFERENCES `role_has_permission` (`role_id`) ON DELETE CASCADE;

ALTER TABLE `permission` ADD FOREIGN KEY (`id`) REFERENCES `role_has_permission` (`permission_id`) ON DELETE CASCADE;

ALTER TABLE `teacher` ADD FOREIGN KEY (`user_id`) REFERENCES `exam` (`creator_id`);

ALTER TABLE `banji` ADD FOREIGN KEY (`id`) REFERENCES `exam` (`banji_id`);

ALTER TABLE `subject` ADD FOREIGN KEY (`id`) REFERENCES `exam` (`subject_id`);

ALTER TABLE `exam` ADD FOREIGN KEY (`id`) REFERENCES `exam_question` (`exam_id`) ON DELETE CASCADE;

ALTER TABLE `student` ADD FOREIGN KEY (`user_id`) REFERENCES `student_exam` (`student_id`) ON DELETE CASCADE;

ALTER TABLE `exam` ADD FOREIGN KEY (`id`) REFERENCES `student_exam` (`exam_id`) ON DELETE CASCADE;

ALTER TABLE `student_exam` ADD FOREIGN KEY (`id`) REFERENCES `student_answer` (`student_exam_id`) ON DELETE CASCADE;

ALTER TABLE `exam_question` ADD FOREIGN KEY (`id`) REFERENCES `student_answer` (`question_id`) ON DELETE CASCADE;

ALTER TABLE `teacher` ADD FOREIGN KEY (`user_id`) REFERENCES `student_answer` (`graded_by`);

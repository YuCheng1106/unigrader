# 考试系统多对多关系设计

本文档说明了考试系统中的多对多关系表设计和使用方法。

## 关系表概览

### 1. exam_user - 用户考试关系表
用户参与的考试关系。

**字段说明：**
- `user_id`: 用户ID
- `exam_id`: 考试ID

### 2. exam_banji - 考试班级关系表
考试对应的班级关系。

**字段说明：**
- `exam_id`: 考试ID
- `banji_id`: 班级ID



### 3. user_banji - 用户班级关系表
用户所属的班级关系。

**字段说明：**
- `user_id`: 用户ID
- `banji_id`: 班级ID

### 4. teacher_subject - 教师学科关系表
教师教授的学科关系。

**字段说明：**
- `teacher_id`: 教师ID
- `subject_id`: 学科ID

### 5. teacher_banji - 教师班级关系表
教师负责的班级关系。

**字段说明：**
- `teacher_id`: 教师ID
- `banji_id`: 班级ID

## 使用示例

### 1. 获取用户参与的所有考试
```python
from app.admin.model import User
from plugin.exam.model import Exam

# 获取用户及其参与的考试
user = await session.get(User, user_id)
exams = user.exams  # 用户参与的所有考试
```

### 2. 获取考试的所有参与用户
```python
from plugin.exam.model import Exam

# 获取考试及其参与用户
exam = await session.get(Exam, exam_id)
users = exam.users  # 参与该考试的所有用户
```

### 3. 获取班级的所有学生
```python
from plugin.exam.model import Banji

# 获取班级及其学生
banji = await session.get(Banji, banji_id)
students = banji.students  # 班级的所有学生
teachers = banji.teachers  # 班级的所有教师
```

### 4. 获取教师教授的学科和班级
```python
from app.admin.model import User

# 获取教师及其教授的学科和班级
teacher = await session.get(User, teacher_id)
subjects = teacher.teaching_subjects  # 教师教授的学科
banjis = teacher.teaching_banjis     # 教师负责的班级
```

### 5. 复杂查询示例
```python
from sqlalchemy import select
from sqlalchemy.orm import selectinload

# 查询某个班级的所有考试
stmt = (
    select(Banji)
    .options(selectinload(Banji.exams))
    .where(Banji.id == banji_id)
)
banji = await session.execute(stmt)
```

## 注意事项

1. **循环导入问题**：使用 `TYPE_CHECKING` 和 `from __future__ import annotations` 来避免循环导入。

2. **关系表命名**：所有关系表都使用字符串形式的表名，避免直接引用表对象。

3. **级联删除**：所有外键都设置了 `ondelete='CASCADE'`，确保数据一致性。

4. **性能优化**：在查询时使用 `selectinload` 或 `joinedload` 来优化 N+1 查询问题。

5. **扩展性**：关系表中包含了额外的字段（如时间戳、状态、角色等），便于后续功能扩展。
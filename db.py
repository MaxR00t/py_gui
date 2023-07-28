import json


class StudentsDB:
    """学生信息管理系统数据模型"""

    def __init__(self):
        self.students = []
        # 加载本地文件中的数据
        self._load_students_data()

    def insert(self, student):
        """将学生数据插入到列表"""
        self.students.append(student)

    def all(self):
        """返回所有的学生数据"""
        return self.students

    def delete_by_name(self, name):
        """根据名字获取学生数据，如果没有就返回 False"""
        for student in self.students:
            if name == student['name']:
                self.students.remove(student)
                break
        else:
            return False
        return True

    def search_by_name(self, name):
        """根据名字查询学员，没有找到就返回 False"""
        for student in self.students:
            if name == student['name']:
                return student
        else:
            return False

    def update(self, stu):
        """更新学员信息"""
        name = stu['name']
        for student in self.students:
            if name == student['name']:
                student.update(stu)
                return True
        else:
            return False

    def _load_students_data(self):
        """从本地文件中加载数据"""
        with open('students.json', mode='r', encoding='utf-8') as f:
            text = f.read()
        if text:
            self.students = json.loads(text)

    def save_data(self):
        """保存数据到本地文件"""
        with open('students.json', mode='w', encoding='utf-8') as f:
            text = json.dumps(self.students, ensure_ascii=False)
            f.write(text)


db = StudentsDB()

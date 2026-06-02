class Student:
    def __init__(self, name, chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name}|语文：{self.chinese}|数学：{self.math}|英语：{self.english}|总分：{self.chinese+self.math+self.english}"
    def update(self,chinese = None,math = None,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class Course:
    version = 1.0
    name = "教务管理系统"
    def __init__(self):
        self.students_list = []
    def add_student(self):
        name = input("输入学生姓名：")
        for s in self.students_list:
            if s.name == name:
                print("学生已经存在！请重新添加~")
                return
        chinese = int(input("请输入学生语文成绩："))
        math = int(input("请输入学生数学成绩："))
        english = int(input("请输入学生英语成绩："))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu = Student(name,chinese,math,english)
            self.students_list.append(stu)
        else:
            print("学生成绩需要在0~100之间")

    def revise_student(self):
        name = input("输入需要修改的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                print(f"姓名：{s.name}|语文：{s.chinese}|数学：{s.math}|英语：{s.english}|总分：{s.chinese + s.math + s.english}")
                chinese = int(input("请输入修改后的语文成绩："))
                math = int(input("请输入修改后的数学成绩："))
                english = int(input("请输入修改后的英语成绩："))
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    s.update(chinese,math,english)
                    print("成绩修改成功！")
                    return
                else:
                    print("学生成绩需要在0~100之间")
                    return
        print("未找到该学生！")

    def remove_student(self):
        name = input("请输入想要删除的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                self.students_list.remove(s)
                print("学生删除成功")
                return
        print("未找到该学生！")

    def show(self):
        name = input("请输入想要查询的学生姓名：")
        for s in self.students_list:
            if s.name == name:
                print(f"{s}")
                return
        print("未找到该学生！")

    def show_all(self):
        for s in self.students_list:
            print(s)

    def run(self):
        print(f"欢迎使用教务系统{Course.version}")
        while True:
            choice = input("1.添加学生成绩\n2.修改学生成绩\n3.删除学生成绩\n4.查询学生成绩\n5.显示学生成绩\n6.退出系统\n请选择想要进行的操作:")
            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.revise_student()
                case "3":
                    self.remove_student()
                case "4":
                    self.show()
                case "5":
                    self.show_all()
                case "6":
                    print("已退出系统")
                    break
                case _:
                    print("输入不合法，请重新输入")
if __name__ == '__main__':
    edu_course = Course()
    edu_course.run()



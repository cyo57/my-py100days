'''
定义类
'''

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')
    
    def watch_movie(self):
        if  self.age < 18:
            print(f'{self.name}只能观看《熊出没》')
        else:
            print(f'{self.name}正在观看岛国爱情电影')

# 创建对象
def main():
    students = []
    students.append(Student('张三', 18))
    students[0].study('睡觉')

if __name__ == '__main__':
    main()
# encoding:utf-8
import Function as A   #将相关不变的函数进行打包引用
import shutil
A.PreocessTwoFloder('D:\\test\\Two')
# 对第二层文件夹进行操作

#对小于60或大于60的照片进行统计
'''
Same = 0
Different = 0

goal = A.Face_To_Match('1.jpg', '2.jpg') #获得包含id以及评分的字典goal

result = goal.get('result')     #得到result这个字典包含的元素
score = result.get('score')     #从字典result中获得比较分值
print(score)

if(score >= 60):
    Same = Same + 1
elif(score < 60):
    Different = Different + 1

print('Same is')
print(Same)

print('Different is')
print(Different)
'''



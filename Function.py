# encoding:utf-8
import os
from aip import AipFace
import base64
import random
import time

# 调试标志 Flag = True为调试状态  Flag = False 为不调试状态
Flag = True

""" 你的 APPID AK SK """
APP_ID = '14803185'
API_KEY = '4FmR91rWRKiyxtkvrSNrsDro'
SECRET_KEY = 'Ed4spz5GdjbxfQCfAGfiko8KXd9q0fC4'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)
print(client)


def Face_To_Match(Figure1, Figure2):
    result = client.match(
        [
            {
                'image': base64.b64encode(open(Figure1, 'rb').read()),
                'image_type': 'BASE64',
            },
            {
                'image': base64.b64encode(open(Figure2, 'rb').read()),
                'image_type': 'BASE64',
            }
        ]
    )
    return result

# 这是第一层文件夹
# 读出D:\\test的孩子（几低一层文件夹）
def fileInFolder(filepath):
    pathDir = os.listdir(filepath)  # 获取filepath文件夹下的所有的文件
    files = []
    for allDir in pathDir:
        child = os.path.join('%s\\%s' % (filepath, allDir))
        files.append(child.decode('gbk'))  # .decode('gbk')是解决中文显示乱码问题
        # print child
        # if os.path.isdir(child):
        #     print child
        #     simplepath = os.path.split(child)
        #     print simplepath
    return files

#这是第三层文件夹
# 判断同一个文件夹中是否只有一个人的图片
def JudgeSame(Filepath):
    # 返回判断的标志
    Judge_Flag = True
    # 将当前文件夹中所有图片的名字提取出来，放在列表FileName_List中
    FileName_List = fileInFolder(Filepath)
    # 获取列表的长度
    length = FileName_List.__len__()
    # 在当前文件夹中选取两张图片的位置
    a = random.randint(0, length - 1)
    b = random.randint(0, length - 1)
    c = random.randint(0, length - 1)
    d = random.randint(0, length - 1)
    # 随机挑选出4张图片，两两作比较
    Figure1 = FileName_List[a]
    Figure2 = FileName_List[b]
    Figure3 = FileName_List[c]
    Figure4 = FileName_List[d]
    # 获取goal字典，其中保护 id以及评分等
    goal1 = Face_To_Match(Figure1, Figure2)
    time.sleep(0.4)         #延时的目的 防止每秒向服务器发送的请求数qps异常
    goal2 = Face_To_Match(Figure3, Figure4)

    time.sleep(0.4)         #延时的目的 防止每秒向服务器发送的请求数qps异常
    # 获得两个评分Score1 和 Score2
    result1 = goal1.get('result')  # 得到result这个字典包含的元素
    score1  = float(result1.get('score'))  # 从字典result中获得比较分值

    result2 = goal2.get('result')  # 得到result这个字典包含的元素
    score2  = float(result2.get('score'))  # 从字典result中获得比较分值

    print('score1 = ')
    print (score1)
    print('score2 = ')
    print (score2)
    # 随机选取的4张图片中，两两之间相似度既有超过60%的，又有小于60%的 故将此文件夹的上一层文件夹存入Not_Sure文件夹中
    if((score1 >= 60 and score2 <= 60) or (score1 <= 60 and score2 >= 60)):
        Judge_Flag = True
    else:# 这个里比较明确，只有一种情况
        Judge_Flag = False
    #判断值
    return Judge_Flag

# 这是第二层文件夹
def Second_Folder(filepath):
    Second_Folder_Flag = True
    # FileName_List 有两个文件名集为列表
    FileName_List = fileInFolder(filepath)

    # 对其中的两个子文件夹进行判断
    if(JudgeSame(FileName_List[0]) == True or JudgeSame(FileName_List[1]) == True):
        Second_Folder_Flag = True
    else:
        Second_Folder_Flag = False

    return Second_Folder_Flag

# 对Two文件夹进行操作里面存在Not_Sure的文件
def PreocessTwoFloder(filepath):
    # FileName_List 有n个文件名集为列表
    FileName_List = fileInFolder(filepath)
    lenght = FileName_List.__len__()
    print('lenght is ')
    print(lenght)
    for path in FileName_List:
        print (path)
        print(type(path))
        time.sleep(0.1)
        #Second_Folder(path)
        '''
        result = A.Second_Folder(path)
        print ('Judge result = ' )
        print (result)

        if(result == True): #说明此文件夹中的图片不明确，将其上一层文件夹剪切入Not_Sure中
            print("Not_Sure")
            #将含有不明确的图片的文件夹的第二层文件夹剪切到Not_Sure中
            shutil.move(path, 'D:\\test\\Not_sure\\Compare')  #回去好好想想 新的路径该怎么修改
        elif(result == False): #说明此文件夹相对明确~，继续判断
            print("Same or Different")
        '''
    return

from torch.utils.data import Dataset
from PIL import Image#读取图片
import os#获取所有图像的库

#help(Dataset)#查看说明书，解释Dataset

class MyData(Dataset):#类
#下面3个def为类函数
    def __init__(self,root_dir,label_dir):#root_dir,label_dir路径相加
        self.root_dir=root_dir#路径1
        self.label_dir=label_dir#路径2
        self.path=os.path.join(self.root_dir,self.label_dir)#路径拼接
        self.img_path=os.listdir(self.path)#获取所有地址


    def __getitem__(self, idx):#获取每一个图像路径
        img_name=self.img_path[idx]#获取图片名称
        img_item_path=os.path.join(self.root_dir,self.label_dir,img_name)#获取图片相对路径
        img=Image.open(img_item_path)#读取图像
        label=self.label_dir#获取label(值)
        return img,label

    def __len__(self):#长度
        return len(self.img_path)#列表长度

root_dir='train'
ants_label_dir='ants_image'
bees_label_dir='bees_image'
ants_dataset=MyData(root_dir,ants_label_dir)#调用类
bees_dataset=MyData(root_dir,bees_label_dir)#调用类

img,label=bees_dataset[0]
#img.show()#调用类函数输出

train_dataset=ants_dataset+bees_dataset#蚂蚁数据集和蜜蜂数据集相加，返回为一个集合
#ants_dataset在前面 bees_dataset在后面
print(len(train_dataset))#输出两个数据集相加后的长度
print(len(ants_dataset))
print(len(bees_dataset))

from torch.utils.tensorboard import SummaryWriter#从tensorboard中导入SummaryWriter类
import numpy as np
from PIL import Image

#help(SummaryWriter)#查看SummaryWriter的解析

#在终端输入tensorboard --logdir=E:\PyTorch\PyTorch\logs --port=6007点击链接查看

writer=SummaryWriter('logs')#日志保持到logs文件中

image_path="E:\\PyTorch\\PyTorch\\train\\ants_image\\0013035.jpg"#获取地址
img_PIL=Image.open(image_path)#获取的图片为PIL类型，使用writer.add_image()需要转换为numpy类型
img_array=np.array(img_PIL)#转换为numpy类型

print(type(img_array))#查看图片的类型 numpy类型
print(img_array.shape)#查看图片的格式 (512,768,3) 512*768大小 3通道

writer.add_image('test',img_array,1,dataformats='HWC')#添加image 步骤1
#writer.add_image('test',img_array,2,dataformats='HWC')#步骤2
#步骤1和步骤2可以在点击链接后拖到进度条查看

for i in range(100):
    writer.add_scalar('y=2x',2*i,i)#添加scalar(数)
    #增加了一个logs文件夹

writer.close()#关闭读写
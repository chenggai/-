# -*- coding: utf-8 -*-
# @File    : uploadfile.py
# 描述     ：
# @Time    : 2020/2/13 10:55
# @Author  :
# @QQ

class Upload:
    def __init__(self,path,ext,size=1024*1024,is_datefilename=False):
        '''
        :param path: 文件保存的绝对路径：settings中的MEDIA_ROOT
        :param ext: 文件后缀类型
        :param size: 文件大小
        :param is_datefilename: 是不是日期目录
        '''
        self.path = path
        self.ext=ext
        self.size = size
        self.is_datefilename = is_datefilename

    def load(self,fobj):
        #1、获取文件上传对象
        if fobj:
            self.fobj=fobj
        else:
            return '错误的文件上传对象'
        # 2、检查文件大小
        if not self.check_size():
            return '文件大小不合格'
        errors={
            -1: "文件没有后缀名",
            -2: "文件后缀不符合要求",
            -3: "规定文件后缀不能识别",
            1: "文件类型符合要求"
        }
        # 3、检查文件类型
        res=self.check_type()
        if res<0:
            return errors[res]
        # 4、拼接文件路径
        path=self.get_path()
        print(path)
        # 5、上传
        if not self.write_file(path):
            return "读写文件出错"
        return True


    def check_size(self):
        if self.fobj.size>self.size:
            return False
        return True
    def check_type(self):
        ext=os.path.splitext(self.fobj.name)
        if len(ext)<=1:
            return -1     #文件没有后缀名
        ext=ext[1].lstrip('.')   #截取掉后缀前面的点
        if isinstance(self.ext,str):   #规定的文件后缀是字符串
            if ext!=self.ext:
                return -2      #文件后缀不符合要求
        elif isinstance(self.ext,(tuple,list)):
            if ext not in self.ext:
                return -2
        else:
            return -3      #规定文件后缀不能识别
        return 1     #文件类型符合要求

    def get_path(self):
        #判断是否是日期文件名
        if self.is_datefilename:
            filename=datetime.now().strftime('%Y-%m-%d')
            # 拼接路径
            path = os.path.join(self.path, path)

            if not os.path.exists(path):   #目录不存在
                os.makedirs(path)  # 创建目录


            #拼接文件名
            path=os.path.join(path,self.fobj.name)

        else:
            path=os.path.join(self.path,self.fobj.name)
        return path

    def write_file(self,path):
        try:
            with open(path,'wb') as fp:
                if self.fobj.multiple_chunks():
                    for chip in self.fobj.chunks():
                        fp.write(chip)
                else:
                    fp.write(self.fobj.read())
            return True
        except:   #如果有读写异常，返回False
            return False
if __name__ == '__main__':
    from day08.settings import MEDIA_ROOT
    fupload = Upload(path=MEDIA_ROOT,ext=['jpg','jpeg','bmp','png'])
    print(fupload.__dict__)






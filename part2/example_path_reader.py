'''
Created on 7 Aug 2016

@author: Wanyu Yin
@version: Python 2.7
Example code for Part II Metrics Essay.
This is a path reader, which provides the functionality to give out file name and extension.
'''

class PathReader:
    def __init__(self, srcPath):
        self.srcPath = srcPath
        self.filename = ''
        self.extension = ''
        
    def get_srcPath(self):
        return self.srcPath
    
    def get_filename(self):
        if self.split_srcPath():
            str_list = self.split_srcPath()
            for i in range(len(str_list)-1):
                self.filename = self.filename + str_list[i] + '.'
            if self.filename[-1] == '.':
                self.filename = self.filename[:-1]
        return self.filename
    
    def get_extension(self):
        if self.split_srcPath():
            str_list = self.split_srcPath()
            self.extension = str_list[-1]
        return self.extension
        
    def split_srcPath(self):
        if self.srcPath is None or len(self.srcPath)==0 or len(self.srcPath.split('.'))<2:
            print 'Invalid source path...'
            return False
        else:
            return self.srcPath.split('.')

if __name__ == '__main__':
    pr = PathReader('aaa.bbb.jpg')
    print pr.get_filename()
    print pr.get_extension()
    
    
        
        

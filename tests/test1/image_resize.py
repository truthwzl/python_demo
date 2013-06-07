#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#@author zcwang3@gmail.com
#@version 2010-10-20 15:47
#图片处理模块（缩放）
 
#import BaseUtil
import os
import Image
import datetime
 
srcImgFolder = srcImgFolder = r"D:\images"
count=0
def resizeFold(dir_proc):
	global count
	starttime = datetime.datetime.now()
	for file in os.listdir(dir_proc):
		fullFile = os.path.join(dir_proc, file)
		if os.path.isdir(fullFile):
			resizeFold(fullFile)
			continue
 
		#带有下划线的目标图片不需要处理
		if fullFile.find("_") != -1:
			continue
 
		#正常图片
		srcImgFullFileName = fullFile
		#BaseUtil.outputInfoMessage("INFO:process file %s" %(os.path.join(dir_proc, file)))
		#处理文件
		if os.path.isfile(srcImgFullFileName):
			folderPath = srcImgFullFileName[:srcImgFullFileName.rfind(os.sep)]
			fileName = srcImgFullFileName[srcImgFullFileName.rfind("\\")+1:]
			count +=1
			print "[%d]:%s" %(count,fileName)
			img = Image.open(srcImgFullFileName)
#			img.show()
			width,height = img.size
			targetWidthArray = (100,120,240,400,640)
			for targetWidth in targetWidthArray:
				targetImg = img.resize(
						   (targetWidth, targetWidth * height / width),
						   Image.ANTIALIAS
						   )
				newFileName = fileName.split(".")[0] + "_" + str(targetWidth) + "." + fileName.split(".")[1]
				targetImg.save(folderPath + os.sep + newFileName, 'jpeg')
 
	endtime = datetime.datetime.now()
	print "时间差:%d" %((endtime-starttime).seconds)
if __name__ == "__main__":
	resizeFold(srcImgFolder)

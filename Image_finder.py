import os, sys
from os import listdir
from collections import defaultdict
import shutil

class Image_finder:

	def __init__(self, directory=None):

		''' Class constructor which generates a dictionary detailing every image file found and where it is stored. '''
		if not os.path.isdir(directory):
			raise ValueError("directory does not exist!")

		self.directory = directory
		self.data = defaultdict(list)

		n = 0

		for root, dirs, files in os.walk(directory, topdown=True):
			for file in files:
				if file.lower().endswith(('.png', '.jpg', '.jpeg')):
					self.data[root].append(file)

					n+=1
					print("{} images found".format(n), end="\r")

		self.no_files = sum(len(lst) for lst in self.data.values())

		print('-'*10,"Imagefinder",'-'*10)
		print("No. directories: {}".format(len(self.data)))
		print("No. files: {}".format(self.no_files))

	def copy_imgs(self, save_dir=None):

		''' Copy images from their location into a folder. '''
		if not os.path.isdir(save_dir):
			os.mkdir(save_dir)
			print("New directory created!")
			
		n = 0

		for dirs, file_lst in self.data.items():
			for file in file_lst:
				shutil.copy(os.path.join(dirs,file),os.path.join(save_dir,file))

				n+=1

				print("Imagefinder: {} of {} images have been copied...".format(n,self.no_files), end="\r")

	def file_lst(self):
		file_lst = list()
		for dirs, files in self.data.items():
			for file in files:
				file_lst.append(os.path.join(dirs,file))
		return file_lst
import re
from text import Text_Class

class Skeleton_Class:

	def __init__(self, skeleton, file_contents):
		cleaned_file_contents = []
		self.texts = []
		for file_content in file_contents:
			cleaned_file_contents.append(text_toolkit.clean(file_content))
		for cleaned_text in cleaned_file_contents:
			self.texts.append(Text_Class(cleaned_text))
		self.skeleton = skeleton

	def break_into_bones(self):
		frequency_scale_bones = list(re.findall("{[\S]*\([ABCDEF],[\s]*[\S]*\)}"), self.skeleton)
		frequency_scale_flesh = []
		for bone in frequency_scale_bones:
			t_index = text_alphakey
			frequency_scale = int(re.match("[\d]+", self.skeleton))
			frequency_scale_flesh.append(self.text[t_index].random_word_by_freq_scale(frequency_scale))
		portmanteau_bones = list(re.findall("{frequency_scale\([ABCDEF],[\s]*[\S]*\)}"), self.skeleton)
		portmanteau_flesh = []
		for bone in portmanteau_bones:
			t_index = text_alphakey
			portmanteau_flesh.append(self.text[t_index].naive_random_portmanteau())
		for index, bone in enumerate(frequency_scale_bones):
			self.skeleton = self.skeleton.replace(bone, frequency_scale_flesh[index])
		for index, bone in enumerate(portmanteau_bones):
			self.skeleton = self.skeleton.replace(bone, portmanteau_flesh[index])
		return self.skeleton

	def get_text_index(bone):
		text_alphakey = re.search("\([ABCDEF],", bone)
		text_alphakey = frequency_scale_call[1:-1]
		text_index = ord(text_alphakey) - 65 if text_alphakey.isupper() else ord(text_alphakey) - 97
		return text_index
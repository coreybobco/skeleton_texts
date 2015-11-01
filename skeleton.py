import re
from text import Text_Class

class Skeleton_Class:

	def __init__(self, skeleton, file_contents):
		self.texts = []
		for file_content in file_contents:
			self.texts.append(Text_Class(file_content))
		self.skeleton = skeleton

	def generate(self):
		frequency_scale_bones = list(re.findall("\{frequency_scale\([ABCDEF],[\s]*[\S]*\)}", self.skeleton))
		frequency_bone_split = list(re.split("{\{frequency_scale\([ABCDEF],[\s]*[\S]*\)}", self.skeleton))
		frequency_scale_flesh = []
		print(frequency_scale_bones)
		for bone in frequency_scale_bones:
			t_index = self.get_text_index(bone)
			frequency_scale = int(re.search("[\d]+", self.skeleton).group(0))
			frequency_scale_flesh.append(self.texts[t_index].random_word_by_freq_scale(frequency_scale))
		flesh_text = ""
		for index, static_bone in enumerate(frequency_bone_split):
			if index == len(frequency_bone_split):
				flesh_text += static_bone
			else:
				flesh_text += static_bone + frequency_scale_flesh[index]

		old_flesh = flesh_text
		portmanteau_bones = list(re.findall("{portmanteau\([ABCDEF],[\s]*[\S]*\)}", old_flesh))
		portmanteau_bone_split = list(re.split("{portmanteau\([ABCDEF],[\s]*[\S]*\)}", old_flesh))
		portmanteau_flesh = []
		for bone in portmanteau_bones:
			t_index = self.get_text_index(bone)
			portmanteau_flesh.append(self.texts[t_index].naive_random_portmanteau())
		for index, bone in enumerate(portmanteau_bone_split):
			if index == len(portmanteau_bone_split):
				flesh_text += static_bone
			else:
				flesh_text += static_bone + portmanteau_flesh[index]
		return flesh

	def get_text_index(self, bone):
		text_alphakey = re.search("\([ABCDEF],", bone).group(0)
		text_alphakey = text_alphakey[1:-1]
		text_index = ord(text_alphakey) - 65 if text_alphakey.isupper() else ord(text_alphakey) - 97
		return text_index
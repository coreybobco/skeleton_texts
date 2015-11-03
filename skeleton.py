import re
from text import Text_Class

class Skeleton_Class:

	def __init__(self, skeleton, file_contents):
		self.texts = []
		for file_content in file_contents:
			self.texts.append(Text_Class(file_content))
		self.skeleton = skeleton

	def generate(self):
		frequency_scale_regex = "\{frequency_scale\([ABCDEF],[\s]*[\S]*\)}"
		frequency_scale_bones = re.findall(frequency_scale_regex, self.skeleton)
		frequency_bone_split = re.split(frequency_scale_regex, self.skeleton)
		frequency_scale_flesh = []
		print(len(frequency_scale_bones))
		for bone in frequency_scale_bones:
			t_index = self.get_text_index(bone)
			frequency_scale = int(re.search("[\d]+", self.skeleton).group(0))
			frequency_scale_flesh.append(self.texts[t_index].random_word_by_freq_scale(frequency_scale))
		flesh_text = ""
		print("Frequency Scales:")
		print(frequency_bone_split)
		print(len(frequency_bone_split))
		for index, static_bone in enumerate(frequency_bone_split):
			if index == len(frequency_bone_split) - 1:
				flesh_text += static_bone
			else:
				flesh_text += static_bone + frequency_scale_flesh[index]

		print(flesh_text)
		portmanteau_regex = "{portmanteau\([ABCDEF],[\s]*[\S]*\)}"
		portmanteau_bones = re.findall(portmanteau_regex, flesh_text)
		portmanteau_bone_split = re.split(portmanteau_regex, flesh_text))
		print("Portmanteaus")
		portmanteau_flesh = []
		for bone in portmanteau_bones:
			t_index = self.get_text_index(bone)
			portmanteau_flesh.append(self.texts[t_index].naive_random_portmanteau())
		print(portmanteau_flesh)
		print(portmanteau_bone_split)
		for index, bone in enumerate(portmanteau_bone_split):
			if index == len(portmanteau_bone_split) - 1:
				flesh_text += static_bone
			else:
				flesh_text += static_bone + portmanteau_flesh[index]
		return flesh_text

	def get_text_index(self, bone):
		text_alphakey = re.search("\([ABCDEF],", bone).group(0)
		text_alphakey = text_alphakey[1:-1]
		text_index = ord(text_alphakey) - 65 if text_alphakey.isupper() else ord(text_alphakey) - 97
		return text_index
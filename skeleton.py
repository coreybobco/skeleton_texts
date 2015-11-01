import re
from text import Text_Class

class Skeleton_Class:

	def __init__(self, skeleton, file_contents):
		cleaned_file_contents = []
		text_toolkit = Text_Class
		for file_content in file_contents:
			cleaned_file_contents.append(text_toolkit.clean(file_contents))
		self.inputs = cleaned_file_contents
		self.skeleton = skeleton

    def break_into_bones(self):
        frequency_scale_bones = list(re.findall("{[\S]*\([ABCDEF],[\s]?[\S]*\)}"), self.skeleton)
        portmanteau_bones = list(re.findall("{frequency_scale\([ABCDEF],[\s]?[\S]*\)}"), self.skeleton)
        for ectoplasm in frequency_scale_bones:
            function_name = re.match("\{[\S]{3,}", ectoplasm)
            call = re.search("\([ABCDEF],[\s]?[\S]*\)", ectoplasm)
            call = frequency_scale_call[1:-1].replace(" ", "")
            call_args = call.split(",")
            call_args[0] = ord(call_args[0]) - 65 if call_args[0].isupper() else ord(call_args[0]) - 97
import os
from sys import argv, exit
from datetime import datetime
from json import load as loadJson
try:
	from yaml import dump as dumpYaml
except:
	print("Cannot import ``dump`` from ``yaml``. Please try to install ``yaml`` via ``python -m pip install yaml`` or ``sudo apt-get install python3-yaml``. ")
	print("Please press the enter key to exit. ")
	try:
		input()
	except:
		print()
	exit(-1)
try:
	os.chdir(os.path.abspath(os.path.dirname(__file__)))
except:
	pass
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)


class Detectors:
	def __init__(self:object) -> object:
		self.__data = None
		self.__flag = False
	def loadJson(self:object, jsonFilePath:str, encoding:str = "utf-8") -> bool:
		try:
			with open(jsonFilePath, "r", encoding = encoding) as f:
				self.__data = loadJson(f)["Detectors"]
			self.__flag = True
			return True
		except BaseException as e:
			print("Cannot load data from \"{0}\". Details are as follows. \t{1}".format(jsonFilePath, e))
			return False
	def checkDetectorFolderPath(self:object, detectorFolderPath:str = ".") -> int:
		if self.__flag and isinstance(detectorFolderPath, str) and os.path.isdir(detectorFolderPath):
			issueCnt, fileNames = 0, [obj for obj in os.listdir(detectorFolderPath) if os.path.splitext(obj)[0] != "README" and os.path.splitext(obj)[1] != ".py"]
			for obj in self.__data:
				if "name" in obj and "latestVersion" in obj:
					fileNameA = "{0}_{1}.apk".format(obj["name"], obj["latestVersion"])
					fileNameB = fileNameA + "s"
					if fileNameA in fileNames:
						fileNames.remove(fileNameA)
					elif fileNameB in fileNames:
						fileNames.remove(fileNameB)
					else:
						issueCnt += 1
						print("File \"{0}\" or File \"{1}\" is not in Folder \"{2}\". ".format(fileNameA, fileNameB, detectorFolderPath))
				else:
					issueCnt += 1
					print("An invalid record {0} is found. ".format(obj))
				if "image" in obj:
					for imageName in obj["image"].values():
						if imageName in fileNames:
							fileNames.remove(imageName)
						else:
							issueCnt += 1
							print("Image \"{0}\" is not in Folder \"{1}\". ".format(imageName, detectorFolderPath))
			if fileNames:
				issueCnt += len(fileNames)
				print("Extra files {0} are detected. ".format(fileNames) if len(fileNames) > 1 else "An extra file entitled \"{0}\" is detected. ".format(fileNames[0]))
			return issueCnt
		else:
			return -1
	def __getSourceStatus(self:object, codes:str, language:str) -> list:
		if isinstance(codes, str) and isinstance(language, str):
			statements = []
			d = {																																	\
				"A":{"UN":"Archieved", "CN":"已存档"}, "C":{"UN":"Closed-source", "CN":"闭源"}, "D":{"UN":"Android Desktop Application", "CN":"安卓桌面应用"}, 		\
				"H":{"UN":"Half-open-source", "CN":"半开源"}, "O":{"UN":"Open-source", "CN":"开源"}, "S":{"UN":"For Sale", "CN":"销售中"}							\
			}
			for code in codes:
				if code in d:
					statements.append(d[code][language] if language in d[code] else d[code]["UN"])
				else:
					print("The code \'{0}\' has no meanings in source status statements. ".format(code))
			return statements
		else:
			return []
	def __getDevelopingPurpose(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			d = {																																						\
				"A":{"UN":"Apatch Detection", "CN":"Apatch 检测"}, "D":{"UN":"Android Desktop Application", "CN":"安卓桌面应用"}, "E":{"UN":"Environment Detection", "CN":"环境检测"}, 	\
				"I":{"UN":"Information Gathering", "CN":"信息收集"}, "K":{"UN":"Key Attestation", "CN":"密钥认证"}, "L":{"UN":"Applist Detection", "CN":"应用列表检测"}, 					\
				"M":{"UN":"Magisk Detection", "CN":"面具检测"}, "P":{"UN":"Play Integrity Check", "CN":"Play 完整性检测"}															\
			}
			if code in d:
				return d[code][language] if language in d[code] else d[code]["UN"]
			else:
				print("The code \'{0}\' has no meanings in developing purpose statements. ".format(code))
		else:
			return ""
	def __getReleaseDate(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			if len(code) >= 8 and code[-8:].isdigit():
				d = {"":"", "=":"", "==":"", "<":{"UN":"Before", "CN":"早于"}, "<=":{"UN":"On or Before", "CN":"不晚于"}, ">":{"UN":"After", "CN":"晚于"}, ">=":{"UN":"On or After", "CN":"不早于"}}
				symbol = code[:-8].strip()
				if symbol in d:
					year, month, day = int(code[-8:-4]), int(code[-4:-2]), int(code[-2:])
					try:
						date = datetime(year, month, day)
					except:
						print("The date in the code \"{0}\" is invalid in release date statements. ".format(code))
						return ""
					if "CN" == language:
						return "{0} {1} 年 {2} 月 {3} 日".format(d[symbol]["CN"] if isinstance(d[symbol], dict) else d[symbol], year, month, day)
					else:
						months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
						suffix = "th" if day % 100 in (11, 12, 13) else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
						return "{0} {1} {2}{3}, {4}".format(d[symbol]["UN"] if isinstance(d[symbol], dict) else d[symbol], months[month - 1], day, suffix, year)
				else:
					print("The symbol in the code \"{0}\" has no meanings in release date statements. ".format(code))
			else:
				print("The code \"{0}\" has no meanings in release date statements. ".format(code))
		return ""
	def __convertToMarkdown(self:object, language:str) -> str:
		if self.__flag and isinstance(language, str):
			if "UK" == language:
				markdown = "| Name | Package Name | Official Link(s) | Source Status | Developing Purpose | Latest Version | Release Date |\n| - | - | - | - | - | - | - |\n"
			elif "CN" == language:
				markdown = "| 名称 | 应用包名 | 官方链接 | 开源状态 | 开发用途 | 最新版本 | 发行日期 |\n| - | - | - | - | - | - | - |\n"
			else:
				return language
			for detector in self.__data:
				markdown += "| "
				markdown += detector["name"] + " | " if "name" in detector else "| "
				markdown += ("; ".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(detector["packageName"], list) else "``{0}``".format(detector["packageName"])) + " | " if "packageName" in detector else "| "
				markdown += ("; ".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(detector["officialLink"], list) else detector["officialLink"]) + " | " if "officialLink" in detector else "| "
				markdown += "&".join(self.__getSourceStatus(detector["sourceStatus"], language)) + " | " if "sourceStatus" in detector else "| "
				markdown += self.__getDevelopingPurpose(detector["developingPurpose"], language) + " | " if "developingPurpose" in detector else "| "
				markdown += "``{0}`` | ".format(detector["latestVersion"]) if "latestVersion" in detector else "| "
				markdown += self.__getReleaseDate(detector["releaseDate"], language) + " |\n" if "releaseDate" in detector else "|\n"
			return markdown
		else:
			return ""
	def __convertToYml(self:object) -> str:
		return dumpYaml(self.__data, allow_unicode = True, sort_keys = False, default_flow_style = False, indent = 2, width = 120) if self.__flag else ""
	def __handleFolder(self:object, fd:str) -> bool:
		try:
			folder = str(fd)
		except:
			return False
		if not folder:
			return True
		elif os.path.exists(folder):
			return os.path.isdir(folder)
		else:
			try:
				os.makedirs(folder)
				return True
			except:
				return False
	def toMarkdownFile(self:object, markdownFilePath:str = None, languages:tuple|list = ["UK", "\n---\n", "CN"], encoding:str = "utf-8") -> str|bool:
		if self.__flag:
			markdown = ""
			for language in languages:
				markdown += self.__convertToMarkdown(language)
			if isinstance(markdownFilePath, str):
				if self.__handleFolder(os.path.split(markdownFilePath)[0]):
					try:
						with open(markdownFilePath, "w", encoding = encoding) as f:
							f.write(markdown)
						print("Successfully wrote data in the format of markdown to \"{0}\". ".format(markdownFilePath))
						return True
					except BaseException as e:
						print("Cannot write data in the format of markdown to \"{0}\". Details are as follows. \n\t{1}".format(markdownFilePath, e))
				else:
					print("Cannot write data in the format of markdown to \"{0}\" since the parent folder was not created successfully. ".format(markdownFilePath))
				return False
			else:
				return markdown
		else:
			return False
	def toYmlFile(self:object, ymlFilePath:str = None, encoding:str = "utf-8") -> str|bool:
		if self.__flag:
			yml = self.__convertToYml()
			if isinstance(ymlFilePath, str):
				if self.__handleFolder(os.path.split(ymlFilePath)[0]):
					try:
						with open(ymlFilePath, "w", encoding = encoding) as f:
							f.write(yml)
						print("Successfully wrote data in the format of yml to \"{0}\". ".format(ymlFilePath))
						return True
					except BaseException as e:
						print("Cannot write data in the format of yml to \"{0}\". Details are as follows. \n\t{1}".format(ymlFilePath, e))
				else:
					print("Cannot write data in the format of yml to \"{0}\" since the parent folder was not created successfully. ".format(ymlFilePath))
				return False
			else:
				return yml
		else:
			return False


def main() -> int:
	jsonFilePath, detectorFolderPath, markdownFilePath, ymlFilePath = "README.json", ".", "README.md", "README.yml"
	detectors = Detectors()
	bRet = detectors.loadJson(jsonFilePath)
	detectors.checkDetectorFolderPath(detectorFolderPath = detectorFolderPath)
	if bRet:
		booleans = [																	\
			detectors.toMarkdownFile(markdownFilePath, languages = ["UK", "\n---\n\n", "CN"]), 	\
			detectors.toYmlFile(ymlFilePath)												\
		]
	exitCode = EXIT_SUCCESS if bRet and all(booleans) else EXIT_FAILURE
	try:
		input("Please press the enter key to exit ({0}). ".format(exitCode))
	except:
		pass
	return exitCode



if "__main__" == __name__:
	exit(main())
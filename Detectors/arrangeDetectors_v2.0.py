import os
from sys import argv, exit
from datetime import datetime
from json import load as loadJson
try:
	from yaml import dump as dumpYaml
except:
	print("Cannot import ``dump`` from ``yaml``. Please try to install ``yaml`` via ``python -m pip install pyyaml`` or ``sudo apt-get install python3-yaml``. ")
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
			print("Cannot load data from \"{0}\". Details are as follows. \n\t{1}".format(jsonFilePath, e))
			return False
	def checkDetectorFolderPath(self:object, detectorFolderPath:str = ".") -> int:
		if self.__flag and isinstance(detectorFolderPath, str) and os.path.isdir(detectorFolderPath):
			issueCnt, fileNames = 0, [obj for obj in os.listdir(detectorFolderPath) if os.path.splitext(obj)[0] != "README" and os.path.splitext(obj)[0] != "TABLE" and os.path.splitext(obj)[1] != ".py"]
			for obj in self.__data:
				if "name" in obj and "latestVersion" in obj:
					fileNameA = "{0}_{1}.apk".format(obj["name"], obj["latestVersion"])
					fileNameB = fileNameA + "s"
					fileNameC, fileNameD = fileNameA + ".nomedia", fileNameB + ".nomedia"
					if fileNameA in fileNames:
						fileNames.remove(fileNameA)
					elif fileNameB in fileNames:
						fileNames.remove(fileNameB)
					elif fileNameC in fileNames:
						fileNames.remove(fileNameC)
					elif fileNameD in fileNames:
						fileNames.remove(fileNameD)
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
				"A":{"*":"Archieved", "zh-CN":"已存档"}, "C":{"*":"Closed-source", "zh-CN":"闭源"}, "D":{"*":"Android Desktop Application", "zh-CN":"安卓桌面应用"}, 		\
				"H":{"*":"Half-open-source", "zh-CN":"半开源"}, "O":{"*":"Open-source", "zh-CN":"开源"}, "S":{"*":"For Sale", "zh-CN":"销售中"}							\
			}
			for code in codes:
				if code in d:
					statements.append(d[code][language] if language in d[code] else d[code]["*"])
				else:
					print("The code \'{0}\' has no meanings in source status statements. ".format(code))
			return statements
		else:
			return []
	def __getDevelopingPurpose(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			d = {																																						\
				"A":{"*":"Apatch Detection", "zh-CN":"Apatch 检测"}, "D":{"*":"Android Desktop Application", "zh-CN":"安卓桌面应用"}, "E":{"*":"Environment Detection", "zh-CN":"环境检测"}, 	\
				"I":{"*":"Information Gathering", "zh-CN":"信息收集"}, "K":{"*":"Key Attestation", "zh-CN":"密钥认证"}, "L":{"*":"Applist Detection", "zh-CN":"应用列表检测"}, 					\
				"M":{"*":"Magisk Detection", "zh-CN":"面具检测"}, "P":{"*":"Play Integrity Check", "zh-CN":"Play 完整性检测"}															\
			}
			if code in d:
				return d[code][language] if language in d[code] else d[code]["*"]
			else:
				print("The code \'{0}\' has no meanings in developing purpose statements. ".format(code))
		else:
			return ""
	def __getReleaseDate(self:object, code:str, language:str) -> str:
		if isinstance(code, str) and isinstance(language, str):
			if len(code) >= 8 and code[-8:].isdigit():
				d = {"":"", "=":"", "==":"", "<":{"*":"Before", "zh-CN":"早于"}, "<=":{"*":"On or Before", "zh-CN":"不晚于"}, ">":{"*":"After", "zh-CN":"晚于"}, ">=":{"*":"On or After", "zh-CN":"不早于"}, "!=":{"*":"Not On", "zh-CN":"不是"}}
				symbol = code[:-8].strip()
				if symbol in d:
					year, month, day = int(code[-8:-4]), int(code[-4:-2]), int(code[-2:])
					try:
						date = datetime(year, month, day)
					except:
						print("The date in the code \"{0}\" is invalid in release date statements. ".format(code))
						return ""
					if "zh-CN" == language:
						return "{0} {1} 年 {2} 月 {3} 日".format(d[symbol]["zh-CN"] if isinstance(d[symbol], dict) else d[symbol], year, month, day)
					else:
						months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
						suffix = "th" if day % 100 in (11, 12, 13) else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
						return "{0} {1} {2}{3}, {4}".format(d[symbol]["*"] if isinstance(d[symbol], dict) else d[symbol], months[month - 1], day, suffix, year)
				else:
					print("The symbol in the code \"{0}\" has no meanings in release date statements. ".format(code))
			else:
				print("The code \"{0}\" has no meanings in release date statements. ".format(code))
		return ""
	def __convertToMarkdownTable(self:object, language:str) -> str:
		if self.__flag and isinstance(language, str):
			if "zh-CN" == language:
				markdown = "## 检测软件\n\n| 名称 | 应用包名 | 官方链接 | 开源状态 | 开发用途 | 最新版本 | 发行日期 |\n| - | - | - | - | - | - | - |\n"
				separator = "；"
			elif len(language) == 2 and "A" <= language[0] <= "Z" and "A" <= language[1] <= "Z":
				markdown = "## Detectors\n\n| Name | Package Name(s) | Official Link(s) | Source Status | Developing Purpose | Latest Version | Release Date |\n| - | - | - | - | - | - | - |\n"
				separator = "; "
			else:
				return language
			for detector in self.__data:
				markdown += "| "
				markdown += detector["name"] + " | " if "name" in detector else "| "
				markdown += (separator.join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(detector["packageName"], list) else "``{0}``".format(detector["packageName"])) + " | " if "packageName" in detector else "| "
				markdown += (separator.join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(detector["officialLink"], list) else "[{0}]({0})".format(detector["officialLink"])) + " | " if "officialLink" in detector else "| "
				markdown += " & ".join(self.__getSourceStatus(detector["sourceStatus"], language)) + " | " if "sourceStatus" in detector else "| "
				markdown += self.__getDevelopingPurpose(detector["developingPurpose"], language) + " | " if "developingPurpose" in detector else "| "
				markdown += "``{0}`` | ".format(detector["latestVersion"]) if "latestVersion" in detector else "| "
				markdown += self.__getReleaseDate(detector["releaseDate"], language) + " |\n" if "releaseDate" in detector else "|\n"
			return markdown
		else:
			return ""
	def __convertToMarkdownText(self:object, language:str) -> str:
		if self.__flag and isinstance(language, str):
			if "en" == language:
				txt = "## Detectors\n\nMomo $\\rightarrow$ Native Root Detector $\\rightarrow$ Native Test ++\n\n"
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and ("*" in detector["alias"] or "en" in detector["alias"]):
						txt += "- **Alias**: "
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						if "en" in detector["alias"]:
							aliasVector += detector["alias"]["en"] if isinstance(detector["alias"]["en"], (tuple, list)) else [detector["alias"]["en"]]
						txt += "; ".join(aliasVector) + "\n"
					txt += (																																												\
						"- **Package Names**: " + "; ".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(detector["packageName"], list) else "- **Package Name**: " + "``{0}``".format(detector["packageName"])	\
					) + "\n" if "packageName" in detector else ""
					txt += (																																							\
						"- **Official Links**: " + "; ".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(detector["officialLink"], list) else "- **Official Link**: " + detector["officialLink"]	\
					) + "\n" if "officialLink" in detector else ""
					txt += "- **Source Status**: " + " & ".join(self.__getSourceStatus(detector["sourceStatus"], "en")) + "\n" if "sourceStatus" in detector else ""
					txt += "- **Developing Purpose**: " + self.__getDevelopingPurpose(detector["developingPurpose"], "en") + "\n" if "developingPurpose" in detector else ""
					txt += "- **Latest Version**: ``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **Release Date**: " + self.__getReleaseDate(detector["releaseDate"], "en") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and ("*" in detector["detectionRemark"] or "en" in detector["detectionRemark"]):
						txt += "- **Detection Remark**: "
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						if "en" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["en"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					if "image" in detector and "en" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["en"])
					txt += "\n"
				return txt
			elif "zh-CN" == language:
				txt = "## 检测软件\n\nMomo $\\rightarrow$ Native Root Detector $\\rightarrow$ 牛头人\n\n"
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and ("*" in detector["alias"] or "zh-CN" in detector["alias"]):
						txt += "- **应用别称**："
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						if "zh-CN" in detector["alias"]:
							aliasVector += detector["alias"]["zh-CN"] if isinstance(detector["alias"]["zh-CN"], (tuple, list)) else [detector["alias"]["zh-CN"]]
						txt += "; ".join(aliasVector) + "\n"
					txt += (																																									\
						"- **应用包名**：{0}\n".format("；".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(detector["packageName"], list) else "``{0}``".format(detector["packageName"]))		\
					) if "packageName" in detector else ""
					txt += (																																									\
						"- **官方链接**：{0}\n".format("；".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(detector["officialLink"], list) else "[{0}]({0})".format(detector["officialLink"]))		\
					) if "officialLink" in detector else ""
					txt += "- **开源状态**：" + " & ".join(self.__getSourceStatus(detector["sourceStatus"], "zh-CN")) + "\n" if "sourceStatus" in detector else ""
					txt += "- **开发用途**：" + self.__getDevelopingPurpose(detector["developingPurpose"], "zh-CN") + "\n" if "developingPurpose" in detector else ""
					txt += "- **最新版本**：``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **发行日期**：" + self.__getReleaseDate(detector["releaseDate"], "zh-CN") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and ("*" in detector["detectionRemark"] or "zh-CN" in detector["detectionRemark"]):
						txt += "- **检测备注**："
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						if "zh-CN" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["zh-CN"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					if "image" in detector and "zh-CN" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["zh-CN"])
					txt += "\n"
				return txt
			elif len(language) == 2 and "A" <= language[0] <= "Z" and "A" <= language[1] <= "Z":
				txt = "## Detectors\n\n"
				for detector in self.__data:
					txt += "### " + detector["name"] + "\n\n"
					if "alias" in detector and "*" in detector["alias"]:
						txt += "- **Alias**: "
						aliasVector = []
						if "*" in detector["alias"]:
							aliasVector += detector["alias"]["*"] if isinstance(detector["alias"]["*"], (tuple, list)) else [detector["alias"]["*"]]
						txt += "; ".join(aliasVector) + "\n"
					txt += (																																												\
						"- **Package Names**: " + "; ".join(["``{0}``".format(pkg) for pkg in detector["packageName"]]) if isinstance(detector["packageName"], list) else "- **Package Name**: " + "``{0}``".format(detector["packageName"])	\
					) + "\n" if "packageName" in detector else ""
					txt += (																																							\
						"- **Official Links**: " + "; ".join(["[{0}]({0})".format(link) for link in detector["officialLink"]]) if isinstance(detector["officialLink"], list) else "- **Official Link**: " + detector["officialLink"]	\
					) + "\n" if "officialLink" in detector else ""
					txt += "- **Source Status**: " + " & ".join(self.__getSourceStatus(detector["sourceStatus"], "*")) + "\n" if "sourceStatus" in detector else ""
					txt += "- **Developing Purpose**: " + self.__getDevelopingPurpose(detector["developingPurpose"], "*") + "\n" if "developingPurpose" in detector else ""
					txt += "- **Latest Version**: ``{0}``\n".format(detector["latestVersion"]) if "latestVersion" in detector else ""
					txt += "- **Release Date**: " + self.__getReleaseDate(detector["releaseDate"], "*") + "\n" if "releaseDate" in detector else ""
					if "detectionRemark" in detector and "*" in detector["detectionRemark"]:
						txt += "- **Detection Remark**: "
						if "*" in detector["detectionRemark"]:
							txt += detector["detectionRemark"]["*"]
						txt += "\n"
					if "image" in detector and "*" in detector["image"]:
						txt += "- ![{0}]({0})\n".format(detector["image"]["*"])
					txt += "\n"
				return txt
			else:
				return language
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
	def toMarkdownFile(self:object, markdownFilePath:str = None, languages:tuple|list = ("en", "\n---\n", "zh-CN"), isTable:bool = False, encoding:str = "utf-8") -> str|bool:
		if self.__flag and isinstance(isTable, bool):
			markdown = ""
			for language in languages:
				markdown += self.__convertToMarkdownTable(language) if isTable else self.__convertToMarkdownText(language)
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
	jsonFilePath, detectorFolderPath, markdownTextFilePath, markdownTableFilePath, ymlFilePath = "README.json", ".", "README.md", "TABLE.md", "README.yml"
	detectors = Detectors()
	bRet = detectors.loadJson(jsonFilePath)
	detectors.checkDetectorFolderPath(detectorFolderPath = detectorFolderPath)
	if bRet:
		booleans = [																					\
			detectors.toMarkdownFile(markdownTextFilePath, languages = ("en", "\n---\n\n", "zh-CN"), isTable = False), 	\
			detectors.toMarkdownFile(markdownTableFilePath, languages = ("en", "\n---\n\n", "zh-CN"), isTable = True), 	\
			detectors.toYmlFile(ymlFilePath)																\
		]
	exitCode = EXIT_SUCCESS if bRet and all(booleans) else EXIT_FAILURE
	try:
		input("Please press the enter key to exit ({0}). ".format(exitCode))
	except:
		pass
	return exitCode



if "__main__" == __name__:
	exit(main())
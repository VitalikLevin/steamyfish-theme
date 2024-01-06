import logging
import re
logFile = logging.FileHandler("out/textclean.log")
consoleOut = logging.StreamHandler()
logging.basicConfig(handlers=(logFile, consoleOut), level=logging.DEBUG)
regexp = re.compile("(<div al){1}[\u0000-\uFFFF]+/div>")
tempFile = open("README.md", encoding="utf8").read()
file = open("README.md", "w", encoding="utf8")
def textclean(text, filR):
  logging.debug("Entered `textclean`")
  text = regexp.sub("> Read about changes in [Unreleased section](CHANGELOG.md#Unreleased).", text, count=0)
  filR.truncate(0)
  filR.write(text)
  logging.debug("README was successfully overwriten")
  filR.close()
textclean(tempFile, file)
#!/usr/bin/python

import os, os.path, argparse, webbrowser

class Appletizer():
	def __init__(self, args):
		print("Appletizer initializing...")
		self.args = args
		if args.create:
			if args.browser:
				self.createApplet(args.browser)
			else:
				self.createApplet()
		if args.executable:
			self.makeExec()
		if args.move:
			self.move()
		print("Appletizer initialized")

	def loadConf(self):
		if not(os.path.exists("~/.config/appletizer/conf")):
			print("no conf")
			self.initConf()
		else:
			print("loading conf...")
			print("loaded conf")

	def initConf(self):
		print("initializing conf...")
		
		print("initialized conf")

	def createApplet(self, browser = "xdg-open"):
		print("creating applet...")
		f = open(self.args.name, 'w')
		f.write("#!/usr/bin/bash\n")
		f.write(browser + " " + self.args.url)
		f.close()
		print("created applet")
		
	def makeExec(self):
		os.system("sudo chmod +x " + self.args.name)

	def move(self):
		os.system("sudo mv " + self.args.name + " /usr/bin/")

	def movePath(self):
		os.system("mv " + self.args.name + " " + self.args.path)
		

parser = argparse.ArgumentParser()

parser.add_argument('-c', action="store_true", dest="create", default=False, help="create applet")
parser.add_argument('-e', action="store_true", dest="executable", default=False, help="make file executable (requires sudo)")
parser.add_argument('-m', action="store_true", dest="move", default=False, help="move file to /usr/bin directory (requires sudo)")
#parser.add_argument('-p', action="store", dest="path", default=False, help="move file to PATH")
#parser.add_argument('-d', action="store_true", dest="dir", default=False, help="creates dir in home for applets, and adds path to .bashrc")
parser.add_argument('-b', action="store", dest="browser", default=False, help="use browser other than default")
parser.add_argument('-u', action="store", dest="url", help="the url for the applet to open")
parser.add_argument('-n', action="store", dest="name", help="the name given to the applet")


appletizer = Appletizer(parser.parse_args());


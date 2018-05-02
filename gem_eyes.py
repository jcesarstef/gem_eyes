import re
import requests
tools = []

gemlockre = "^\W*([a-zA-Z-_0-9]*)[\t (=><~]*([0-9.]*)"

def getgems(gemfile):
	with open(gemfile) as f:
		lines = f.readlines()
	for line in lines:
		a = line.split("'")
		try:
			#print(a[1] + " " + a[3].split(" ")[1])
			tools.append("https://www.versioneye.com/ruby/" + a[1] + "/" + a[3].split(" ")[1])
			#print(a[3])
		except IndexError:
			pass
		try:
			linere = re.findall(gemlockre, line)
			if len(linere[0][1]) != 0:
				tools.append("https://www.versioneye.com/ruby/" + linere[0][0] + "/" + linere[0][1])
		except IndexError:
			pass
	requesteyes(tools)
def requesteyes(list_urls):
	for url in list_urls:
		resp = requests.get(url)
		#print(str(resp.status_code) + " " + url)
		if resp.status_code == 200:
			resp.text
			vuln = re.findall("Security Vulnerabilities", resp.text)
			if len(vuln) != 0:
				print(url + "\n" + vuln[0] + ":")
				for item in re.findall("<h2>(.*?)</h2>", resp.text):
					print(" > " + item)
				print("Reference: " + url + "\n")


if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser(description = 'gem_eyes. Search for vulnerables gems.\nCreated by @jcesrstef.')
	parser.add_argument('--file', '-f',action = 'store', dest = 'file', required = True, help = 'File to scan.')

	arguments = parser.parse_args()
	getgems(arguments.file)

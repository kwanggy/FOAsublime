import sublime, sublime_plugin,subprocess,urllib2,urllib,json

class FormatterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0,self.view.size())
		content = self.view.substr(sublime.Region(0,self.view.size()))
		data = {'fullText': content }
		data = urllib.urlencode(data)
		filename = str(self.view.file_name()).split("/")[-1]
		url='http://localhost:8081/xtext-service/format?resource='+filename
		response = urllib2.urlopen(url,data)
		text = json.loads(response.read())['formattedText']
		self.view.replace(edit,region,text)


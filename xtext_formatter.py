import sublime, sublime_plugin, urllib2, urllib, json

class FormatterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0,self.view.size())
		content = self.view.substr(sublime.Region(0,self.view.size()))
		data = {'fullText': content }
		data = urllib.urlencode(data)
		url='http://localhost:8081/xtext-service/format?resource=text.statemachine'
		response = urllib2.urlopen(url,data)
		text = json.loads(response.read())['formattedText']
		self.view.replace(edit,region,text)


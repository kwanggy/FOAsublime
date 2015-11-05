import sublime, sublime_plugin, urllib2, urllib, json

class ValidatorCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0,self.view.size())
		content = self.view.substr(sublime.Region(0,self.view.size()))
		data = {'fullText': content }
		data = urllib.urlencode(data)
		url='http://localhost:8081/xtext-service/validate?resource=text.statemachine'
		response = urllib2.urlopen(url,data)
		self.view.insert(edit,self.view.size(),"\n")
		response = json.loads(response.read())['issues']
		for key, value in enumerate(response):
			for index,title in enumerate(value):
				self.view.insert(edit,self.view.size(),"# "+str(title)+" : "+str(value[title])+"\n")

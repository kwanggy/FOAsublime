import sublime, sublime_plugin, urllib2, urllib, json , styled_popup


class ValidatorCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = sublime.Region(0,self.view.size())
		self.view.add_regions("text",[region],"")
		content = self.view.substr(sublime.Region(0,self.view.size()))
		data = {'fullText': content }
		data = urllib.urlencode(data)
		filename = str(self.view.file_name()).split("/")[-1]
		url='http://localhost:8081/xtext-service/validate?resource='+filename
		response = urllib2.urlopen(url,data)
		self.view.insert(edit,self.view.size(),"\n")
		response = json.loads(response.read())['issues']
		for key, value in enumerate(response):
			for index,title in enumerate(value):
				self.view.insert(edit,self.view.size(),"# "+str(title)+" : "+str(value[title])+"\n")
				if(title=="offset"):
					print(value[title])
					self.view.add_regions(str(key),[self.view.word(value[title])],"invalid")
			self.view.insert(edit,self.view.size(),"\n")

		#self.view.add_regions("text",[region],"")
		#self.view.add_regions("test",[self.view.word(102)],"invalid")
		#self.view.add_regions("test",[self.view.word(94)],"invalid")
		#self.view.add_regions("test",[self.view.word(167)],"invalid")

		
		'''
		sublime.message_dialog("hhijaldifhlaidfjlaijdfliasfdhlaidfjlij")
		html = """Each <span class="keyword">element</span> within
                  the <span class="entity name class">html</span> can be styled
                  individually using common <span class="string quoted">scope</span> names.
                  Simply wrap each element to be styled in a span and apply the
                  <span class="comment line">css classes</span> for each scope."""

        styled_popup.show_popup(self.window.active_view(), html)
        '''
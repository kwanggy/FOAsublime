import sublime, sublime_plugin, urllib2, urllib, json

class GoogleAutocomplete(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        region = sublime.Region(0,view.size())
        content = view.substr(sublime.Region(0,view.size()))
        row = view.rowcol(locations[0])[0]
        col = view.rowcol(locations[0])[1]
        offset = view.text_point(row,col)
        data = {'caretOffset': offset ,'fullText': content }
        data = urllib.urlencode(data)
        filename = str(view.file_name()).split("/")[-1]
        url='http://localhost:8081/xtext-service/assist?resource='+filename
        response = urllib2.urlopen(url,data)
        response = json.loads(response.read())['entries']
        output = []
        for key, value in enumerate(response):
            output.append(self.create_completion(value["proposal"],"xtext"))
        #output = [x['proposal'] for x in response ]
        #output = [ "hi" ,"hello ","hoho"]
        print output
        return output

    def create_completion(self, var, location):
        return (var + '\t' + location, var)
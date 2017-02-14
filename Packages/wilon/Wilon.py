import sublime
import sublime_plugin
import decimal
import re
from . import simplejson as json
from .simplejson import OrderedDict

# 命令：format_blog_json
class FormatBlogJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # 获取当前文件全文
        selection = sublime.Region(0, self.view.size())
        full_text = self.view.substr(selection)
        res_text = full_text.replace('\\n', '\n')
        res_text = re.sub(r'\"des\":\s+\"\s+', '"des": "\n', res_text)
        self.view.replace(edit, selection, res_text)
        print(edit, selection, res_text)

class MinifyBlogJsonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print(self, edit)

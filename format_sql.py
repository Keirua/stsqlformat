import sublime
import sublime_plugin
from .sqlparse import format

class FormatSqlCommand(sublime_plugin.TextCommand):  
    def run(self, edit):
        settings = self.view.settings()
        indent_size = int(settings.get("tab_size"))
        for s in self.view.sel():
            txt = format(
                self.view.substr(s).encode("utf-8"),
                keyword_case="upper",
                identifier_case="lower",
                reindent=True,
                indent_width=indent_size
            )

            self.view.replace(edit, s, txt)

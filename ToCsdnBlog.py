# -*- coding: utf-8 -*-
'''
#======================================================================
#       FileName: ToCsdnBlog.py
#           Desc: 将Sublime Text的Markdown Preview插件生成的HTML代码段
#                 转换为CSDN博客支持的HTML代码段
#         Author: Xuan Jun (idxuanjun@gmail.com)
#           Link: http://idxuanjun.github.io
#        Version: 0.1.0
#     LastChange: 2013-11-18 16:53:07
#        History:
#======================================================================
'''

import sublime, sublime_plugin

class ConvertHtmlCodeSegmentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        '''
        将Sublime Text的Markdown Preview插件生成的HTML代码段转换为CSDN博客支持的HTML代码段。
        以下转换有顺序，请勿随意变更。
        '''
        # replace"<pre><code class="plain">"
        src = self.view.find_all("<pre><code class=\"plain\">", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<pre name=\"code\" class=\"plain\">")
        # replace"<pre lang="plain"><code>"
        src = self.view.find_all("<pre lang=\"plain\"><code>", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<pre name=\"code\" class=\"plain\">")
        # replace"<pre><code>"
        src = self.view.find_all("<pre><code>", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<pre name=\"code\" class=\"plain\">")
        # replace"</code></pre>"
        src = self.view.find_all("</code></pre>", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "</pre>")
        # replace"<code>"
        src = self.view.find_all("<code>", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<code style=\"background-color: rgb(204, 204, 204);\">")
        # replace"<h1 id="
        src = self.view.find_all("<h1 id=", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<br /><h1 id=")
        # replace"<h2 id="
        src = self.view.find_all("<h2 id=", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<br /><h2 id=")
        # replace"<h3 id="
        src = self.view.find_all("<h3 id=", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "<br /><h3 id=")
        # replace"</h2>\n"
        src = self.view.find_all("</h2>\n", sublime.IGNORECASE)
        src.reverse()
        for r in src:
            self.view.replace(edit, r, "</h2><hr />\n")

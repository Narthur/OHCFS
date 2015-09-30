class HtmlGenerator:
    def _element(self, name, content):
        return '<{}>{}</{}>'.format(name,content,name)

    def h1(self, content):
        return self._element('h1',content)

    def _li(self, content):
        return self._element('li',content)

    def list(self, items):
        itemMarkup = ''
        for item in items:
            itemMarkup += self._li(item)
        return self._element('ul',itemMarkup)
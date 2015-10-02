class HtmlGenerator:
    def _element(self, name, content, props=None):
        propsMarkup = self._propsMarkup(props)

        return '<{}{}>{}</{}>'.format(name,propsMarkup,content,name)

    def _propsMarkup(self, props):
        propsMarkup = ''
        if props != None:
            for prop, value in props.iteritems():
                propsMarkup += ' {}="{}"'.format(prop, value)
        return propsMarkup

    def h1(self, content):
        return self._element('h1',content)

    def _li(self, content):
        return self._element('li',content)

    def list(self, items):
        itemMarkup = ''
        for item in items:
            itemMarkup += self._li(item)
        return self._element('ul',itemMarkup)

    def link(self, url, text, classes=None):
        if classes==None:
            props = {'href':url}
        else:
            props = {'href':url,'class':classes}
        return self._element('a',text,props)

    def table(self, tabularData):
        htmlBody = ''
        for row in tabularData:
            htmlRow = ''
            for cell in row:
                htmlCell = self._element('td',cell)
                htmlRow += htmlCell
            htmlBody += self._element('tr',htmlRow)
        htmlTable = self._element('tbody',htmlBody)
        return self._element('table',htmlTable)
class HtmlGenerator:
    def _element(self, name, content, props=None):
        propsMarkup = self._propsMarkup(props)

        return '<{}{}>{}</{}>'.format(name,propsMarkup,content,name)

    def _propsMarkup(self, props):
        propsMarkup = ''
        if props is not None:
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
        if classes is None:
            props = {'href':url}
        else:
            props = {'href':url,'class':classes}
        return self._element('a',text,props)

    def table(self, tabularData, headings=None):
        htmlHead = self._tableHead(headings)
        htmlBody = self._tableBody(tabularData)
        return self._element('table', htmlHead + htmlBody)

    def _tableHead(self, headings):
        if headings:
            headingsRow = self._tableHeadingsRow(headings)
            return self._element('thead', headingsRow)
        else:
            return ''

    def _tableHeadingsRow(self, headings):
        headingsHtml = ''
        for heading in headings:
            headingsHtml += self._tableHeaderCell(heading)
        return self._element('tr', headingsHtml)

    def _tableHeaderCell(self, heading):
        return self._element('th', heading)

    def _tableBody(self, tabularData):
        htmlRows = ''
        for row in tabularData:
            htmlRows += self._tableRow(row)
        return self._element('tbody', htmlRows)

    def _tableRow(self, row):
        htmlCells = ''
        for cell in row:
            htmlCells += self._tableCell(cell)
        return self._element('tr', htmlCells)

    def _tableCell(self, cell):
        return self._element('td', cell)

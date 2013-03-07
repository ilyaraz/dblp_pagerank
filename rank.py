from xml.sax import make_parser, handler

class Parser(handler.ContentHandler):
    def __init__(self):
        self.authors_list = []
        self.in_author = False
        self.current_author = ""
    def startElement(self, name, attrs):
        if name == "article":
            self.authors_list = []
        if name == "author":
            self.in_author = True
            self.current_author = ""
    def endElement(self, name):
        if name == "author":
            self.in_author = False
            self.authors_list.append(self.current_author)
        if name == "article":
            self.processPaper()
    def characters(self, content):
        if self.in_author:
            self.current_author += content
    def processPaper(self, ):


parser = make_parser()
parser.setContentHandler(Parser())
parser.parse("dblp.xml")

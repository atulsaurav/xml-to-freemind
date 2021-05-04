import sys
from lxml import etree as et
from xml.sax.saxutils import quoteattr

class FreeMindCreator:
	"""FreeMindCreator class. Accepts the outputfile as an argument. If not provided, writes the xml to stdout"""
	def __init__(self, outfile=sys.stdout):
		self.outfile = outfile
		self.line_counter = 1
		self.mmlines = ['<map version="1.0.1">\n',
		'<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->\n'
		]
	
	def start(self, tag, attrib):
		attrib = ' '.join([f"{key}={value}" for key, value in attrib.items()])
		blank, space = '', " "
		mmattr = quoteattr(tag + (space if attrib.strip() else blank) + attrib.strip())
		mmtext = f'<node ID="ID_{self.line_counter}" TEXT={mmattr}>'
		self.mmlines.append(mmtext + '\n')
		self.line_counter += 1

	def end(self, tag):
		self.mmlines.append("</node>\n")

	def data(self, data):
		data = data.strip()
		if data:
			self.mmlines[-1] = self.mmlines[-1][:-3] + " text='" + data + "'\">" 
		
	def close(self):
		self.mmlines.append("</map>")
		with open(self.outfile, 'w') as of:
			of.writelines(self.mmlines)

	def generate_mm(self):
		self.mmlines.append('</map>')
		with open(self.outfile, 'w') as of:
			of.writelines(self.mmlines)

if __name__ == "__main__":
	infile = sys.argv[1]
	outfile = sys.argv[2]
	parser = et.XMLParser(target=FreeMindCreator(outfile))
	print('Parser initialized, Parsing xml...')
	_ = et.parse(infile, parser)
	print(f'Parse complete. Generated {outfile}')

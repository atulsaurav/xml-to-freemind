# xml-to-freemind
Python script to convert and xml to Freemind mindmap.

FreeMind is an opensource mindmapping software. It is also a great way to vizualize the structure of an xml. On a windows machine it is easy to just paste a well indented xml into a new mindmap to get it imported in FreeMind.

This functionality however doesn't work on the MacOS version of Freemind. This tool is intended to solve this problem. `xml2mm.py` is a python3 script that reads an xml as an input and generates a Freemind compatible mindmap file as output. It needs `lxml` to be installed into the python environment.

It accepts 2 arguments and the usage is as below

```bash
$ python xml2mm.py xml_input_file mm_output_file
```

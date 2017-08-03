# -*- coding:utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas=[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.writelines('<html>')
        fout.writelines('<head>')
        fout.writelines("<meta charset='utf-8'>")
        fout.writelines('</head>')
        fout.writelines('<body>')
        fout.writelines("<table border=\"1\">")
        fout.writelines("<tr><th></th> <th></th>  </tr>")
        for data in self.datas:
            fout.writelines("<tr>")
            fout.writelines("<td><a href='%s' target='_blank'>%s</a></td>" % (data['url'], data['title']))
            fout.writelines("<td>%s</td>" % data['summary'])
            fout.writelines('</tr>')
        fout.writelines('</table>')
        fout.writelines('</body>')
        fout.writelines('</html>')
        fout.close()

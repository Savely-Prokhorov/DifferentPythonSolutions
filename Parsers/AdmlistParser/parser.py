from lxml import html
import requests

adm_set = set()
f = open('admlist.csv', 'w', encoding='utf-8')


def parse(univers_urls):
    for el in univers_urls:
        univer_url = url + el
        r = requests.get(univer_url)
        r.encoding = 'utf-8'
        page = r.text
        tree = html.fromstring(page)

        progs_urls = []
        for table in tree.xpath('//table'):
            for cell in table.xpath('.//tr/td[1]'):
                progs_urls.extend(cell.xpath('.//a/@href'))

        for el in progs_urls:
            prog_url = univer_url[:-10]+el # обрезаем "index.html"
            print(prog_url)

            r = requests.get(prog_url)
            r.encoding = 'utf-8'
            page = r.text

            tree = html.fromstring(page)
            university_title = tree.xpath('//center/h2/a/text()')[0]
            prog_title = tree.xpath('//center/h2/text()')[0]
            title = university_title + prog_title

            try:
                for table in tree.xpath('//table')[1]:
                    for row in table.xpath('.//tr'):
                        name = row.xpath('.//td[4]/text()')
                        if name != []:
                            name = name[0]
                        else:
                            name = ''

                        progr = row.xpath('.//a/text()')
                        type_of_doc = row.xpath('.//td[5]/text()')
                        if not type_of_doc == []:
                            type_of_doc = type_of_doc[0]
                        else:
                            type_of_doc = ''
                        progr.append(title + ' - ' + type_of_doc)

                        if not name in adm_set:
                            adm_set.update(name)
                            progr = ';'.join(progr)
                            f.write("%s;%s\n" % (name, progr))
            except IndexError:
                pass

# получаем список ссылок на университеты
url = 'http://admlist.ru/'
r = requests.get(url)
r.encoding = 'utf-8'
page = r.text
tree = html.fromstring(page)

univers_urls = []
for table in tree.xpath('//table')[0:2]:  # только Москва или Питер
    for cell in table.xpath('.//tr/td[1]'):
        univers_urls.extend(cell.xpath('.//a/@href'))

parse(univers_urls)
# Получаем список ссылок на программы
print(len(adm_set))
f.close()

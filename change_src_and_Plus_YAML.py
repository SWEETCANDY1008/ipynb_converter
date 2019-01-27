import markdown
import sys, os
import datetime

class test:
    def __init__(self, files, file_name):
        self.files = files
        self.file_name = file_name


    def change_scr_tag(self):

        fs = open(self, 'r', encoding='UTF8')
        text = fs.readlines()
        
        f = open(self, 'w+t', encoding='UTF8')
        for start in text:
            # 이미지일때만 바꿔야한다. javascript 같은게 다 바뀌어버림
            finding = start.find('src="')
            finding_next = start.find('"', finding + 5)

            finding2 = start.find("```python")
            finding3 = start.find("```")

            finding4 = start.find("```txt")
            
            if finding == -1:
                if finding2 == -1:
                    if finding3 == -1:
                        if finding4 == -1:
                            starts = start
                            f.write(starts)
                        else:
                        starts = start.replace('```txt', "<blockquote>")
                        f.write(starts)
                    else:
                        starts = start.replace('```', "</blockquote>")
                        f.write(starts)
                else:
                    starts = start.replace('```python', "<blockquote>")
                    f.write(starts)

            else:
                # 만약 글자들 사이에 개행문자가 존재할 경우 개행문자를 공백으로 바꾸어 주어야 한다.
                starts = start.replace(start[finding+4:finding_next+1], "\"{{ \"assets/" + start[finding+5:finding_next+1] + " | relative_url }}\"")
                f.write(starts)

        f.close()
        fs.close()

    def plus_YAML(self, file_name, category):
        dt = datetime.datetime.now()
        day = dt.strftime('%Y-%m-%d-')
        insert_text_day = dt.strftime('%Y-%m-%d %H:%M:%S +0900')

        insert_text = "---\nlayout: post\ntitle: " + file_name + "\ndate: " + insert_text_day + "\ncategories: " + category + "\n---\n"

        f = open(self, 'r', encoding='UTF8')
        htmlmarkdown=markdown.markdown( f.read() )
        print(htmlmarkdown)
        fs = open(self, 'w+t', encoding='UTF8')
        new_text = insert_text + htmlmarkdown
        fs.write(new_text)
        f.close()
        fs.close()
        

        os.rename(self, day + file_name + '.md')


def run():
    name = sys.argv[1]
    file_name = sys.argv[2]
    category = sys.argv[3]
    # layout = sys.argv[2]
    # title = sys.argv[3]
    # date = sys.argv[4]
    # categories = sys.argv[5]

    test.change_scr_tag(name)
    test.plus_YAML(name, file_name, category)

if __name__ == "__main__":
    run()

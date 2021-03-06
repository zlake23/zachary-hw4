import glob
import os
from jinja2 import Template


pages = []


#builds pages list by iterating through files in content directory
def page_list():
    all_html_files = glob.glob('content/*.html')
    for item in all_html_files:
        file_path = os.path.basename(item)
        name_only, extension = os.path.splitext(file_path) 
        pages.append({
        "filename": item,
        "output": 'docs/' + file_path,
        "active": name_only,
        "title": name_only,
        "link": file_path,
        })

def new_page():
    file_name = input('File name? ')
    file_content = '''<h1>New Page</h1>
    <p>New content...</p>'''
    open('content/' + file_name, 'w+').write(file_content)

# apply_template function will read in base template and
# replace {{content}} {{title}} and {{active_...} string 
# with code from each html page
def apply_template(content, page, active):
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    result = template.render({
        "title": page['title'],
        "content": content,
        "pages": pages,
        page['active']: "active",
    })
    return result

# build function will write the completed webpage 
# to the docs directory
def build(doc, page):
    finished_doc = open(page['output'], 'w+').write(doc)
    return finished_doc

# main function will read in content from pages list
# build pages with apply_template and write to docs directory with build
def main():
    page_list()
    for page in pages:
        content = open(page['filename']).read()
        active = page['active']
        print('Reading:', page['filename'])
        doc = apply_template(content, page, active)
        print('Compiling template...')
        finished_webpage = build(doc, page)
        print('Writing to docs:', page['output'])
    print('[Website built]')
print('[Building Site...]')
import glob
import os
from jinja2 import Template

all_html_files = glob.glob('content/*.html')
pages = []


def page_list():
    for item in all_html_files:
        file_path = os.path.basename(item)
        name_only, extension = os.path.splitext(file_path) 
        pages.append({
        "filename": item,
        "output": 'docs/' + file_path,
        "active": 'active_' + name_only,
        })


# index_html = open("content/index.html").read()
# template_html = open("templates/base.html").read()
# template = Template(template_html)
# result = template.render({
#     "title": "Homepage",
#     "content": index_html,
#     page['active']: "active",
# })
# print(result)

# pages = [
#     {
#         "filename": "content/index.html",
#         "output": "docs/index.html",
#         "title": "Zachary Lake",
#         "active": "active-index",
#     },
   
#     {
#         "filename": "content/blog.html",
#         "output": "docs/blog.html",
#         "title": "My Blog",
#         "active": "active-blog",
#     },

#     {
#         "filename": "content/projects.html",
#         "output": "docs/projects.html",
#         "title": "My Projects",
#         "active": "active-projects",
#     },
#     {
#         "filename": "content/contact.html",
#         "output": "docs/contact.html",
#         "title": "Contact Page",
#         "active": "active-contact",
#     },
# ]

# apply_template function will read in base template and
# replace content and title string with code from each html page
def apply_template(content, page, active):
    template_html = open("templates/base.html").read()
    template = Template(template_html)
    result = template.render({
        "title": "Homepage",
        "content": content,
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

# invoke main function to run build script       
if __name__ == "__main__":
    main()
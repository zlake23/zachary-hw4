print('[Building Site...]')
pages = [
    {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Zachary Lake",
        "active": "active-index",
    },
   
    {
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "My Blog",
        "active": "active-blog",
    },

    {
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "My Projects",
        "active": "active-projects",
    },
    {
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Page",
        "active": "active-contact",
    },
]

# apply_template function will read in base template and
# replace content and title string with code from each html page
def apply_template(content, title, active):
    template = open('./templates/base.html').read()
    template = template.replace("{{content}}", content)
    template = template.replace("{{title}}", title)
    template = template.replace("{{" + active + "}}", "active")
    return template

# build function will write the completed webpage 
# to the docs directory
def build(doc, page):
        finished_doc = open(page['output'], 'w+').write(doc)
        return finished_doc

# main function will read in content from pages list
# build pages with apply_template and write to docs directory with build
def main():
    for page in pages:
        content = open(page['filename']).read()
        title = page['title']
        active = page['active']
        print('Reading:', page['filename'])
        doc = apply_template(content, title, active)
        print('Compiling template...')
        finished_webpage = build(doc, page)
        print('Writing to docs:', page['output'])
    print('[Website built]')

# invoke main function to run build script       
if __name__ == "__main__":
    main()
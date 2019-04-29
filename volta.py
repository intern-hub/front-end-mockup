import random
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

c_list = ['g', 'n']
POSTS = []

for i in range(10):
  company = {}
  ind = random.randint(0, 1)
  company['logo'] = c_list[ind] + '-logo.png'
  company['desc'] = "Software Engineer"
  company['link'] = "APP LINK"
  POSTS.append(company)

# Render post in Jinja2
env = Environment(loader=FileSystemLoader('templates'))
index_template = env.get_template('index-template.html')
index_html_content = index_template.render(posts = POSTS)

# Write POSTS to index.html
with open('index.html', 'w') as file:
    file.write(index_html_content)
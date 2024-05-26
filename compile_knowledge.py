"""Generates a plain text file that can be used as the knowledge for the RNAcanvas AI assistant custom GPT."""


import requests


print()


# URLs to files to containing the information to include
reference_doc_urls = [
    'https://raw.githubusercontent.com/pzhaojohnson/rnacanvas.code/main/README.md',
    'https://raw.githubusercontent.com/pzhaojohnson/rnacanvas.draw.bases/main/README.md',
    'https://raw.githubusercontent.com/pzhaojohnson/rnacanvas.bases-layout/main/README.md',
]

separator = '\n\n\n' + ('#' * 80) + '\n\n\n'

compiled_knowledge_file_path = 'compiled_knowledge.txt'

with open(compiled_knowledge_file_path, 'w') as f:
    f.write(separator.join(map(lambda url : requests.get(url).text, reference_doc_urls)))

print(f'Wrote compiled knowledge to {compiled_knowledge_file_path}')
print()

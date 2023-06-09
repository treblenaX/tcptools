file_map = {
    'ping.md': 'Using \"ping\"',
    'tracert.md': 'Using \"tracert\"',
    'ngrok.md': 'Using \"ngrok\"',
    'wireshark.md': 'Using packet-capture tools',
    'spy.md': 'Spy on your opponents',
    'insecure.md': 'Insecure web server',
}

readme = ''

# read the stub
with open('stubs/README.stub', 'r') as f:
    readme = f.read()

for file, title in file_map.items():
    # read the file
    with open('markdown/' + file, 'r') as f:
        readme += '''<details>
                <summary>{}</summary>
                    {}</details>\n'''.format(title, f.read())

with open('README.md','w') as f:
    f.write(readme)
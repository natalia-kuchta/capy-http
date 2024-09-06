import utils
import glob
import os
import frontmatter


files = [os.path.basename(file) for file in glob.glob(utils.base_official_dir + "/*")]

for file_name in files:
    (basename, ext) = file.split('.')
    code = int(basename.replace('Capy','')

#     code = file.replace('.md', '')
#     ext = post['cover'].split('.')[-1]

    file_path = os.path.join(utils.base_content_dir, str(code) + '.md')
    with open(file_path, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    post['cover'] = f'https://firebasestorage.googleapis.com/v0/b/capy-http.appspot.com/o/Capy{code}.{ext}?alt=media'

    updated_content = frontmatter.dumps(post)

    with open(file_path, 'w', encoding='utf-8-sig') as g:
        g.write(updated_content)

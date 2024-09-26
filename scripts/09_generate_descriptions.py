from openai import OpenAI
client = OpenAI()

import utils
import glob
import os
import frontmatter
from termcolor import colored

files = [os.path.basename(file) for file in glob.glob(utils.base_content_dir + "/*")]

counter = 0

for file in files:
#     print(file)

    # Read the file and load frontmatter
    file_path = os.path.join(utils.base_content_dir, file)
    with open(file_path, encoding="utf-8-sig") as f:
        post = frontmatter.load(f)

    # Update cover URL
    code = file.replace('.md', '')
    title = post['title']

    # Check if cover needs updating
    if post.content != '__DESCRIPTION__':
        print(colored(f"SKIP {code}", "yellow"))
        continue

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""I creating website similar to http.cat but with capybaras. Create me Markdown description about code

    {code} {title}

    funny description and nomad style, print only content of this article without your comments or an introduction to answer."""
            }
        ]
    )

    post.content = completion.choices[0].message.content
    post.content = post.content.removeprefix('```markdown')
    post.content = post.content.removesuffix('```')

    # Safely dump the updated frontmatter
    updated_content = frontmatter.dumps(post)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8-sig') as g:
        g.write(updated_content)

    print(colored(f"DONE {code}", "green"))

   # counter += 1

    if counter > 4:
        break

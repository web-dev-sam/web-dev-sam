import os
import json

if __name__ == "__main__":
	articles = json.loads(os.environ["ARTICLES"])
	articles = sorted(articles, key=lambda x: x['public_reactions_count'], reverse=True)
	
	# Assuming each article has 'title', 'url', 'description', 'public_reactions_count', 'comments_count', and optionally 'cover_image'
	articles_html = '<table style="border-collapse: collapse; width: 100%;">\n'
	for i in range(0, min(4, len(articles)), 2):  # Loop through 4 articles, 2 at a time
		articles_html += '<tr style="border: none;">\n'
		for j in range(2):
			if i + j < len(articles):
				article = articles[i + j]
				title = article['title']
				url = article['url']
				description = article['description']
				likes = article['public_reactions_count']
				comments = article['comments_count']
				image = article.get('cover_image', '')  # Use cover_image if it exists, else use an empty string
				articles_html += f'''
<td align="center" width="50%" style="border: none; padding: 10px;">
	&nbsp;<br>
	<a href="{url}">
		<img src="{image}" alt="{title}" style="max-width:100%;">
	</a>
	<h3><a href="{url}">{title}</a></h3>
	<p>{description}</p>
	<p>👍 {likes} &nbsp; 💬 {comments}</p>
	&nbsp;<br>
</td>
	'''
		articles_html += '</tr>\n'
	articles_html += '</table>\n'

	readme = f"""
<h1 align="center">Welcome👋</h1>

<br>

<p align="center">
Hey, I'm a frontend focused web developer. Have a look around, you might find something useful or interesting 😁.
</p>

<br>

<p align="center">
  <a href="https://vuejs.org/"><img src="https://img.shields.io/badge/Vue-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D"></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white"></a>
  <a href="https://tailwindcss.com/"><img src="https://img.shields.io/badge/Tailwind-2682ab?style=for-the-badge&logo=tailwind-css&logoColor=white"></a>
</p>

<br>

<h2 align="center">Dev.To Articles</h2>
{articles_html}

<br>

<h2 align="center">Language Stats</h2>

<p align="center">
  <a href="https://webry.com/"><img src="https://github-readme-stats.vercel.app/api/top-langs/?username=web-dev-sam&hide=htm&theme=one_dark_pro" /></a>
</p>
"""
	
	# Write the generated README to a file (or further processing)
	with open('README.md', 'w') as f:
		f.write(readme)

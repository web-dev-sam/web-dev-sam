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
<br>
Hey, I'm a frontend focused web developer. Have a look around, you might find something useful or interesting 😁.

<br>&nbsp;

The stack of dreams:

<img src="https://img.shields.io/badge/Vue-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D">
<img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/Tailwind-2682ab?style=for-the-badge&logo=tailwind-css&logoColor=white">

<br>&nbsp;

<a href="https://www.webry.com/"><img src="https://img.shields.io/badge/Webry.com-1E1E1E?style=for-the-badge&logo=blog&logoColor=white"></a>
<a href="https://dev.to/samuel-braun"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white"></a>
<a href="https://www.linkedin.com/in/samuel-braun/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://bitbucket.org/samuel-braun/"><img src="https://img.shields.io/badge/Bitbucket-0747a6?style=for-the-badge&logo=bitbucket&logoColor=white"></a>

&nbsp;<br>&nbsp;

<h2>Dev.To Articles</h2>
{articles_html}

&nbsp;<br>&nbsp;


<h2>Language Stats</h2>

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=web-dev-sam&hide=htm&theme=one_dark_pro)](https://github.com/web-dev-sam)
"""
	
	# Write the generated README to a file (or further processing)
	with open('README.md', 'w') as f:
		f.write(readme)

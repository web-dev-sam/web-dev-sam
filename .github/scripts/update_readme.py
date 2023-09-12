import os
import json

if __name__ == "__main__":
	articles = json.loads(os.environ["ARTICLES"])
	
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
	<a href="{url}">
		<img src="{image}" alt="{title}" style="max-width:100%;">
	</a>
	<h3><a href="{url}">{title}</a></h3>
	<p>{description}</p>
	<p>👍 {likes} &nbsp; 💬 {comments}</p>
</td>
	'''
		articles_html += '</tr>\n'
	articles_html += '</table>\n'

	readme = f"""
<div align="center">
<br>

Have a look around, you might find something useful or interesting 😁.

<a href="https://dev.to/samuel-braun"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white"></a>
<a href="https://www.webry.com/"><img src="https://img.shields.io/badge/Webry.com-1E1E1E?style=for-the-badge&logo=blog&logoColor=white"></a>
<a href="https://www.linkedin.com/in/samuel-braun/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
<a href="https://bitbucket.org/samuel-braun/"><img src="https://img.shields.io/badge/Bitbucket-0747a6?style=for-the-badge&logo=bitbucket&logoColor=white"></a>
<a href="https://gitlab.com/braunsa/"><img src="https://img.shields.io/badge/GitLab-eb452a?style=for-the-badge&logo=gitlab&logoColor=white"></a>
<a href="https://ko-fi.com/samuelbraun"><img src="https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=white"></a>
<a href="https://open.spotify.com/user/office.samigo.a"><img src="https://img.shields.io/badge/Spotify-16a349?&style=for-the-badge&logo=spotify&logoColor=white"></a>

<br>&nbsp;

I'm a frontend focused web developer. Here are the technologies I use the most.

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
<img src="https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white">
<img src="https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D">
<img src="https://img.shields.io/badge/Tailwind-2682ab?style=for-the-badge&logo=tailwind-css&logoColor=white">

<br>&nbsp;

Tools I use most often.

<img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white">
<img src="https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white">
<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white">

&nbsp;<br>&nbsp;

<h2>Dev.To Articles</h2>

<h2>Dev.To Articles</h2>
{articles_html}

&nbsp;<br>&nbsp;
"""
	
	# Write the generated README to a file (or further processing)
	with open('README.md', 'w') as f:
		f.write(readme)

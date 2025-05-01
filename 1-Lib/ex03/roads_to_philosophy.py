from bs4 import BeautifulSoup
import requests
import sys

visited = []

def roads_to_philosophy(title):
	url = "https://en.wikipedia.org/wiki/" + title

	try:
		response = requests.get(url)
		response.raise_for_status()
	except:
		return print("It leads to a dead end!")

	soup = BeautifulSoup(response.text, 'html.parser')
	title = soup.find(id='firstHeading').text

	if title in visited:
		return print("It leads to an infinite loop!")

	visited.append(title)
	print(title)

	if title == 'Philosophy':
		return print(f"{len(visited)} roads from {visited[0]} to philosophy")

	content = soup.find(id='mw-content-text')
	if not content:
		return print("It leads to a dead end!")

	links = content.select('p > a')

	for link in links:
		href = link.get('href', '')
		if href.startswith('/wiki/') and not (href.startswith('/wiki/Wikipedia:') or href.startswith('/wiki/Help:')):
			parent = link.parent
			if parent.name == 'i' or parent.name == 'em':
				continue

			link_text = str(parent)
			pos = link_text.find(str(link))
			if pos != -1:
				open_count = link_text[:pos].count('(')
				close_count = link_text[:pos].count(')')
				if open_count > close_count:
					continue

			return roads_to_philosophy(href[6:])

	return print("It leads to a dead end!")

def main():
	if len(sys.argv) == 2:
		try:
			title = sys.argv[1].replace(' ', '_')
			roads_to_philosophy(title)
		except Exception as e:
			print(f"An error occurred: {e}")
	else:
		print("Usage: python3 roads_to_philosophy.py <page>")

if __name__ == '__main__':
	main()
import webbrowser

search_term = input('Enter to search: ').replace(" ", '+')

webbrowser.open(f'https://google.com/search?q={search_term}')
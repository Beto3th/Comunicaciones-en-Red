import webbrowser

url1 = 'https://www.marcombo.com/'
url2 = 'https://www.amazon.es/'
url3 = 'https://www.google.com/'

# Abrir el url en una nueva pestaña si ya existe una ventana del navegador abierto
webbrowser.open_new_tab(url1)

# Abrir la URL en una nueva ventana, si es posible
webbrowser.open_new(url2)

edge_path = "/usr/bin/microsoft-edge-stable %U"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open_new(url3)




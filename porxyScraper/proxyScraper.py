import os
import requests
from bs4 import BeautifulSoup
import re
from typing import List

# Lista de URLs de prixies
URLS = [
    "https://www.sslproxies.org/",
    "https://free-proxy-list.net/",
    "https://www.us-proxy.org/"
]

def obtener_proxies_de_url(url: str) -> List[str]:
    proxies = []
    try:
        response = requests.get(url)
        response.raise_for_status()  # Si la peticion no es 200 lanzara una excepcion

        # Usar BeautifulSoup para parsear el contenido HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Para cada sitio habría que ver la estructura que tiene cada tabla, habría que adaptar el codigo a cada sitio
        if 'sslproxies.org' in url:
            # En el caso de sslproxies.org
            table = soup.find('table', {'id': 'proxylisttable'})
            if table:
                rows = table.find_all('tr')[1:]  # Saltamos la primera fila que contiene los encabezados
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) > 0:
                        ip = columns[0].text.strip()
                        port = columns[1].text.strip()
                        if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip) and port.isdigit():
                            proxies.append(f"{ip}:{port}")

        elif 'free-proxy-list.net' in url:
            # En el caso de free-proxy-list.net
            table = soup.find('table', {'id': 'proxylisttable'})
            if table:
                rows = table.find_all('tr')[1:]  # Cabecera
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) > 0:
                        ip = columns[0].text.strip()
                        port = columns[1].text.strip()
                        if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip) and port.isdigit():
                            proxies.append(f"{ip}:{port}")

        elif 'us-proxy.org' in url:
            # En el caso de us-proxy.org
            table = soup.find('table', {'class': 'table table-striped table-bordered'})
            if table:
                rows = table.find_all('tr')[1:]  # Cabecera
                for row in rows:
                    columns = row.find_all('td')
                    if len(columns) > 0:
                        ip = columns[0].text.strip()
                        port = columns[1].text.strip()
                        if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip) and port.isdigit():
                            proxies.append(f"{ip}:{port}")
    except requests.RequestException as e:
        print(f"Error al obtener proxies de {url}: {e}")

    return proxies

def obtener_proxies_de_varias_urls(urls: List[str]) -> List[str]:

    #Obtiene proxies de varias URLs y las combina en una sola lista.

    all_proxies = []
    for url in urls:
        print(f"Obteniendo proxies de: {url}")
        proxies = obtener_proxies_de_url(url)
        all_proxies.extend(proxies)
    return all_proxies

def mostrar_proxies(proxies: List[str]):
    if proxies:
        with open("proxies.txt", "w") as file:
            for proxy in proxies:
                file.write(proxy + "\n")
        print("Proxies guardados en proxies.txt")
    else:
        print("No se encontraron proxies.")

if __name__ == "__main__":
    proxies = obtener_proxies_de_varias_urls(URLS)
    mostrar_proxies(proxies)
import time
import requests 
from config.settings import SCRAPING_DELAY, TIMEOUT, MAX_RETRIES

class JobScraper:
    def __init__(self):
        self.jobs_founds = []
        self.total_requests = 0
         
    def _make_request(self, url):
        self.total_requests += 1
        for attempt in range(MAX_RETRIES):
            try:
                print(f"Intento {attempt + 1} para {url}")
                response = requests.get(url, timeout=TIMEOUT)
                if response.status_code == 200:
                    print("Request exitoso")
                    return response
                else:
                    print(f"Error: {response.status_code}")
            except requests.Timeout:
                print("⏰ Timeout - la página tardó mucho")
            except requests.RequestException as e:
                print(f"🚫 Error de conexión: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(SCRAPING_DELAY)
        return None
    
    def scrape_all_sites(self):  # Metodo para scrapear los sitios
        print("Iniciando Scraping de ofertas de empleo")
        test_sites = [
            "https://httpbin.org/delay/1",
            "https://httpbin.org/status/200"
        ]
        for site_url in test_sites:
            print(f"Scrapeando: {site_url}")
            response = self._make_request(site_url)
            if response:
                fake_jobs = [f"Trabajo desde {site_url}", f"Otro trabajo desde {site_url}"]
                self.jobs_founds.extend(fake_jobs)
                print(f"Encontrados {len(fake_jobs)} trabajos")
            else:
                print("No se encontraron trabajos")
        print(f"Scraping completado. Total de trabajos: {len(self.jobs_founds)}")
        return self.jobs_founds
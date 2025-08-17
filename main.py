from src.scraper.job_scraper import JobScraper
from config.settings import SCRAPING_DELAY, TIMEOUT #Search on the config folder for the settings file and brings it all
#I may use import ... as ... To import with an alias
#I may use from ... import ... to import a single variable

def main():
    print("=== SCRAPER DE OFERTAS DE EMPLEO ===")
    print(f"Configuración: Delay={SCRAPING_DELAY}s, Timeout={TIMEOUT}s")
    scraper = JobScraper()
    jobs = scraper.scrape_all_sites()
    print(f"Total de requests: {scraper.total_requests}")
    print(f"Trabajos encontrados: {len(jobs)}")
    print("Lista de trabajos")
    for i, job in enumerate(jobs, 1):
        print(f" {i}. {job}")

if __name__ == "__main__":
    main() 

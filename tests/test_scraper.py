import unittest
from src.scraper.job_scraper import JobScraper

class TestJobScraper(unittest.TestCase):
    
    def setUp(self):
        """Se ejecuta antes de cada test"""
        self.scraper = JobScraper()
    
    def test_scraper_initialization(self):
        """Probar que el scraper se inicializa correctamente"""
        self.assertEqual(len(self.scraper.jobs_founds), 0)  # ← CORREGIDO
        self.assertEqual(self.scraper.total_requests, 0)
    
    def test_scrape_returns_list(self):
        """Probar que scrape_all_sites devuelve una lista"""
        jobs = self.scraper.scrape_all_sites()
        self.assertIsInstance(jobs, list)
        self.assertGreater(len(jobs), 0, "Debería encontrar al menos algunos trabajos")
    
    def test_requests_counter(self):
        """Probar que se cuenta correctamente el número de requests"""
        initial_count = self.scraper.total_requests
        self.scraper.scrape_all_sites()
        self.assertGreater(self.scraper.total_requests, initial_count)

if __name__ == '__main__':
    unittest.main()

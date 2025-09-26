"""
Web Scraper Project
==================

A web scraping application demonstrating HTTP requests, HTML parsing,
data extraction, and file operations.
"""

import requests
import json
import csv
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse
import os

class WebScraper:
    """A simple web scraper with rate limiting and data export."""
    
    def __init__(self, delay=1, timeout=10):
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.scraped_data = []
    
    def fetch_page(self, url):
        """Fetch a web page with error handling."""
        try:
            print(f"Fetching: {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # Rate limiting
            time.sleep(self.delay)
            
            return response.text
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_quotes(self, html_content):
        """Extract quotes from HTML (simulated parsing)."""
        # In a real scraper, you'd use BeautifulSoup or similar
        # This is a simplified simulation
        
        quotes = []
        
        # Simulate finding quotes in HTML
        sample_quotes = [
            {
                "text": "The way to get started is to quit talking and begin doing.",
                "author": "Walt Disney",
                "tags": ["inspirational", "wisdom"]
            },
            {
                "text": "Life is what happens to you while you're busy making other plans.",
                "author": "John Lennon", 
                "tags": ["life", "planning"]
            },
            {
                "text": "The future belongs to those who believe in the beauty of their dreams.",
                "author": "Eleanor Roosevelt",
                "tags": ["future", "dreams"]
            }
        ]
        
        # Simulate extracting quotes based on content
        for quote in sample_quotes:
            if quote["author"].lower() in html_content.lower():
                quotes.append(quote)
        
        return quotes
    
    def scrape_quotes_site(self, base_url="http://quotes.toscrape.com"):
        """Scrape quotes from a quotes website (simulated)."""
        print("Starting quote scraping...")
        
        # Simulate multiple pages
        for page in range(1, 4):  # Pages 1-3
            url = f"{base_url}/page/{page}/"
            
            # Simulate HTML content for different pages
            simulated_content = f"""
            <html>
                <body>
                    <div class="quote">
                        <span class="text">Page {page} content with Walt Disney</span>
                        <small class="author">by Walt Disney</small>
                    </div>
                    <div class="quote">
                        <span class="text">Page {page} content with John Lennon</span>
                        <small class="author">by John Lennon</small>
                    </div>
                </body>
            </html>
            """
            
            # In real scraping, you'd use: html_content = self.fetch_page(url)
            html_content = simulated_content
            
            if html_content:
                quotes = self.extract_quotes(html_content)
                
                for quote in quotes:
                    quote['page'] = page
                    quote['scraped_at'] = datetime.now().isoformat()
                    self.scraped_data.append(quote)
                
                print(f"Extracted {len(quotes)} quotes from page {page}")
            
            # Simulate delay between requests
            time.sleep(self.delay)
        
        print(f"Scraping completed. Total quotes: {len(self.scraped_data)}")
    
    def scrape_news_headlines(self):
        """Scrape news headlines (simulated)."""
        print("Scraping news headlines...")
        
        # Simulate news data
        news_data = [
            {
                "headline": "Technology Advances in 2024",
                "summary": "Major breakthroughs in AI and quantum computing",
                "category": "Technology",
                "published": "2024-01-15"
            },
            {
                "headline": "Climate Change Summit Results",
                "summary": "World leaders agree on new environmental policies",
                "category": "Environment", 
                "published": "2024-01-14"
            },
            {
                "headline": "Economic Markets Update",
                "summary": "Stock markets show positive trends",
                "category": "Finance",
                "published": "2024-01-13"
            }
        ]
        
        for article in news_data:
            article['scraped_at'] = datetime.now().isoformat()
            self.scraped_data.append(article)
        
        print(f"Scraped {len(news_data)} news articles")
    
    def export_to_json(self, filename="scraped_data.json"):
        """Export scraped data to JSON file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.scraped_data, f, indent=2, ensure_ascii=False)
            
            print(f"Data exported to {filename}")
            return True
        
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def export_to_csv(self, filename="scraped_data.csv"):
        """Export scraped data to CSV file."""
        if not self.scraped_data:
            print("No data to export")
            return False
        
        try:
            # Get all unique keys from all records
            all_keys = set()
            for item in self.scraped_data:
                all_keys.update(item.keys())
            
            fieldnames = sorted(all_keys)
            
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for item in self.scraped_data:
                    # Handle list fields (like tags)
                    row = {}
                    for key, value in item.items():
                        if isinstance(value, list):
                            row[key] = ', '.join(map(str, value))
                        else:
                            row[key] = value
                    writer.writerow(row)
            
            print(f"Data exported to {filename}")
            return True
        
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def get_statistics(self):
        """Get statistics about scraped data."""
        if not self.scraped_data:
            return "No data available"
        
        stats = {
            "total_items": len(self.scraped_data),
            "data_types": {},
            "sample_keys": set()
        }
        
        # Analyze data structure
        for item in self.scraped_data:
            for key, value in item.items():
                stats["sample_keys"].add(key)
                
                value_type = type(value).__name__
                if value_type not in stats["data_types"]:
                    stats["data_types"][value_type] = 0
                stats["data_types"][value_type] += 1
        
        stats["sample_keys"] = sorted(stats["sample_keys"])
        
        return stats
    
    def clear_data(self):
        """Clear all scraped data."""
        self.scraped_data.clear()
        print("Scraped data cleared")

class DataAnalyzer:
    """Analyze scraped data."""
    
    @staticmethod
    def analyze_quotes(data):
        """Analyze quote data."""
        quotes = [item for item in data if 'author' in item]
        
        if not quotes:
            return "No quote data found"
        
        # Count by author
        author_counts = {}
        tag_counts = {}
        
        for quote in quotes:
            author = quote.get('author', 'Unknown')
            author_counts[author] = author_counts.get(author, 0) + 1
            
            # Count tags
            tags = quote.get('tags', [])
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        analysis = {
            "total_quotes": len(quotes),
            "unique_authors": len(author_counts),
            "top_authors": sorted(author_counts.items(), key=lambda x: x[1], reverse=True)[:5],
            "top_tags": sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)[:5]
        }
        
        return analysis
    
    @staticmethod
    def analyze_news(data):
        """Analyze news data."""
        news = [item for item in data if 'headline' in item]
        
        if not news:
            return "No news data found"
        
        # Count by category
        category_counts = {}
        
        for article in news:
            category = article.get('category', 'Uncategorized')
            category_counts[category] = category_counts.get(category, 0) + 1
        
        analysis = {
            "total_articles": len(news),
            "categories": category_counts,
            "recent_headlines": [article['headline'] for article in news[:5]]
        }
        
        return analysis

def display_menu():
    """Display the scraper menu."""
    print("\n" + "=" * 50)
    print("           WEB SCRAPER MENU")
    print("=" * 50)
    print("1. Scrape Quotes")
    print("2. Scrape News Headlines")
    print("3. View Scraped Data")
    print("4. Export to JSON")
    print("5. Export to CSV")
    print("6. Analyze Data")
    print("7. Clear Data")
    print("8. Statistics")
    print("0. Exit")
    print("=" * 50)

def display_data(data, limit=10):
    """Display scraped data with pagination."""
    if not data:
        print("No data to display")
        return
    
    print(f"\nDisplaying first {min(limit, len(data))} items:")
    print("-" * 60)
    
    for i, item in enumerate(data[:limit]):
        print(f"\nItem {i+1}:")
        for key, value in item.items():
            if isinstance(value, list):
                print(f"  {key}: {', '.join(map(str, value))}")
            else:
                print(f"  {key}: {value}")
    
    if len(data) > limit:
        print(f"\n... and {len(data) - limit} more items")

def main():
    """Main scraper application."""
    scraper = WebScraper(delay=0.5)  # 0.5 second delay between requests
    analyzer = DataAnalyzer()
    
    print("Welcome to the Web Scraper!")
    print("This is a demonstration scraper with simulated data.")
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-8): ").strip()
            
            if choice == "0":
                print("Thank you for using Web Scraper!")
                break
            
            elif choice == "1":
                scraper.scrape_quotes_site()
            
            elif choice == "2":
                scraper.scrape_news_headlines()
            
            elif choice == "3":
                display_data(scraper.scraped_data)
            
            elif choice == "4":
                filename = input("Enter JSON filename (or press Enter for default): ").strip()
                if not filename:
                    filename = "scraped_data.json"
                scraper.export_to_json(filename)
            
            elif choice == "5":
                filename = input("Enter CSV filename (or press Enter for default): ").strip()
                if not filename:
                    filename = "scraped_data.csv"
                scraper.export_to_csv(filename)
            
            elif choice == "6":
                if not scraper.scraped_data:
                    print("No data to analyze. Please scrape some data first.")
                    continue
                
                print("\nData Analysis:")
                print("-" * 30)
                
                quote_analysis = analyzer.analyze_quotes(scraper.scraped_data)
                if isinstance(quote_analysis, dict):
                    print("Quote Analysis:")
                    for key, value in quote_analysis.items():
                        print(f"  {key}: {value}")
                
                news_analysis = analyzer.analyze_news(scraper.scraped_data)
                if isinstance(news_analysis, dict):
                    print("\nNews Analysis:")
                    for key, value in news_analysis.items():
                        print(f"  {key}: {value}")
            
            elif choice == "7":
                confirm = input("Are you sure you want to clear all data? (y/N): ")
                if confirm.lower() == 'y':
                    scraper.clear_data()
                else:
                    print("Clear operation cancelled")
            
            elif choice == "8":
                stats = scraper.get_statistics()
                print("\nScraping Statistics:")
                print("-" * 30)
                if isinstance(stats, dict):
                    for key, value in stats.items():
                        print(f"{key}: {value}")
                else:
                    print(stats)
            
            else:
                print("Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n\nScraper interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
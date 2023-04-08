import argparse
from utils import fetch_pages, get_reviews_dataframe

def run():
    parser = argparse.ArgumentParser(
        prog='TrustPilot Scraper',
        description='A script to scrape reviews from TrustPilot'
    )

    parser.add_argument('-d', '--domain', type=str,
                        help='The domain for which you wish to obtain the reviews. Example: www.example.com')
    parser.add_argument('-p', '--pages', type=int,
                        help='The number of pages to be scraped')
    parser.add_argument('-o', '--output', type=str, choices=['csv', 'xlsx'],
                        help='The extension of the result file to be generated')
    
    args = parser.parse_args()

    domain, pages, output = args.domain, args.pages, args.output

    if domain and pages:
        print(f'\n[+] Obtaining data for {domain}')
        responses = fetch_pages(domain, pages, 1)
        reviews_df = get_reviews_dataframe(responses)
        
        if output == 'csv':
            reviews_df.to_csv(f'{domain}.csv', encoding='utf-8', index=False)
        else:
            reviews_df.to_excel(f'{domain}.xlsx', sheet_name='reviews', index=False)
        
        print(f'\n[+] File created: {domain}.{output}')


if __name__ == '__main__':
    run()
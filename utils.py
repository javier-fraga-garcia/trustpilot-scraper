import pandas as pd
import requests
import time
import sys
from tqdm.auto import tqdm
from bs4 import BeautifulSoup

def fetch_pages(domain: str, n_pages: int, delay: int = 3):
    """Performs requests to the pages
    
    Args:
        domain: The domain you wish to obtain reviews from
        n_pages: The number of pages to request
        delay: Delay between requests. Default 3 seconds
    
    Returns:
        A list of responses objects
    """
    try:
        responses = []
        for page in tqdm(range(1, n_pages+1), desc='Fetching pages: '):
            res = requests.get(f'https://es.trustpilot.com/review/{domain}?page={page}')
            if res.status_code == 200:
                responses.append(res)
            time.sleep(delay)
        return responses
    except:
        sys.exit('[!] Something went wrong')


def get_reviews_from_response(response: requests.Response):
    """Gets the review data of a page
    
    Args:
        response: Response object of requests with the data of the request to the page.

    Returns:
        A tuple with the data of the page
    """
    try:
        html = BeautifulSoup(response.text, 'html.parser')
        reviews = html.select('section.styles_reviewContentwrapper__zH_9M')
        scores = [int(review.select('div.styles_reviewHeader__iU9Px')[0]['data-service-review-rating']) if review.select('div.styles_reviewHeader__iU9Px')[0]['data-service-review-rating'] else 0 for review in reviews]
        dates = [review.select('time')[0]['datetime'] if review.select('time')[0]['datetime'] else 'no date' for review in reviews]
        titles = [review.select('h2')[0].getText().lower().strip() if review.select('h2') else 'no title' for review in reviews]
        texts = [review.select('.typography_body-l__KUYFJ.typography_appearance-default__AAY17.typography_color-black__5LYEn')[0].get_text().lower().strip() if review.select('.typography_body-l__KUYFJ.typography_appearance-default__AAY17.typography_color-black__5LYEn') else 'no review' for review in reviews]
        assert len(scores) == len(dates) == len(titles) == len(texts)
        return (scores, dates, titles, texts)

    except AssertionError:
        print(f'[!] Data are not the same length')
        return (None, None, None, None)
    except:
        sys.exit('[!] Something went wrong')


def get_reviews_dataframe(responses: list[requests.Response]):
    """Generate a dataframe with the reviews

    Args:
        responses: A list with the responses of the requested pages
    
    Returns:
        A dataframe with the reviews scraped from TrustPilot
    """
    reviews = {
        'scores': [],
        'dates': [],
        'titles': [],
        'texts': []
    }
    for response in tqdm(responses, desc='Getting data: '):
        scores, dates, titles, texts = get_reviews_from_response(response)
        if scores:
            reviews['scores'] += scores
            reviews['dates'] += dates
            reviews['titles'] += titles
            reviews['texts'] += texts
        
    return pd.DataFrame(reviews)

import requests
import sys

URL = 'https://api.semanticscholar.org/v1/author/'
URL_PAPER = 'https://api.semanticscholar.org/v1/paper/'


def gather_citations(author_id):
    resp = requests.get(URL + author_id)
    if resp.status_code != 200:
        raise ValueError('GET v1 author {}'.format(resp.status_code))

    author_data = resp.json()

    author_name = author_data['name']
    print('Citantions of all papers by', author_name)

    for paper in author_data['papers']:

        paper_id = paper['paperId']
        paper_title = paper['title']
        paper_year = paper['year']

        resp = requests.get(URL_PAPER + paper_id)
        if resp.status_code != 200:
            raise ValueError('GET v1 paper {}'.format(resp.status_code))

        paper_data = resp.json()
        paper_authors = paper_data['authors']
        paper_venue = paper_data['venue']
        paper_citations = paper_data['citations']

        print()
        print(
            'Paper "{}"'.format(paper_title),
            'published in', paper_venue,
            'in', paper_year,
            'has been citedy', len(paper_citations),
            'times:'
        )

        for citation in paper_citations:
            # print(citation.keys())
            citation_title = citation['title']
            citation_venue = citation['venue']
            citation_year = citation['year']
            citation_authors = [a['name'] for a in citation['authors']]
            citation_authors_str = ', '.join(citation_authors)

            print('- {}. {}, {} {}'.format(
                citation_authors_str if citation_authors_str else 'V.A.',
                citation_title,
                citation_venue if citation_venue else 'ArXiv',
                citation_year
            ))


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        author_id = sys.argv[1]
        gather_citations(author_id)
    else:
        print("Usage: python gather-citations.py <AUTHOR_SEMANTIC_SCHOLAR_ID>")
        sys.exit(-1)

# gather-citations-S2
Script to gather all the citations of all the papers of an author on [Semantic Scholar](https://www.semanticscholar.org).
It uses the [Semantic Scholar API](https://api.semanticscholar.org).

## Install

In order to use the script just install the `requests` package using `pip`:

```
pip install requests
```

## Usage

First figure out the ID of the author you want to gather the citations of.
You can obtain the ID from the URL of the author, for instance the ID of `https://www.semanticscholar.org/author/Piero-Molino/34890911` is the string after the last `/`, `34890911`.

In order to gather the citations of this author, just run:

```
python gather-citations-S2.py 34890911
```

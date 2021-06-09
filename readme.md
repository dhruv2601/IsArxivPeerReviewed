# Is the Arxiv paper Peer-reviewed?

## What is it?
The problem I was facing was to find which among my dataset of 1.7 Million research papers on Arxiv are peer-reviewed papers? i.e. are the papers publised in any peer-reviewed conference or journal or only hosted on Arxiv. The purpose to find this was essentially to maintain quality of my dataset.

This tool takes in the arxiv article id and outputs the Conference/Journal the paper is published in with the link as well, or if it's only arxiv published.

## How it works?
The tool semanticscholar.org contains the most frequently indexed and reliable database of papers and the good thing about their indexing algorithm is that their relevance scored results shows the paper on the conference/journal website higher in relevance, even if the paper is there on Arxiv.
Thus, the task is divided as follows - 
* Fetch the title from Arxiv website.
* Form Semantic scholar query with the title.
* Crawl semantic scholar to find the relevant result.
* Filter the relevant elements to do the magic.

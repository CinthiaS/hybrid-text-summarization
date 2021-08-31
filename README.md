# Study of training approaches of a hybrid summarization model using the metrics ROUGE and NUBIA


## Dataset Creation

Libraries:

os              -- sudo pip install os
requests        -- sudo pip install requests
re              -- sudo pip install re
BeautifulSoup   -- sudo pip install beautifulsoup4


### To create the databaseset, is used the code provided in:

hybrid-text-summarization/src/create_database_train_valid

This code was implemented to automatically download patents from the USPTO database.

The code was divided into five steps:

1. Extracting codes from subgroups of a given class (searchSubgroups.py)
2. Extraction of patent links from the USPTO page; (LinksExtract.py)
3. Download the content of the links; (LinksDownload.py)

** At the end of this step, there are files organized in two folders "summary/" "title/" each of the folders
have subfolders with the name of the document class, where in these folders they have the document summary of
patent (in "abstract/") in .txt format and the title of the document (in "title/") in .txt format.

4. Database blend (blend_database.py)
5. Removal of repeated files between documents in subgroups 43 47 52 and 56, removal of files with duplicate content and pre-processing of documents (organize_base.py)

Command to list duplicate files on linux
find . -type f -exec md5sum '{}' ';' | sort | uniq --all-repeated=separate -w 20 > ../duplicate_files.txt


In the folder, hybrid-text-summarization/src/create_database_train_valid/IDs/, you will find the IDs of all groups in which documents were collected.

## Hybrid text summarization:

hybrid-text-summarization/notebooks/hybrid_text_summarization.ipynb

## Baselines

The performance of different State-of-the-art algorithms in task of text summarization was evaluated.

### Extractive Methods

- Sumbasic: 
    Paper: [https://doi.org/10.1016/j.ipm.2007.01.023](https://doi.org/10.1016/j.ipm.2007.01.023)

    Python Library: [https://pypi.org/project/sumy/](https://pypi.org/project/sumy/)

- TextRank:  
    
    Paper: [https://aclanthology.org/W04-3252.pdf](https://aclanthology.org/W04-3252.pdf)
    
    Python Library: [https://pypi.org/project/sumy/](https://pypi.org/project/sumy/)
    
- BERT Extractive Summarizer: https://arxiv.org/abs/1906.04165

    Paper: [https://arxiv.org/abs/1908.08345](https://arxiv.org/abs/1908.08345)

    Github: [https://github.com/nlpyang/PreSumm](https://github.com/nlpyang/PreSumm)

    Our adaptation [https://github.com/CinthiaS/hybrid-text-summarization/blob/main/notebooks/BertSumm.ipynb](https://github.com/CinthiaS/hybrid-text-summarization/blob/main/notebooks/BertSumm.ipynb)
    
- BERTSum: 

    Paper: [https://arxiv.org/abs/1908.08345](https://arxiv.org/abs/1908.08345)

    Github: [https://github.com/nlpyang/PreSumm](https://github.com/nlpyang/PreSumm)

    Our adaptation: [https://github.com/CinthiaS/hybrid-text-summarization/blob/main/notebooks/BertSumm.ipynb](https://github.com/CinthiaS/hybrid-text-summarization/blob/main/notebooks/BertSumm.ipynb)
  
- BigBird-Pegasus: 

    Paper: [https://proceedings.neurips.cc//paper/2020/file/c8512d142a2d849725f31a9a7a361ab9-Paper.pdf](https://proceedings.neurips.cc//paper/2020/file/c8512d142a2d849725f31a9a7a361ab9-Paper.pdf)

    Github: [https://github.com/google-research/bigbird](https://github.com/google-research/bigbird)

- Pegasus:

Paper: [https://arxiv.org/pdf/1912.08777.pdf](https://arxiv.org/pdf/1912.08777.pdf)

Github: [https://github.com/google-research/pegasus](https://github.com/google-research/pegasus)


- R-Drop:

  Github: [https://github.com/dropreg/R-Drop](https://github.com/dropreg/R-Drop)

  Paper: [https://arxiv.org/pdf/2106.14448.pdf](https://arxiv.org/pdf/2106.14448.pdf)

### Abstractive Methods

- Seq2Seq LSTM: 

Paper: [https://link.springer.com/article/10.1007/s11192-020-03732-x](https://link.springer.com/article/10.1007/s11192-020-03732-x)

## Validation

To validate the results obtained, the ROUGE set of metrics and the NUBIA metric were used.

- ROUGEs

  Paper: [http://research.nii.ac.jp/ntcir/ntcir-ws4/NTCIR4-WN/OPEN/OPENSUB_Chin-Yew_Lin.pdf](http://research.nii.ac.jp/ntcir/ntcir-ws4/NTCIR4-WN/OPEN/OPENSUB_Chin-Yew_Lin.pdf)

- NUBIA

  Paper: [https://arxiv.org/pdf/2004.14667.pdf](https://arxiv.org/pdf/2004.14667.pdf)

  Github: [https://github.com/wl-research/nubia](https://github.com/wl-research/nubia)


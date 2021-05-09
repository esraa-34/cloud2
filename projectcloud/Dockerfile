#base image
FROM python:3
COPY . /projectcloud
WORKDIR /projectcloud
RUN pip install nltk
RUN pip install stopwords
CMD python pyfile.py
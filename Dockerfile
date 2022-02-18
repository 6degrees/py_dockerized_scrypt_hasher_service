FROM python:3

ADD main.py /
ADD requirements.txt /
ADD firebasescrypt /firebasescrypt

RUN pip install --upgrade pip
RUN pip install flask python-dotenv
RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

EXPOSE 5959:5959
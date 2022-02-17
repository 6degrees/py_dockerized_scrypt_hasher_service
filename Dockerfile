FROM python:3.8

ADD main.py /

RUN pip install --upgrade pip
RUN pip install flask dotenv
RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]

EXPOSE 5959:5000
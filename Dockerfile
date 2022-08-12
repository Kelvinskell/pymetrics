FROM python

WORKDIR /pymetrics

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV OPTION=''

CMD ["sh", "-c", "python main.py ${OPTION}"]

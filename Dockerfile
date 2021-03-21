FROM python:3.8-slim-buster

WORKDIR /app

COPY web/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY web/ .

ARG GITHUB_SHA
ARG GITHUB_REF
ENV SHA=$GITHUB_SHA
ENV REF=$GITHUB_REF

RUN sed -i 's,SHA,'"$GITHUB_SHA"',' app.py
RUN sed -i 's,REF,'"$GITHUB_REF"',' app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]

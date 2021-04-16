FROM python:3.7
WORKDIR /code
# ENV FLASK_APP=manage.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
RUN apt update && apt install -y \ 
 gcc \
 make \
 libffi-dev \
 libc-dev \
 musl-dev 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# COPY setup.py setup.py
# RUN python install setup.py
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
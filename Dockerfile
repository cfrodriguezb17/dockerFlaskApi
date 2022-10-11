FROM python:3.10.6

WORKDIR /app
COPY . . 

RUN pip3 install flask pyrebase firebase-admin pycryptodome pyjwt
RUN pip3 freeze > requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
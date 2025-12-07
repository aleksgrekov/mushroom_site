FROM python:3.12-slim

ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "run.py", "runserver", "0.0.0.0:8000"]

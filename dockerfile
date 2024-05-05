FROM python:3.11

RUN mkdir /project_dir

WORKDIR /project_dir

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker_instructions/*.sh

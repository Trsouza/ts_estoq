FROM python:3.6

MAINTAINER Tathiane Souza

RUN apt update && \
    apt install -y netcat-openbsd

# define a variável env para dizer onde o aplicativo será instalado dentro do docker
ENV INSTALL_PATH /Docker-Flask
RUN mkdir -p $INSTALL_PATH

# define o contexto de onde os comandos serão executados e documentados
WORKDIR $INSTALL_PATH

# Copia do diretório atual para o diretório de trabalho
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /Docker-Flask/docker-entrypoint.sh

CMD ["/bin/bash", "/Docker-Flask/docker-entrypoint.sh"]

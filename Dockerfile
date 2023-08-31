FROM python:3.8

EXPOSE 8501 
EXPOSE 3000

ENV WORKSPACE="/var/lib/app"
ENV PYTHONPATH=$WORKSPACE
ENV CACHE_PATH=$WORKSPACE-cache
# To avoid integrity errors fails
ENV BUN_CONFIG_NO_VERIFY=1

VOLUME $CACHE_PATH 

WORKDIR $WORKSPACE

# this is needed to run reflex
RUN apt update -y

COPY ./service/requirements.txt ./

RUN pip install -r requirements.txt 
RUN pip install --upgrade jinja2
RUN reflex init

COPY ./service ./

ENTRYPOINT ["./resources/scripts/bootstrap.sh"]

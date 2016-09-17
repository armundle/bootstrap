FROM python:3.5-onbuild
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ENV PROJECT_DIR=/app
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR

EXPOSE 80
CMD ["sh","-x","run.sh"]

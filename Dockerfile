FROM tensorflow/tensorflow:latest-gpu

COPY . /app/

WORKDIR /app

RUN pip install -r requirements.txt
# RUN pip install tensorflow

ENTRYPOINT ["/bin/bash"]

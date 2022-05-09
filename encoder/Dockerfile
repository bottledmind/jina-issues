FROM tensorflow/tensorflow

COPY . /executor_root/

WORKDIR /executor_root

RUN pip install --upgrade pip && pip install -r requirements.txt


ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
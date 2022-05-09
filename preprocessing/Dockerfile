FROM jinaai/jina:3.3.15

# make sure the files are copied into the image
COPY . /executor_root/

WORKDIR /executor_root

# RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["jina", "executor", "--uses", "config.yml"]
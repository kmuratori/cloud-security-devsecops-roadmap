FROM    python:3.12-slim
WORKDIR /app
RUN     useradd -r user0
RUN     chown user0:user0 /app
COPY    --chown=user0 requirements.txt ./
RUN     pip install -r ./requirements.txt
COPY    --chown=user0 main.py ./
USER    user0
CMD     [ "python", "main.py" ]

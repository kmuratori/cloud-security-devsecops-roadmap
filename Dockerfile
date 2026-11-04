FROM    python:3.12-slim AS builder
WORKDIR /app
COPY    ./requirements.txt .
RUN     pip install --prefix=/build -r ./requirements.txt

FROM    python:3.12-slim AS runner
WORKDIR /app
RUN     mkdir /data
RUN     useradd -u 4200 -r user0
RUN     chown user0:user0 /app
RUN     chown user0:user0 /data
COPY    --chown=user0 --from=builder /build /usr/local
COPY    --chown=user0 --exclude=requirements.txt . .
USER    user0
CMD     [ "python", "app.py" ]

FROM alpine:latest
LABEL authors="odivalneto"

ENTRYPOINT ["top", "-b"]
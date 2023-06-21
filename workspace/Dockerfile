FROM alpine:3.18

RUN apk update && apk add wget
RUN apk add zig --repository=https://dl-cdn.alpinelinux.org/alpine/edge/testing

WORKDIR /app
COPY . .
 
RUN zig build

CMD ["/bin/sh", "-c", "/app/zig-out/bin/workspace"]

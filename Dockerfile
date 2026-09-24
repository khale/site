# Pinned Hugo toolchain for this site (matches netlify.toml).
# Wowchemy v5.7 does not build on current Hugo releases, so keep this at 0.108.0.
FROM golang:1.21-bookworm

ARG HUGO_VERSION=0.108.0
# Set automatically by BuildKit (arm64 on Apple Silicon, amd64 elsewhere).
ARG TARGETARCH

RUN apt-get update \
 && apt-get install -y --no-install-recommends ca-certificates curl git \
 && rm -rf /var/lib/apt/lists/*

# Hugo *extended* is required: the theme compiles SCSS.
RUN curl -fsSL -o /tmp/hugo.tgz \
      "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-${TARGETARCH}.tar.gz" \
 && tar -xzf /tmp/hugo.tgz -C /usr/local/bin hugo \
 && rm /tmp/hugo.tgz \
 && hugo version

# enableGitInfo reads .git from the bind-mounted repo, which is owned by your
# host user, not the container's; allow it.
RUN git config --system --add safe.directory '*'

# Hugo modules (the Wowchemy theme) are cached here; compose.yaml mounts a volume
# so they are downloaded once, not on every start.
ENV HUGO_CACHEDIR=/cache
WORKDIR /src
EXPOSE 1313

ENTRYPOINT ["hugo"]
# Dev server reachable from the host browser at http://localhost:1313/
#   --bind 0.0.0.0        listen on all container interfaces so the port mapping works
#   --baseURL/appendPort  make generated links and livereload point at localhost:1313
#   --poll                reliable change detection on macOS bind mounts
CMD ["server", "--bind", "0.0.0.0", "--port", "1313", \
     "--baseURL", "http://localhost:1313/", "--appendPort=false", \
     "--disableFastRender", "--poll", "700ms"]

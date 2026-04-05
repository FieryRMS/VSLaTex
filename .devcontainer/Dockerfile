FROM ghcr.io/astral-sh/uv:latest AS uv


FROM texlive/texlive:latest-full AS tex
RUN apt-get update


FROM tex AS texuv
COPY --from=uv /uv /uvx /bin/


FROM texuv AS vslatex
RUN apt-get update && apt-get install -y \
    perl \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*
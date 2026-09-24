# Local preview/build environment for the site: Python + the three libraries in requirements.txt.
# The repo is bind-mounted at /site by compose.yaml, so edits on the Mac show up immediately.
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /site
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

EXPOSE 8000
ENTRYPOINT ["python3", "build.py"]
CMD ["serve"]

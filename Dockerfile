FROM python:3.10-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# Set work directory
WORKDIR /app

# Install system dependencies for building Python packages
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    libwebp-dev \
    tiff-dev \
    openjpeg-dev \
    freetype-dev \
    lcms2-dev \
    libimagequant-dev \
    libraqm-dev \
    libxcb-dev \
    harfbuzz-dev \
    fribidi-dev

# Install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files (CRITICAL FOR RAILWAY)
RUN python manage.py collectstatic --noinput

EXPOSE 8080

# Start command for Railway
CMD python manage.py migrate && gunicorn dict.wsgi --bind 0.0.0.0:$PORT
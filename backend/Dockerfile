FROM python:3.7

WORKDIR /srv

# Install packages
# (Currently not needed because mysql is bundled with python:3 image)
#RUN apt-get install -y \
#        libmysqlclient-dev \
# && rm -rf /var/lib/apt/lists/*


# Install Python packages
COPY requirements.txt .

RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy the source
COPY . ./


# Make Django ready
ARG DJANGO_BASE=project
ENV DJANGO_BASE="$DJANGO_BASE"
ARG DJANGO_SETTINGS_MODULE="$DJANGO_BASE.settings.production"
ENV DJANGO_SETTINGS_MODULE="$DJANGO_SETTINGS_MODULE"

RUN echo "Settings: $DJANGO_SETTINGS_MODULE" \
 && python manage.py collectstatic --noinput \
 && python manage.py check --deploy

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]

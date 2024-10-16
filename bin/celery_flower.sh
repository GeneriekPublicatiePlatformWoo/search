#!/bin/bash
exec celery flower --app woo_search --workdir src

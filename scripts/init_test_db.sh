#!/bin/bash

psql -tc "SELECT 1 FROM pg_database WHERE datname = 'tagged_images_manager_service_test_db'" | grep -q 1 || psql -c "CREATE DATABASE tagged_images_manager_service_test_db"

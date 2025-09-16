#!/bin/bash
pytest /app/tests --base_url=$BASE_URL --alluredir=/app/allure-results --browser=remote --headless --selenoid_url=$SELENOID_URL
chown -R 105:108 /app/allure-results
chown -R 105:108 /app/logs
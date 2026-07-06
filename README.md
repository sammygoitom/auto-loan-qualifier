# Auto Loan Qualifier

Full-stack Flask web app that evaluates auto-loan eligibility from a user’s financial profile and returns vehicles grouped by approval status.

## Project Info

[Project Presentation](https://docs.google.com/presentation/d/1NcaUOtVPDeoQt9SD4xyeZKA4chRJq_n2v68p1_aDFlU/edit?usp=drive_link)

## Features

- Scores applicants based on credit score, income, down payment, employment status, and finance term
- Uses a modular weighted scoring engine built with separate Python classes for each financial factor
- Groups vehicles into approved and manual-review categories based on applicant score and budget
- Loads vehicle inventory from an S3-hosted Excel file using Pandas and Boto3
- Displays vehicle results with make, year, price, mileage, and image URLs
- Includes batch image URL population using SerpAPI
- Containerized with Docker and served with Gunicorn
- Deployed to AWS Elastic Beanstalk with IAM instance role access to S3

## Tech Stack

**Backend:** Python, Flask, Pandas  
**Frontend:** HTML, CSS, Bootstrap, Jinja2  
**Cloud / Deployment:** AWS Elastic Beanstalk, IAM, S3, Docker, Gunicorn  
**APIs / Scripts:** SerpAPI

FROM public.ecr.aws/lambda/python:3.11

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Lambda code
COPY lambda_function.py .

# Lambda entry point
CMD ["lambda_function.lambda_handler"]
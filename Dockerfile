FROM python:3.11.5
COPY . /
RUN pip install poetry
RUN cd user_service
RUN poetry update
RUN poetry install
EXPOSE 8000

CMD ["./wait-for-it.sh", "user-db:5432", "--", "poetry", "run", "uvicorn", "user_service.server:app", "--host", "0.0.0.0", "--port", "8000"]

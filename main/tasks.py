from base.celery import app


@app.task
def example_task(args):
    print(args)

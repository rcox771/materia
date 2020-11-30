from prefect import task
from prefect import Flow


@task
def say_hello(person: str) -> None:
    print("Hello, {}!".format(person))


with Flow("My first flow!") as flow:
    first_result = say_hello("bob")

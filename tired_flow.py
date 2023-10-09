from prefect import flow
from time import sleep

@flow(log_prints=True)
def tired_flow():
    print("I'm so tired...")
    sleep(1)
    for i in range(10):
        print("zzzzz...")
        sleep(6)
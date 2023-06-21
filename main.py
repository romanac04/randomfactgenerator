from fastapi import FastAPI
import random
import uvicorn
app = FastAPI()

file_path = r"C:\Users\roman\OneDrive\Documents\space_facts.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

@app.get("/facts/random")
def get_random_fact():
    fact = random.choice(space_facts)
    return JSONResponse(content={"fact": fact})

@app.get("/facts")
def get_fact_by_index(index: int = None):
    if index is None:
        fact = random.choice(animal_facts)
    else:
        fact = animal_facts[index]
    return JSONResponse(content={"fact": fact})

@app.post("/facts")
def add_fact(new_fact: str):
    with open('space_facts.txt', 'a') as file:
        file.write(new_fact + "\n")
    return {"message": "Fact added successfully"}
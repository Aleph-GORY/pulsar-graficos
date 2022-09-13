#!/usr/bin/env python3
import numpy as np

propuestas = [
    "propuesta1",
    "propuesta2",
    "propuesta3",
    "propuesta4"
]

if __name__=="__main__":
    for propuesta in np.random.choice(propuestas, size=3, replace=False):
        print(propuesta)
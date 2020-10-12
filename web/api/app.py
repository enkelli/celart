"""
    Web server app.
"""

from fastapi import FastAPI
from fastapi import Path

from cartist import Artist

app = FastAPI()


MIN_VALUE_FOR_SQRT = 1
MAX_VALUE_FOR_SQRT = 1000


@app.get('/api/sqrt/{value}/value')
def sqrt_value(value: int = Path(..., title='Value to be squared', ge=MIN_VALUE_FOR_SQRT, le=MAX_VALUE_FOR_SQRT)):
    artist = Artist(value)
    return {'value': artist.sqrt}


@app.get('/api/sqrt/{value}/steps')
def sqrt_steps(value: int = Path(..., title='CA steps to get sqrt for the value', ge=MIN_VALUE_FOR_SQRT, le=MAX_VALUE_FOR_SQRT)):
    artist = Artist(value)
    return {
        'steps': list(artist.steps()),
        'sqrt': artist.sqrt,
    }

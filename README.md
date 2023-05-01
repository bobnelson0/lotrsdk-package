# lotrsdk-package

A Python SDK package for using The One API

## Install
The package can be found on PyPi here: https://pypi.org/project/lotrsdkbybnelson0/1.0.0/
and can be install using pip like this:
```bash
pip install lotrsdkbybnelson0
```

## Usage (Recommended)
### Set up
1. Get an `api-key` from [The One Ring](https://the-one-api.dev/).

2. Set the `api-key` as an environment variable. There are lots of ways to do this in Python. I recommend using [python-dotenv](https://pypi.org/project/python-dotenv/). See that documenation for additional info. The following steps will reference this method.

3. Create a .env file in the root of your project directory. The contents will look like this:
```
# .env file
lotrsdk-api-key = "YOUR_KEY_HERE"
```
4. Import the `lotrsdk` objects (packages) into your project.
```py
from lotrsdk import Movie, Quote
```
5. In your python project, using `dotenv`, load the `.env` file which contains the key
```py
from dotenv import load_dotenv
load_dotenv()
```
6. (Optional) You can validate the api-key loaded with the following
```py
import os
print(os.environ.get('lotrsdk-api-key'))
```

### Example Usage
```py
# Returns a Movie object
movie = Movie.get_by_id('5cd95395de30eff6ebccde5b')
print(movie) # This is an object, but has a string representation

# Returns a Collection object of Movies
movies = Movie.get_all()
print(movies) # This is an object, but has a string representation
print(movies.total)
print(movies.entities[0])

# Returns a Quote object
quote = Quote.get_by_id('5cd96e05de30eff6ebcce834')
print(quote) # This is an object, but has a string representation

# Returns a Collection object of Quotes
quotes = Quote.get_all()
print(quotes) # This is an object, but has a string representation
print(quotes.total)
print(quotes.entities[0])

# Returns a Collection object of Quotes by movie id
# Paging and additional parameters can be passed
movie_quotes = Movie.get_quotes('5cd95395de30eff6ebccde5b', {'page': 2})
print(movie_quotes) # This is an object, but has a string representation
print(movie_quotes.total)
print(movie_quotes.entities[0])
```

## Test

This package uses the `unittest` python package which is standard
#### Run the unit test suite
```bash
$ python -m unittest
```
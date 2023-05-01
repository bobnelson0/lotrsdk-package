# Design of lotrsdk-package
Design details for the lotrsdk package

## Initial thoughts
When designing an SDK, I like to imagine how I, as a user of the SDK, would want to use it. So I started with an initial idea like this:

```py
id = 'abc123'
movie = Movie.get(id)
print(movie.name)
```

I know I wanted to be to only interact with the SDKs objects and treat them as such. However, I also wanted to offer the ability to use the objects and clients that are under the hood. So I set out to design with that simple piece of code above, but I started with building the ApiClient so that I could get that figured out first.

## ApiClient
This is a simple REST client that only performs `GET` requests at the moment. It could be easily extended to include on ther request verbs (`POST`, `PUT`, etc). The ApiClient needs an api-key to operate with, which brings us to...

### Using dotenv
The usage instructions require that `dotenv` be used and that you store the `api-key` in the environment variables. I chose this because it is considered a best practice, more info here: [12 Factor App](https://12factor.net/config)

## Entity APIs
I separated the request logic (ApiClient) from the request logic of each entity (`./api/*_api.py`) to keep things clean and allow for potential customization. What is nice about this is that it is very simple to add a new entity integration making a new file and using the other entity apis as a template. 

## Entities & Collections
### Entity classes
I implemented each entity as its own object when all matching parameters from what I found in `The One Ring` docs. Each entity object makes calls to its matching entity api. For now, these objects have mostly static methods which return an object. However, I designed these with the idea that I may need to support `save`, `update`, etc methods in the future. Implementing that would be as simple as creating a new object instance and calling a `save` method. This of course would integrate with a new method in the matching api class. 
In addition, you can pass other ApiClients to the entities in case you have a need for using a non-default client. This also comes in handy if you need to use separate `api-key`s for various calls. I've seen it in the real world, trust me.

### Collection class
For API calls which return multiple objects, I created a custom `Collection` object which also contained metadata about the entities requests. This makes it easy to make additional requests and do proper paging as needed.



# What's next (TODO)
With any project that has to be done under a tight deadline, there will be a list of `#TODO` that would make this even better. A few thoughts I had...
* Objects like `Quote` have movie and character IDs. It might be nice to replace those IDs with the actual objects. This would require extra rest calls
* I implemented base querying based on the docs. However, negation (`!=`) and comparison (`> < >= <=`) operators aren't implemented yet.
* Only `GET` calls are implemented. Should do the others when needed.
* The unit tests only test the easy to test functions. Additional unit tests should be added, using mock objects, to mock and test the API requests.
* I had an idea to add support for a custom logger to the `ApiClient`, but didn't get around to it.
* I also want to integrate the unit test status (`pass`|`fail`) into github.
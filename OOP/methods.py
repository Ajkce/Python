"""""
By definition, a method is a function that is bound to an instance of a class. 
This tutorialhelps you understand how it works under the hood.
"""

class Request:
    def send(*args):
        print('Sent', args)

# print(Request.send)

http = Request()

# print(http.send)

"""""So when you define a function inside a class,
it's purely a function. However, when you access that function via an object,
the function becomes a method."""

print(http)
Request.send()
http.send()

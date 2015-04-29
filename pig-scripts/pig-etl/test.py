from pig_util import outputSchema

# the output schema is zipcode
@outputSchema("id:chararray")
def test():
    return "hello"

@outputSchema("as:int")
def square(num):
    if num == None:
        return None
    return ((num) * (num))

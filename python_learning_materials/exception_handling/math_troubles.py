
def get_numbers():
    return []


try:
    array_of_numbers = get_numbers()
    average = sum(array_of_numbers) / len(array_of_numbers)

    print "The average is {}".format(average)
except Exception as e:
    print "Something went wrong: %s" % e.message
finally:
    print "But always print this."




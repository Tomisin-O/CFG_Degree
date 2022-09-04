requests.get('https://www.google.com'))

.get send a request say this is a get request
.post

get different responses
400 ststus code means we did something wrong
API-use a prgram to talk to another prgram over the ingternet
communicate with a server that deals with the requests and sends back a response
e.g ask for info it send thast info

we send request and get a response thast is the status code
api name for anything we use for ine prgram to talk to another

base url https://pokeapi.co/api/v2/
type pokemon

ditto.res(json) converts to json

# year = input('What is the year')
new_year = []
def yearfunction (year):
    if (year[:2]) == "18":
        new_year.append("Eighteenth Century")
    elif (year[:2]) == "19":
        new_year.append("Twentieth Century")

    if ((year[2:3])) == "1":
        new_year.append("Tens")
    elif ((year[2:3])) == "2":
         new_year.append("Twenties")
    elif ((year[2:3])) == "3":
        new_year.append("Thirties")
    elif ((year[2:3])) == "4":
        new_year.append("Fourties")
    elif ((year[2:3])) == "5":
        new_year.append("Fifties")
    elif ((year[2:3])) == "6":
        new_year.append("Sixties")
    elif ((year[2:3])) == "7":
        new_year.append("Seventies")
    elif ((year[2:3])) == "8":
        new_year.append("Eighties")
    elif ((year[2:3])) == "9":
        new_year.append("Ninety")
    return(new_year)

print(yearfunction("1800"))

## Importing required modules
import click
import requests as r
from termcolor import colored as c


def getDefinition(word):
    '''
    Define command takes the word and gives us the definition of the word
    by calling the Merriam API.
    '''
    ## Merriam Dictionary API details ##
    ## In a real production env, best practice is to do some kind of encryption and store it in an actual secrets service and retrieve as the program starts ##
    apiKey = "e6cf8123-8a5f-4d47-a5fb-3a21bb7cc7c1"
    apiUrl = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{w}?key={k}".format(k = apiKey, w=word)
    try:
        ## Printing the some helpful info to User ##
        click.echo(c(f"Working on getting definition for the: {word}", "yellow", attrs=['bold']))
        click.echo("------------------------------------------------")
        ## Curling the url and getting the word definition from Merriam Dictionary Api ##
        wordJson = r.get(apiUrl).json()
        
        ## Word pronunciation storing in variable##
        pronunciation = wordJson[0]["hwi"]["prs"][0]["mw"]
        ## Storing what kind of word it is ##
        kind = wordJson[0]["fl"]

        ## Storing definition of the word ##
        definition = wordJson[0]["def"][0]["sseq"][0][0][1]["dt"][0][1]

        ##Returining the ouput as we wanted ## 
        result = str(pronunciation + " " + "(" + kind + ")" + ":" + " " + definition)

        click.echo(c("The defiinition for the word:{w}".format(w=word), "green", attrs=['bold']))
        click.echo("------------------------------------------------")
        click.echo(c(result, "green", attrs=['bold']))
    except:
        click.echo(c("Oops, something went wrong, maybe check the spelling of the word you have entered? & try again!!", "red", attrs=['bold']))

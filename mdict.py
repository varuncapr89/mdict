import click 
from termcolor import colored as c 
from commands import get

@click.group()
def mdict():
    '''
    mdict gets the definition of the word you give to it "Ex:mdict define -w exercise"
    '''
    pass

@click.command(name='define')
@click.option('--word', '-w', help="Give the word you would like to get the definition for ex: mdict -w omnipresent", required=True, prompt="Give a word you would like to check the definition for? please?\n")
def define(word):
    '''
    This command calls the merriam dict api for the requested word definition. 
    '''
    if word.isalpha():

        get.getDefinition(word.lower())
    else:
        click.echo(c("Please enter only a valid word!!", "red", attrs=['bold']))

mdict.add_command(define)
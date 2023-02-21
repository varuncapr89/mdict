# mdict
## About mdict

mdict is a cli to help getting the definitions of words from Merriam dictionary API
## Building mdict

**Step 1**: Use pip to install mdict

```sh
$ pip3 install --editable .
```

**Step 2**: Run mdict
```sh
$ mdict --help
Usage: mdict [OPTIONS]...

Options:
  --help    "Shows help message for this cli"

mdict sub_Commands:
  define    "Gets the definition of the word from Merriam dictionary API"

Options:
  -w, --word  "Give the word, you would like to get the definition for ex:mdict define -w omnipresent"
```
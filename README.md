# redirect_block_URL

A basic python program that can redirect or block URLs locally on your PC. This should work on all Unix OS systems.

## How it works

The program will add entries to the /etc/hosts file that will either redirect or block a given website. This will need sudo privilege be aware of that. Also for redirecting a URL the code snipped needs a working internet connection.

## Usage

When you want to redirect a website do the following code snippet:
```
python3 redirect_block_URL.py -r <to where the URL should be redirected to> -ra <the URL that will be redirected>
```
When you want to block a website do the following code snippet:
```
python3 redirect_block_URL.py -b <blocked URL>
```

This can also be found with the 
```
python3 redirect_block_URL.py -h
```

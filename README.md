# webprobe
Nifty and sophisticated web path scanner

A sophisticated web path scanner designed for the most descerning bug bounty hunters.


This CLI brute forces directories and files in webservers.


### Installation & Usage
                                                
**Requirement: python 3.8 or higher**

- Install with PyPi: `pip3 install webprobe`


### How to use

Some common examples on how to use webprobe.

:NOTE: If you need to see a list of all options, just use the **-h** argument

To use multiple wordlists, you can separate your wordlists with commas. Example: `wordlist1.txt,wordlist2.txt`

### Simple usage

```python

webprobe -u https://target.com

```

```python

webprobe -e php,html,js -u https://target.com

```

```
webprobe -e php,html,js -u https://target.com -w /path/t
o/wordlist

```



## License📑

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This software is licensed under the `MIT License`. See the [License](https://github.com/scalabli/webprobe/blob/master/LICENSE) file in the top distribution directory for the full license text.

## Donate🎁
In order to for us to maintain this project and grow our community of contributors.
[Donate](https://ko-fi.com/scalabli)


## Code of Conduct
Code of Conduct is adapted from the Contributor Covenant, version 1.2.0 available at [Code of Conduct](http://contributor-covenant.org/version/1/2/0/)

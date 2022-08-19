[![Downloads](https://pepy.tech/badge/webprobe)](https://pepy.tech/project/webprobe)
[![PyPI version](https://badge.fury.io/py/webprobe.svg)](https://badge.fury.io/py/webprobe)
[![Wheel](https://img.shields.io/pypi/wheel/webprobe.svg)](https://pypi.com/project/webprobe)
[![licence](https://img.shields.io/pypi/l/webprobe.svg)](https://opensource.org/licenses/MIT)
[![Twitter Follow](https://img.shields.io/twitter/follow/gerrishon_s.svg?style=social)](https://twitter.com/gerrishon_s)

[![Logo](https://raw.githubusercontent.com/scalabli/webprobe/main/images/webprobe.png)](https://github.com/scalabli/webprobe)

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

## Pausing progress

You can pause the scanning progress with CTRL+C  from here, you can save the progress (and continue later), skip the current target, or skip the current sub-directory.

## Recursion
- Brutforcing recursively can be achieved using `-r` or `--recursive` flag.

For example, if webprobe finds `admin/`, it will brute-force `admin/* ` (`*` is where it brute forces).

```python

webprobe -e php,html,js -u https://example.com -r

```

- You can set the max recursion depth with `--recursion-depth` and status codes to recurse with `--recursion-status`

```python

webprobe -e php,html,js -u https://example.com -r --recursion-depth 3 --recursion-status 200-39

```
- You can brute force recursively all found paths, not just paths end with `/` using `--force-recursive` flag.

- You can recursively brute-force all depths of a path (`a/b/c` => add `a/`, `a/b/`) using `--deep-recursive` flag.

- If there are sub-directories that you do not want to brute-force recursively use `--exclude-subdirs` flag.

```python

webprobe -e php,html,js -u https://example.com -r --exclude-subdirs image/,media/,css/

```

## Threads
Thread number (`-t | --threads`) reflects the number of separated brute force processes. The bigger the thread number, the faster webprobe runs. By default, the number of threads is 25, but you can increase it if you want to speed up the progress.

However, the speed still depends on the response time of the server.
:bulb: keep the threads number within a reasonable range because it can cause DoS (Denial of Service).

```python

webprobe -e php,htm,js,bak,zip,tgz,txt -u https://example.com -t 20

```

## Filters
Use **-i | --include-status** and **-x | --exclude-status** flags to select allowed and not allowed response status-codes

For more advanced filters: **--exclude-sizes**, **--exclude-texts**, **--exclude-regexps**, **--exclude-redirects** and **--exclude-response**

```python

webprobe  -e php,html,js -u https://example.com --exclude-sizes 1B,243KB

```                                                      
```python

webprobe -e php,html,js -u https://example.com --exclude-texts "403 Forbidden"

```

```python

webprobe -e php,html,js -u https://example.com --exclude-regexps "^Error$"

```

```python

webprobe -e php,html,js -u https://example.com --exclude-redirects "https://(.*).okta.com/*"

```

```python

webprobe -e php,html,js -u https://example.com --exclude-response /error.html

```

## Scan sub-directories
- You can scan a list of sub-directories with **--subdirs** flag.

```python

webprobe -e php,html,js -u https://example.com --subdirs /,admin/,folder/
```
## Proxies
- Webprobe supports both SOCKS and HTTP proxy. You can enlist a proxy server or a list of proxy servers from a file.

```python

webprobe -e php,html,js -u https://example.com --proxy 127.0.0.1:8080

```

```python

webprobe -e php,html,js -u https://example.com --proxy socks5://10.10.0.1:8080

```

```python

webprobe -e php,html,js -u https://example.com --proxylist proxyservers.txt

```
## More example commands

```python

cat urls.txt | python3 webprobe --stdin

```

```python

webprobe -u https://example.com --max-time 360

```

```python

webprobe -u https://example.com --auth admin:pass --auth-type basic

```

```python

webprobe -u https://example.com --header-list rate-limit-bypasses.txt

```

## Reports
Supported report formats are: **simple**, **plain**, **json**, **xml**, **md**, **csv**,  **html**, **sqlite**
:bulb: We will be adding `yaml` soon

```python
 webprobe -e php -l URLs.txt --format plain -o report.txt
```

```python
 webprobe -e php -u https://example.com --format html -o example.json
```

## License📑

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This software is licensed under the `MIT License`. See the [License](https://github.com/scalabli/webprobe/blob/master/LICENSE) file in the top distribution directory for the full license text.

## Donate🎁
In order to for us to maintain this project and grow our community of contributors.
[Donate](https://ko-fi.com/scalabli)


## Code of Conduct
Code of Conduct is adapted from the Contributor Covenant, version 1.2.0 available at [Code of Conduct](http://contributor-covenant.org/version/1/2/0/)

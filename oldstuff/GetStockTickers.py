# taken directly from https://www.xavignu.com/?p=1152
# slight modification to


#!/usr/bin/env python
import ftplib
import os
import re


def getTickers():

        # Connect to ftp.nasdaqtrader.com
        ftp = ftplib.FTP('ftp.nasdaqtrader.com', 'anonymous', 'anonymous@debian.org')
        # Download files nasdaqlisted.txt and otherlisted.txt from ftp.nasdaqtrader.com
        for ficheiro in ["nasdaqlisted.txt", "otherlisted.txt"]:
                ftp.cwd("/SymbolDirectory")
                localfile = open(ficheiro, 'wb')
                ftp.retrbinary('RETR ' + ficheiro, localfile.write)
                localfile.close()
        ftp.quit()
        # Grep for common stock in nasdaqlisted.txt and otherlisted.txt
        for ficheiro in ["nasdaqlisted.txt", "otherlisted.txt"]:
                localfile = open(ficheiro, 'r')
                for line in localfile:
                        if re.search("Common Stock", line):
                                ticker = line.split("|")[0]
                                if ticker == "ACAMU":
                                        x = 0
                                # Append tickers to file tickers.txt
                                open("tickers.txt","a+").write(ticker + "\n")


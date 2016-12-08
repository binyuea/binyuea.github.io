#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib
import re
from bs4 import BeautifulSoup



if __name__ == '__main__':
	page ='<p style="min-height: 1em; max-width: 100%; line-height: 1.5em; word-wrap: break-word !important; box-sizing: border-box !important;"><span style="font-family: Helvetica; -webkit-text-stroke: rgb(0, 0, 0); max-width: 100%; word-wrap: break-word !important; box-sizing: border-box !important;">2. 量入为出。别和我一样傻逼。<br  /></span></p>'
	soup = BeautifulSoup(str(page),'html.parser')

	results = soup.find_all("span")
	for item in results:
		if item.has_attr("class"):
			continue
		if item.span:
			continue

		if item.getText() and item.getText() != ' ':
			if item.br:
				print item.getText()+'\n',
			print "hi"
			# print item.getText(),







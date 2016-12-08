#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import urllib
import re
from bs4 import BeautifulSoup
from time import gmtime, strftime


# url = 'http://mp.weixin.qq.com/s?__biz=MzA3MDM3MDYwMg==&mid=2653888920&idx=6&sn=ce64610af0a495c1159af89c1ec200ea&chksm=84e655ddb391dccb2918ba067fd05fab6a10ce7734167afda6d1eb7ee6959614637f155f6957&mpshare=1&scene=1&srcid=1208Y06Ofu0jGs5ej7hStjsn#rd'
out_dir = '_posts/'


def getDescription(soup):
	results = soup.find_all("span")
	for item in results:
		if item.has_attr("class"):
			continue
		if item.span:
			continue
		if item.getText() and item.getText() != ' ':
			return item.getText()	


def download(url):
	page = urllib.urlopen(url).read()
	soup = BeautifulSoup(str(page),'html.parser')

	# writeHead
	Title = soup.find('title').getText()
	# if ' ' in Title:
	# 	Title = Title.split(' ')
	# 	Title = ''.join(Title)
	if '\'' in Title:
		Title = Title.split('\'')[1]
		# Title = '~'.join(Title)
	if '\"' in Title:
		Title = Title.split('\"')[1]
		# Title = '~'.join(Title)
	Title = Title.encode('utf-8')
	Time = strftime("%Y-%m-%d", gmtime())
	f = open('_posts/'+ Time + '-' + Title + '.md','w+')
	f.write('---\n')
	f.write('layout: post \n')
	f.write('title: '+ Title +'\n')
	f.write('date:\t'+ Time +'\n')
	f.write('description: '+ getDescription(soup).encode('utf-8') + '\n')
	f.write('category: Moments \n')
	f.write('keywords: Moments, Weixin \n')
	f.write('comments: true \n')
	f.write('---\n')
	# f.write()

	flag = False
	results = soup.find_all("span")
	for item in results:
		if item.has_attr("class"):
			continue
		if item.span:
			continue
		if item.getText() and item.getText() != ' ':
			if flag:
				# print item.getText(),
				if item.br:
					f.write(item.getText().encode('utf-8')+'\n')
				else:
					f.write(item.getText().encode('utf-8'))
			else:
				flag = True


	f.close()


# def writeHead(title):


if __name__ == '__main__':
	# download(url)
	f = open('./posts/urls')
	for line in f:
		download(line)

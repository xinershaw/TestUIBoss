#!-*-coding:utf-8-*-
"""
@FileName:
@Date: 2020-4-14
@Author:April Shaw
@Description:
"""
import yaml


def get_yaml_data(yaml_file):
	try:
		with open(yaml_file,'r',encoding='utf-8') as f:
			return yaml.load(f)
	except yaml.YAMLError:
		raise






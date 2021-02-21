#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2

	sous_total = 0

	for i in data:
		sous_total += i[INDEX_QUANTITY]*i[INDEX_PRICE]

	taxes = sous_total*0.15
	total = sous_total + taxes

	data_bill = [
		("SOUS TOTAL", sous_total),
		("TAXES     ", taxes),
		("TOTAL     ", total)
	]

	result = name
	for db in data_bill:
		result += "\n" + f"{db[0]} {db[1] : >10.2f} $"

	#print(f"SOUS TOTAL {format(sous_total, '.2f'): >10} $")
	#print(f"TAXES {format(taxes, '.2f') : >10} $")
	#print(f"TOTAL {format(total, '.2f'): >10} $")

	return result


def format_number(number, num_decimal_digits):
	return ""

def get_triangle(num_rows):
	return ""


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))

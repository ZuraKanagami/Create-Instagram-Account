if __name__ == "__main__":
	try:
		__import__("run").security()
	except Exception as e:
		exit(str(e))

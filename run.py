if __name__ == "__main__":
	try:
		__import__("run_enc").security()
	except Exception as e:
		exit(str(e))

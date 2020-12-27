mode = input("Anna luku: ")

try:
	mode = int(mode)
	print("Syöte oli kelvollinen.")
	
except Exception:
	print("Virheellinen syöte!")

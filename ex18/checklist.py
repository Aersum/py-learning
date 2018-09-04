def add_checklist(exersise,complete_status):
	with open("checklist.md",'a') as f:
		if complete_status:
			f.write(f"[x] {exersise}\n")
		else:
			f.write(f"[ ] {exersise}\n")
	print("Complete!")
add_checklist("Exersise 1", True)
add_checklist("Exersise 20", False)

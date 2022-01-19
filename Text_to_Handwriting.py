import pywhatkit
text = str(input("Enter the text => "))
pywhatkit.text_to_handwriting(text,save_to= "pic.png")
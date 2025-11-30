# import qrcode

# url = input("enter the url");
# filename = input("file name you want to save it as: ");
# if (filename.endswith(".png")):
#     filename = filename + ".png"
   
# img = qrcode.make(url)
# img.save(filename)
# print(f"QR Code saved successfully as {filename}")

# import qrcode
# upi_id = input("enter your Gpay number & upi Id:=  ");

# phonePay_url = f"upi://pay?pa={upi_id}&pn=Recipient&cu=INR"
# gPay_url =f"upi://pay?pa={upi_id}&pn=Recipient&cu=INR"
# Paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient&cu=INR"

# phonePay_qr = qrcode.make(phonePay_url);
# gPay_qr = qrcode.make(gPay_url);
# Paytm_qr = qrcode.make(Paytm_url);

# phonePay_qr.save('payphone.png')
# gPay_qr.save('googlePay.png')
# Paytm_qr.save('paytm.png')
# # show the display qr code
# phonePay_qr.show()
# gPay_qr.show()
# Paytm_qr.show()

# only show the number 
import qrcode

number = input("Enter your mobile number: ")

# Convert number → UPI ID
upi_id = f"{number}@upi"     # you can also use @ybl, @okaxis, @paytm, etc.

# UPI URL
upi_url = f"upi://pay?pa={upi_id}&pn=Recipient&cu=INR"

# Generate QR Code
qr = qrcode.make(upi_url)

# Save & Show
qr.save("upi_number_qr.png")
qr.show()

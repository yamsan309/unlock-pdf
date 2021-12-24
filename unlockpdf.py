import sys
import PyPDF2

def unlock(input_path,output_path,password):
    pdf = PyPDF2.PdfFileReader(input_path)
    pdf.decrypt(password)
    writer = PyPDF2.PdfFileWriter()
    for num in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(num))
    output = open(output_path,"wb")
    writer.write(output)
    output.close


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print("usage: unlockodf.py (input) (output) (password)")
        exit()
    unlock(args[1],args[2],args[3])
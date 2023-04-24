from mongoDbOperations import find_inMongoDb,insertToMongoDB
from resume_read import docReader,docxReader,pdfReader


link = "https://vtelecom319.sharepoint.com/:w:/r/sites/ResumeDb/Shared%20Documents/Resume%20Data/Project_Construction/Alexandra%20Darrow%20Resume.docx?d=w16d8d2db12034ed3a1eb266cfd4f9a34&csf=1&web=1&e=4TjWmp"
file_path = "C:/Users/vedan/Downloads/Project_Construction/Project_Construction/Alexandra Darrow Resume.docx"


recivedPayload =docxReader(file_path,link)
if recivedPayload:
    insertToMongoDB(recivedPayload)
    print(f'-- Payload inserted in MongoDB')
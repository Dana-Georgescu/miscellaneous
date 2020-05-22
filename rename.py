import os
url = '/Users/danageorgescu/Agence universitaire de la Francophonie/Fichiers de ma direction - SP2020/Stages locaux/Stages RFI/Suivi RFI ECO/'
os.chdir(url)
print(os.getcwd())
dossiers = os.listdir()
# todo os.rename(src, dst)

for dossier in dossiers[1:]:
    print(dossier.lstrip('1234567890 .'))
    os.rename(url + dossier, url + dossier.lstrip('1234567890 .'))



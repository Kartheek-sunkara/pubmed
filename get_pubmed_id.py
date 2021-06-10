project_id="ACS+Chem+Biol|2020|15|1016||65d58f4af87bf8b44fd35e0dcec81791d609|"
#ACS+Chemical+Biology

#project_id="Nature|2009|459|356||65d58f4af87bf8b44fd35e0dcec81791d609|"
def getPubmedId(bdata):
    URL="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/ecitmatch.cgi?db=pubmed&retmode=xml&bdata="  
    doc_url = "{0}".format(bdata)
    final_doc_url = URL + doc_url
    r = requests.get(url = final_doc_url)
    data = str(r.content)
    word=data.replace("\\n'","")
    finalWord=word.split("|")
    finalWord=finalWord[-1]
    return finalWord

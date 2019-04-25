REPO=/Users/alexajo/github/MBV3070-H19-hub

echo; echo Files from folder 'lab'
rsync -a --out-format %n%L [0-9]*.ipynb ${REPO}/

echo; echo folder 'code'
rsync -a --out-format %n%L code/   ${REPO}/code/


echo; echo folder 'data'
rsync -a --out-format %n%L data/*.fasta data/*.gbk   ${REPO}/data/

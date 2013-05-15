# Answers week 1

```python
seq = "ATTATGAGATTACAGAGCTAAGAC"   
mrna = seq.replace("T", "U")
start = mrna.find("AUG")
stop = mrna.find("UAA")
print mrna[start:stop]
```

```python
dna = "CGCTACGGACGTAGCCAGCGA"
CG = dna.count("CG")
CG_dinuc = CG*100.0/(len(dna)-1)
print CG_dinuc
```

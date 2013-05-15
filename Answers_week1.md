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
GC = dna.count("GC")
GC_dinuc = GC*100.0/(len(dna)-1)
print GC_dinuc
```

# bbst


去重url

```
for i in $(cat path.txt); do cat httpx.txt | grep "$i" | shuf | tail -n 1; done
```

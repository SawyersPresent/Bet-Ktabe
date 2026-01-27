

pretty simple

`assetfinder teslam.com`

`assetfinder teslam.com`



```
#!/bin/bash

url=$1

if [ ! -d "$url" ]; then
    mkdir "$url"
fi

if [ ! -d "$url/recon" ]; then
    mkdir "$url/recon"
fi

echo "Harvesting subdomains with assetfinder..."
assetfinder "$url" >> "$url/recon/assets.txt"
cat "$url/recon/assets.txt" | grep "$url" >> "$url/recon/final.txt"
rm "$url/recon/assets.txt"

```
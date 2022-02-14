# download dataset
mkdir -p data/arc/
wget -nc -P data/arc/ https://ai2-public-datasets.s3.amazonaws.com/arc/ARC-V1-Feb2018.zip

cd data/arc/
yes n | unzip ARC-V1-Feb2018.zip

# create output folders
mkdir -p grounded/
mkdir -p graph/
mkdir -p statement
